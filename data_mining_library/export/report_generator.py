class ReportGenerator:
    def __init__(self, results, df):
        self.results = results
        self.df = df

    def generate_summary_report(self, output_path):
        # Create output directory if it doesn't exist
        output_path.mkdir(parents=True, exist_ok=True)

        # Generate summary report content
        report_content = self._create_report_content()

        # Write report to a file
        report_file = output_path / "summary_report.txt"
        with open(report_file, 'w') as file:
            file.write(report_content)

    def _create_report_content(self):
        content = "Analysis Summary Report\n"
        content += "=" * 30 + "\n\n"

        content += f"Total students analyzed: {len(self.df)}\n"
        content += f"Features processed: {len(self.results.get('feature_distributions', []))}\n"
        
        if "academic_performance" in self.results:
            content += "\nAcademic Performance:\n"
            content += str(self.results["academic_performance"]) + "\n"

        if "correlations" in self.results:
            content += "\nCorrelations:\n"
            content += str(self.results["correlations"]) + "\n"

        if "dropout_patterns" in self.results:
            content += "\nDropout Patterns:\n"
            content += str(self.results["dropout_patterns"]) + "\n"

        if "risk_assessment" in self.results:
            content += "\nRisk Assessment:\n"
            content += str(self.results["risk_assessment"]) + "\n"

        if "semester_patterns" in self.results:
            content += "\nSemester Patterns:\n"
            content += str(self.results["semester_patterns"]) + "\n"

        return content.strip()