class TaskManager:
    """Manages a collection of tasks"""
    
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task):
        """Add a task to the manager"""
        self.tasks[task.task_id] = task
    
    def delete_task(self, task_id):
        """Delete a task by ID"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        del self.tasks[task_id]
    
    def get_task_by_id(self, task_id):
        """Get a task by its ID"""
        return self.tasks.get(task_id)
    
    def get_all_tasks(self):
        """Get all tasks as a list"""
        return list(self.tasks.values())
    
    def filter_by_status(self, status):
        """Filter tasks by status"""
        return [task for task in self.tasks.values() if task.status == status]
    
    def filter_by_priority(self, priority):
        """Filter tasks by priority"""
        return [task for task in self.tasks.values() if task.priority == priority]
    
    def sort_by_due_date(self):
        """Sort tasks by due date"""
        return sorted(self.tasks.values(), key=lambda task: task.due_date)

