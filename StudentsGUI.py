from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from AddStudent import AddStudent
from EditStudent import EditStudent
import displaytable as disp
import SISdatabase


class StudentGUI:
    def __init__(self, frame):
        self.student_cont_frame = frame

        self.search_stud = StringVar()

        self.add_button_img = PhotoImage(file=r"images\addstudent.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"images\editstudent.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"images\deletestudent.png").subsample(1, 1)
        self.srch_img = PhotoImage(file=r"images\searchbuttonimg.png").subsample(1, 1)

        add_student_btn = Button(self.student_cont_frame, bg="#A51d23", image=self.add_button_img,
                                 command=self.add_student)
        add_student_btn.photo = self.add_button_img
        add_student_btn.place(x=10, y=50, width=70, height=70)

        edit_student_btn = Button(self.student_cont_frame, bg="#A51d23", image=self.edit_button_img,
                                  command=self.edit_student)
        edit_student_btn.photo = self.edit_button_img
        edit_student_btn.place(x=85, y=50, width=70, height=70)

        delete_student_btn = Button(self.student_cont_frame, bg="#A51d23", image=self.delete_button_img,
                                    command=self.delete_student)
        delete_student_btn.photo = self.delete_button_img
        delete_student_btn.place(x=160, y=50, width=70, height=70)

        search_code_label = Label(self.student_cont_frame, font=("Blinker", 11, "bold"), bg="#A51d23", fg="white",
                                  text="Student ID:")
        search_code_label.place(x=515, y=85, width=80, height=35)
        self.search_student_bar_entry = Entry(self.student_cont_frame, textvariable=self.search_stud,
                                              font=("Blinker", 15, "bold"), highlightthickness=2,
                                              highlightbackground="#A51d23")
        self.search_student_bar_entry.place(x=595, y=85, width=250, height=35)
        self.search_stud.trace("w", lambda name, index, mode, sv=self.search_stud: self.search_student())

        search_student_lbl = Label(self.student_cont_frame, image=self.srch_img)
        search_student_lbl.photo = self.srch_img
        search_student_lbl.place(x=845, y=85, width=35, height=35)

        self.stud_list_label = Label(self.student_cont_frame, bg="#A51d23", fg="white", anchor='w',
                                     text="   LIST OF STUDENTS", font=("Blinker", 15, "bold"))

        self.stud_list_frame = Frame(self.student_cont_frame, bg="white", highlightbackground="#A51d23",
                                     highlightthickness=2)

        self.stud_list_label.place_configure(x=370, y=140, width=510, height=30)
        self.stud_list_frame.place_configure(x=370, y=170, width=510, height=370)

        scroll_x_stud_list = Scrollbar(self.stud_list_frame, orient=HORIZONTAL)
        scroll_y_stud_list = Scrollbar(self.stud_list_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.stud_list_frame, xscrollcommand=scroll_x_stud_list.set,
                                          yscrollcommand=scroll_y_stud_list.set, columns=("id_no", "name",
                                                                                          "course_code", "year",
                                                                                          "gender"))
        scroll_x_stud_list.pack(side=BOTTOM, fill=X)
        scroll_y_stud_list.pack(side=RIGHT, fill=Y)
        scroll_x_stud_list.config(command=self.student_table.xview)
        scroll_y_stud_list.config(command=self.student_table.yview)
        self.student_table.heading("id_no", text="ID Number")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course_code", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table['show'] = 'headings'
        self.student_table.column("id_no", width=70)
        self.student_table.column("name", width=170)
        self.student_table.column("course_code", width=70)
        self.student_table.column("year", width=60)
        self.student_table.column("gender", width=60)

        self.student_table.pack(fill=BOTH, expand=1)

        self.heading_label = Label(self.student_cont_frame, bg="#A51d23", fg="white", anchor='w',
                                   font=("Blinker", 15, "bold"))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.features_frame = Frame(self.student_cont_frame, bg="white", highlightbackground="#A51d23",
                                    highlightthickness=2)
        self.add_student_frame = Frame(self.student_cont_frame, bg="white", highlightbackground="#A51d23",
                                       highlightthickness=2)
        self.edit_student_frame = Frame(self.student_cont_frame, bg="white", highlightbackground="#A51d23",
                                        highlightthickness=2)

        self.default_layout()
        disp.display_student_table(self.student_table)

    def default_layout(self):
        self.heading_label.config(text="  FEATURES")
        self.hide_widgets()
        self.features_frame.place(x=10, y=170, width=340, height=370)

        add_button_nav = Button(self.features_frame, command=self.add_student,
                                activebackground="#A51d23", fg="white", activeforeground="#FA9412", bg="#A51d23",
                                text=" ADD STUDENT", image=self.add_button_img, compound="left", anchor="w",
                                font=("Blinker", 20, "bold")
                                )
        add_button_nav.place(x=20, y=40, width=290, height=70)
        edit_button_nav = Button(self.features_frame, font=("Blinker", 20, "bold"), command=self.edit_student,
                                 activebackground="#A51d23", fg="white", activeforeground="#FA9412", bg="#A51d23",
                                 text=" EDIT STUDENT", image=self.edit_button_img, compound="left", anchor="w",
                                 )
        edit_button_nav.place(x=20, y=120, width=290, height=70)
        delete_button_nav = Button(self.features_frame, command=self.delete_student,
                                   activebackground="#A51d23", fg="white", activeforeground="#FA9412", bg="#A51d23",
                                   text=" DELETE STUDENT", image=self.delete_button_img, compound="left", anchor="w",
                                   font=("Blinker", 20, "bold")
                                   )
        delete_button_nav.place(x=20, y=200, width=290, height=70)

    def hide_widgets(self):
        self.features_frame.place_forget()
        self.add_student_frame.place_forget()
        self.edit_student_frame.place_forget()

    def add_student(self):
        self.heading_label.config(text="  ADD STUDENT")
        self.hide_widgets()
        self.add_student_frame.place(x=10, y=170, width=340, height=370)
        AddStudent(self.add_student_frame, self.student_table, self.search_student_bar_entry.get())

    def edit_student(self):
        self.heading_label.config(text="  EDIT STUDENT")
        self.hide_widgets()
        self.edit_student_frame.place(x=10, y=170, width=340, height=370)
        EditStudent(self.edit_student_frame, self.student_table)

    def delete_student(self):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        rows = contents['values']
        if rows == "":
            messagebox.showerror("Error", "Select a student first!")
        else:
            if messagebox.askyesno("Delete Student", "Do you wish to delete this student?"):
                SISdatabase.delete_student_rec(rows[0])
                messagebox.showinfo("Success", "Student deleted in database!")
                disp.display_student_table(self.student_table)
                self.default_layout()
                return
            else:
                return

    def search_student(self):
        result = SISdatabase.search_student_rec(self.search_stud.get().upper())
        self.student_table.delete(*self.student_table.get_children())
        if not result:
            return
        else:
            for x in result:
                self.student_table.insert('', 0, values=(x[0], x[1], x[3], x[2], x[4]))
