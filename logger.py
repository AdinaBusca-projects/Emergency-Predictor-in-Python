import csv
import os

LOG_FILE = "users_log.csv"

def log_user_input(age,symptoms,prediction):
    headers = ["age"] + list(symptoms.keys())  + ["emergency"]
    row = [age] + list(symptoms.values()) + [prediction]
    
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline = '') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(row)
    