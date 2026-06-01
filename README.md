# Disease Prediction Application

A Flask-based web application that uses machine learning to predict disease likelihood from symptom inputs.

## Features

- User login interface
- Symptom collection form
- Disease prediction using Decision Tree Classifier
- Result display with predicted disease

## Local Setup

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open `http://localhost:5000`

## Deployment

This project is ready for deployment using a WSGI server like `gunicorn`.

- `Procfile` is configured for deployment with:
  ```bash
  web: gunicorn app:app
  ```

## Notes

- Make sure `dataset.csv` is present in the repo root.
- The app uses the `PORT` environment variable when running in production.
