# Peat Notify Documentation

## Overview

**Peat Notify** is an email notification service based on the amount of food available in a pet feeder. The service runs continuously and, at regular intervals, makes a request to the API to check the current food quantity. If the quantity is below a predefined threshold, it retrieves a list of emails from the API and sends a predefined message to each one.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/viniciusmecosta/PeatNotify.git
cd PeatNotify
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Create a `.env` File

Create a `.env` file in the root directory of the project and add the following environment variables:

```
EMAIL_SENDER=email@email.com
EMAIL_PASS=passpass
API_URL=http://127.0.0.1:8000
API_TOKEN=token
```

> These variables are used to authenticate and send emails, and to connect to the API.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Service

```bash
python app/main.py
```

This will start the notification loop which checks the food quantity and sends emails when necessary.

---

## API

This service consumes data from the [Peat Data API](https://github.com/viniciusmecosta/PeatData.git).

---

## Built With

- Python
- `requests` for API communication
- `smtplib` for email delivery
- `python-dotenv` for managing environment variables

---
