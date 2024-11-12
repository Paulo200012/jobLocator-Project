from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv("mongodb+srv://juxapaulo:qL7J1Fo9h0AL5Dwm@joblocator.cx8l7.mongodb.net/?retryWrites=true&w=majority&appName=jobLocator"))
db = client['jobLocatorDB']
graduates_collection = db['graduates']

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to add a graduate
@app.route('/add_graduate', methods=['POST'])
def add_graduate():
    name = request.form.get('name')
    email = request.form.get('email')
    qualifications = request.form.get('qualifications')
    
    graduates_collection.insert_one({
        'name': name,
        'email': email,
        'qualifications': qualifications
    })
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
