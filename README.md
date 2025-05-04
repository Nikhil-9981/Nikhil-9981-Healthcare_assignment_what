
# 🏥 Healthcare Backend System – Django + DRF

A secure, modular backend for managing users, patients, doctors, and doctor-patient mappings. Built using Django REST Framework and PostgreSQL.

---

## 📌 Objective

This system allows users to register, log in securely using JWT tokens, and perform full CRUD operations for managing patients and doctors, along with assigning doctors to patients.

---

## 🧰 Tech Stack

- **Backend Framework:** Django 4+
- **API Toolkit:** Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Documentation:** Swagger UI (`drf-yasg`)
- **Environment Config:** python-dotenv
- **Security:** DRF permissions + rate limiting
- **Testing:** Django `APITestCase`

---

## 🚀 Features

- 🔐 User registration & secure login with JWT
- 👤 Full CRUD APIs for patients (owner-restricted)
- 🩺 Full CRUD APIs for doctors (global access)
- 🔄 Assign/unassign doctors to/from patients
- ⚠️ Duplicate doctor-patient mappings prevented
- 📄 Swagger API documentation at `/swagger/`
- 🔒 DRF rate limiting to protect API usage
- ✅ Unit tests using DRF's APITestCase
- 🔧 Environment variables for sensitive settings

---

## 🔐 Authentication Flow

1. **Register:**  
   `POST /api/auth/register/`  
   Required fields: `username`, `email`, `password`

2. **Login:**  
   `POST /api/auth/login/`  
   Returns `access` and `refresh` tokens

3. **Authorization Header Example:**

```
Authorization: Bearer <access_token>
```

---

## 📡 API Endpoints

### 🧾 Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login with username & password |
| POST | `/api/auth/token/refresh/` | Refresh JWT token |

---

### 👨‍⚕️ Doctor Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/doctors/` | Add a doctor |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/<id>/` | Get doctor details |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

---

### 🧑‍🦽 Patient Management (User-Scoped)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients/` | Add patient |
| GET | `/api/patients/` | List user’s patients |
| GET | `/api/patients/<id>/` | Get patient details |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

---

### 🔗 Patient-Doctor Mappings
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/mappings/` | Assign doctor to patient |
| GET | `/api/mappings/` | List all mappings |
| GET | `/api/mappings/<patient_id>/doctors/` | List all doctors for a patient |
| DELETE | `/api/mappings/<id>/` | Remove doctor from patient |

---

## 🛠️ Project Setup

### 🔑 Environment Variables (`.env`)

```
SECRET_KEY=your_django_secret
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 🧪 Local Development Setup

```bash
# 1️⃣ Clone the repo from GitHub
git clone https://github.com/Nikhil-9981/Nikhil-9981-Healthcare_assignment_what.git

# 2️⃣ Navigate into the main folder
cd Nikhil-9981-Healthcare_assignment_what

# 3️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# 4️⃣ Install dependencies
pip install -r requirements.txt

# 5️⃣ Configure environment variables
cp .env.example .env  # Then open .env and add DB credentials + secret key

# 6️⃣ Move into the Django project folder
cd healthcare

# 7️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

# 8️⃣ (Optional) Create a superuser for admin access
python manage.py createsuperuser

# 9️⃣ Start the development server
python manage.py runserver

```

---

## 🧪 Run Tests

```bash
python manage.py test
```

> ✅ 10 unit tests cover user registration, login, patient/doctor CRUD, and mappings.

---

## 📊 API Docs

- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc UI: `http://localhost:8000/redoc/`

---

## 👨‍💻 Admin Access

```bash
python manage.py createsuperuser
```
Admin panel: `http://localhost:8000/admin/`

---

## 🧾 Rate Limiting

Enabled via DRF settings:

- `user`: 1000 requests/day
- `anon`: 50 requests/day

Modify in `settings.py` under `DEFAULT_THROTTLE_RATES`.

---

## 📁 Folder Structure (Important for Submission)

```
```Healthcare_Assignment/
│
├── healthcare/                        # Django project root
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                    # Main settings with dotenv support
│   ├── urls.py                        # Root URL configuration with Swagger
│   ├── wsgi.py
│
├── patients/                          # Patient management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # Patient model
│   ├── serializers.py
│   ├── views.py                       # PatientViewSet
│   ├── tests.py                       # DRF API test cases
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── doctors/                           # Doctor management app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # Doctor model
│   ├── serializers.py
│   ├── views.py                       # DoctorViewSet
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── mappings/                          # Doctor-patient mapping app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # Mapping model
│   ├── serializers.py
│   ├── views.py                       # MappingViewSet
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
├── users/                             # User registration and authentication
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py                      # Optional custom user extension
│   ├── serializers.py
│   ├── views.py                       # RegisterView
│   ├── tests.py
│   └── migrations/
│       ├── __init__.py
│
├── manage.py                          # Django entry script
├── requirements.txt                   # All dependencies
├── .env                               # Your actual environment file (not committed)
├── .env.example                       # Sample env file for deployment
├── README.md                          # Full project documentation
├── .gitignore                         # Git ignore rules (Python, Django, envs, etc.)

```

---
 
