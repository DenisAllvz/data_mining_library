import unittest
from data_mining_library.utils.validation_utils import DataValidator

class TestDataValidator(unittest.TestCase):

    def setUp(self):
        self.df_valid = pd.DataFrame({
            'Target': [0, 1, 2, 1, 0],
            'Feature1': [1.0, 2.0, 3.0, 4.0, 5.0],
            'Feature2': ['A', 'B', 'C', 'A', 'B']
        })
        self.df_invalid_columns = pd.DataFrame({
            'Feature1': [1.0, 2.0, 3.0, 4.0, 5.0],
            'Feature2': ['A', 'B', 'C', 'A', 'B']
        })
        self.df_invalid_values = pd.DataFrame({
            'Target': [0, 1, 3, 1, 0],
            'Feature1': [1.0, 2.0, 3.0, 4.0, 5.0],
            'Feature2': ['A', 'B', 'C', 'A', 'B']
        })

    def test_validate_required_columns(self):
        DataValidator.validate_required_columns(self.df_valid, ['Target'])
        with self.assertRaises(ValueError):
            DataValidator.validate_required_columns(self.df_invalid_columns, ['Target'])

    def test_validate_target_values(self):
        DataValidator.validate_target_values(self.df_valid, {0, 1, 2})
        with self.assertRaises(ValueError):
            DataValidator.validate_target_values(self.df_invalid_values, {0, 1, 2})

if __name__ == '__main__':
    unittest.main()