import argparse
from utils.employee_reader import CSVEmployeeReader
from utils.report_factory import ReportFactory

def parse_args():
    parser = argparse.ArgumentParser(description="Payroll report generator")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument("--report", required=True, choices=["payout"], help="Type of report")
    return parser.parse_args()

def main():
    args = parse_args()
    employees = []
    for file in args.files:
        reader = CSVEmployeeReader(file)
        employees.extend(reader.read())
    report = ReportFactory.get_report(args.report)
    report.generate(employees)

if __name__ == "__main__":
    main()