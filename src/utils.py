import pandas as pd

def save_model(model, filename):
    """Save trained model to file."""
    import joblib
    joblib.dump(model, filename)

def load_model(filename):
    """Load saved model from file."""
    import joblib
    return joblib.load(filename)

def load_data(file_path):
    """Helper function to load data."""
    return pd.read_csv(file_path)
