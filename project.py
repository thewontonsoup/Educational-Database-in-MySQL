import mysql.connector
import os
from pathlib import Path
import csv
#import traceback #print(traceback.format_exc())
#People who have contributed to the project: Wilson Su

# This script will initialize your local DB to have the table created and data loaded
# please make sure that you have filled in the constants correctly to run this query successfully
sql_file_path = 'cs122a_db.sql'

# Create a connection to the database

USER = "root"
PASSWORD = "dsu701017"
DATABASE = "cs122a"
'''
USER = "test"
PASSWORD = "password"
DATABASE = "cs122a"
'''

TESTIMPORT_FOLDER = "python project.py import test_data" #python project.py import test_data >> result0.txt
TESTINSERT_STUDENT = "python project.py insertStudent testID test@uci.edu Alice NULL Wong"
TESTINSERT_EMAIL = "python project.py addEmail testID test@gmail.com"
TESTDELETE = "python project.py deleteStudent testID"
TESTINSERT_MACHINE = "python project.py insertMachine 102 test.com 192.168.10.5 Active “DBH 1011”"
TESTINSERT_USE = "python project.py insertUse 5 testID 102 2023-01-09 2023-03-10"
TESTUPDATE = "python project.py updateCourse 1287 “Intro do db management”"
TESTLIST = "python project.py listCourse mchang13"
TESTPOP = "python project.py popularCourse 3"
TESTADMIN = "python project.py adminEmails 1"
#TESTACTIVE = "python project.py activeStudent 4 2 "2020-01-01" "2020-05-10""
TESTUSAGE = "python project.py machineUsage 4"


PRIORITY_DICT = {"users.csv": 0, "students.csv": 1, "admins.csv": 2, "machines.csv": 3, "courses.csv": 4, "projects.csv": 5,  "use.csv": 6, "manage.csv": 7, "emails.csv": 8}
COMMAND = {"users.csv": """INSERT INTO `Users` VALUES (%s, %s, %s, %s)""",
           "students.csv": """INSERT INTO `Students` VALUES (%s)""",
           "admins.csv": """INSERT INTO `Administrators` VALUES (%s)""",
           "courses.csv": """INSERT INTO `Courses` VALUES (%s, %s, %s)""",
           "projects.csv": """INSERT INTO `Projects` VALUES (%s, %s, %s, %s)""",
           "machines.csv": """INSERT INTO `Machines` VALUES (%s, %s, %s, %s, %s)""",
           "use.csv": """INSERT INTO `StudentUseMachinesInProject` VALUES (%s, %s, %s, %s, %s)""",
           "manage.csv": """INSERT INTO `AdministratorManageMachines` VALUES (%s, %s)""",
           "emails.csv": """INSERT INTO `UserEmail` VALUES (%s, %s)"""}

import sys

