import unittest
from validator import Validator

class TestValidator(unittest.TestCase):
    
    def test_valid_date_format(self):
        """Test valid date format YYYY-MM-DD"""
        self.assertTrue(Validator.validate_date("2025-11-15"))
        self.assertTrue(Validator.validate_date("2025-01-01"))
    
    def test_invalid_date_format(self):
        """Test invalid date formats"""
        self.assertFalse(Validator.validate_date("15-11-2025"))  # Wrong format
        self.assertFalse(Validator.validate_date("2025/11/15"))  # Wrong separator
        self.assertFalse(Validator.validate_date(""))  # Empty string
        self.assertFalse(Validator.validate_date("invalid"))  # Not a date
    
    def test_invalid_date_values(self):
        """Test invalid date values (boundary)"""
        self.assertFalse(Validator.validate_date("2025-13-01"))  # Invalid month
        self.assertFalse(Validator.validate_date("2025-11-32"))  # Invalid day
    
    def test_valid_priority(self):
        """Test valid priority values"""
        self.assertTrue(Validator.validate_priority("High"))
        self.assertTrue(Validator.validate_priority("Medium"))
        self.assertTrue(Validator.validate_priority("Low"))
    
    def test_invalid_priority(self):
        """Test invalid priority values (equivalence partitioning)"""
        self.assertFalse(Validator.validate_priority("Urgent"))
        self.assertFalse(Validator.validate_priority(""))
        self.assertFalse(Validator.validate_priority("high"))  # Wrong case
        self.assertFalse(Validator.validate_priority("123"))

if __name__ == '__main__':
    unittest.main()
