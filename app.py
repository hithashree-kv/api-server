from flask import Flask, jsonify, request
from datetime import datetime
import platform
import socket

app = Flask(__name__)

# In-memory data store
employees = [
    {
        "id": 1,
        "name": "Alice",
        "role": "Backend Engineer"
    },
    {
        "id": 2,
        "name": "Bob",
        "role": "DevOps Engineer"
    }
]

next_id = 3


# -----------------------------
# Root Endpoint
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "application": "DevOps Assignment API",
        "version": "1.0.0",
        "status": "Running"
    }), 200


# -----------------------------
# Health Check
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP"
    }), 200


# -----------------------------
# Version
# -----------------------------
@app.route("/version", methods=["GET"])
def version():
    return jsonify({
        "version": "1.0.0"
    }), 200


# -----------------------------
# System Information
# -----------------------------
@app.route("/system", methods=["GET"])
def system():
    return jsonify({
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }), 200


# =====================================================
# CRUD OPERATIONS
# =====================================================

# GET All Employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify({
        "count": len(employees),
        "employees": employees
    }), 200


# GET Employee By ID
@app.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({
            "message": "Employee not found"
        }), 404

    return jsonify(employee), 200


# CREATE Employee
@app.route("/employees", methods=["POST"])
def create_employee():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    if "name" not in data or "role" not in data:
        return jsonify({
            "message": "Both 'name' and 'role' are required"
        }), 400

    new_employee = {
        "id": next_id,
        "name": data["name"],
        "role": data["role"]
    }

    employees.append(new_employee)
    next_id += 1

    return jsonify({
        "message": "Employee created successfully",
        "employee": new_employee
    }), 201


# UPDATE Employee
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({
            "message": "Employee not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    employee["name"] = data.get("name", employee["name"])
    employee["role"] = data.get("role", employee["role"])

    return jsonify({
        "message": "Employee updated successfully",
        "employee": employee
    }), 200


# DELETE Employee
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    employee = next(
        (emp for emp in employees if emp["id"] == employee_id),
        None
    )

    if employee is None:
        return jsonify({
            "message": "Employee not found"
        }), 404

    employees.remove(employee)

    return jsonify({
        "message": "Employee deleted successfully"
    }), 200


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )