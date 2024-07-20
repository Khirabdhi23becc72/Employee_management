# Import the create_app function and db instance from the app module
from app import create_app, db

# Create an instance of the Flask application using the create_app function
app = create_app()

# Use the application context to interact with the database
with app.app_context():
    # Create all database tables defined in the models
    db.create_all()
    
    # Print a message to indicate that the database has been initialized
    print("Database initialized!")