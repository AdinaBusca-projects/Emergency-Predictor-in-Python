import tkinter as tk
from tkinter import messagebox
from utils import ask_severity_symptom
from model import train_model
import pandas as pd
from logger import log_user_input

class EmergencyPredictorUI:
    def __init__(self,master):
        self.master = master
        self.master.title("Emergency Predictor")
        
        self.master.geometry("500x550")
        self.master.minsize(500, 550)
        
        self.age_label = tk.Label(master, text="Enter your age (18-90):")
        self.age_label.grid(row=0, column=0)
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=0, column=1)
        
        self.symptoms_label = tk.Label(master, text="On a scale of 0 (none) to 5 (severe),, how bad is your symptom")
        self.symptoms_label.grid(row=1, column=0)
        self.symptoms = [
            "chest_pain", "dizziness", "past_stroke", "shortness_breath", "fever", 
            "high_heart_rate", "nausea", "fatigue", "headache", "vomiting", "blurred_vision", 
            "numbness", "loss_consciousness", "difficulty_speaking"
        ]
        self.symptom_entries = {}
        for idx, symptom in enumerate(self.symptoms, start=2):
            label = tk.Label(master, text=symptom)
            label.grid(row=idx, column=0)
            entry = tk.Entry(master)
            entry.grid(row=idx, column=1)
            self.symptom_entries[symptom] = entry
        
        self.predict_button = tk.Button(master, text="Predict", command=self.predict)
        self.predict_button.grid(row=len(self.symptoms)+2, column=0, columnspan=2)
        
    
    def predict(self):
        try:
            age = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please eneter a valid age(18-90)")
            return
        
        symptom_severity = {}
        for symptom, entry in self.symptom_entries.items():
            try:
                severity = int(entry.get())
                if 0 <= severity <= 5:
                    symptom_severity[symptom] = severity
                else:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Input Error", f"Please enter a severity between 0 and 5 for {symptom}.")
                return
          
        #train or load model  
        model = train_model()
        
        input_data = [[age] + [symptom_severity[symptom] for symptom in self.symptoms]]
        input_df = pd.DataFrame(input_data, columns=["age"] + self.symptoms)
        prediction = model.predict(input_df)
        confidence = model.predict_proba(input_df)[0][1]
        
        if prediction[0] == 1:
            result = "This could be a medical emergency. Seek help immediately."
        else:
            result = "This likely isn’t an emergency, but monitor your condition."
        
        log_user_input(age, symptom_severity, int(prediction[0]))
        result_message = f"Confidence: {confidence * 100:.2f}%\n{result}"
        messagebox.showinfo("Prediction Result", result_message)

def run_ui():
    root = tk.Tk()
    app = EmergencyPredictorUI(root)
    root.mainloop()