from flask import Flask

# Create an instance of the Flask class and name it 'app'
app = Flask(__name__)

# Define your routes and other Flask application logic here
@app.route('/')
def index():
    return 'Hello, World!'

# Ensure this file is run only if it's the main script
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
