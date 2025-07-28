
# 🎬 Movie Recommender System

A sleek, full-stack movie recommendation web application that lets users select a movie they like and get visually appealing suggestions for similar movies. Powered by content-based filtering and a modern, responsive UI built with Tailwind CSS and Flask.

---

## 🌟 Features

* 🔍 **Movie Selection Dropdown** — Choose your favorite movie from a preloaded list.
* 🤖 **Smart Recommendations** — Backend model recommends similar movies based on cosine similarity of features.
* 🎨 **Beautiful UI** — Tailwind CSS-styled interface with animated poster cards.
* 🚀 **Fast & Lightweight** — Uses minimal dependencies for rapid local deployment.
* 📱 **Responsive Design** — Works great on both mobile and desktop.

---

## 🛠️ Tech Stack

| Frontend             | Backend       | ML & Data            |
| -------------------- | ------------- | -------------------- |
| HTML5, Tailwind CSS  | Flask, Jinja2 | Pandas, scikit-learn |
| JavaScript (vanilla) | Python        | Cosine Similarity    |

---


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, manually install:

```bash
pip install flask pandas scikit-learn
```

### 4. Run the App

```bash
python app.py
```

Navigate to `http://localhost:5000` in your browser.

---

## 📊 How It Works

1. The user selects a movie from the dropdown.
2. The backend (Flask) fetches similar movies using **cosine similarity** on feature vectors.
3. Recommendations and poster URLs are returned as JSON.
4. JavaScript dynamically injects the movie cards into the UI.

---
<img width="1440" height="821" alt="Screenshot 2025-07-28 at 8 58 57 PM" src="https://github.com/user-attachments/assets/33d0609e-5f7f-4692-a8bc-c03c336c9c02" />


---

<img width="1440" height="823" alt="Screenshot 2025-07-28 at 8 58 02 PM" src="https://github.com/user-attachments/assets/c8993355-7b2d-40e5-a30b-b1c9e3416f14" />


## 🧠 Model Details

* **Model:** Content-Based Filtering
* **Features Used:** Movie metadata (e.g., genres, cast, keywords)
* **Similarity Metric:** Cosine Similarity

Training logic and vector generation is handled inside `Recommendation_Model.ipynb`.

---



