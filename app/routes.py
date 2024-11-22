from app import app

@app.route('/')
def home():
    return "Hello, Jenkins and Docker!"
