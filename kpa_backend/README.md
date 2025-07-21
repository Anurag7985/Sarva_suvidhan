
# Sarva Suvidhan KPA Backend

Welcome! This project powers the backend API for managing wheel specification forms. It’s built with Django REST Framework and PostgreSQL, following best practices for reliability, security, and maintainability.


### Prerequisites
- Python 3.12 or newer
- PostgreSQL database
- pip (Python package manager)

### Getting Started
1. **Get the code:** Clone this repo or unzip the source files.
2. **Set up a virtual environment (recommended):**
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On Mac/Linux
    ```
3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
4. **Configure your database:**
    - Create a PostgreSQL database and user.
    - Add your database credentials to a `.env` file (see below).
5. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```
6. **Start the server:**
    ```sh
    python manage.py runserver
    ```

---

## 🛠️ Tech Stack
- Python 3.12
- Django 5.2
- Django REST Framework
- PostgreSQL
- pytest-django (for testing)
- python-dotenv (for environment variables)

---

## 📋 API Overview

### 1. Submit Wheel Specification Form (POST)
- **Endpoint:** `/api/forms/wheel-specifications/`
- **Method:** POST
- **What it does:** Lets you submit a new wheel specification form. All required fields go in the request body.
- **Sample Request:**
  ```json
  {
     "formNumber": "WHEEL-2025-001",
     "submittedBy": "user_id_123",
     "submittedDate": "2025-07-03",
     "fields": {
        "axleBoxHousingBoreDia": "280 (+0.030/+0.052)",
        "bearingSeatDiameter":   "130.043 TO 130.068",
        "condemningDia":         "825 (800-900)",
        "intermediateWWP":       "20 TO 28",
        "lastShopIssueSize":     "837 (800-900)",
        "rollerBearingBoreDia":  "130 (+0.0/-0.025)",
        "rollerBearingOuterDia": "280 (+0.0/-0.035)",
        "rollerBearingWidth":    "93 (+0/-0.250)",
        "treadDiameterNew":      "915 (900-1000)",
        "variationSameAxle":     "0.5",
        "variationSameBogie":    "5",
        "variationSameCoach":    "13",
        "wheelDiscWidth":        "127 (+4/-0)",
        "wheelGauge":            "1600 (+2,-1)",
        "wheelProfile":          "29.4 Flange Thickness"
     }
  }
  ```

### 2. Get Wheel Specification Forms (GET)
- **Endpoint:** `/api/forms/wheel-specifications/`
- **Method:** GET
- **What it does:** Fetches wheel specification forms. You can filter by `formNumber`, `submittedBy`, or `submittedDate` using query parameters.
- **Sample Response:**
  ```json
  {
     "success": true,
     "message": "Filtered wheel specification forms fetched successfully.",
     "data": [ ... ]
  }
  ```

---

## 📝 Testing the APIs
- Use Postman to send requests to the endpoints.
- Set `Content-Type: application/json` in your headers.
- Check out the included Postman collection for working examples.

---

## ⚙️ Environment Variables
Create a `.env` file in your project root with:
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
```

---

## ✅ Best Practices
- Always use a virtual environment for Python projects.
- Keep your `SECRET_KEY` and database credentials out of source control.
- Write clear, descriptive commit messages.
- Test your APIs thoroughly before submission.
- Document any limitations or assumptions in your README.

---

## 📦 requirements.txt
```
Django>=5.2
psycopg2-binary>=2.9.9
pytest-django>=4.5.2
djangorestframework>=3.15.0
python-dotenv>=1.0.1
```

---

## ❗ Limitations & Assumptions
- Only backend APIs are implemented; no frontend integration.
- All required fields must be present in the request body.
- Database credentials are managed via environment variables.

---

## 📧 Submission Checklist
- [x] Source code zipped or on GitHub
- [x] Postman collection exported and uploaded
- [x] README file complete and uploaded
- [x] Screen recording uploaded and named correctly
- [x] Email with all links ready

