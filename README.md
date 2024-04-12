# Educational Database Management System in MySQL
A simple demonstration of using Python's MySQL by creating an Educational Database

## Introduction

This project is a comprehensive system designed to manage and utilize an educational database. It includes functionalities such as importing data, inserting and updating course information, listing courses, managing popular courses, handling administrative emails, tracking active students, and managing machine usage within a university setting. The system is developed in Python and interacts with a MySQL database, showcasing the integration of various Python modules for database operations.

## Requirements

- Python 3.x
- MySQL Server
- mysql-connector-python

Ensure that you have MySQL Server running and accessible. You may need to configure the `constants.py` file to match your database connection settings, including the host, user, password, and database name.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python package: `mysql-connector-python`.

 ```bash
 pip install mysql-connector-python
 ```
## Usage

To run the system, use the following command format from the terminal:
   ```bash
   python project.py <function name> [params]
   ```
Replace <function name> with any of the available function names described below, and [params] with the appropriate parameters for that function.

## Function Descriptions

- `import`: Import data from a specified folder into the database.
- `insertUse`: Insert a usage record for a project.
- `updateCourse`: Update the title of a specified course.
- `listCourse`: List all courses associated with a given student.
- `popularCourse`: Retrieve the top N popular courses based on enrollment.
- `adminEmails`: List administrator emails for a specified machine.
- `activeStudent`: List active students for a given machine within a specified date range.
- `machineUsage`: Get machine usage statistics for a specific course.
- `insertStudent`: Insert a new student record into the database.
- `addEmail`: Add an email to an existing student record.
- `deleteStudent`: Delete a student record from the database.
- `insertMachine`: Insert a new machine record into the database.

### Example Commands

- Import data: `python project.py import test_data`
- Insert student usage: `python project.py insertUse 2 aanthony4 1 2024-03-01 2024-03-15`
- Update course title: `python project.py updateCourse 1 "Database Management"`
- List courses for a student: `python project.py listCourse mchang13`

Refer to the specific function documentation in the code for detailed parameter descriptions and additional examples.
