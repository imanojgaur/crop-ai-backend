# 🌱 Intelligent Crop Recommendation Engine 

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

A high-performance Machine Learning API that predicts the optimal crop to plant based on soil metrics and environmental conditions. 

*If you are looking for the frontend interface, please visit the [Next.js Frontend interface](https://dap-plant-app.vercel.app/services/crop-recommend) and for repository [Next.js frontend repository](https://github.com/imanojgaur/DAP)*

## 📖 Table of Contents
- [About the Project](#-about-the-project)
- [Architectural Upgrades](#-architectural-upgrades-flask-vs-fastapi)
- [Tech Stack](#️-tech-stack)
- [Security & Environment Variables](#-security--environment-variables)
- [API Reference](#-api-reference)
- [Local Development Setup](#-local-development-setup)
- [Directory Structure](#-directory-structure)
- [Contributing](#-contributing)

---

## 🎯 About the Project

- The Intelligent Crop Recommendation engine is a modern backend microservice
- Its aim is precise agricultural decision-making. 
- It analyzing soil nutrient levels (N, P, K) and environmental factors (Temperature, Humidity, pH, Rainfall), 
- The API serves real-time machine learning predictions on the most suitable crops to maximize yield.

---

## 🚀 Architectural Upgrades (Flask vs. FastAPI)

This repository houses the modernized backend, which was recently upgraded from a legacy Flask architecture to **FastAPI** to achieve production-grade performance and safety:

* **ASGI Thread-Pooling:** 
- Replaced Flask's blocking WSGI architecture. 
- CPU-heavy Scikit-Learn predictions (`.predict()`) are automatically offloaded to background thread.
- It keeps the main event loop 100% unblocked for concurrent web traffic.

* **Strict Type Validation:** 
- Integrated **Pydantic Schema** to validate incoming JSON payloads. 
- Invalid data types from the frontend are instantly rejected with clean `422 Unprocessable Entity` errors before they can reach or crash the AI model.

* **Server-to-Server Security:** 
- Implemented a strict Dependency Injection bouncer pattern. 
- The API is locked down behind a required `x-api-key` header
- This ensures only authorized servers (like our Next.js frontend) can trigger the AI math.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI (Python)
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Processing:** NumPy, Pandas
* **Model Serialization:** Pickle
* **Security:** `python-dotenv`, HTTP Header Authentication

---

## 🔒 Security & Environment Variables

This API is designed to communicate exclusively with a trusted server (e.g., Next.js Server Actions). It does not use CORS. Instead, it relies on a cryptographic API key.

Create a `.env` file in the root directory:

```env
# A secure 64-character hex string
CROP_BACKEND_SECRET_KEY=your_generated_secret_key_here

```

> **Note:** The server includes a self-destruct tripwire. If this environment variable is missing on boot, the server will intentionally crash via `RuntimeError` to prevent deploying an unprotected endpoint to production.

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
* `422 Unprocessable Entity`: The JSON payload is missing fields or contains invalid data types.
* `500 Internal Server Error`: The AI model encountered a critical math or NumPy failure.

---

## 💻 Local Development Setup

1. **Clone the Repository:**
```bash
git clone [https://github.com/imanojgaur/crop-ai-backend.git](https://github.com/imanojgaur/crop-ai-backend.git)
cd crop-ai-backend

```


2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Train the Model (If `.pkl` is missing or dataset is updated):**
Ensure you have your raw dataset and run the training script to generate the serialized model.
```bash
python train.py

```


5. **Start the FastAPI Server:**
```bash
uvicorn main:app --reload --port 8000

```


*The app will start on `localhost:8000`.*

6. **View Interactive Docs:**
Open your browser and navigate to `http://localhost:8000/docs` to test the API directly using the built-in Swagger UI.

---

## 📁 Directory Structure

```text
├── Data/
│   ├── Crop_NPK.csv                  # Raw nutrient values 
│   └── crop_recommendation.csv       # Training dataset
├── Crop_Recommendation2.pkl          # Serialized Random Forest Model
├── main.py                           # Main FastAPI application
├── train.py                          # ML Training script
├── requirements.txt                  # Python dependencies
└── .env                              # Environment variables (Git Ignored)

```

---

## 🤝 Contributing

Contributions are highly encouraged! To get started:

1. **Fork the Repository** and clone it locally.
2. **Create a New Branch** for your feature or bug fix:
```bash
git checkout -b feature/YourFeatureName

```


3. **Commit Changes** and push to your branch:
```bash
git push origin feature/YourFeatureName

```


4. **Submit a Pull Request** for review.

---

*Enjoy farming smarter! 🌱✨*
