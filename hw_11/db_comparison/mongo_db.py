"""
MongoDB-based To-Do list repository.
"""

from pymongo import MongoClient
from bson import ObjectId
from typing import List, Dict

DB_CONFIG = {
    "uri": "mongodb://localhost:27017/",
    "dbname": "todo_db",
    "collection": "tasks"
}


class TodoMongo:
    """
    A class to interact with a MongoDB database for managing a to-do list.

    This class provides methods for creating, reading, updating, and deleting
    tasks in a MongoDB collection.
    """

    def __init__(self) -> None:
        """
        Initializes the MongoDB connection and ensures the 'tasks' collection exists.

        This constructor establishes a connection to MongoDB and creates a unique
        index on the 'title' field to prevent duplicate task titles.
        """

        self.client = MongoClient(DB_CONFIG["uri"])
        self.db = self.client[DB_CONFIG["dbname"]]
        self.tasks_collection = self.db[DB_CONFIG["collection"]]

        self.tasks_collection.create_index("title", unique=True)

    def create_task(self, title: str, description: str) -> str:
        """
        Inserts a new task into the MongoDB collection and returns its ID.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.

        Returns:
            str: The ID of the inserted task.
        """

        task = {"title": title, "description": description, "completed": False}
        result = self.tasks_collection.insert_one(task)

        return str(result.inserted_id)

    def get_tasks(self) -> List[Dict[str, str | bool]]:
        """
        Fetches all tasks from the MongoDB collection.

        Returns:
            List[Dict[str, str | bool]]: A list of dictionaries, each containing:
                - _id (str): The task ID.
                - title (str): The task title.
                - description (str): The task description.
                - completed (bool): The task completion status.
        """

        tasks = self.tasks_collection.find({},
                                           {"_id": 1, "title": 1,
                                            "description": 1, "completed": 1})

        return [{"_id": str(task["_id"]), "title": task["title"],
                 "description": task["description"], "completed": task["completed"]}
                for task in tasks]

    def update_task(self, task_id: str, title: str, description: str, completed: bool) -> None:
        """
        Updates an existing task in the MongoDB collection.

        Args:
            task_id (str): The ID of the task to update.
            title (str): The updated title of the task.
            description (str): The updated description of the task.
            completed (bool): The updated completion status.
        """

        self.tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"title": title, "description": description, "completed": completed}}
        )

    def delete_task(self, task_id: str) -> None:
        """
        Deletes a task from the MongoDB collection by its ID.

        Args:
            task_id (str): The ID of the task to delete.
        """

        self.tasks_collection.delete_one({"_id": ObjectId(task_id)})


if __name__ == "__main__":
    mongo_todo = TodoMongo()
    task_id = mongo_todo.create_task("Learn MongoDB", "Understand NoSQL concepts")

    print("Task created with ID:", task_id)
    print("All tasks:", mongo_todo.get_tasks())
