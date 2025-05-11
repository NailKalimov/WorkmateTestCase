from abc import ABC, abstractmethod
from collections import defaultdict


class Report(ABC):
    @abstractmethod
    def generate(self, employees: list[dict]) -> None:
        pass


class PayoutReport(Report):
    def generate(self, employees: list[dict]) -> None:
        col_widths = {
            "name": 18,
            "hours": 7,
            "rate": 6,
            "payout": 9,
        }
        header = f'{"":18}{"name":{col_widths["name"]}}{"hours":>{col_widths["hours"]}}{"rate":>{col_widths["rate"]}}{"payout":>{col_widths["payout"]}}'
        print(header)
        departments = defaultdict(list)
        for emp in employees:
            departments[emp["department"]].append(emp)
        for dept, emps in departments.items():
            print(f"\n{dept}")
            total_hours = 0
            total_payout = 0
            for emp in emps:
                payout = emp["hours"] * emp["rate"]
                total_hours += emp["hours"]
                total_payout += payout
                print(
                    f'{"-"*15} {emp["name"]:<{col_widths["name"]}}{emp["hours"]:>{col_widths["hours"]}}{emp["rate"]:>{col_widths["rate"]}}${payout:>{col_widths["payout"]}}$')
            print(
                f'{" "*15} {" ":{col_widths["name"]}}{total_hours:>{col_widths["hours"]}}{" ":{col_widths["rate"]+1}}{total_payout:>{col_widths["payout"]}}$')
