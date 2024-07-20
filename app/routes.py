from flask import Blueprint, jsonify, request
from .models import Employee, db

# Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home route with a welcome message."""
    return jsonify({"message": "Welcome to the Employee Management System!"})

@main.route('/employees', methods=['GET'])
def get_employee():
    """Get all employees."""
    employees = Employee.query.all()
    return jsonify({"employees": [employee.to_dict() for employee in employees]})

@main.route('/employee', methods=['POST'])
def create_employee():
    """Create a new employee."""
    data = request.get_json()
    new_employee = Employee(
        name=data['name'],
        age=data['age'],
        position=data['position'],
        department=data['department']
    ) # type: ignore
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee created successfully!"}), 201

@main.route('/employee/<int:id>', methods=['PUT'])
def update_employee(id):
    """Update an existing employee."""
    data = request.get_json()
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"message": "Employee not found"}), 404

    employee.name = data['name']
    employee.age = data['age']
    employee.position = data['position']
    employee.department = data['department']
    db.session.commit()
    return jsonify({"message": "Employee updated successfully!"})

@main.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    """Delete an employee."""
    employee = Employee.query.get(id)
    if not employee:
        return jsonify({"message": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully!"})
