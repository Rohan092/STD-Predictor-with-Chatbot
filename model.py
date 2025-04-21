import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,f1_score
import pickle

df = pd.read_csv("STD.csv")
df = df.drop(columns=['S.no'])
df = df.dropna()

X = df.drop('STD Status', axis=1)
y = df['STD Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "DecisionTree": DecisionTreeClassifier(),
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(),
    "SVM": SVC(),
    "KNN": KNeighborsClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    

    with open(f"{name}_model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='binary')
    combined_score = (accuracy + f1) / 2 
    print(f"{name} Accuracy: {accuracy * 100:.2f}%")
    print(f"{name} F1 Score: {f1:.2f}")
    print(f"{name} Combined Score (Avg of Accuracy & F1): {combined_score:.2f}")
    print("-" * 50)