from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class AddStudent:
    def __init__(self, frame):
        self.add_student_frame = frame

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.add_name_entry = Entry(self.add_student_frame, textvariable=self.name, highlightthickness=2,
                                    highlightbackground="#A51d23", font=("Bebas Neue", 18))

        self.add_id_entry = Entry(self.add_student_frame, textvariable=self.id_no, highlightthickness=2,
                                  highlightbackground="#A51d23", font=("Bebas Neue", 18))
        self.add_year_combo = ttk.Combobox(self.add_student_frame, textvariable=self.year, font=("Bebas Neue", 18),
                                           values=[
                                               "1st Year",
                                               "2nd Year",
                                               "3rd Year",
                                               "4th Year",
                                               "5th Year"])
        self.add_course_id_entry = Entry(self.add_student_frame, textvariable=self.course, highlightthickness=2,
                                         highlightbackground="#A51d23", font=("Bebas Neue", 18))
        self.add_gender_combo = ttk.Combobox(self.add_student_frame, textvariable=self.gender, font=("Bebas Neue", 18),
                                             values=["Male", "Female", "Other"])

        name_label = Label(self.add_student_frame, text="NAME", font=("Bebas Neue", 17), bg="#A51d23",
                           fg="white")
        name_label.place(x=10, y=20, width=80, height=35)
        self.add_name_entry.place(x=90, y=20, width=235, height=35)
        name_format = Label(self.add_student_frame, text="Last Name, First Name, M.I", font=("Oswald", 8),
                            fg="#A51d23", bg="white")
        name_format.place(x=95, y=56, height=20)
        id_no_label = Label(self.add_student_frame, text="ID NO.", font=("Bebas Neue", 17), bg="#A51d23",
                            fg="white")
        id_no_label.place(x=10, y=80, width=80, height=35)
        self.add_id_entry.place(x=90, y=80, width=235, height=35)
        year_label = Label(self.add_student_frame, text="YEAR", font=("Bebas Neue", 17), bg="#A51d23",
                           fg="white")
        year_label.place(x=10, y=125, width=80, height=35)
        self.add_year_combo.place(x=90, y=125, width=235, height=35)
        course_id_label = Label(self.add_student_frame, text="COURSE ID", font=("Bebas Neue", 17), bg="#A51d23",
                                fg="white")
        course_id_label.place(x=10, y=170, width=80, height=35)
        self.add_course_id_entry.place(x=90, y=170, width=235, height=35)
        gender_label = Label(self.add_student_frame, text="GENDER", font=("Bebas Neue", 17), bg="#A51d23",
                             fg="white")
        gender_label.place(x=10, y=215, width=80, height=35)
        self.add_gender_combo.place(x=90, y=215, width=235, height=35)

        add_info_button = Button(self.add_student_frame, command=self.add_student, text="ADD",
                                 bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                 font=("Bebas Neue", 15))
        add_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.add_student_frame, command=self.clear_data, text="CLEAR",
                                   bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                   font=("Bebas Neue", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.add_id_entry.delete(0, END)
        self.add_name_entry.delete(0, END)
        self.add_course_id_entry.delete(0, END)
        self.add_year_combo.delete(0, END)
        self.add_gender_combo.delete(0, END)

    def add_student(self):
        if messagebox.askyesno("Add Student", "Do you want to add the student in the database"):
            if self.name.get() == "" or self.id_no.get() == "" or self.year == "" or self.course.get() == "" \
                    or self.gender.get() == "":
                messagebox.showerror("Error", "Please fill out all fields")
                return
            elif not self.id_checker():
                messagebox.showerror("Error", "Invalid ID Number")
                return
            else:
                messagebox.showinfo("Success", "Student added to database")
                self.clear_data()
                return

    def id_checker(self):
        id_num = self.id_no.get()
        if len(id_num) != 9 or id_num[4] != '-' or not id_num.replace("-", "").isdigit():
            return False
        else:
            return True
