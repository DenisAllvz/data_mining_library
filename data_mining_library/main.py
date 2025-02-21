import argparse
from pathlib import Path
from typing import Dict

from data_mining_library.config.logging_config import setup_logging
from data_mining_library.config.analysis_config import ANALYSIS_PARAMS, TARGET_NAMES

from data_mining_library.preprocessing.data_loader import DataLoader
from data_mining_library.preprocessing.data_preprocessor import DataPreprocessor

from data_mining_library.analysis.feature_analyzer import FeatureAnalyzer
from data_mining_library.analysis.performance_analyzer import PerformanceAnalyzer
from data_mining_library.analysis.correlation_analyzer import CorrelationAnalyzer
from data_mining_library.analysis.risk_analyzer import RiskAnalyzer
from data_mining_library.analysis.semester_analyzer import SemesterAnalyzer

from data_mining_library.visualization.plot_config import setup_plot_style

from data_mining_library.utils.validation_utils import DataValidator

from data_mining_library.export.report_generator import ReportGenerator
from data_mining_library.export.data_exporter import DataExporter

def main(file_path: str) -> Dict:
    logger = setup_logging()
    logger.info("Starting main execution")

    try:
        setup_plot_style()
        logger.info(f"Loading data from: {file_path}")
        df = DataLoader.load_data(file_path)

        logger.info("Validating data")
        DataValidator.validate_required_columns(df, ["Target"])
        DataValidator.validate_target_values(df, {0, 1, 2})

        logger.info("Preprocessing data")
        preprocessor = DataPreprocessor()
        df = preprocessor.setup_data_types(df)

        results = {}

        logger.info("Starting feature analysis")
        feature_analyzer = FeatureAnalyzer(
            df=df,
            numeric_features=preprocessor.numeric_features,
            categorical_features=preprocessor.categorical_features,
            target_names=TARGET_NAMES,
        )
        results["feature_distributions"] = feature_analyzer.analyze_feature_distributions()

        logger.info("Starting performance analysis")
        performance_analyzer = PerformanceAnalyzer(df)
        results["academic_performance"] = performance_analyzer.analyze_academic_performance()

        logger.info("Starting correlation analysis")
        correlation_analyzer = CorrelationAnalyzer(
            df=df,
            numeric_features=preprocessor.numeric_features,
            categorical_features=preprocessor.categorical_features,
        )
        results["correlations"] = correlation_analyzer.analyze_correlations()

        logger.info("Starting risk analysis")
        risk_analyzer = RiskAnalyzer(
            df=df,
            numeric_features=preprocessor.numeric_features,
            analysis_params=ANALYSIS_PARAMS,
        )
        results["dropout_patterns"] = risk_analyzer.analyze_dropout_patterns()
        results["risk_assessment"] = risk_analyzer.generate_risk_assessment()

        logger.info("Starting semester analysis")
        semester_analyzer = SemesterAnalyzer(df, TARGET_NAMES)
        results["semester_patterns"] = semester_analyzer.analyze_semester_patterns()

        logger.info("Generating reports and exporting results")
        report_generator = ReportGenerator(results, df)
        output_path = Path("analysis_results")
        report_generator.generate_summary_report(output_path)

        data_exporter = DataExporter(results)
        data_exporter.export_results()

        logger.info("Analysis completed successfully")
        return results

    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        logger.exception("Detailed error trace:")
        return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run data analysis pipeline.")
    parser.add_argument("file_path", type=str, help="Path to the input dataset")
    args = parser.parse_args()
    main(args.file_path)