import re
from datetime import datetime

class Validator:
    """Validates user inputs"""
    
    @staticmethod
    def validate_date(date_string):
        """Validate date format YYYY-MM-DD"""
        if not date_string:
            return False
        
        # Check format with regex
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, date_string):
            return False
        
        # Check if it's a valid date
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_priority(priority):
        """Validate priority level"""
        valid_priorities = ["High", "Medium", "Low"]
        return priority in valid_priorities

