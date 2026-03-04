Here is your clean and simple `README.md` 👇

---

```markdown
# 📘 Student Attendance System

A simple full-stack Student Attendance System built using:

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Database:** SQLite

This project is designed as a practical learning project to understand API development, database integration, and frontend-backend communication.

---

## 🚀 Project Structure

```

attendance-system/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   └── attendance.db
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md

````

---

## 🛠 Features

- Add new students
- View student list
- Mark attendance (Present / Absent)
- View attendance percentage
- SQLite-based persistent storage

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite

### Frontend
- Streamlit
- Requests (for API calls)

---

## 🧱 Database Schema

### Students Table
- id (Primary Key)
- name
- roll_number

### Attendance Table
- id (Primary Key)
- student_id (Foreign Key)
- date
- status (Present / Absent)

---

## 🖥️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd attendance-system
````

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Backend Server

```bash
cd backend
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 5️⃣ Run Frontend (Streamlit)

Open new terminal:

```bash
cd frontend
streamlit run app.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## 🔄 API Endpoints

* `POST /add-student`
* `GET /students`
* `POST /mark-attendance`
* `GET /attendance/{student_id}`

---

## 🎯 Learning Objectives

* Build REST APIs using FastAPI
* Design and connect SQLite database
* Connect frontend to backend via HTTP requests
* Understand full-stack workflow
* Practice project structuring

---

## 📌 Future Improvements

* Add authentication (JWT)
* Role-based access (Admin / Teacher)
* Attendance analytics dashboard
* Docker deployment
* PostgreSQL upgrade
* AI-based attendance (Face Recognition)

---

## 🧠 Project Vision

This project is built as part of a structured learning journey toward becoming a strong AI/Backend Engineer.
Start simple. Build solid. Upgrade strategically.

---

🔥 Built with discipline.

```

---

