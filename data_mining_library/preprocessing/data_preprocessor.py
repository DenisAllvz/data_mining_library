class DataPreprocessor:
    def __init__(self):
        self.numeric_features = []
        self.categorical_features = []

    def setup_data_types(self, df):
        # Implementation for setting up data types for the DataFrame
        for column in df.columns:
            if df[column].dtype in ['int64', 'float64']:
                self.numeric_features.append(column)
            else:
                self.categorical_features.append(column)
        return df