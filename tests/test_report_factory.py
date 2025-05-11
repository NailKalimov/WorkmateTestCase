import pytest
from utils.report_factory import ReportFactory
from utils.report import PayoutReport

def test_get_report_returns_payout_report():
    report = ReportFactory.get_report("payout")
    assert isinstance(report, PayoutReport)

def test_get_report_invalid_type():
    with pytest.raises(ValueError) as excinfo:
        ReportFactory.get_report("unknown")
    assert "Unknown report type" in str(excinfo.value)