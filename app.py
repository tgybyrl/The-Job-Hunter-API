from flask import Flask

app = Flask(__name__)

# The @app.route decorator binds the URL ("/") to the function below it.
@app.route("/")
def hello_world():
    # This simply returns a string when someone visits the home page.
    return "Hello World!"

if __name__ == "__main__":
    # app.run starts the local development server. 
    # debug=True means the server will automatically reload if we change the code, and show useful error messages.
    app.run(debug=True, port=5000)
