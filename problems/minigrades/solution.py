"""
mini-grades v0 - simplified implementation

Scope: Functional structure and basic logic only.
Limitations: Loops and lists are not yet used; data is not persistently stored.
"""

import sys
import os

# --- FUNCTION DEFINITIONS ---

def initialize():
    """Creates the .minigrades directory and data file for the system to operate."""
    if os.path.exists(".minigrades"):
        return "Already initialized"
    os.mkdir(".minigrades")
    f = open(".minigrades/data.txt", "w")
    f.close()
    return "Initialized empty system in .minigrades/"

def add_student(id, name):
    """Enables adding a new student to the system."""
    if not id.isdigit():
        return "Invalid input: Please enter a numeric value."
    
    if not os.path.exists(".minigrades/data.txt"):
        return "Not initialized. Run: python solution.py init"
    
    f_check = open(".minigrades/data.txt", "r")
    content = f_check.read()
    f_check.close()
    
    # Searching for ID with a delimiter ( |) to avoid partial matches (e.g., finding 1 inside 101).
    if id + " |" in content:
        return f"Error: Student with ID {id} already exists."
    
    f = open(".minigrades/data.txt", "a")
    # Saving data in a delimited format (ID | Name).
    f.write(id + " | " + name + "\n")
    f.close()

    return "Student added successfully."

def add_grade(id, grade):
    """Enables adding a grade to a specific student."""
    if not id.isdigit():
        return "Invalid input: Please enter a numeric value."
    
    if not os.path.exists(".minigrades/data.txt"):
        return "Not initialized. Run: python solution.py init"

    # Reading data from data.txt into the content variable
    f_check = open(".minigrades/data.txt", "r")
    content = f_check.read()
    f_check.close()

    # Checking if the requested student exists in the content
    if not id + " |" in content:
        return f"Error: No student found with ID {id}."
    
    if not grade.isdigit():
        return "Invalid input: Please enter a numeric value."
        
    if int(grade) < 0 or int(grade) > 100:
        return "Invalid grade: Grades must be between 0 and 100."
    else:
        return f"Grades added successfully for student {id}."

def delete_student(id):
    """Enables deleting a student from the system."""
    if not os.path.exists(".minigrades/data.txt"):
        return "Not initialized. Run: python solution.py init"
    
    if not id.isdigit():
        return "Invalid input: Please enter a numeric value."

    f_check = open(".minigrades/data.txt", "r")
    content = f_check.read()
    f_check.close()

    # Checking if the requested student exists in the content
    if not id + " |" in content:
        return f"Error: No student found with ID {id}."
    
    return "Student and all grades deleted successfully."

def list_students():
    """Lists all students currently in the system."""
    if not os.path.exists(".minigrades/data.txt"):
        return "Error: No students found in the system. Operation aborted."
    
    f = open(".minigrades/data.txt", "r")
    content = f.read()
    f.close()

    # Checking if content is empty (if so, no data exists)
    if content == "":
        return "Error: No students found in the system. Operation aborted."
    
    return content

def calculate_average(id):
    """Calculates the average of a student (v0 Simulation)."""
    if not os.path.exists(".minigrades/data.txt"):
        return "Not initialized. Run: python solution.py init"
    
    f_check = open(".minigrades/data.txt", "r")
    content = f_check.read()
    f_check.close()

    # Checking if the requested student exists in the content
    if not id + " |" in content:
        return f"Error: No student found with ID {id}."
    
    return "Average calculation will be implemented in future weeks."

def generate_report():
    """Generates a report file from the system data."""
    if not os.path.exists(".minigrades/data.txt"):
        return "Error: No data available to generate a report."
    
    f = open(".minigrades/data.txt", "r")
    current_data = f.read()
    f.close()

    if current_data == "":
        return "Error: No data available to generate a report."
    
    r = open(".minigrades/report.txt", "w")
    r.write("ID | NAME\n-----------\n")
    r.write(current_data)
    r.close()

    return "Report saved to .minigrades/report.txt"

# --- MAIN PROGRAM ---

if len(sys.argv) < 2:
    print("Usage: python solution.py <command> [args]")

elif sys.argv[1] == "init":
    print(initialize())

elif sys.argv[1] == "add":
    if len(sys.argv) < 4:
        print("Usage: python solution.py add <id> <name>")
    else:
        print(add_student(sys.argv[2], sys.argv[3]))

elif sys.argv[1] == "add-grade":
    if len(sys.argv) < 4:
        print("Usage: python solution.py add-grade <id> <grades>")
    else:
        print(add_grade(sys.argv[2], sys.argv[3]))

elif sys.argv[1] == "delete":
    if len(sys.argv) < 3:
        print("Usage: python solution.py delete <id>")
    else:
        print(delete_student(sys.argv[2]))

elif sys.argv[1] == "list":
    print(list_students())

elif sys.argv[1] == "report":
    print(generate_report())

elif sys.argv[1] == "average":
    if len(sys.argv) < 3:
        print("Usage: python solution.py average <id>")
    else:
        print(calculate_average(sys.argv[2]))

else:
    print("Unknown command: " + sys.argv[1] + ". Please select from the menu.")