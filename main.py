from calculator import *
from database import *
from logger import log_operation
from reports import generate_report
from weather import get_weather, send_email

def console_interface():
    init_db()
    print("Weather + Calculator Application")

    while True:
        print("\nChoose an option:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Get Weather\n6. Generate Report\n7. Exit")

        choice = input("Enter choice: ")
        if choice == '7':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    result = add(a, b)
                    op = 'Add'
                elif choice == '2':
                    result = subtract(a, b)
                    op = 'Subtract'
                elif choice == '3':
                    result = multiply(a, b)
                    op = 'Multiply'
                elif choice == '4':
                    result = divide(a, b)
                    op = 'Divide'

                print(f"Result: {result}")
                save_operation(op, a, b, result)
                log_operation(op, a, b, result)

            except ValueError:
                print("Invalid number. Please enter numeric values.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            city = input("Enter city name: ")
            try:
                weather = get_weather(city)
                desc = weather['weather'][0]['description']
                temp = weather['main']['temp']
                message = f"Weather in {city.capitalize()}: {desc}, Temp: {temp}°C"
                print(message)
                send_email(f"Weather Update: {city}", message, "receiver@example.com")
            except Exception as e:
                print(f"Error fetching weather: {e}")

        elif choice == '6':
            try:
                generate_report()
                print("Report generated: operations_report.csv")
            except Exception as e:
                print(f"Error generating report: {e}")

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    print("Launching Weather + Calculator Application...\n")
    console_interface()
