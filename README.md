# DevOps Assignment API

A simple RESTful API built using Python and Flask for demonstrating the complete DevOps deployment workflow.

This project is created as part of a DevOps assignment and will be used to demonstrate:

- Git & GitHub
- Docker
- Docker Hub
- Helm
- Kubernetes (Kind)
- Ingress
- CI/CD using GitHub Actions

---

## Technologies Used

- Python 3.12
- Flask 3.x
- Git
- Docker
- Kubernetes
- Helm

---

## Project Structure

```
api-server/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── venv/
```

---

## Running the Application

### Activate Virtual Environment

Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Application

```bash
python app.py
```

The server starts on

```
http://localhost:5000
```

---

## Available APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Application Information |
| GET | /health | Health Check |
| GET | /version | API Version |
| GET | /system | System Information |
| GET | /employees | Get All Employees |
| GET | /employees/{id} | Get Employee By ID |
| POST | /employees | Create Employee |
| PUT | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |

