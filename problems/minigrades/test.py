"""
SPECS test scenarios
Project: mini-grades
"""

import subprocess
import os
import shutil
import pytest

# --- Helper Functions ---
def run_cmd(args):
    """Executes the command in the terminal. Runs 'init' first to ensure the system is always ready."""
    # Automatically prepare the system at the start of each test
    subprocess.run(["python", "solution.py", "init"], capture_output=True, text=True)
    
    result = subprocess.run(
        ["python", "solution.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def setup_function():
    """Resets the .minigrades directory before each test."""
    if os.path.exists(".minigrades"):
        shutil.rmtree(".minigrades")

# --- add student tests ---
def test_add_student_success():
    """Tests the successful addition of a new student with a unique ID."""
    response = run_cmd(["add", "101", "Berke"])
    assert response == "Student added successfully."

def test_add_student_duplicate():
    """Tests the 'Duplicate ID' error when attempting to add a student with an existing ID."""
    run_cmd(["add", "101", "Berke"])
    response = run_cmd(["add", "101", "Efe"])
    assert response == "Error: Student with ID 101 already exists."

def test_add_student_non_numeric_id():
    """Tests the numeric value error when a non-numeric string is entered as an ID."""
    response = run_cmd(["add", "abc", "Berke"])
    assert response == "Invalid input: Please enter a numeric value."

# --- add grade tests ---
def test_add_grade_success():
    """Tests the successful addition of valid grades to an existing student."""
    run_cmd(["add", "101", "Berke"])
    response = run_cmd(["add-grade", "101", "80"])
    assert response == "Grades added successfully for student 101."

def test_add_grade_non_numeric_grade():
    """Tests that the added grade must consist of numbers."""
    run_cmd(["add", "101", "Berke"])
    response = run_cmd(["add-grade", "101", "abc"])
    assert response == "Invalid input: Please enter a numeric value."

def test_add_grade_student_not_found():
    """Tests the error when trying to add a grade to a student ID that does not exist."""
    response = run_cmd(["add-grade", "999", "80"])
    assert response == "Error: No student found with ID 999."

# --- delete student tests ---
def test_delete_student_success():
    """Tests the deletion of an existing student via their ID."""
    run_cmd(["add", "101", "Berke"])
    response = run_cmd(["delete", "101"])
    assert response == "Student and all grades deleted successfully."

def test_delete_student_not_found():
    """Tests the error message when attempting to delete a non-existent ID."""
    response = run_cmd(["delete", "999"])
    assert response == "Error: No student found with ID 999."

# --- calculate average tests ---
def test_calculate_average_success():
    """Tests the (simulation message) for a registered student's average calculation."""
    run_cmd(["add", "101", "Berke"])
    response = run_cmd(["average", "101"])
    assert response == "Average calculation will be implemented in future weeks."

def test_calculate_average_student_not_found():
    """Tests the error when querying the average of a non-registered student."""
    response = run_cmd(["average", "999"])
    assert response == "Error: No student found with ID 999."

# --- list students tests ---
def test_list_students_success():
    """Tests the listing of all registered students according to the format (ID | Name)."""
    run_cmd(["add", "101", "Berke"])
    run_cmd(["add", "102", "Efe"])
    response = run_cmd(["list"])
    assert "101 | Berke" in response
    assert "102 | Efe" in response

def test_list_students_empty():
    """Tests the error when listing is requested while no students are registered."""
    response = run_cmd(["list"])
    assert response == "Error: No students found in the system. Operation aborted."

# --- generate report tests ---
def test_generate_report_success():
    """Tests the successful generation of a report from system data."""
    run_cmd(["add", "101", "Berke"])
    run_cmd(["add", "102", "Efe"])
    response = run_cmd(["report"])
    assert response == "Report saved to .minigrades/report.txt"
    assert os.path.exists(".minigrades/report.txt")

def test_generate_report_empty():
    """Tests the error when report generation is requested with no registered students."""
    response = run_cmd(["report"])
    assert response == "Error: No data available to generate a report."

# --- unknown command test ---
def test_unknown_command():
    """Tests the error provided when an unknown command is entered."""
    response = run_cmd(["hello"])
    assert "Unknown command: hello. Please select from the menu." in response