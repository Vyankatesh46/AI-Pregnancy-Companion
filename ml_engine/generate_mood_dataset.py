import csv
import random
import os

random.seed(42)

DATASET_SIZE = 5000

OUTPUT_PATH = os.path.join(
    "data",
    "raw",
    "mood_training_data.csv"
)

COLUMNS = [
    "q1",
    "q2",
    "q3",
    "q4",
    "q5",
    "sleep_hours",
    "phq_score",
    "risk_level"
]

def generate_phq_answers():
    """
    Generate realistic PHQ questionnaire responses.
    Each question value ranges from 0 to 3.
    """

    answers = []

    for _ in range(5):
        value = random.choices(
            population=[0, 1, 2, 3],
            weights=[0.4, 0.3, 0.2, 0.1]
        )[0]

        answers.append(value)

    return answers

def generate_sleep_hours():
    """
    Generate realistic sleep hours for pregnant users.
    """

    sleep = random.choices(
        population=[4,5,6,7,8],
        weights=[0.1,0.2,0.3,0.3,0.1]
    )[0]

    return sleep

def calculate_phq_score(answers):
    """
    Calculate PHQ score from questionnaire responses.
    """

    return sum(answers)

def determine_risk_level(phq_score):
    """
    Convert PHQ score into depression risk level.
    """

    if phq_score <= 4:
        return "Low"

    elif phq_score <= 9:
        return "Moderate"

    else:
        return "High"
    
def generate_dataset():
    """
    Generate the synthetic mood training dataset
    and save it to CSV.
    """

    rows = []

    for _ in range(DATASET_SIZE):

        answers = generate_phq_answers()

        sleep_hours = generate_sleep_hours()

        phq_score = calculate_phq_score(answers)

        risk_level = determine_risk_level(phq_score)

        row = answers + [sleep_hours, phq_score, risk_level]

        rows.append(row)

    return rows

def save_dataset(rows):
    """
    Save dataset rows to CSV file.
    """

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(COLUMNS)

        writer.writerows(rows)
        
if __name__ == "__main__":

    dataset_rows = generate_dataset()

    save_dataset(dataset_rows)

    print("Dataset generation complete.")
    print(f"Saved to: {OUTPUT_PATH}")