def import_folder(folder_name):
    # First put in the skeleton for everything.
        # Open and read the SQL file
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()

    # Execute each statement in the SQL file
    for statement in sql_script.split(';'):
        # Ignore empty statements (which can occur due to splitting by ';')
        if statement.strip():
            #print("running: ", statement)
            cursor.execute(statement)


    folder_name = Path(folder_name)


    csv_files = [f for f in os.listdir(folder_name) if f.endswith('.csv')]
    csv_files = sorted(csv_files, key = lambda item: PRIORITY_DICT[item.lower()])
    csv_files = [os.path.join(folder_name, f) for f in csv_files]

    result = []

    for file in csv_files:
        strname = os.path.basename(file).lower()
        i = 0
        with open(file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                row = [None if element == "NULL" else element for element in row]
                #print(row)
                #print(COMMAND[strname.lower()])
                cursor.execute(COMMAND[strname], row)
                i+=1
            if strname in ["users.csv", "machines.csv", "courses.csv"]:
                result.append(i)

    #print("This worked holy moly")
    db_connection.commit()
    print(f"{result[0]},{result[1]},{result[2]}")

def insertStudent(student):

    try:
        student = [None if element == "NULL" else element for element in student]
        cursor.execute(COMMAND["users.csv"], (student[0], student[2], student[3], student[4]))
        cursor.execute(COMMAND["students.csv"], (student[0], ))
        cursor.execute(COMMAND["emails.csv"], (student[0], student[1]))
        db_connection.commit()
        print("Success")
        return
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def addEmail(e_info):
    try:
        e_info = [None if element == "NULL" else element for element in e_info]
        cursor.execute(COMMAND["emails.csv"], (e_info))
        db_connection.commit()
        print("Success")
        return
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
def insertMachine(m_info):
    try:
        m_info = [None if element == "NULL" else element for element in m_info]
        cursor.execute(COMMAND["machines.csv"], (m_info))
        db_connection.commit()
        print("Success")
        return
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def deleteStudent(UCINetID):
    try:
        UCINetID = None if UCINetID == "NULL" else UCINetID
        #cursor.execute("""DELETE FROM `AdministratorManageMachines` WHERE AdministratorUCINetID = %s""", (UCINetID,))
        #cursor.execute("""DELETE FROM `StudentUseMachinesInProject` WHERE StudentUCINetID = %s""", (UCINetID,))
        cursor.execute("""DELETE FROM `Users` WHERE UCINetID = %s""", (UCINetID,))
        cursor.execute("""DELETE FROM `Students` WHERE UCINetID = %s""", (UCINetID,))
        db_connection.commit()
        print("Success")
        return
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
def insertUse(record):
    try:
        record = [None if element == "NULL" else element for element in record]
        cursor.execute(COMMAND["use.csv"], (record))
        db_connection.commit()
        print("Success")
        return
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def updateCourse(courseinfo):
    try:
        courseinfo = [None if element == "NULL" else element for element in courseinfo]
        cursor.execute("""UPDATE Courses SET title = %s WHERE CourseID = %s""", (courseinfo[1], courseinfo[0]))
        db_connection.commit()
        print("Success")
        return
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def listCourse(ID):
    ID = None if ID == "NULL" else ID
    try:
        cursor.execute(
        """SELECT DISTINCT c.CourseID, c.Title, c.Quarter
    FROM StudentUseMachinesInProject AS s
    INNER JOIN Projects AS p 
        ON p.ProjectID = s.ProjectID 
        AND s.StudentUCINetID = %s
    INNER JOIN Courses AS c 
        ON c.CourseID = p.CourseID
    ORDER BY c.CourseID ASC""", (ID,))
        rows = cursor.fetchall()
        for row in rows:
            print(",".join([str(i) if i is not None else "NULL" for i in row]))
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def popularCourse(num):
    num = None if num == "NULL" else int(num)
    try:
        cursor.execute(
        """SELECT c.CourseID, c.Title, COUNT(DISTINCT s.StudentUCINetID) AS Number
    FROM StudentUseMachinesInProject AS s
    INNER JOIN Projects AS p 
        ON p.ProjectID = s.ProjectID 
    INNER JOIN Courses AS c 
        ON c.CourseID = p.CourseID
    GROUP BY c.CourseID
    ORDER BY Number DESC, CourseID DESC
    LIMIT %s;""", (num,))
        rows = cursor.fetchall()
        for row in rows:
            print(",".join([str(i) if i is not None else "NULL" for i in row]))
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def adminEmails(id):
    id = None if id == "NULL" else id
    try:
        cursor.execute(
            """SELECT a.UCINetID, a.FirstName, a.MiddleName, a.LastName, e.Email
        FROM Users AS a
        INNER JOIN AdministratorManageMachines AS am
            ON a.UCINetID = am.AdministratorUCINetID and am.MachineID = %s 
        LEFT JOIN UserEmail AS e
            ON a.UCINetID = e.UCINetID
        ORDER BY a.UCINetID ASC;""", (id,))
        rows = cursor.fetchall()
        outputdict = {}
        for row in rows:
            if((row[0], row[1], row[2], row[3]) in outputdict):
                outputdict[(row[0], row[1], row[2], row[3])].append(row[-1])
            else:
                outputdict[(row[0], row[1], row[2], row[3])] = [row[-1]]
        for admin in outputdict:
            if(len(outputdict[admin]) > 1 or len(outputdict[admin]) == 1 and outputdict[admin][0] is not None):
                print(",".join([str(i) if i is not None else "NULL" for i in admin]) + ","+";".join([str(i) for i in outputdict[admin]]))
            else:
                print(",".join([str(i) if i is not None else "NULL" for i in admin]))
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def activeStudent(machine):
    ID = None if machine[0] == "NULL" else int(machine[0])
    N = None if machine[1] == "NULL" else machine[1]
    start = None if machine[2] == "NULL" else machine[2]
    end = None if machine[3] == "NULL" else machine[3]
    try:
        cursor.execute(
        """SELECT U.UCINetID, U.FirstName, U.MiddleName, U.LastName
FROM Users U
JOIN (
    SELECT StudentUCINetID
    FROM StudentUseMachinesInProject
    WHERE MachineID = %s
      AND StartDate <= %s 
      AND EndDate >= %s
    GROUP BY StudentUCINetID
    HAVING COUNT(*) >= %s
) AS active_students ON U.UCINetID = active_students.StudentUCINetID
ORDER BY U.UCINetID ASC;
""", (ID, end, start, N))
        rows = cursor.fetchall()
        for row in rows:
            print(",".join([str(i) if i is not None else "NULL" for i in row]))
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass

def machineUsage(courseid):
    courseid = None if courseid == "NULL" else int(courseid)
    try:
        cursor.execute(
            """SELECT M.MachineID, M.Hostname, M.IPAddress, COALESCE(COUNT(S.MachineID), 0) AS Mcount
    FROM Courses AS C
    INNER JOIN Projects AS P
    ON C.CourseID = %s AND C.CourseID = P.CourseID
    INNER JOIN StudentUseMachinesInProject as S
    ON P.ProjectID = S.ProjectID
    RIGHT JOIN Machines AS M
    ON M.MachineID = S.MachineID
    GROUP BY M.MachineID
    ORDER BY M.MachineID DESC;
    """, (courseid,))
        rows = cursor.fetchall()
        for row in rows:
            print(",".join([str(i) if i is not None else "NULL" for i in row]))
    except mysql.connector.IntegrityError as e:
        print("Fail")
        return
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        return
    pass
def printResult(result):
    pass
if __name__ == "__main__":
    db_connection = None
    cursor = None
    try:
        db_connection = mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE)
        cursor = db_connection.cursor()
        if len(sys.argv) >= 3:
            command = sys.argv[1]
            result = False
            if command == "import":
                import_folder(sys.argv[2])
            elif command == "insertStudent":
                insertStudent(sys.argv[2:])
            elif command == "addEmail":
                addEmail(sys.argv[2:])
            elif command == "deleteStudent":
                deleteStudent(sys.argv[2])
            elif command =="insertMachine":
                insertMachine(sys.argv[2:])
            elif command == "insertUse":
                insertUse(sys.argv[2:])
            elif command == "updateCourse":
                updateCourse(sys.argv[2:])
            elif command == "listCourse":
                listCourse(sys.argv[2])
            elif command == "popularCourse":
                popularCourse(sys.argv[2])
            elif command == "adminEmails":
                adminEmails(sys.argv[2])
            elif command == "activeStudent":
                activeStudent(sys.argv[2:])
            elif command =="machineUsage":
                machineUsage(sys.argv[2])
            else:
                print(f"Unknown command: {command}")
        else:
            print("Wrong format my dude")
        db_connection.commit()
    finally:
        if db_connection is not None and cursor is not None and db_connection.is_connected():
            cursor.close()
            db_connection.close()
