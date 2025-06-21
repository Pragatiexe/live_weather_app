#  live_Weather + Calculator_App 🌤️➗

This is a Python-based application that combines a weather forecast tool with a basic arithmetic calculator. It offers both a **console interface** (optional) and a modern **Tkinter GUI**, allowing users to:
- Get real-time weather updates
- Perform basic arithmetic operations
- Send weather info via **Email** or **SMS**
- View history of operations
- Export reports to CSV
- Toggle between **Light/Dark themes**

---

## 🚀 Features

### ✅ Calculator
- Add, Subtract, Multiply, Divide
- Error handling (e.g., divide by zero)
- Save operations to SQLite
- View history in a tab
- Export report (CSV)

### 🌦️ Weather
- Get real-time weather data using OpenWeatherMap API
- Input any city name
- Email the weather report
- Send SMS weather update (via Twilio)

### 💾 Reports
- Generate operation logs
- Save to `operations_report.csv`

### 🎨 UI
- Built with `Tkinter` and `ttkbootstrap` for a modern look
- Toggle between **Light and Dark themes**

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter (`ttkbootstrap`)
- SQLite
- `smtplib` (for email)
- Twilio (for SMS)
- OpenWeatherMap API
- `pandas` (optional, for data handling)
- `matplotlib` (optional, for future visualizations)

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/weather-calculator-app.git
cd weather-calculator-app


