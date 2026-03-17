import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

import joblib

BASE_DIR = os.path.dirname(__file__)

DATASET_PATH = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "mood_training_data.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "mood_risk_model.pkl"
)


def load_model():
    print("Looking for model at:", MODEL_PATH)

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

    model = joblib.load(MODEL_PATH)

    return model

def predict_mood_risk(answers, sleep_hours):
    """
    Predict depression risk level from questionnaire answers.
    """

    model = load_model()

    input_data = pd.DataFrame(
        [[answers[0], answers[1], answers[2], answers[3], answers[4], sleep_hours]],
        columns=["q1", "q2", "q3", "q4", "q5", "sleep_hours"]
    )

    prediction = model.predict(input_data)[0]

    phq_score = sum(answers)

    return {
        "risk_level": prediction,
        "score": phq_score
    }

def load_dataset():
    """
    Load mood dataset and split features and labels.
    """

    df = pd.read_csv(DATASET_PATH)

    print("Dataset loaded successfully.")
    print("Dataset shape:", df.shape)

    return df

def prepare_features(df):
    """
    Prepare feature matrix X and target vector y.
    """

    X = df[["q1", "q2", "q3", "q4", "q5", "sleep_hours"]]

    y = df["risk_level"]

    return X, y

def train_model(X, y):
    """
    Train Random Forest classifier on the dataset.
    """

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    """
    Evaluate trained model performance.
    """

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\nModel Evaluation Results")
    print("------------------------")
    print("Accuracy:", accuracy)

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    
def save_model(model):
    """
    Save trained model to disk.
    """

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print("\nModel saved successfully.")
    print(f"Saved to: {MODEL_PATH}")
    
if __name__ == "__main__":

    print("Starting mood risk model training...")

    df = load_dataset()

    X, y = prepare_features(df)

    model, X_test, y_test = train_model(X, y)

    evaluate_model(model, X_test, y_test)

    save_model(model)

    print("\nTraining pipeline completed successfully.")
