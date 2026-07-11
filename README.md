# ResuMatch — AI-Powered Resume Screener

**Live Application**: [https://resume-scan-5.onrender.com/](https://resume-scan-5.onrender.com/)

ResuMatch is a modern, AI-powered web application designed to automate and streamline the resume screening process for recruitment teams and job applicants. By leveraging Natural Language Processing (NLP) and Machine Learning (ML), the platform evaluates candidate resumes against job descriptions to predict suitability, detect fraud, calculate compatibility scores, and offer feedback for career improvement.

---

## 🚀 Key Features

*   **Eligibility Prediction**: Uses text extraction and NLP vector similarity (TF-IDF & Cosine Similarity, with local BERT fallback) to determine if a candidate's resume meets a job description's requirements.
*   **Resume Scoring**: Calculates a normalized compatibility score percentage to help recruiters prioritize the top applicants.
*   **Resume Fraud Detection**: Runs rule-based logic and NLP heuristics to flag potential fraud, exaggerated claims, or suspicious formatting patterns.
*   **Job Role Recommendations**: If an applicant is deemed not eligible for a specific role, the system automatically suggests other active job vacancies in the system that better align with their current skillset.
*   **Skill Gap Analysis & Course Recommendations**: Identifies key missing skills required for the position and recommends targeted learning courses to help the applicant bridge the gap.
*   **Django Administration Panel**: Provides a secure backend portal for recruiters to manage job postings, review applicants, and monitor screen results.

---

## 🛠️ Tech Stack

*   **Backend Framework**: Django 5.1.7 (Python 3.12+)
*   **Natural Language Processing (NLP)**: Scikit-learn, PyMuPDF (fitz), Python-docx
*   **Data Models**: SQLite (supports PostgreSQL configuration)
*   **Deployment Platforms**: Render (configured for lightweight, cached Docker/Python runtime builds)
*   **Styling & Frontend**: Vanilla HTML5, CSS3, and JavaScript

---

## 📁 Project Structure

```text
ResumeScreener/
│
├── resumescreener/          # Django Project Configuration
│   ├── settings.py          # Configuration settings (SQLite fallback, auth redirects)
│   ├── urls.py              # Root URL routing
│   └── wsgi.py / asgi.py    # Production server gateways
│
├── resume_scanner/          # Django Core Application
│   ├── migrations/          # Database schema migrations
│   ├── templates/           # HTML templates (Login, Signup, Joblist, FraudCheck)
│   ├── ml/                  # ML & Text Matching modules
│   │   ├── predict_eligibility.py   # TF-IDF & BERT Similarity Matching
│   │   ├── fraud_detection.py       # Heuristic Fraud Checking
│   │   ├── skill_gap.py             # Skill extraction and difference analysis
│   │   └── improvement_resources.py # Course recommendation engine
│   ├── models.py            # Job, Applicant, and FraudCheck models
│   ├── views.py             # Request handlers (Apply, Signin, Signup, Scoreboard)
│   └── urls.py              # Application-specific routing
│
├── app.py                   # Render production WSGI entry point
├── runtime.txt              # Render runtime engine settings
├── requirements.txt         # Package dependencies
└── manage.py                # Django CLI entry point
```

---

## 💻 Local Installation & Setup

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/SowjanyaBodala/rescume-scan.git
    cd rescume-scan
    ```

2.  **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    # Activate on Windows:
    venv\Scripts\activate
    # Activate on macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Database Migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin)**:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**:
    ```bash
    python manage.py runserver
    ```
    Access the application locally at `http://127.0.0.1:8000/`.
