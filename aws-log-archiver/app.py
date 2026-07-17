import time
import random
import boto3
from datetime import datetime

LOG_MESSAGES = [
    ("INFO", "User logged in"),
    ("INFO", "User logged out"),
    ("INFO", "File uploaded"),
    ("WARNING", "High memory usage"),
    ("WARNING", "Slow API response"),
    ("ERROR", "Database connection failed"),
    ("ERROR", "Invalid user credentials"),
]

LOG_FILE = "logs/app.log"

def generate_logs():
    log_level, message = random.choice(LOG_MESSAGES)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"{timestamp} | {log_level: <7} | {message}"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry + " \n")

    print(log_entry)


while True:
    generate_logs()
    time.sleep(2)
