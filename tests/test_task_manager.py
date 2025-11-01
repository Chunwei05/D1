import unittest
from task_manager import TaskManager
from task import Task

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.manager = TaskManager()
    
    def test_add_task(self):
        """Test adding a task"""
        task = Task(1, "Test", "Description", "High", "2025-11-15")
        self.manager.add_task(task)
        self.assertEqual(len(self.manager.get_all_tasks()), 1)
    
    def test_delete_task(self):
        """Test deleting a task"""
        task = Task(1, "Test", "Description", "High", "2025-11-15")
        self.manager.add_task(task)
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.get_all_tasks()), 0)
    
    def test_delete_nonexistent_task(self):
        """Test deleting non-existent task raises error"""
        with self.assertRaises(ValueError):
            self.manager.delete_task(999)
    
    def test_get_task_by_id(self):
        """Test retrieving task by ID"""
        task = Task(1, "Test", "Description", "High", "2025-11-15")
        self.manager.add_task(task)
        retrieved = self.manager.get_task_by_id(1)
        self.assertEqual(retrieved.title, "Test")
    
    def test_filter_by_status(self):
        """Test filtering tasks by status"""
        task1 = Task(1, "Task 1", "Desc", "High", "2025-11-15")
        task2 = Task(2, "Task 2", "Desc", "Low", "2025-11-16")
        task1.mark_complete()
        
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        
        completed = self.manager.filter_by_status("Complete")
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0].task_id, 1)
    
    def test_filter_by_priority(self):
        """Test filtering tasks by priority"""
        task1 = Task(1, "Task 1", "Desc", "High", "2025-11-15")
        task2 = Task(2, "Task 2", "Desc", "Low", "2025-11-16")
        
        self.manager.add_task(task1)
        self.manager.add_task(task2)
        
        high_priority = self.manager.filter_by_priority("High")
        self.assertEqual(len(high_priority), 1)

if __name__ == '__main__':
    unittest.main()
