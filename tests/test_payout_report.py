import pytest
from utils.report import PayoutReport

def test_payout_report_output(capsys):
    employees = [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
        {"name": "Jane", "department": "HR", "hours": 20, "rate": 200},
    ]
    report = PayoutReport()
    report.generate(employees)
    out = capsys.readouterr().out
    assert "IT" in out
    assert "HR" in out
    assert "100" in out
    assert "200" in out 
