"""Tests for the simple study planner project."""

import unittest
from datetime import date, timedelta
import module


class TestStudyPlanner(unittest.TestCase):
    """Test cases for the functions in module.py."""

    def test_calculate_grade(self):
        scores = [80, 90, 100]
        result = module.calculate_grade(scores)
        self.assertEqual(result, 90.0)

    def test_days_left(self):
        tomorrow = date.today() + timedelta(days=1)
        tomorrow_string = tomorrow.strftime("%Y-%m-%d")
        result = module.days_left(tomorrow_string)
        self.assertEqual(result, 1)

    def test_task_priority(self):
        result = module.task_priority(5, 2)
        self.assertEqual(result, 48)

    def test_make_study_plan(self):
        result = module.make_study_plan("final project", 3)
        self.assertEqual(result, "Study final project for about 3 hour(s).")


if __name__ == "__main__":
    unittest.main()
    
