import requests
import smtplib
from email.message import EmailMessage

API_KEY = "9b05c299d67b8b7ff4aa3af04b050105"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print(f"Fetching: {url}")
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or 'weather' not in data:
        raise Exception(data.get("message", "Weather data not available"))
    return data

def send_email(subject, message, recipient):
    
    EMAIL = "cuteparro20@gmail.com"
    PASSWORD = "ahohffgwumrzzciu"
    

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = recipient

    try:
        print("Connecting to SMTP...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASSWORD)
            print("Login successful")
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

