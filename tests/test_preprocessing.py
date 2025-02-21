import pytest
import pandas as pd
from data_mining_library.preprocessing.data_loader import DataLoader
from data_mining_library.preprocessing.data_preprocessor import DataPreprocessor

def test_setup_data_types():
    # Create a sample DataFrame
    data = {
        'Feature1': [1, 2, 3],
        'Feature2': ['A', 'B', 'C'],
        'Target': [0, 1, 2]
    }
    df = pd.DataFrame(data)

    # Initialize the DataPreprocessor
    preprocessor = DataPreprocessor()

    # Setup data types
    processed_df = preprocessor.setup_data_types(df)

    # Check if the data types are set correctly
    assert processed_df['Feature1'].dtype == 'int64'
    assert processed_df['Feature2'].dtype == 'object'
    assert processed_df['Target'].dtype == 'int64'

def test_load_data():
    # Assuming a sample CSV file path
    file_path = 'sample_data.csv'
    
    # Create a sample CSV file for testing
    df = pd.DataFrame({
        'Feature1': [1, 2, 3],
        'Feature2': ['A', 'B', 'C'],
        'Target': [0, 1, 2]
    })
    df.to_csv(file_path, index=False)

    # Load data using DataLoader
    loaded_df = DataLoader.load_data(file_path)

    # Check if the loaded DataFrame matches the original
    pd.testing.assert_frame_equal(df, loaded_df)