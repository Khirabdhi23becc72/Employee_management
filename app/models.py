from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Fixed typo here
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Employee {self.name}>'
