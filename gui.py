import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from tkinter import ttk, messagebox
import sqlite3

from calculator import add, subtract, multiply, divide
from weather import get_weather, send_email
from database import init_db, save_operation
from logger import log_operation
from reports import generate_report
from sms_sender import send_sms

def run_gui():
    init_db()
    app = tk.Tk()
    app.title("☀️ Weather + ✖️ Calculator App")
    app.geometry("800x600")
    app.configure(bg='#f8f9fa')

    current_theme = tk.StringVar(value="superhero")  # Default modern dark theme
    style = Style(current_theme.get())

    def switch_theme():
        new_theme = "litera" if current_theme.get() == "superhero" else "superhero"
        current_theme.set(new_theme)
        style.theme_use(new_theme)

    theme_frame = ttk.Frame(app)
    theme_frame.pack(fill='x', padx=15, pady=10)
    ttk.Label(theme_frame, text="🌟 Theme:", font=("Segoe UI", 10, "bold")).pack(side='left')
    ttk.Button(theme_frame, text="Toggle Light/Dark", command=switch_theme).pack(side='left', padx=10)

    notebook = ttk.Notebook(app)
    notebook.pack(expand=True, fill='both', padx=15, pady=10)

    # --- Weather Tab ---
    weather_tab = ttk.Frame(notebook, padding=20)
    notebook.add(weather_tab, text="☁️ Weather")

    city_var = tk.StringVar()
    phone_var = tk.StringVar()
    weather_result = tk.StringVar()

    ttk.Label(weather_tab, text="📍 Enter City:", font=("Segoe UI", 11)).pack(pady=5)
    ttk.Entry(weather_tab, textvariable=city_var, width=30).pack()
    ttk.Label(weather_tab, text="📱 Phone Number (+91...):", font=("Segoe UI", 11)).pack(pady=5)
    ttk.Entry(weather_tab, textvariable=phone_var, width=30).pack()

    def fetch_weather():
        city = city_var.get().strip()
        phone = phone_var.get().strip()

        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        try:
            weather = get_weather(city)
            desc = weather['weather'][0]['description']
            temp = weather['main']['temp']
            message = f"{city.title()}: {desc}, {temp}°C"
            weather_result.set(message)

            send_email(f"Weather in {city}", message, "receiver@example.com")

            if phone:
                if not phone.startswith("+") or len(phone) < 10:
                    messagebox.showerror("Phone Error", "Use format +91XXXXXXXXXX")
                    return
                send_sms(phone, message)
                messagebox.showinfo("Success", f"SMS sent to {phone}")
            else:
                messagebox.showinfo("Info", "Weather fetched. No phone number provided.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch weather or send SMS: {e}")

    ttk.Button(weather_tab, text="Get Weather Info", bootstyle="success-outline", command=fetch_weather).pack(pady=15)
    ttk.Label(weather_tab, textvariable=weather_result, font=("Segoe UI", 12, "bold")).pack(pady=10)

    # --- Calculator Tab ---
    calc_tab = ttk.Frame(notebook, padding=20)
    notebook.add(calc_tab, text="✖️ Calculator")

    num1_var = tk.StringVar()
    num2_var = tk.StringVar()
    result_var = tk.StringVar()

    ttk.Label(calc_tab, text="🔢 First Number:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    ttk.Entry(calc_tab, textvariable=num1_var).grid(row=0, column=1)

    ttk.Label(calc_tab, text="🔢 Second Number:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    ttk.Entry(calc_tab, textvariable=num2_var).grid(row=1, column=1)

    def perform_operation(op_name):
        try:
            a = float(num1_var.get())
            b = float(num2_var.get())
            if op_name == 'Add': result = add(a, b)
            elif op_name == 'Subtract': result = subtract(a, b)
            elif op_name == 'Multiply': result = multiply(a, b)
            elif op_name == 'Divide': result = divide(a, b)
            result_var.set(f"Result: {result}")
            save_operation(op_name, a, b, result)
            log_operation(op_name, a, b, result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(calc_tab, text="Add", command=lambda: perform_operation("Add")).grid(row=2, column=0, pady=10)
    ttk.Button(calc_tab, text="Subtract", command=lambda: perform_operation("Subtract")).grid(row=2, column=1, pady=10)
    ttk.Button(calc_tab, text="Multiply", command=lambda: perform_operation("Multiply")).grid(row=3, column=0, pady=10)
    ttk.Button(calc_tab, text="Divide", command=lambda: perform_operation("Divide")).grid(row=3, column=1, pady=10)

    ttk.Label(calc_tab, textvariable=result_var, font=("Segoe UI", 13, "bold"), foreground="#0d6efd").grid(row=4, columnspan=2, pady=15)

    # --- Report Tab ---
    report_tab = ttk.Frame(notebook, padding=20)
    notebook.add(report_tab, text="📄 Reports")

    def generate_csv():
        try:
            generate_report()
            messagebox.showinfo("Success", "Report generated: operations_report.csv")
        except Exception as e:
            messagebox.showerror("Report Error", str(e))

    ttk.Button(report_tab, text="Generate CSV Report", bootstyle="info-outline", command=generate_csv).pack(pady=30)

    # --- History Tab ---
    history_tab = ttk.Frame(notebook, padding=20)
    notebook.add(history_tab, text="📈 History")

    tree = ttk.Treeview(history_tab, columns=("Operation", "Operand1", "Operand2", "Result"), show='headings')
    for col in tree['columns']:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.pack(expand=True, fill='both', padx=10, pady=10)

    def load_history():
        try:
            conn = sqlite3.connect("history.db")
            cursor = conn.cursor()
            cursor.execute("SELECT operation, operand1, operand2, result FROM operations")
            rows = cursor.fetchall()
            conn.close()
            for row in rows:
                tree.insert('', tk.END, values=row)
        except Exception as e:
            messagebox.showerror("DB Error", str(e))

    ttk.Button(history_tab, text="Load History", bootstyle="warning-outline", command=load_history).pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    run_gui()
