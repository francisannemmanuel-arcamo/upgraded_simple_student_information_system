from tkinter import messagebox
import sqlite3


def student_data():
    # student data
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS studentdata (stud_id VARCHAR(9) NOT NULL PRIMARY KEY, "
                "stud_name VARCHAR(100) NOT NULL, stud_year VARCHAR(8), stud_course_id VARCHAR(10) NOT NULL,"
                "stud_gender VARCHAR(6) NOT NULL,"
                "FOREIGN KEY(stud_course_id) REFERENCES coursedata(course_id))")
    con.commit()
    con.close()


def course_data():
    # course data
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS coursedata (course_id VARCHAR(10) NOT NULL PRIMARY KEY, course_name " 
                "VARCHAR(100) NOT NULL)")
    con.commit()
    con.close()


def add_course_rec(course_id, course_name):
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO coursedata VALUES (?, ?)", (course_id, course_name))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Course ID already in database.")
        return False


def view_student_rec():
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM studentdata")
    students = cur.fetchall()
    con.close()
    return students


def view_course_rec():
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM coursedata")
    courses = cur.fetchall()
    con.close()
    return courses


def delete_course_rec(course_id):
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    cur.execute("DELETE FROM coursedata WHERE course_id=?", (course_id,))
    con.commit()
    con.close()


def update_course_rec(key, course_id, course_name):
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    try:
        if key != course_id:
            cur.execute("UPDATE coursedata SET course_id=?, course_name=?  WHERE course_id=?",
                        (course_id, course_name, key))
        else:
            cur.execute("UPDATE coursedata SET course_name=?  WHERE course_id=?", (course_name, course_id))
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Course ID already in database.")
        return False


def search_course_rec(course_id):
    con = sqlite3.connect("csc.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM coursedata WHERE course_id=?", (course_id,))
    result = cur.fetchall()
    con.close()
    return result
