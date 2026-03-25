from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# --- DATABASE SETUP ---
# We tell Flask to use a local file named 'job_hunter.db' for our SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'job_hunter.db')

# Disable modification tracking to save memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database tool
db = SQLAlchemy(app)

# --- DATABASE MODEL ---
# A 'model' is just a Python class that represents a table in our database.
class Application(db.Model):
    # This creates a table with 4 columns: ID, Company Name, Job URL, and the Cover Letter Text.
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    job_url = db.Column(db.String(500), nullable=False)
    cover_letter_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Application for {self.company_name}>"

# --- ROUTES ---
@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    # Create the database tables before running the app
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")
        
    app.run(debug=True, port=5000)
