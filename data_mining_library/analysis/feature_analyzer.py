class FeatureAnalyzer:
    def __init__(self, df, numeric_features, categorical_features, target_names):
        self.df = df
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features
        self.target_names = target_names

    def analyze_feature_distributions(self):
        distributions = {}
        for feature in self.numeric_features:
            distributions[feature] = self.df[feature].describe()
        for feature in self.categorical_features:
            distributions[feature] = self.df[feature].value_counts()
        return distributions