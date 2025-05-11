from abc import ABC, abstractmethod

class EmployeeReader(ABC):
    @abstractmethod
    def read(self) -> list[dict]:
        pass

class CSVEmployeeReader(EmployeeReader):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> list[dict]:
        with open(self.filepath, encoding="utf-8") as f:
            header = f.readline().strip().split(",")
            col_map = {
                "name": "name",
                "department": "department",
                "hours_worked": "hours",
                "hours": "hours",
                "hourly_rate": "rate",
                "rate": "rate",
                "salary": "rate",
            }
            idx = {col_map.get(h, h): i for i, h in enumerate(header) if col_map.get(h, h) in {"name", "department", "hours", "rate"}}
            employees = []
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split(",")
                employees.append({
                    "name": parts[idx["name"]],
                    "department": parts[idx["department"]],
                    "hours": int(parts[idx["hours"]]),
                    "rate": int(parts[idx["rate"]]),
                })
            return employees