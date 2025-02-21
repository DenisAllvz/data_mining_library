class DataLoader:
    @staticmethod
    def load_data(file_path: str) -> pd.DataFrame:
        """Load data from a specified file path.

        Args:
            file_path (str): The path to the data file.

        Returns:
            pd.DataFrame: The loaded data as a DataFrame.
        """
        return pd.read_csv(file_path)  # Assuming the data is in CSV format. Adjust as necessary.