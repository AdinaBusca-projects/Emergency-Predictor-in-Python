import joblib  
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from data import load_mock_data
import matplotlib.pyplot as plt

MODEL_PATH = "emergency_predictor_model.pkl"

def save_model(model):
    """Save trained model to file"""
    joblib.dump(model,MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    
def load_model():
    """Load trained model from file"""
    try:
        model = joblib.load(MODEL_PATH)
        print(f"Model loaded from {MODEL_PATH}")
        return model
    except FileNotFoundError:
        print("Model file not found. A new model will be trained.")
        return None
    
def train_model():
    #check if trained model exists
    model = load_model()
    if model is not None:
        return model
    
    df = load_mock_data()
    features = df.columns.drop("emergency")
    X = df[features]
    y = df["emergency"]
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
    
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    acc = accuracy_score(y_test,model.predict(X_test))
    print(f"\n[INFO] Model Accuracy: {acc * 100:.2f}%")
    
    #show feature importance
    importances = model.feature_importances_
    plt.figure(figsize=(10,6))
    plt.barh(features,importances)
    plt.title("Symptom Importance for Emergency Prediction")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.show()
    
    #save model after trained
    save_model(model)
    
    return model