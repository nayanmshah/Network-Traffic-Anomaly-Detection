from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def train_isolation_forest(X_train):
    # Train Isolation Forest model
    iso_forest = IsolationForest(contamination=0.01, random_state=42)
    iso_forest.fit(X_train)
    return iso_forest

def predict_anomalies(model, X_test):
    # Predict anomalies: -1 for anomalies, 1 for normal data
    y_pred = model.predict(X_test)
    return y_pred

def visualize_anomalies(X_test, y_pred):
    # Reduce to 2D using PCA for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_test)

    # Plot anomalies (in red) and normal points (in blue)
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=(y_pred == -1), cmap='coolwarm', edgecolor='k', s=50)
    plt.title('Anomaly Detection using Isolation Forest')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
