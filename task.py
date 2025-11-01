class Task:
    """Represents a single task"""
    
    def __init__(self, task_id, title, description, priority, due_date):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = "Pending"
    
    def mark_complete(self):
        """Mark the task as complete"""
        self.status = "Complete"
    
    def mark_incomplete(self):
        """Mark the task as incomplete"""
        self.status = "Pending"
    
    def __str__(self):
        return f"[{self.task_id}] {self.title} - {self.priority} - Due: {self.due_date} - {self.status}"
