from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Import our custom helper functions
from scraper import scrape_job_description
from ai_helper import generate_cover_letter

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
def index():
    # Displays our home page form instead of "Hello World"
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # Fetches all saved cover letters from our DB (newest first)
    applications = Application.query.order_by(Application.id.desc()).all()
    # Sends that data to be rendered by Jinja2 in dashboard.html
    return render_template("dashboard.html", applications=applications)

@app.route("/generate", methods=["POST"])
def generate():
    """
    This is the core logic of our app! It runs when a user submits the form.
    It expects 'company_name' and 'job_url' via a POST request.
    """
    # 1. Grab the data submitted by the user
    company_name = request.form.get("company_name")
    job_url = request.form.get("job_url")

    if not company_name or not job_url:
        return jsonify({"error": "Missing company_name or job_url"}), 400

    # 2. Call our Scraper Utility
    print(f"Scraping URL: {job_url}...")
    scraped_text = scrape_job_description(job_url)
    
    # 3. Pass the scraped text to our AI Utility
    print(f"Generating letter for: {company_name}...")
    cover_letter = generate_cover_letter(company_name, scraped_text)

    # 4. Save the generated cover letter to our Database
    new_application = Application(
        company_name=company_name,
        job_url=job_url,
        cover_letter_text=cover_letter
    )
    db.session.add(new_application) # Stages the save
    db.session.commit()             # Permanently saves it to job_hunter.db

    # 5. We are now seamlessly redirecting the user to the visual dashboard!
    return redirect(url_for("dashboard"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete_application(id):
    """
    Finds a specific cover letter in the database by ID and deletes it perfectly.
    """
    app_to_delete = Application.query.get_or_404(id)
    try:
        db.session.delete(app_to_delete)
        db.session.commit()
        return redirect(url_for('dashboard'))
    except Exception as e:
        return f"There was a problem deleting that record: {e}"

if __name__ == "__main__":
    # Create the database tables before running the app
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")
        
    app.run(debug=True, port=5000)
