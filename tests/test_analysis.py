import pytest
import pandas as pd
from data_mining_library.analysis.performance_analyzer import PerformanceAnalyzer
from data_mining_library.analysis.correlation_analyzer import CorrelationAnalyzer
from data_mining_library.analysis.risk_analyzer import RiskAnalyzer
from data_mining_library.analysis.semester_analyzer import SemesterAnalyzer
from data_mining_library.preprocessing.data_loader import DataLoader
from data_mining_library.utils.validation_utils import DataValidator

@pytest.fixture
def sample_data():
    data = {
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [5, 4, 3, 2, 1],
        'Target': [0, 1, 2, 1, 0]
    }
    return pd.DataFrame(data)

def test_performance_analysis(sample_data):
    analyzer = PerformanceAnalyzer(sample_data)
    result = analyzer.analyze_academic_performance()
    assert isinstance(result, dict)

def test_correlation_analysis(sample_data):
    analyzer = CorrelationAnalyzer(df=sample_data, numeric_features=['Feature1', 'Feature2'], categorical_features=['Target'])
    result = analyzer.analyze_correlations()
    assert isinstance(result, pd.DataFrame)

def test_risk_analysis(sample_data):
    analyzer = RiskAnalyzer(df=sample_data, numeric_features=['Feature1', 'Feature2'], analysis_params={})
    dropout_patterns = analyzer.analyze_dropout_patterns()
    risk_assessment = analyzer.generate_risk_assessment()
    assert isinstance(dropout_patterns, dict)
    assert isinstance(risk_assessment, dict)

def test_semester_analysis(sample_data):
    analyzer = SemesterAnalyzer(df=sample_data, target_names=['Graduate', 'Enrolled', 'Dropout'])
    result = analyzer.analyze_semester_patterns()
    assert isinstance(result, dict)

def test_data_validation(sample_data):
    DataValidator.validate_required_columns(sample_data, ['Target'])
    DataValidator.validate_target_values(sample_data, {0, 1, 2})