import sqlite3
import bcrypt


def initializeStudentTable():
    conn = sqlite3.connect('students_signup_db.db')
    c = conn.cursor()

    # Create the students_signup_db table if it doesn't exist yet
    c.execute('''CREATE TABLE IF NOT EXISTS students_signup_db
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT NOT NULL, 
                 password TEXT NOT NULL,
                 email TEXT NOT NULL
                 password 10)''')


def initializeTeachersTable():
    conn = sqlite3.connect('teachers_signup_db.db')
    c = conn.cursor()

    # Create the students_signup_db table if it doesn't exist yet
    c.execute('''CREATE TABLE IF NOT EXISTS teachers_signup_db
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT NOT NULL, 
                 password TEXT NOT NULL,
                 email TEXT NOT NULL
                 priority INTEGER DEFAULT 20)''')


def initializeItStaffTable():
    conn = sqlite3.connect('it_staff_signup_db.db')
    c = conn.cursor()

    # Create the students_signup_db table if it doesn't exist yet
    c.execute('''CREATE TABLE IF NOT EXISTS it_staff_signup_db
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT NOT NULL, 
                 password TEXT NOT NULL,
                 email TEXT NOT NULL
                 priority INTEGER DEFAULT 10)''')


def createStudent(username, password, email):
    """
    Given a username, password, and email, insert new student into the student database
    """
    conn = sqlite3.connect('students_signup_db.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO students_signup_db (username, password, email) VALUES (?, ?, ?)",
        (username, encrypt_password(password=password), email)
    )
    conn.commit()
    conn.close()

def createTeacher(username, password, email):
    """
    Given a username, password, and email, insert new teacher into the teacher database
    """
    conn = sqlite3.connect('teachers_signup_db.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO teachers_signup_db (username, password, email) VALUES (?, ?, ?)",
        (username, encrypt_password(password=password), email)
    )
    conn.commit()
    conn.close()

def createItStaff(username, password, email):
    """
    Given a username, password, and email, insert new it staff into the it staff database
    """
    conn = sqlite3.connect('it_staff_signup_db.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO it_staff_signup_db (username, password, email) VALUES (?, ?, ?)",
        (username, encrypt_password(password=password), email)
    )
    conn.commit()
    conn.close()

def getStudentByUsername(username: str):
    """
    Return a user from the database by its username
    """
    conn = sqlite3.connect('students_signup_db.db')
    c = conn.cursor()

    # Check if the username exists in the database
    c.execute(
        "SELECT * FROM students_signup_db WHERE username = ?", (username,))

    student = c.fetchone()
    return student


def getStudentByEmail(email: str):
    """
    Return a user from the database by its email
    """
    conn = sqlite3.connect('students_signup_db.db')
    c = conn.cursor()

    # Check if the email exists in the database
    c.execute(
        "SELECT * FROM students_signup_db WHERE email = ?", (email,))

    student = c.fetchone()
    return student

def getTeacherByUsername(username: str):
    """
    Return a teacher from the teacher database by its username
    """
    conn = sqlite3.connect('teachers_signup_db.db')
    c = conn.cursor()

    # Check if the username exists in the database
    c.execute(
        "SELECT * FROM teachers_signup_db WHERE username = ?", (username,))

    teach = c.fetchone()
    return teach


def getTeacherByEmail(email: str):
    """
    Return a teacher from the teacher database by its email
    """
    conn = sqlite3.connect('teachers_signup_db.db')
    c = conn.cursor()

    # Check if the email exists in the database
    c.execute(
        "SELECT * FROM teachers_signup_db WHERE email = ?", (email,))

    teach = c.fetchone()
    return teach


###### for it staff ##########################
def getItStaffByUsername(username: str):
    """
    Return a it staff from the it staff database by its username
    """
    conn = sqlite3.connect('it_staff_signup_db.db')
    c = conn.cursor()

    # Check if the username exists in the database
    c.execute(
        "SELECT * FROM it_staff_signup_db WHERE username = ?", (username,))

    itStaff = c.fetchone()
    return itStaff

def getItStaffByEmail(email: str):
    """
    Return a it staff from the it staff database by its email
    """
    conn = sqlite3.connect('it_staff_signup_db.db')
    c = conn.cursor()

    # Check if the email exists in the database
    c.execute("SELECT * FROM it_staff_signup_db WHERE email = ?", (email,))

    itStaff = c.fetchone()
    return itStaff
###### for it staff ##########################



def teacherExistsByUsername(username: str):
    """
    Return true if a teacher exists in teacher database with this username, false otherwise.
    """
    teacher = getTeacherByUsername(username)

    return not (teacher is None)


def teacherExistsByEmail(email: str):
    """
    Return true if a teacher exists in teacher database with this email, false otherwise.
    """
    teacher = getTeacherByEmail(email)

    return not (teacher is None)


def studentExistsByUsername(username: str):
    """
    Return true if a student exists in database with this username, false otherwise.
    """
    student = getStudentByUsername(username)

    return not (student is None)


def studentExistsByEmail(email: str):
    """
    Return true if a student exists in database with this email, false otherwise.
    """
    student = getStudentByEmail(email)

    return not (student is None)

def itStaffExistsByUsername(username: str):
    """
    Return true if a it staff exists in database with this username, false otherwise.
    """
    it_staff = getItStaffByUsername(username)

    return not (it_staff is None)


def itStaffExistsByEmail(email: str):
    """
    Return true if a it staff exists in database with this email, false otherwise.
    """
    it_staff = getItStaffByEmail(email)

    return not (it_staff is None)


def encrypt_password(password: str):
    """
    Takes a string, applies salting and hashing
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def check_password(user, password: str):
    """
    Given a user and a raw password, checks if password is correct
    """

    hashed_password = user[2]
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def check_username(user, username: str):
    username_str = user[1]
    return username_str == username


def check_email(user, email: str):
    email_str = user[3]
    return email_str == email


def change_student_password(email: str, password: str):
    conn = sqlite3.connect('students_signup_db.db')
    c = conn.cursor()

    # Update the password for the student with the given email
    c.execute("UPDATE students_signup_db SET password = ? WHERE email = ?",
              (encrypt_password(password), email))
    conn.commit()
    conn.close()


def change_teacher_password(email: str, password: str):
    conn = sqlite3.connect('teachers_signup_db.db')
    c = conn.cursor()

    # Update the password for the student with the given email
    c.execute("UPDATE teachers_signup_db SET password = ? WHERE email = ?",
              (encrypt_password(password), email))
    conn.commit()
    conn.close()


def change_student_password(email: str, password: str):
    conn = sqlite3.connect('it_staff_signup_db.db')
    c = conn.cursor()

    # Update the password for the student with the given email
    c.execute("UPDATE it_staff_signup_db SET password = ? WHERE email = ?",
              (encrypt_password(password), email))
    conn.commit()
    conn.close()


