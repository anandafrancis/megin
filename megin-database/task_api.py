# Required Imports
from pymongo import MongoClient
from datetime import datetime, timedelta

class TaskAPI:
    def __init__(self, uri, db_name, collection_name):
        """
        Initializes the TaskAPI class.

        Parameters:
        - uri (str): The URI for MongoDB connection.
        - db_name (str): The name of the MongoDB database.
        - collection_name (str): The name of the collection within the database.
        """
        # Establish connection to MongoDB
        self.client = MongoClient(uri)
        # Select the database
        self.db = self.client[db_name]
        # Select the collection within the database
        self.collection = self.db[collection_name]

    def create_task(self, title, description, due_date=None, priority=None, status="Pending"):
        """
        Creates a new task in the collection.

        Parameters:
        - title (str): The title of the task.
        - description (str): The description of the task.
        - due_date (datetime): The due date of the task (optional).
        - priority (str): The priority of the task (optional).
        - status (str): The status of the task (optional).

        Returns:
        - inserted_id: The ObjectId of the newly inserted task.
        """
        # Construct a document representing the task
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "status": status
        }
        # Insert the task document into the collection
        result = self.collection.insert_one(task)
       
        # Return the ObjectId of the newly inserted task
        return result.inserted_id

    def get_all_tasks(self):
        """
        Retrieves all tasks from the collection.

        Returns:
        - list: A list containing all tasks in the collection.
        """
        # Retrieve all documents from the collection and convert them to a list
        return list(self.collection.find())

    def delete_task(self, task_id):
        """
        Deletes a task from the collection.

        Parameters:
        - task_id: The ObjectId of the task to delete.

        Returns:
        - int: The number of tasks deleted (0 or 1).
        """
        # Delete the task document with the specified ObjectId from the collection
        result = self.collection.delete_one({"_id": task_id})
        
        # Return the number of tasks deleted
        return result.deleted_count

    def generate_schedule(self):
        """
        Generates a schedule based on tasks with due dates.

        Returns:
        - dict: A dictionary representing the schedule, where keys are
                the number of days remaining until the due date,
                and values are lists of tasks due on that day.
        """
        # Find all documents in the collection with a due_date field and sort them by due date
        tasks = self.collection.find({"due_date": {"$exists": True}}).sort("due_date", 1)
        
        # Initialize an empty dictionary to store the schedule
        schedule = {}
        
        # Iterate over the tasks
        for task in tasks:
            # Get the due date from the task document
            due_date = task.get("due_date")
            # If the due date exists
            if due_date:
                # Calculate the number of days remaining until the due date
                days_remaining = (due_date - datetime.now()).days
                # If the number of days remaining is not in the schedule, initialize it as an empty list
                if days_remaining not in schedule:
                    schedule[days_remaining] = []
                # Append the task to the corresponding day in the schedule
                schedule[days_remaining].append(task)
       
        # Return the generated schedule
        return schedule