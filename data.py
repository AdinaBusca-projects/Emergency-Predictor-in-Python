import pandas as pd
import random

def generate_randsample():
    def rand(): return random.randint(0,5)
    
    age = random.randint(18,90)
    symptoms = {
        "chest_pain": rand(),
        "dizziness": rand(),
        "past_stroke": rand(),
        "shortness_breath": rand(),
        "fever": rand(),
        "high_heart_rate": rand(),
        "nausea": rand(),
        "fatigue": rand(),
        "headache": rand(),
        "vomiting": rand(),
        "blurred_vision": rand(),
        "numbness": rand(),
        "loss_consciousness": rand(),
        "difficulty_speaking": rand(),
    }
    
    critical_symptoms = [
        "chest_pain", "shortness_breath", "loss_consciousness", 
        "high_heart_rate", "difficulty_speaking"
    ]
    
    symptoms_score = sum(symptoms.values())
    critical_symptoms_score = sum(symptoms[s] for s in critical_symptoms)
    
    age_risk = 1 if age > 50 else 0
    
    #scores (0 to 1)
    total_score = symptoms_score / 70
    only_critical_symptoms_score = critical_symptoms_score / 25
    
    base_probability = (
        0.4 * total_score +
        0.5 * only_critical_symptoms_score +
        0.1 * age_risk
    )
    
    emergency = 1 if base_probability > 0.6 else 0
    
    return {
        "age": age,
        **symptoms,
        "emergency": emergency
    }
    
def load_mock_data(num_samples=300):
    return pd.DataFrame([generate_randsample() for _ in range(num_samples)])