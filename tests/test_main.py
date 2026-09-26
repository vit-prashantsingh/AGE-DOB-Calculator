import unittest
from unittest.mock import patch
import io
import sys

# Import functions from project modules
from src.age_calculator import age_calculation_student_data
from src.dob_calculator import dob_calculation_student_data


class TestAgeAndDOBCalculator(unittest.TestCase):

    def test_age_calculation_student_data(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Input DATA: Current Date (2026-09-26), Birth Date (2000-05-10)
        age_calculation_student_data(2026, 9, 26, 2000, 5, 10)

        sys.stdout = sys.__stdout__
        expected_output = "Your currently 26years,4months and 16days old \n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_dob_calculation_student_data(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Input DATA: Current Date (2026-09-26), Age (26 years, 4 months, 16 days)
        dob_calculation_student_data(2026, 9, 26, 26, 4, 16)

        sys.stdout = sys.__stdout__
        expected_output = "You were born on: 10/5/2000\n"
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()