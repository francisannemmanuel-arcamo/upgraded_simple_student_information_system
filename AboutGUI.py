from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class AboutGUI:
    def __init__(self, frame):
        self.about_cont_frame = frame

        about = "This project is a simple student information system that manages the student data and course\n" \
                "data using SQLite. This simple SIS application has different features, such as the DASHBOARD\n " \
                "where it shows the list of students with their corresponding details \n" \
                "\n   \u2713  student id (must be unique), " \
                "\n   \u2713  name, " \
                "\n   \u2713  year, " \
                "\n   \u2713  course id (must be in the database), and " \
                "\n   \u2713  gender \n" \
                "\n and the list of the courses with their corresponding details \n" \
                "\n   \u2713  course id (must be unique), and" \
                "\n   \u2713  course \n" \
                "\nFor both students and courses, the user has the freedom to ADD, EDIT, and DELETE an entry \n" \
                "(or entries). A SEARCH feature is also present to guide the  user in determining if the certain \n" \
                "entry (student id or course id) is in the database." \

        self.about = Text(self.about_cont_frame, bg="white", fg="#A51d23", highlightcolor="black",
                          highlightthickness=0, font=("Blinker", 15), relief=FLAT)
        self.about.insert(INSERT, about)
        self.about.config(state=DISABLED)
        self.about.place(x=40, y=30, width=800, height=470)

        self.author = Label(self.about_cont_frame, fg="#A51d23", bg="white", font=("Blinker", 14, "bold"),
                            text="\u00A9 FRANCIS ANN EMMANUEL ARCAMO", anchor='w')
        self.author.place(x=40, y=500, height=30, width=300)
