# FastAPI Employee CRUD API
 
A RESTful Employee Management API built using FastAPI, SQLAlchemy ORM, and MySQL.
 
## Features
 
- Create Employee
- Get All Employees
- Get Employee by ID
- Update Employee
- Delete Employee
- Automatic Swagger Documentation
 
## Technologies Used
 
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Uvicorn
 
## Project Structure
 
```text
Fastapi/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   └── routers/
│       └── employee.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
 
## Installation
 
Clone the repository:
 
```bash
git clone https://github.com/your-username/fastapi-employee-crud.git
```
 
Go into the project:
 
```bash
cd fastapi-employee-crud
```
 
Create a virtual environment:
 
```bash
python -m venv venv
```
 
Activate it (Windows):
 
```bash
venv\Scripts\activate
```
 
Install dependencies:
 
```bash
pip install -r requirements.txt
```
 
Run the project:
 
```bash
uvicorn app.main:app --reload
```
 
## API Documentation
 
Swagger UI:
 
http://127.0.0.1:8000/docs
 
ReDoc:
 
http://127.0.0.1:8000/redoc
 
## API Endpoints
 
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /employees | Create Employee |
| GET | /employees | Get All Employees |
| GET | /employees/{id} | Get Employee By ID |
| PUT | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |
 