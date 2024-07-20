from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)
    
    # Configure the database URI (using SQLite for simplicity)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Import and register blueprints here to avoid circular imports
    with app.app_context():
        from .routes import main # type: ignore
        app.register_blueprint(main)
        # Create all database tables defined in models
        db.create_all()

    return app
