from marshmallow import Schema, fields, validate

class EmployeeSchema(Schema):
    id = fields.Int(dump_only=True)  # ID field, only used for output (dump)
    name = fields.Str(required=True, validate=validate.Length(min=1))  # Name field
    department = fields.Str(required=True, validate=validate.Length(min=1))  # Department field
    position = fields.Str(required=True, validate=validate.Length(min=1))  # Position field
    salary = fields.Float(required=True)  # Salary field
