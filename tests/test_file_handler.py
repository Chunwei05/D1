import unittest
from unittest.mock import mock_open, patch, MagicMock
import json
from file_handler import FileHandler
from task import Task

class TestFileHandler(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.handler = FileHandler("test_tasks.json")
        self.sample_tasks = {
            1: Task(1, "Task 1", "Description 1", "High", "2025-11-15"),
            2: Task(2, "Task 2", "Description 2", "Low", "2025-11-20")
        }
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_save_tasks_to_file(self, mock_json_dump, mock_file):
        """Test saving tasks to file using mock"""
        self.handler.save_tasks(self.sample_tasks)
        
        # Verify file was opened in write mode
        mock_file.assert_called_once_with("test_tasks.json", 'w')
        
        # Verify json.dump was called
        mock_json_dump.assert_called_once()
    
    @patch('builtins.open', new_callable=mock_open, read_data='[{"task_id": 1, "title": "Test", "description": "Desc", "priority": "High", "due_date": "2025-11-15", "status": "Pending"}]')
    @patch('json.load')
    def test_load_tasks_from_file(self, mock_json_load, mock_file):
        """Test loading tasks from file using mock"""
        # Mock the return value of json.load
        mock_json_load.return_value = [
            {
                "task_id": 1,
                "title": "Test",
                "description": "Desc",
                "priority": "High",
                "due_date": "2025-11-15",
                "status": "Pending"
            }
        ]
        
        tasks = self.handler.load_tasks()
        
        # Verify file was opened in read mode
        mock_file.assert_called_once_with("test_tasks.json", 'r')
        
        # Verify we got tasks back
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[1].title, "Test")
    
    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_tasks_file_not_found(self, mock_file):
        """Test loading when file doesn't exist returns empty dict"""
        tasks = self.handler.load_tasks()
        self.assertEqual(tasks, {})
    
    @patch('builtins.open', new_callable=mock_open, read_data='invalid json')
    @patch('json.load', side_effect=json.JSONDecodeError("Error", "", 0))
    def test_load_tasks_corrupted_file(self, mock_json_load, mock_file):
        """Test loading corrupted JSON file returns empty dict"""
        tasks = self.handler.load_tasks()
        self.assertEqual(tasks, {})
    
    def test_task_to_dict(self):
        """Test converting task to dictionary"""
        task = Task(1, "Test", "Description", "High", "2025-11-15")
        task_dict = self.handler.task_to_dict(task)
        
        self.assertEqual(task_dict["task_id"], 1)
        self.assertEqual(task_dict["title"], "Test")
        self.assertEqual(task_dict["priority"], "High")
    
    def test_dict_to_task(self):
        """Test converting dictionary to task"""
        task_dict = {
            "task_id": 1,
            "title": "Test",
            "description": "Description",
            "priority": "High",
            "due_date": "2025-11-15",
            "status": "Pending"
        }
        
        task = self.handler.dict_to_task(task_dict)
        
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Test")
        self.assertEqual(task.status, "Pending")

if __name__ == '__main__':
    unittest.main()
