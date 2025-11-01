import unittest
from datetime import datetime
from task import Task

class TestTask(unittest.TestCase):
    
    def test_create_task_with_valid_data(self):
        """Test creating a task with valid input"""
        task = Task(
            task_id=1,
            title="Complete assignment",
            description="Finish FIT2107 project",
            priority="High",
            due_date="2025-11-15"
        )
        
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Complete assignment")
        self.assertEqual(task.description, "Finish FIT2107 project")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.due_date, "2025-11-15")
        self.assertEqual(task.status, "Pending")
    
    def test_mark_task_complete(self):
        """Test marking a task as complete"""
        task = Task(1, "Test task", "Description", "Medium", "2025-11-10")
        task.mark_complete()
        self.assertEqual(task.status, "Complete")
    
    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete"""
        task = Task(1, "Test task", "Description", "Low", "2025-11-10")
        task.mark_complete()
        task.mark_incomplete()
        self.assertEqual(task.status, "Pending")

if __name__ == '__main__':
    unittest.main()
