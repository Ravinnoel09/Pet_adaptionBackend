# 🐾 Pet Adoption System

A simple yet powerful web application for managing pet adoptions. This system allows users to view available pets, submit adoption requests, and track their request status. Admins can manage pets and review adoption requests.

---

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, Bootstrap
- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Tools**: Postman (for API testing)

---

## 📁 Project Structure

```
pet_adoption/
├── backend/
│   ├── app.py
│   ├── db.py
│   └── models.sql
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 🔸 Prerequisites

- Python 3.12+
- PostgreSQL installed and running
- pip

---

### 🔸 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/pet-adoption-system.git
cd pet-adoption-system
```

---

### 🔸 Step 2: Set Up Python Environment

```bash
python3 -m venv pet_adap
source pet_adap/bin/activate
pip install -r requirements.txt
```

---

### 🔸 Step 3: Set Up PostgreSQL Database

1. Start PostgreSQL service:
```bash
sudo service postgresql start
```

2. Open PostgreSQL shell:
```bash
psql -U postgres
```

3. Create a new database:
```sql
CREATE DATABASE pet_adoption;
\q
```

4. Run schema to create tables:
```bash
psql -U postgres -d pet_adoption -f backend/models.sql
```

---

### 🔸 Step 4: Run Flask Backend Server

```bash
cd backend
python app.py
```

The server will start on `http://127.0.0.1:5000`

---

## 🧪 API Endpoints

| Method | Endpoint             | Description                   |
|--------|----------------------|-------------------------------|
| GET    | `/pets`              | Fetch all available pets      |
| POST   | `/owners`            | Register a new owner          |
| POST   | `/request`           | Submit a new adoption request |
| GET    | `/my_requests/<id>`  | View owner's adoption requests|

---

## 🎯 Features & Rubrics Covered

| Feature                                | Description                                         |
|----------------------------------------|-----------------------------------------------------|
| 🐶 View Available Pets                 | View pet photos, breed, age, and status            |
| 📥 Submit Adoption Requests            | Owners can request to adopt pets                   |
| 📋 Track Adoption Status               | Owners can view status of their requests           |
| 👤 Admin Panel                         | Admin can login to manage pets & view requests     |
| 🖼️ Image Upload for Pets              | Pets have image previews stored in uploads folder  |
| ⬇️ Pet Dropdown on Request Form       | Pet name with image dropdown using live DB fetch   |

---

## 🗂️ Pet Image Handling

- All pet photos are stored in the `static/uploads/` folder.
- Displayed dynamically inside each pet card.
- Uploads are handled using Flask file upload.

---

## 🔐 Admin Panel

- The admin login page is included in the frontend.
- Admin can:
  - View adoption requests
  - Add or remove pets
  - Approve or reject adoption

> You can enhance this further with Flask-Login for authentication.

---

## 📫 Postman Usage

- Import collection and test the following:
  - Add Owner (POST /owners)
  - Submit Request (POST /request)
  - View Pets (GET /pets)
  - View My Requests (GET /my_requests/<owner_id>)


## 📌 Notes

- Make sure PostgreSQL is running before launching the backend.
- Keep the uploads folder accessible and static for pet image display.
- Use a modern browser for full frontend compatibility.
