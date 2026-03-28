# Healcom - Smart Healthcare Dashboard

Healcom is a modern Django-based healthcare platform designed to streamline post-operative recovery tracking and communication between patients and doctors.

## 🚀 Features
- **Smart Patient Dashboard**: Interactive recovery logging with pain maps and milestone tracking.
- **AI-Powered Analytics**: Trend analysis using Least Squares Linear Regression to predict recovery paths.
- **Real-time Messaging**: Secure communication channel for patients and assigned medical staff.
- **HealBot AI Assistant**: Contextual recovery advice powered by a custom-built rule engine.
- **Payment Integration**: Standard UPI "Scan & Pay" system for educational medical resources.

## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Vanilla CSS3 (Flex/Grid), Chart.js, Vanilla JavaScript
- **Database**: MySQL
- **Auth**: Django Allauth (Google SSO Support)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/healcom.git
   cd healcom
   ```

2. **Setup Virtual Environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Database Configuration:**
   - Create a MySQL database named `healcom_db`.
   - Update `DATABASES` settings in `healcom/settings.py` or use environment variables.
   - Import the provided SQL dump:
     ```bash
     mysql -u root -p healcom_db < healcom_database_backup.sql
     ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start Server:**
   ```bash
   python manage.py runserver
   ```

## 📄 License
This project is for educational purposes. All rights reserved.
