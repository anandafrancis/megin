from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from flask_apscheduler import APScheduler

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())
CORS(app)

# MongoDB setup
client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"))
db = client.megin_database
ideas_collection = db.ideas

# Initialize scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route('/ideas', methods=['POST'])
def create_idea():
    data = request.get_json()

    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Missing title or description"}), 400

    # Adding timestamp for 'created_at' and optionally 'reminder_at'
    idea = {
        "title": data['title'],
        "description": data['description'],
        "urgency": data.get('urgency', 'Medium'),
        "importance": data.get('importance', 'Medium'),
        "created_at": datetime.utcnow(),
        "reminder_at": data.get('reminder_at')  # Optional: Expecting a datetime string from the client
    }
    
    if 'reminder_at' in idea and idea['reminder_at']:
        idea['reminder_at'] = datetime.strptime(idea['reminder_at'], '%Y-%m-%dT%H:%M:%S')  # Parsing string to datetime

    idea_id = ideas_collection.insert_one(idea).inserted_id

    return jsonify({"message": "Idea created successfully", "id": str(idea_id)}), 201

@app.route('/ideas', methods=['GET'])
def get_ideas():
    """
    Endpoint to retrieve all ideas.
    Returns a list of ideas with their attributes.
    """
    ideas = list(ideas_collection.find({}, {"_id": 0}))
    return jsonify(ideas)

def check_for_reminders():
    """
    This function will run periodically to check for ideas that need reminding.
    Adjust the logic to suit how you categorize urgency and importance.
    """
    # Implement logic to determine which ideas need reminding
    # This could involve setting a 'next_reminder_date' in the idea documents
    # and checking if any ideas have this date due or past due.
    # For demonstration, let's print a simple message:
    print("Checking for reminders...")

# Schedule the 'check_for_reminders' to run at intervals (e.g., every day at 10:00AM)
scheduler.add_job(id='Scheduled Reminders', func=check_for_reminders, trigger='cron', hour=10, minute=0)

@app.route('/reminders', methods=['GET'])
def get_reminders():
    """
    Endpoint to retrieve current reminders.
    For this example, we'll simulate retrieving reminders based on urgency.
    Implement your actual logic for fetching and storing reminders.
    """
    # Simulate getting reminders, for example, ideas marked with 'High' urgency
    reminders = list(ideas_collection.find({"urgency": "High"}, {"_id": 0}))
    return jsonify({"reminders": reminders})

if __name__ == '__main__':
    app.run(debug=True)




