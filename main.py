from task import Task
from task_manager import TaskManager
from validator import Validator
from file_handler import FileHandler

class TaskApp:
    """Main application class for Task Manager"""
    
    def __init__(self):
        self.task_manager = TaskManager()
        self.file_handler = FileHandler("tasks.json")
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file on startup"""
        tasks = self.file_handler.load_tasks()
        self.task_manager.tasks = tasks
        
        # Set next_id to be one more than the highest existing ID
        if tasks:
            self.next_id = max(tasks.keys()) + 1
        
        print(f"✓ Loaded {len(tasks)} task(s) from file.")
    
    def save_tasks(self):
        """Save tasks to file"""
        if self.file_handler.save_tasks(self.task_manager.tasks):
            print("✓ Tasks saved successfully.")
        else:
            print("✗ Error saving tasks.")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("📋 TASK MANAGER - MAIN MENU")
        print("="*50)
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. View Tasks by Status")
        print("4. View Tasks by Priority")
        print("5. Mark Task as Complete")
        print("6. Mark Task as Incomplete")
        print("7. Edit Task")
        print("8. Delete Task")
        print("9. Sort Tasks by Due Date")
        print("0. Exit")
        print("="*50)
    
    def add_task(self):
        """Add a new task"""
        print("\n--- Add New Task ---")
        
        title = input("Enter task title: ").strip()
        if not title:
            print("✗ Title cannot be empty!")
            return
        
        description = input("Enter task description: ").strip()
        
        # Get and validate priority
        while True:
            priority = input("Enter priority (High/Medium/Low): ").strip()
            if Validator.validate_priority(priority):
                break
            else:
                print("✗ Invalid priority! Please enter High, Medium, or Low.")
        
        # Get and validate due date
        while True:
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            if Validator.validate_date(due_date):
                break
            else:
                print("✗ Invalid date format! Please use YYYY-MM-DD.")
        
        # Create and add task
        task = Task(self.next_id, title, description, priority, due_date)
        self.task_manager.add_task(task)
        self.next_id += 1
        
        print(f"✓ Task added successfully! (ID: {task.task_id})")
        self.save_tasks()
    
    def view_all_tasks(self):
        """Display all tasks"""
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("\n📭 No tasks found!")
            return
        
        print(f"\n--- All Tasks ({len(tasks)} total) ---")
        self.display_tasks(tasks)
    
    def view_tasks_by_status(self):
        """Display tasks filtered by status"""
        print("\n--- Filter by Status ---")
        print("1. Pending")
        print("2. Complete")
        
        choice = input("Select status (1-2): ").strip()
        
        if choice == "1":
            status = "Pending"
        elif choice == "2":
            status = "Complete"
        else:
            print("✗ Invalid choice!")
            return
        
        tasks = self.task_manager.filter_by_status(status)
        
        if not tasks:
            print(f"\n📭 No {status} tasks found!")
            return
        
        print(f"\n--- {status} Tasks ({len(tasks)} total) ---")
        self.display_tasks(tasks)
    
    def view_tasks_by_priority(self):
        """Display tasks filtered by priority"""
        print("\n--- Filter by Priority ---")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        
        choice = input("Select priority (1-3): ").strip()
        
        if choice == "1":
            priority = "High"
        elif choice == "2":
            priority = "Medium"
        elif choice == "3":
            priority = "Low"
        else:
            print("✗ Invalid choice!")
            return
        
        tasks = self.task_manager.filter_by_priority(priority)
        
        if not tasks:
            print(f"\n📭 No {priority} priority tasks found!")
            return
        
        print(f"\n--- {priority} Priority Tasks ({len(tasks)} total) ---")
        self.display_tasks(tasks)
    
    def mark_task_complete(self):
        """Mark a task as complete"""
        self.view_all_tasks()
        
        if not self.task_manager.get_all_tasks():
            return
        
        try:
            task_id = int(input("\nEnter task ID to mark as complete: ").strip())
            task = self.task_manager.get_task_by_id(task_id)
            
            if task:
                task.mark_complete()
                print(f"✓ Task {task_id} marked as complete!")
                self.save_tasks()
            else:
                print(f"✗ Task with ID {task_id} not found!")
        except ValueError:
            print("✗ Invalid ID! Please enter a number.")
    
    def mark_task_incomplete(self):
        """Mark a task as incomplete"""
        self.view_all_tasks()
        
        if not self.task_manager.get_all_tasks():
            return
        
        try:
            task_id = int(input("\nEnter task ID to mark as incomplete: ").strip())
            task = self.task_manager.get_task_by_id(task_id)
            
            if task:
                task.mark_incomplete()
                print(f"✓ Task {task_id} marked as incomplete!")
                self.save_tasks()
            else:
                print(f"✗ Task with ID {task_id} not found!")
        except ValueError:
            print("✗ Invalid ID! Please enter a number.")
    
    def edit_task(self):
        """Edit an existing task"""
        self.view_all_tasks()
        
        if not self.task_manager.get_all_tasks():
            return
        
        try:
            task_id = int(input("\nEnter task ID to edit: ").strip())
            task = self.task_manager.get_task_by_id(task_id)
            
            if not task:
                print(f"✗ Task with ID {task_id} not found!")
                return
            
            print(f"\nEditing Task: {task.title}")
            print("(Press Enter to keep current value)")
            
            # Edit title
            new_title = input(f"Title [{task.title}]: ").strip()
            if new_title:
                task.title = new_title
            
            # Edit description
            new_desc = input(f"Description [{task.description}]: ").strip()
            if new_desc:
                task.description = new_desc
            
            # Edit priority
            while True:
                new_priority = input(f"Priority [{task.priority}] (High/Medium/Low): ").strip()
                if not new_priority:
                    break
                if Validator.validate_priority(new_priority):
                    task.priority = new_priority
                    break
                else:
                    print("✗ Invalid priority!")
            
            # Edit due date
            while True:
                new_date = input(f"Due Date [{task.due_date}] (YYYY-MM-DD): ").strip()
                if not new_date:
                    break
                if Validator.validate_date(new_date):
                    task.due_date = new_date
                    break
                else:
                    print("✗ Invalid date format!")
            
            print(f"✓ Task {task_id} updated successfully!")
            self.save_tasks()
            
        except ValueError:
            print("✗ Invalid ID! Please enter a number.")
    
    def delete_task(self):
        """Delete a task"""
        self.view_all_tasks()
        
        if not self.task_manager.get_all_tasks():
            return
        
        try:
            task_id = int(input("\nEnter task ID to delete: ").strip())
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip().lower()
            
            if confirm == 'y':
                self.task_manager.delete_task(task_id)
                print(f"✓ Task {task_id} deleted successfully!")
                self.save_tasks()
            else:
                print("✗ Deletion cancelled.")
                
        except ValueError as e:
            print(f"✗ Error: {e}")
        except Exception as e:
            print(f"✗ Invalid input: {e}")
    
    def sort_tasks_by_due_date(self):
        """Display tasks sorted by due date"""
        tasks = self.task_manager.sort_by_due_date()
        
        if not tasks:
            print("\n📭 No tasks found!")
            return
        
        print(f"\n--- Tasks Sorted by Due Date ({len(tasks)} total) ---")
        self.display_tasks(tasks)
    
    def display_tasks(self, tasks):
        """Display tasks in a formatted table"""
        if not tasks:
            print("📭 No tasks to display.")
            return
        
        # Header
        print("\n" + "-"*100)
        print(f"{'ID':<5} {'Title':<25} {'Priority':<10} {'Due Date':<12} {'Status':<10}")
        print("-"*100)
        
        # Tasks
        for task in tasks:
            status_symbol = "✓" if task.status == "Complete" else "○"
            print(f"{task.task_id:<5} {task.title[:24]:<25} {task.priority:<10} {task.due_date:<12} {status_symbol} {task.status:<10}")
        
        print("-"*100)
    
    def run(self):
        """Main application loop"""
        print("\n🎯 Welcome to Task Manager!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.view_tasks_by_status()
            elif choice == "4":
                self.view_tasks_by_priority()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.mark_task_incomplete()
            elif choice == "7":
                self.edit_task()
            elif choice == "8":
                self.delete_task()
            elif choice == "9":
                self.sort_tasks_by_due_date()
            elif choice == "0":
                print("\n👋 Thank you for using Task Manager!")
                print("✓ All tasks saved. Goodbye!")
                break
            else:
                print("\n✗ Invalid choice! Please enter a number between 0-9.")
            
            input("\nPress Enter to continue...")


def main():
    """Entry point of the application"""
    app = TaskApp()
    app.run()


if __name__ == "__main__":
    main()
