class CorrelationAnalyzer:
    def __init__(self, df, numeric_features, categorical_features):
        self.df = df
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features

    def analyze_correlations(self):
        correlation_results = {}
        
        # Analyze correlations for numeric features
        correlation_matrix = self.df[self.numeric_features].corr()
        correlation_results['numeric_correlations'] = correlation_matrix

        # Analyze correlations for categorical features
        for cat_feature in self.categorical_features:
            for num_feature in self.numeric_features:
                correlation = self.df.groupby(cat_feature)[num_feature].mean()
                correlation_results[f'correlation_{cat_feature}_{num_feature}'] = correlation

        return correlation_results