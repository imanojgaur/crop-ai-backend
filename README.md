Greetings Traveler. 🧙‍♂️

# Intelligent Crop Recommendation Engine🌾

A high-performance Machine Learning API that predicts the optimal crop to plant based on soil metrics and environmental conditions. 

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)


## 🛠️ Tech Stack
* **Framework:** FastAPI (Python)
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Processing:** NumPy, Pandas
* **Model Loading:** Pickel
* **Security:** `python-dotenv`, HTTP Header Authentication


## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Architectural](#-architectural)
- [Tech Stack](#️-tech-stack)
- [Security & Environment Variables](#-security--environment-variables)
- [API Reference](#-api-reference)
- [Local Development Setup](#-local-development-setup)
- [Directory Structure](#directory-structure)
- [Usage](#usage)
- [Contributing](#contributing)

---

## About the Project

The Intelligent Crop Recommendation engine is a FastAPI based recommendation system aimed for precise crop decision making by utilizing machine learning models. By analyzing soil nutrient levels and environmental factors, the api provides recommendations on the most suitable crops. 

---


## Features

- **Crop Recommendation API:** Suggests the best crops based on soil nutrient content and environmental data.
---

## 🚀 Architectural 

* **ASGI Thread-Pooling:** Replaced Flask's blocking WSGI architecture. CPU-heavy Scikit-Learn predictions (`.predict()`) are automatically offloaded to background threads, keeping the main event loop 100% unblocked for concurrent traffic.
* **Strict Type Validation:** Integrated **Pydantic** to validate incoming JSON payloads. Invalid data types from the frontend are instantly rejected with clean `422 Unprocessable Entity` errors before they can crash the AI model.
* **Server-to-Server Security:** Implemented a strict Dependency Injection bouncer pattern. The API is locked down behind a required `x-api-key` header, ensuring only authorized servers (like our Next.js frontend) can trigger the AI math.

---


#### This repository houses the modern **FastAPI** backend,
 - provide strict data validation,   
 - tokenised secure server-to-server communication.

---






---

## 🔒 Security & Environment Variables

This API is designed to communicate exclusively with a trusted server (e.g., Next.js Server). It does not use CORS. Instead, it relies on a cryptographic API key.

Create a `.env` file in the root directory:

```env
# A secure 64-character hex string
CROP_BACKEND_SECRET_KEY=your_generated_secret_key_here

```

> **Note:** The server includes a self-destruct tripwire. If this environment variable is missing on boot, the server will intentionally crash via `RuntimeError` to prevent deploying an unprotected endpoint.

---

## 📡 API Reference

### Predict Crop

Predicts the best crop based on 7 environmental features.

**Endpoint:** `POST /predict`

**Headers Required:**

```http
Content-Type: application/json
x-api-key: <CROP_BACKEND_SECRET_KEY>

```

**Request Body (JSON):**

```json
{
  "N": 90.0,
  "P": 42.0,
  "K": 43.0,
  "temperature": 20.8,
  "humidity": 82.0,
  "ph": 6.5,
  "rainfall": 202.9
}

```

**Success Response (200 OK):**

```json
{
  "recommended_crop": "rice"
}

```

**Error Responses:**

* `401 Unauthorized`: The `x-api-key` header is missing or incorrect.
* `422 Unprocessable Entity`: The JSON payload is missing fields or contains invalid data types (e.g., strings instead of floats).
* `500 Internal Server Error`: The AI model encountered a math or NumPy failure.

---

## 💻 Local Development Setup

1. **Clone the Repository:**

```bash
   git clone https://github.com/imanojgaur/crop-ai-backend.git
   cd crop-ai-backend
```


2. **Create a virtual environment & install dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install fastapi uvicorn numpy scikit-learn pydantic python-dotenv

```


3. **Train the Model (If `.pkl` is missing or something break):**
Ensure you have your raw dataset and run the training script to generate `Crop_Recommendation2.pkl`.
```bash
python train.py

```


4. **Start the FastAPI Server:**
```bash
uvicorn main:app --reload --port 8000

```
The app will start on `localhost:8000` .


5. **View Interactive Docs:**
Open your browser and navigate to `http://localhost:8000/docs` to test the API directly using the Swagger UI.


## Directory Structure

### Data Directory
- **Data/Crop_NPK.csv** and **Data/crop_recommendation.csv**: Contain nutrient values and recommendations for different crops.

### Models
Crop_Recommendation2.pkl: Saved model file used for crop recommendations.

### Application Files
- **app.py**: Main application file. 
- **requirements.txt** : Specify Python dependencies .


---

* * *

Usage
-----

* * *

Contributing
------------

Contributions are highly encouraged! To get started:

1.  **Fork the Repository** and clone it locally.
2.  **Create a New Branch** for your feature or bug fix:
    
    ```bash
    git checkout -b feature/YourFeatureName
    ```
    
3.  **Commit Changes** and push to your branch:
    
    ```bash
    git push origin feature/YourFeatureName
    ```
    
4.  **Submit a Pull Request** for review.

* * *

* * *

With the Intelligent Crop Recommendation API, you can easily determine the optimal crops and fertilizers tailored to specific soil and environmental conditions. Whether you are a developer, farmer, or agricultural scientist, we welcome your contributions and feedback to improve the system.

Enjoy farming smarter! 🌱✨

* * *
