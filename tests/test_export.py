import pytest
from data_mining_library.export.data_exporter import DataExporter
from data_mining_library.export.report_generator import ReportGenerator

def test_data_exporter_initialization():
    results = {"test_key": "test_value"}
    data_exporter = DataExporter(results)
    assert data_exporter.results == results

def test_export_results(mocker):
    results = {"test_key": "test_value"}
    data_exporter = DataExporter(results)
    
    mock_open = mocker.patch("builtins.open", mocker.mock_open())
    data_exporter.export_results()
    
    mock_open.assert_called_once_with("exported_results.json", "w")

def test_report_generator_initialization():
    results = {"test_key": "test_value"}
    df = None  # Placeholder for DataFrame
    report_generator = ReportGenerator(results, df)
    assert report_generator.results == results
    assert report_generator.df is None

def test_generate_summary_report(mocker):
    results = {"test_key": "test_value"}
    df = None  # Placeholder for DataFrame
    report_generator = ReportGenerator(results, df)
    
    mock_save = mocker.patch.object(report_generator, "generate_summary_report")
    report_generator.generate_summary_report("test_output_path")
    
    mock_save.assert_called_once_with("test_output_path")