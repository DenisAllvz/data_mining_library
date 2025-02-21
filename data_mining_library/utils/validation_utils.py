class DataValidator:
    @staticmethod
    def validate_required_columns(df, required_columns):
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

    @staticmethod
    def validate_target_values(df, valid_values):
        invalid_values = df[~df['Target'].isin(valid_values)]['Target'].unique()
        if invalid_values.size > 0:
            raise ValueError(f"Invalid target values found: {', '.join(map(str, invalid_values))}")