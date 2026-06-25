# 🚨 Real-Time UPI Fraud Detection System

## 📌 Project Overview

The Real-Time UPI Fraud Detection System is a Machine Learning-based cybersecurity project designed to identify potentially fraudulent UPI transactions in real time. The system analyzes transaction details such as transaction amount, transaction time, device information, and location mismatch to calculate a fraud risk score and classify transactions as either safe or fraudulent.

The project simulates a real-world banking fraud detection system by continuously generating transactions and providing instant fraud analysis reports in the terminal.

---

## 🎯 Objectives

* Detect suspicious UPI transactions in real time.
* Calculate fraud risk scores using Machine Learning.
* Generate detailed fraud analysis reports.
* Store transaction history for future investigation.
* Allow users to check the status of previous transactions.

---

## ✨ Features

* Real-time transaction monitoring.
* Fraud risk score calculation.
* High, Medium, and Low risk classification.
* Transaction history logging using CSV.
* Search previous transactions by Transaction ID.
* User-controlled transaction generation (`next`, `check`, `exit`).
* Detailed fraud indicators:

  * High transaction amount
  * New device detected
  * Location mismatch
  * Unusual transaction time

---

## 🛠 Technologies Used

* Python
* Machine Learning
* Random Forest Classifier
* Pandas
* NumPy
* Scikit-learn
* CSV File Handling

---

## 📂 Project Structure

```text
upi_fraud_detection/
│
├── app.py
├── fraud_detector.py
├── transaction_generator.py
├── train_model.py
├── transactions.csv
├── transaction_log.csv
├── model.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Step 1: Clone the repository

```bash
git clone <repository-link>
cd upi_fraud_detection
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train the model

```bash
python train_model.py
```

### Step 4: Run the application

```bash
python app.py
```

---

## 📊 Sample Output

```text
=========================================
UPI FRAUD ANALYSIS REPORT
=========================================
Transaction ID : TXN264406
Timestamp      : 25-06-2026 22:33:21
User ID        : USER7640
UPI ID         : user9307@upi
Location       : Delhi, India
Amount         : ₹2975
Merchant       : ABC Electronics
Risk Score     : 17.00%
Status         : ✓ SAFE TRANSACTION
=========================================

Type 'next' for another transaction,
'check' to search a transaction,
or 'exit' to quit: exit
```

---

## 🧠 Machine Learning Model

Algorithm Used:

* Random Forest Classifier

Input Features:

* Transaction Amount
* Transaction Time
* New Device Detection
* Location Mismatch

Output:

* Fraud (1)
* Safe Transaction (0)

---

## 🔮 Future Enhancements

* Real UPI transaction dataset integration
* Live banking API integration
* Streamlit web dashboard
* Email and SMS alerts
* Database integration using SQLite or MySQL
* User authentication and admin panel
* Fraud analytics and visualization dashboard
* Deep Learning-based fraud detection

---

## 👨‍💻 Author

**Tirth Shingala**

diploma in computer engineering

Cybersecurity and Machine Learning Enthusiast

---

## 📜 License

This project is developed for educational and research purposes only.
this project is not parfectly build on real-time output