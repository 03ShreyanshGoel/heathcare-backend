# 🏥 Healthcare Backend

A **Django REST API** for a healthcare system, built with **Django REST Framework (DRF)** and **PostgreSQL**.
It supports **JWT authentication**, **patient/doctor management**, and **patient-doctor mappings**.

---

## ✨ Features

* 🔐 **JWT Authentication** with `djangorestframework-simplejwt`
* 👨‍⚕️ **CRUD operations** for Patients (user-specific) and Doctors
* 🔗 **Patient-Doctor mapping** with ownership validation
* 🗄 **PostgreSQL database** with Django ORM
* ⚙️ **Secure configuration** using `.env`
* 🛡 **Robust error handling**

---

## 🛠 Tech Stack

* **Backend:** Django 4.x, Django REST Framework
* **Auth:** djangorestframework-simplejwt
* **Database:** PostgreSQL 16.x
* **Language:** Python 3.x
* **Utilities:** python-dotenv, psycopg2-binary

---

## 🚀 Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/healthcare-backend.git
cd healthcare-backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary python-dotenv
```

### 4️⃣ Setup Environment Variables

Create a `.env` file in the project root:

```ini
SECRET_KEY=hja628aom&w+kw1w$c4!!f1awitb(7!rs53v=1i9y81@03z86#
DB_PASSWORD=Shiggysonu@3
```

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Access at 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗄 Database

* **DB Name:** `healthcare_db`
* **Tables:**

  * `api_user`
  * `api_patient`
  * `api_doctor`
  * `api_patientdoctormapping`
  * Default Django tables (`auth_*`, `django_*`)

Check tables:

```sql
\dt
SELECT id, user_id, name FROM api_patient;
```

---

## 📡 API Endpoints

All **authenticated endpoints** require:

```http
Authorization: Bearer <access_token>
```

(Access tokens expire in **5 minutes**)

---

### 🔑 Authentication

#### Register User

```http
POST /api/auth/register/
```

```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{"name":"Test User","email":"test@example.com","password":"strongpass123"}'
```

#### Login (Get JWT Tokens)

```http
POST /api/auth/login/
```

#### Refresh Token

```http
POST /api/auth/refresh/
```

---

### 👨‍⚕️ Patient Management

* `POST   /api/patients/` → Create patient
* `GET    /api/patients/` → List user’s patients
* `GET    /api/patients/<id>/` → Get patient
* `PUT    /api/patients/<id>/` → Update patient
* `DELETE /api/patients/<id>/` → Delete patient

Example:

```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"name":"John Doe","date_of_birth":"1990-01-01","gender":"Male","address":"123 Main St","phone":"555-1234"}'
```

---

### 🩺 Doctor Management

* `POST   /api/doctors/` → Create doctor
* `GET    /api/doctors/` → List doctors
* `GET    /api/doctors/<id>/` → Get doctor
* `PUT    /api/doctors/<id>/` → Update doctor
* `DELETE /api/doctors/<id>/` → Delete doctor

---

### 🔗 Patient-Doctor Mapping

* `POST   /api/mappings/` → Assign doctor to patient
* `GET    /api/mappings/` → List mappings
* `GET    /api/mappings/<id>/` → Get doctors for patient
* `DELETE /api/mappings/<id>/` → Remove mapping

Example:

```bash
curl -X POST http://127.0.0.1:8000/api/mappings/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <access_token>" \
-d '{"patient":1,"doctor":1}'
```

---

## 🧪 Testing

### Using `curl`

```bash
set TOKEN=<access_token>
curl -X POST http://127.0.0.1:8000/api/patients/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer %TOKEN%" \
-d '{"name":"John Doe","date_of_birth":"1990-01-01","gender":"Male","address":"123 Main St","phone":"555-1234"}'
```

### Using Postman

* Import `curl` commands
* Or manually set `Authorization` header

### Database Check

```sql
SELECT * FROM api_patientdoctormapping;
```

---

## 🐞 Troubleshooting

* **401 Unauthorized** → Refresh token or re-login
* **400 Bad Request** → Check patient ownership

```sql
SELECT id, user_id FROM api_patient WHERE user_id=<user_id>;
```

* **Database/Server issues**

```bash
python manage.py runserver
net start postgresql-x64-16
```

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.
