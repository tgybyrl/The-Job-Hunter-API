# The Automated Job Hunter 🚀

A full-stack Python web application engineered to streamline the job application process by dynamically scraping job descriptions and using Generative AI to write highly-tailored cover letters.

## 🌟 Features

- **Automated Web Scraping**: Safely extracts the core text from any publicly accessible job description URL using `requests` and `BeautifulSoup4`.
- **AI-Powered Generation**: Integrates seamlessly with the **Google Gemini API** (via `google-generativeai`) to generate exactly a 3-paragraph, professional backend developer cover letter tailored specifically to the scraped company and position.
- **Persistent Local Database**: Utilizes `Flask-SQLAlchemy` with SQLite to securely and instantly save all generated cover letters so users never lose an application.
- **Modern Responsive Dashboard**: Features a 100% custom-built frontend using highly responsive vanilla CSS Grid, CSS Variables, and dynamic `Jinja2` templating.
- **Built-in Error Handling**: Gracefully catches scraping blockers (like LinkedIn 403 errors) and incorrect API keys, safely routing users back to the homepage with a friendly error banner instead of crashing the server.

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, SQLAlchemy
- **Frontend**: HTML5, Vanilla CSS, Jinja2, JavaScript (Clipboard API)
- **Database**: SQLite
- **Libraries**: `beautifulsoup4`, `requests`, `python-dotenv`, `google-generativeai`

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/The-Job-Hunter-API.git
cd The-Job-Hunter-API
```

### 2. Set Up the Virtual Environment
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory of the project and add your Google Gemini API key:
```env
GEMINI_API_KEY=your_actual_api_key_here
```
*(You can get a free API key from [Google AI Studio](https://aistudio.google.com/)).*

### 5. Run the Application
```bash
python app.py
```
Open your web browser and navigate to `http://127.0.0.1:5000` to start hunting!
