import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

def build_and_save_model():
    print("🔄 Loading baseline training logs...")
    try:
        df = pd.read_csv("logs.csv")
    except FileNotFoundError:
        print("❌ Error: logs.csv not found to establish baseline training!")
        return

    # Process baseline features
    df['status'] = df['status'].map({'success': 0, 'failed': 1}).fillna(1)
    features = ['status', 'attempts', 'duration_ms', 'bytes_sent']
    X = df[features].fillna(0)

    # Train model
    print("🤖 Training Isolation Forest baseline...")
    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(X)

    # Save the trained model brain to disk
    joblib.dump(model, "security_model.pkl")
    print("💾 Model successfully trained and saved as 'security_model.pkl'!")

if __name__ == "__main__":
    build_and_save_model()