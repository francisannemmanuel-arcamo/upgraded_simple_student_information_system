from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import SISdatabase
import displaytable


class EditStudent:
    def __init__(self, frame, table):
        self.edit_student_frame = frame
        self.student_table = table

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.rows = []

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

        update_info_button = Button(self.edit_student_frame, command=self.update_student, text="UPDATE",
                                    bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                    font=("Bebas Neue", 15))
        update_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.edit_student_frame, command=self.clear_data, text="CLEAR",
                                   bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                   font=("Bebas Neue", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)
        self.student_table.bind("<ButtonRelease-1>", self.select_student)

    def update_student(self):
        if not self.rows:
            messagebox.showerror("Error", "Choose a student from the table first")
            return
        elif not SISdatabase.info_checker(self.id_no.get(), self.name.get().upper(), self.year.get(),
                                          self.course.get().upper(), self.gender.get().upper()):
            return
        else:
            if messagebox.askyesno("Update Course", "Do you wish to update the student information?"):
                if SISdatabase.update_student_rec(self.rows[0], self.id_no.get(), self.name.get().upper(),
                                                  self.year.get(), self.course.get().upper(),
                                                  self.gender.get()):
                    messagebox.showinfo("Success", "Information on student has been updated!")
                    self.clear_data()
                    self.rows = []
                    displaytable.display_student_table(self.student_table)

    def clear_data(self):
        self.edit_id_entry.delete(0, END)
        self.edit_name_entry.delete(0, END)
        self.edit_year_combo.delete(0, END)
        self.edit_course_entry.delete(0, END)
        self.edit_gender_combo.delete(0, END)

    def select_student(self, ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        self.rows = contents['values']
        self.clear_data()
        if not self.rows:
            return
        else:
            self.edit_name_entry.insert(0, self.rows[1])
            self.edit_id_entry.insert(0, self.rows[0])
            self.edit_year_combo.insert(0, self.rows[3])
            self.edit_course_entry.insert(0, self.rows[2])
            self.edit_gender_combo.insert(0, self.rows[4])
