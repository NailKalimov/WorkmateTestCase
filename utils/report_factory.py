from .report import PayoutReport

class ReportFactory:
    _reports = {
        "payout": PayoutReport,
    }

    @classmethod
    def get_report(cls, name: str):
        if name not in cls._reports:
            raise ValueError(f"Unknown report type: {name}")
        return cls._reports[name]()