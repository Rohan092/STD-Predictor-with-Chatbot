# STD-Predictor-with-Chatbot
🔍 Overview<Br>
Furiosa Care 2.0 is a machine learning-based web application designed to predict Sexually Transmitted Disease (STD) status using real patient data. Built as a college-level project, it demonstrates full-stack ML deployment — from data preprocessing to model training, evaluation, and integration with a Flask web interface. The app also features a smart chatbot powered by Cohere's NLP API for user interaction.<br>

# ✨ Features
🧠 Predict STD status based on medical input data<br>

🤖 Trains and evaluates 5 ML models<br>

📊 Measures performance using Accuracy, F1 Score, and a Combined Score<br>

🌐 Web interface built with Flask for real-time prediction<br>

💬 Integrated AI chatbot for additional guidance (via Cohere)<br>

💾 Saves models using Pickle for easy loading during prediction<br>

# ✅ Key Points
• Full machine learning pipeline: preprocessing → training → evaluation → deployment<br>

• Trains multiple models and compares them side-by-side<br>

• Uses a custom hybrid metric to combine accuracy and F1 score<br>

• Handles missing data and ensures clean inputs<br>

• Easily extendable and deployable<br>

# ⚙️ How It Works
## Data Preprocessing (model.py)

• Reads the STD.csv dataset<br>

• Drops missing values and irrelevant columns<br>

• Splits data into training and test sets<br>

## Model Training & Evaluation<br>

• Trains 5 models: Decision Tree, Logistic Regression, Random Forest, SVM, KNN<br>

• Evaluates each using:
Accuracy Score<br>
F1 Score<br>
Combined score: (Accuracy + F1) / 2<br>
• Saves models as .pkl using Pickle

## Web Interface (app.py)

• User inputs features on a simple HTML form<br>

• The app loads the trained model and makes predictions<br>

• Displays either: STD Positive or STD Negative<br>

## AI Chatbot

• User can type a message<br>

• Input is sent to Cohere NLP API<br>

• App displays an intelligent reply<br>

# 🛠 Tech Stack

Category  :	Tools / Libraries<br>
Programming  : 	Python<br>
ML Libraries : 	Pandas, Scikit-learn, Pickle<br>
Web Framework : 	Flask<br>
Frontend  :	 HTML, CSS<br>
Dataset	 :  Custom Healthcare Dataset (STD.csv)<br>
NLP Integration  :	Cohere API<br>
Development	  :  Jupyter Notebook, VSCode<br>
