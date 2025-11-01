import json
from task import Task

class FileHandler:
    """Handles saving and loading tasks from JSON file"""
    
    def __init__(self, filename="tasks.json"):
        self.filename = filename
    
    def save_tasks(self, tasks_dict):
        """
        Save tasks to JSON file
        Args:
            tasks_dict: Dictionary of tasks {task_id: Task object}
        """
        try:
            # Convert tasks to list of dictionaries
            tasks_list = [self.task_to_dict(task) for task in tasks_dict.values()]
            
            with open(self.filename, 'w') as file:
                json.dump(tasks_list, file, indent=4)
            
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False
    
    def load_tasks(self):
        """
        Load tasks from JSON file
        Returns:
            Dictionary of tasks {task_id: Task object}
        """
        try:
            with open(self.filename, 'r') as file:
                tasks_list = json.load(file)
            
            # Convert list of dictionaries to dictionary of Task objects
            tasks_dict = {}
            for task_data in tasks_list:
                task = self.dict_to_task(task_data)
                tasks_dict[task.task_id] = task
            
            return tasks_dict
        
        except FileNotFoundError:
            print(f"File {self.filename} not found. Starting with empty task list.")
            return {}
        
        except json.JSONDecodeError:
            print(f"Error reading {self.filename}. File may be corrupted. Starting fresh.")
            return {}
        
        except Exception as e:
            print(f"Unexpected error loading tasks: {e}")
            return {}
    
    def task_to_dict(self, task):
        """
        Convert Task object to dictionary
        Args:
            task: Task object
        Returns:
            Dictionary representation of task
        """
        return {
            "task_id": task.task_id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "due_date": task.due_date,
            "status": task.status
        }
    
    def dict_to_task(self, task_dict):
        """
        Convert dictionary to Task object
        Args:
            task_dict: Dictionary with task data
        Returns:
            Task object
        """
        task = Task(
            task_id=task_dict["task_id"],
            title=task_dict["title"],
            description=task_dict["description"],
            priority=task_dict["priority"],
            due_date=task_dict["due_date"]
        )
        task.status = task_dict["status"]
        return task
