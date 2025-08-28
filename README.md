Healthcare Backend
Django-based REST API for a healthcare system using Django REST Framework (DRF) and PostgreSQL. Supports user authentication (JWT), patient/doctor management, and patient-doctor mappings.
Features

JWT authentication (djangorestframework-simplejwt)
CRUD for patients (user-specific) and doctors
Assign doctors to patients with ownership validation
PostgreSQL with Django ORM
Environment variables for secure config
Error handling for invalid inputs

Technologies

Django 4.x
Django REST Framework
djangorestframework-simplejwt
PostgreSQL 16.x
Python 3.x
python-dotenv, psycopg2-binary

Setup

Navigate to Project:
cd C:\Users\Shreyansh Goel\Documents\Shreyansh\project\health-care-backend


Virtual Environment:
python -m venv venv
venv\Scripts\activate


Install Dependencies:
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary python-dotenv


Environment Variables:

Create .env in project root:SECRET_KEY=hja628aom&w+kw1w$c4!!f1awitb(7!rs53v=1i9y81@03z86#
DB_PASSWORD=Shiggysonu@3




Apply Migrations:
python manage.py makemigrations
python manage.py migrate


Run Server:
python manage.py runserver



Database

Database: PostgreSQL (healthcare_db)
Tables: api_user, api_patient, api_doctor, api_patientdoctormapping, Django tables (auth_*, django_*)
Verify:"C:\Program Files\PostgreSQL\16\bin\psql.exe" -U postgres -d healthcare_db
\dt
SELECT id, user_id, name FROM api_patient;



API Endpoints
Authenticated endpoints require Authorization: Bearer <access_token> (5-minute expiry).
Authentication

POST /api/auth/register/: Register usercurl -X POST http://127.0.0.1:8000/api/auth/register/ -H "Content-Type: application/json" -d "{\"name\": \"Test User\", \"email\": \"test@example.com\", \"password\": \"strongpass123\"}"


POST /api/auth/login/: Get JWT tokenscurl -X POST http://127.0.0.1:8000/api/auth/login/ -H "Content-Type: application/json" -d "{\"email\": \"test@example.com\", \"password\": \"strongpass123\"}"


POST /api/auth/refresh/: Refresh tokencurl -X POST http://127.0.0.1:8000/api/auth/refresh/ -H "Content-Type: application/json" -d "{\"refresh\": \"<refresh_token>\"}"



Patient Management (Authenticated)

POST /api/patients/: Add patientcurl -X POST http://127.0.0.1:8000/api/patients/ -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d "{\"name\": \"John Doe\", \"date_of_birth\": \"1990-01-01\", \"gender\": \"Male\", \"address\": \"123 Main St\", \"phone\": \"555-1234\"}"


GET /api/patients/: List user’s patients
GET /api/patients//: Get patient
PUT /api/patients//: Update patient
DELETE /api/patients//: Delete patient

Doctor Management (Authenticated)

POST /api/doctors/: Add doctorcurl -X POST http://127.0.0.1:8000/api/doctors/ -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d "{\"name\": \"Dr. Smith\", \"specialty\": \"Cardiology\", \"phone\": \"555-9012\", \"email\": \"dr.smith@example.com\"}"


GET /api/doctors/: List doctors
GET /api/doctors//: Get doctor
PUT /api/doctors//: Update doctor
DELETE /api/doctors//: Delete doctor

Patient-Doctor Mapping (Authenticated)

POST /api/mappings/: Assign doctor to patientcurl -X POST http://127.0.0.1:8000/api/mappings/ -H "Content-Type: application/json" -H "Authorization: Bearer <access_token>" -d "{\"patient\": 1, \"doctor\": 1}"


GET /api/mappings/: List mappings
GET /api/mappings//: Get doctors for patient
DELETE /api/mappings//: Remove mapping

Testing

curl Workflow:set TOKEN=<access_token>
curl -X POST http://127.0.0.1:8000/api/patients/ -H "Content-Type: application/json" -H "Authorization: Bearer %TOKEN%" -d "{\"name\": \"John Doe\", \"date_of_birth\": \"1990-01-01\", \"gender\": \"Male\", \"address\": \"123 Main St\", \"phone\": \"555-1234\"}"
curl -X POST http://127.0.0.1:8000/api/doctors/ -H "Content-Type: application/json" -H "Authorization: Bearer %TOKEN%" -d "{\"name\": \"Dr. Smith\", \"specialty\": \"Cardiology\", \"phone\": \"555-9012\", \"email\": \"dr.smith@example.com\"}"
curl -X POST http://127.0.0.1:8000/api/mappings/ -H "Content-Type: application/json" -H "Authorization: Bearer %TOKEN%" -d "{\"patient\": 1, \"doctor\": 1}"


Postman: Import curl commands or set headers manually.
Database Check:SELECT * FROM api_patientdoctormapping;



Troubleshooting

401 Unauthorized: Re-login or refresh token.
400 Bad Request: Verify IDs and ownership:SELECT id, user_id, name FROM api_patient WHERE user_id = <user_id>;


Server Issues:python manage.py runserver
net start postgresql-x64-16



License
MIT License. See LICENSE.
