# STD-Predictor-with-Chatbot
🔍 Overview<Br>
Furiosa Care 2.0 is a machine learning-based web application designed to predict Sexually Transmitted Disease (STD) status using real patient data. Built as a college-level project, it demonstrates full-stack ML deployment — from data preprocessing to model training, evaluation, and integration with a Flask web interface. The app also features a smart chatbot powered by Cohere's NLP API for user interaction.<br>

# ✨ Features
🧠 Predict STD status based on medical input data<br>

🤖 Trains and evaluates 5 ML models :  Decision Tree, Logistic Regression, Random Forest, SVM, and KNN<br>

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

# Repository Structure
Data : https://github.com/Rohan092/STD-Predictor-with-Chatbot.git
# 📷 Screenshots
![Screenshot 2025-04-14 145714](https://github.com/user-attachments/assets/1d7c4289-683f-46c5-8f4f-6ad2aba5e9a6)<br>
![Screenshot 2025-04-14 145745](https://github.com/user-attachments/assets/4ab62686-7cec-48be-97d3-d0e02942a288)<br>
![Screenshot 2025-04-14 145815](https://github.com/user-attachments/assets/fb994d46-5da6-44d0-a554-150262dc99cd)<br>
![Screenshot 2025-04-14 145842](https://github.com/user-attachments/assets/a84a39f2-46a0-4cdd-b0fb-3c527e0857c5)<br>
![Screenshot 2025-04-14 145905](https://github.com/user-attachments/assets/641cd6c0-4bf6-4b7b-9d92-a708226f7a17)<br>
![Screenshot 2025-04-14 145937](https://github.com/user-attachments/assets/42eb1543-6393-43ad-9079-1eb9688416f3)<br>


# 🔗 How to Run
1. Clone the repo
2. Install dependencies
3. Run app.py
4. Open localhost:5000 in your browser

# Feedback & Collabration
Your feedback is always appreciated! If you’re interested in collaborating on similar projects or discussing new opportunities, feel free to reach out. I’m always open to connecting and sharing insights!
