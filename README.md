# CLOTHING_E_COMMERCE_AUTOMATED_REVIEW_SYSTEM

Customer Review Sentiment Analysis Project
## 📌 Project Overview

This project focuses on analyzing customer clothing reviews to predict sentiment using Natural Language Processing (NLP) and Machine Learning techniques.

The system processes raw customer reviews, converts text into numerical features using TF-IDF Vectorization, and predicts sentiment using a Logistic Regression model.
The trained model is deployed using a Flask API that returns predictions in JSON format, making it production-ready.

## 🎯 Problem Statement

Understanding customer sentiment helps businesses:

Improve product quality

Analyze customer satisfaction

Make data-driven decisions

This project predicts whether a review is:

❌ Negative

😐 Neutral

✅ Positive

🗂️ Dataset Description

The dataset contains 23,480+ real-world clothing reviews with structured and unstructured data.

## 📊 Key Columns

Clothing ID – Unique identifier for each product

Age – Age of the reviewer

Title – Review title

Review Text – Customer’s written feedback

Rating – Product rating (1 = Worst, 5 = Best)

Recommended IND – 1 = Recommended, 0 = Not recommended

Positive Feedback Count – Helpful votes by other users

Division Name – High-level product division

Department Name – Product department

Class Name – Specific product class

# 🧠 Machine Learning Approach
🔹 Text Preprocessing

Lowercasing

Removal of HTML tags

URL and punctuation cleaning

Stopword removal

Tokenization & Lemmatization

🔹 Vectorization
TF-IDF Vectorizer

Converts text into numerical features

Reduces importance of frequent words

Highlights meaningful terms

Efficient for large text datasets

🔹 Model Selection
Logistic Regression

Fast and interpretable

Works well with sparse TF-IDF features

Suitable for lightly imbalanced datasets

Strong baseline for NLP classification

# 🚀 Model Pipeline
Raw Review Text
     ↓
Text Cleaning
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression Model
     ↓
Sentiment Prediction

# 🌐 API Development (Flask)

A Flask REST API is created to serve predictions as JSON responses, making the model usable by:

Web applications

Streamlit dashboards

Mobile apps

Other backend services

Example JSON Output:
{
  "name": "Alice",
  "review": "This product is amazing!",
  "predicted_sentiment": "positive",
  "predicted_rating": 2
}

# **📁 Project Folder Structure**
project-root/
│
├── dataset/
│   └── clothing_reviews.csv
│   📌 Contains raw and cleaned datasets
│
├── notebook/
│   └── sentiment_analysis.ipynb
│   📌 Data exploration, preprocessing & model training
│
├── flask/
│   ├── model/
│   │   ├── LogisticRegression.pkl
│   │   └── tfidf_vectorizer.pkl
│   │   📌 Trained model and vectorizer
│   │
│   ├── api.py
│   │   📌 Flask API for prediction
│   │
│   └── test.py
│       📌 Script to test API using POST requests
│
├── documentation/
│   └── Model_and_Flask_Explanation.pdf
│   📌 Detailed explanation of model development & API
│
├── requirements.txt
│   📌 Project dependencies
│
└── README.md
    📌 Project overview and instructions

# 🧪 Testing Strategy

test.py sends multiple review texts to the Flask API

Ensures predictions work consistently

Helps validate model behavior on different inputs

# 📄 Documentation

The documentation folder contains a PDF explaining:

Model development process

Feature engineering decisions

Evaluation metrics

Flask API architecture

Request/Response workflow


# 🏁 Conclusion

This project demonstrates a complete machine learning lifecycle, from data preprocessing to model deployment using Flask, following industry best practices. It is suitable for real-world applications and scalable for future improvements.


🧠 Convert this into a project presentation (PPT)

Just tell me 👌
