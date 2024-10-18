from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS  # Import CORS

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app) 

# MongoDB connection
client = MongoClient('mongodb+srv://neeraj:mypassword@cluster0.ktb8c.mongodb.net/portfolio')  # Change if needed
db = client['portfolio']  # Database name: 'portfolio'

# Collections
skills_collection = db['skills']
introduction_collection = db['introduction']
project_collection = db['projects']
experience_collection = db['experience']

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

# API to fetch skills
@app.route('/skills', methods=['GET'])
def get_skills():
    try:
        skills = list(skills_collection.find({}, {'_id': 0}))  # Exclude the _id field
        return jsonify(skills), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch introduction
@app.route('/introduction', methods=['GET'])
def get_introduction():
    try:
        introduction = list(introduction_collection.find({}, {'_id': 0})) 
        print(introduction) # Exclude the _id field
        return jsonify(introduction[0]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch projects
@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = list(project_collection.find({}, {'_id': 0}))  # Exclude the _id field
        return jsonify(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API to fetch experience
@app.route('/experience', methods=['GET'])
def get_experience():
    try:
        experience = list(experience_collection.find({}, {'_id': 0}))  # Exclude the _id field
        return jsonify(experience), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

