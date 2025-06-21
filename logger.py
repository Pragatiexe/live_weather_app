from datetime import datetime

def log_operation(operation, a, b, result):
    with open("operations.log", "a") as file:
        file.write(f"{datetime.now()} - {operation}: {a}, {b} => {result}\n")
