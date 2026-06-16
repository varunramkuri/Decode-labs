import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def run_classification_pipeline():
    print("--- PHASE 1: INPUT ---")
    # 1. Load the Iris Benchmark
    iris = load_iris()
    X = iris.data  # 4 Dimensions: Sepal/Petal Length and Width
    y = iris.target # 3 Classes: Setosa, Versicolor, Virginica
    print(f"Dataset Loaded: {X.shape[0]} samples, {X.shape[1]} dimensions.")

    # 2. Structural Integrity: Train-Test Split (80% Train, 20% Test)
    # The random_state ensures reproducibility, while shuffle=True removes order bias.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)
    print(f"Data Split: {len(X_train)} Training samples, {len(X_test)} Testing samples.")

    # 3. The Gatekeeper Rule: Scaling
    # StandardScaler transforms data to have Mean = 0, Variance = 1
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("Data Scaling Complete (StandardScaler applied).\n")

    print("--- PHASE 2: PROCESS ---")
    # 4. The Workflow: Scikit-Learn
    # INSTANTIATE (Build the frame) with Optimal K=5
    model = KNeighborsClassifier(n_neighbors=5)
    
    # FIT (Memorize the map)
    model.fit(X_train_scaled, y_train)
    print("Model Training Complete (K-Nearest Neighbors, K=5).\n")

    print("--- PHASE 3: OUTPUT ---")
    # PREDICT (Apply logic)
    predictions = model.predict(X_test_scaled)
    
    # 5. Output Validation
    acc = accuracy_score(y_test, predictions)
    print(f"Baseline Accuracy: {acc * 100:.2f}%\n")
    
    print("The Diagnostic Tool: Confusion Matrix")
    # Rows are actual classes, Columns are predicted classes
    cm = confusion_matrix(y_test, predictions)
    print(cm)
    print("\nStrategic Trade-offs: Precision, Recall, and F1 Score")
    # classification_report generates precision, recall, and the F1 Score (Harmonic Mean)
    report = classification_report(y_test, predictions, target_names=iris.target_names)
    print(report)

if __name__ == "__main__":
    run_classification_pipeline()