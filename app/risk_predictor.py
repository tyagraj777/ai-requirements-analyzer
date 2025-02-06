import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load sample historical project data
df = pd.read_csv("data/historical_projects.csv")

# Features: Complexity, Team Size, Timeline
X = df[["complexity", "team_size", "timeline_weeks"]]
y = df["risk_level"]  # 0 = Low Risk, 1 = High Risk

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

def predict_risk(complexity, team_size, timeline_weeks):
    """Predicts project risk based on input factors."""
    X_input = scaler.transform([[complexity, team_size, timeline_weeks]])
    risk = model.predict(X_input)
    return "High Risk" if risk[0] == 1 else "Low Risk"
