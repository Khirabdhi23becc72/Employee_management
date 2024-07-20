# Import necessary modules and classes from Flask, Marshmallow, and SQLAlchemy
from flask import Blueprint, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

# Create a Blueprint for handling errors
errors = Blueprint('errors', __name__)

# Error handler for HTTP 400 Bad Request
@errors.app_errorhandler(400)
def bad_request_error(error):
    """
    Handles 400 Bad Request errors.
    Returns a JSON response with the error message and details.
    """
    return jsonify({"message": "Bad Request", "details": str(error)}), 400

# Error handler for HTTP 404 Not Found
@errors.app_errorhandler(404)
def not_found_error(error):
    """
    Handles 404 Not Found errors.
    Returns a JSON response with the error message and details.
    """
    return jsonify({"message": "Not Found", "details": str(error)}), 404

# Error handler for HTTP 415 Unsupported Media Type
@errors.app_errorhandler(415)
def unsupported_media_type_error(error):
    """
    Handles 415 Unsupported Media Type errors.
    Returns a JSON response with the error message and details.
    """
    return jsonify({"message": "Unsupported Media Type", "details": str(error)}), 415

# Error handler for HTTP 500 Internal Server Error
@errors.app_errorhandler(500)
def internal_server_error(error):
    """
    Handles 500 Internal Server Error.
    Returns a JSON response with the error message and details.
    """
    return jsonify({"message": "Internal Server Error", "details": str(error)}), 500

# Error handler for Marshmallow ValidationError
@errors.app_errorhandler(ValidationError)
def handle_validation_error(error):
    """
    Handles Marshmallow validation errors.
    Returns a JSON response with the validation error messages.
    """
    return jsonify({"message": "Validation Error", "details": error.messages}), 400

# Error handler for SQLAlchemy errors
@errors.app_errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(error):
    """
    Handles SQLAlchemy database errors.
    Returns a JSON response with the error message and details.
    """
    return jsonify({"message": "Database Error", "details": str(error)}), 500

# Error handler for any other generic exceptions
@errors.app_errorhandler(Exception)
def handle_generic_error(error):
    """
    Handles any unexpected errors.
    Returns a JSON response with a generic error message and details.
    """
    return jsonify({"message": "An unexpected error occurred", "details": str(error)}), 500
