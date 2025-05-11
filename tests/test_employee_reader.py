import tempfile
import os
import pytest
from utils.employee_reader import CSVEmployeeReader
from utils.report import PayoutReport

@pytest.fixture
def csv_file():
    content = "name,department,hours,rate\nJohn,IT,10,100\nJane,HR,20,200\n"
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        f.write(content)
        f.flush()
        yield f.name
    os.remove(f.name)

def test_csv_employee_reader(csv_file):
    reader = CSVEmployeeReader(csv_file)
    employees = reader.read()
    assert employees == [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
        {"name": "Jane", "department": "HR", "hours": 20, "rate": 200},
    ]

def test_csv_employee_reader_hourly_rate():
    content = "name,department,hours,hourly_rate\nJohn,IT,10,100\n"
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        f.write(content)
        f.flush()
        reader = CSVEmployeeReader(f.name)
        employees = reader.read()
    os.remove(f.name)
    assert employees == [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
    ]

def test_csv_employee_reader_salary():
    content = "name,department,hours,salary\nJohn,IT,10,100\n"
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        f.write(content)
        f.flush()
        reader = CSVEmployeeReader(f.name)
        employees = reader.read()
    os.remove(f.name)
    assert employees == [
        {"name": "John", "department": "IT", "hours": 10, "rate": 100},
    ]



def test_csv_employee_reader_file_not_found():
    with pytest.raises(FileNotFoundError):
        reader = CSVEmployeeReader("definitely_no_such_file.csv")
        reader.read()