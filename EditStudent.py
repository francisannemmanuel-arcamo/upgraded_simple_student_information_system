from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class EditStudent:
    def __init__(self, frame):
        self.edit_student_frame = frame

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        # Edit
        self.edit_name_entry = Entry(self.edit_student_frame, textvariable=self.name, highlightthickness=2,
                                     highlightbackground="#A51d23", font=("Bebas Neue", 18))
        self.edit_id_entry = Entry(self.edit_student_frame, textvariable=self.id_no, highlightthickness=2,
                                   highlightbackground="#A51d23", font=("Bebas Neue", 18))
        self.edit_year_combo = ttk.Combobox(self.edit_student_frame, textvariable=self.year, font=("Bebas Neue", 18),
                                            values=[
                                                "1st Year",
                                                "2nd Year",
                                                "3rd Year",
                                                "4th Year",
                                                "5th Year"])
        self.edit_course_entry = Entry(self.edit_student_frame, textvariable=self.course, font=("Bebas Neue", 18),
                                       highlightthickness=2, highlightbackground="#A51d23")
        self.edit_gender_combo = ttk.Combobox(self.edit_student_frame, textvariable=self.gender,
                                              font=("Bebas Neue", 18),
                                              values=["Male", "Female", "Other"])

        # attributes on edit student feature
        name_label = Label(self.edit_student_frame, text="NAME", font=("Bebas Neue", 17), bg="#A51d23",
                           fg="white")
        name_label.place(x=10, y=20, width=80, height=35)
        self.edit_name_entry.place(x=90, y=20, width=235, height=35)
        name_format = Label(self.edit_student_frame, text="Last Name, First Name, M.I", font=("Oswald", 8),
                            fg="#A51d23", bg="white")
        name_format.place(x=95, y=56, height=20)
        id_no_label = Label(self.edit_student_frame, text="ID NO.", font=("Bebas Neue", 17), bg="#A51d23",
                            fg="white")
        id_no_label.place(x=10, y=80, width=80, height=35)
        self.edit_id_entry.place(x=90, y=80, width=235, height=35)
        year_label = Label(self.edit_student_frame, text="YEAR", font=("Bebas Neue", 17), bg="#A51d23",
                           fg="white")
        year_label.place(x=10, y=125, width=80, height=35)
        self.edit_year_combo.place(x=90, y=125, width=235, height=35)
        course_label = Label(self.edit_student_frame, text="COURSE ID", font=("Bebas Neue", 17), bg="#A51d23",
                             fg="white")
        course_label.place(x=10, y=170, width=80, height=35)
        self.edit_course_entry.place(x=90, y=170, width=235, height=35)
        gender_label = Label(self.edit_student_frame, text="GENDER", font=("Bebas Neue", 17), bg="#A51d23",
                             fg="white")
        gender_label.place(x=10, y=215, width=80, height=35)
        self.edit_gender_combo.place(x=90, y=215, width=235, height=35)

        update_info_button = Button(self.edit_student_frame, command='', text="UPDATE",
                                    bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                    font=("Bebas Neue", 15))
        update_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.edit_student_frame, command=self.clear_data, text="CLEAR",
                                   bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                   font=("Bebas Neue", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.edit_id_entry.delete(0, END)
        self.edit_name_entry.delete(0, END)
        self.edit_year_combo.delete(0, END)
        self.edit_course_entry.delete(0, END)
        self.edit_gender_combo.delete(0, END)
