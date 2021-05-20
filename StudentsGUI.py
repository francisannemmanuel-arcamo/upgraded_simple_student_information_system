from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class StudentGUI:
    def __init__(self, frame):
        self.student_cont_frame = frame

        self.stud_count = Label(self.student_cont_frame, text="No. of Students", font=("Blinker", 15))
        self.stud_count.place(x=595, y=10, width=250, height=40)

        self.add_button_img = PhotoImage(file=r"addstudent.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"editstudent.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"deletestudent.png").subsample(1, 1)
        self.srch_btn_img = PhotoImage(file=r"searchbuttonimg.png").subsample(1, 1)
        self.refresh_btn_img = PhotoImage(file=r"refreshbutton.png").subsample(1, 1)

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

        self.search_student_bar_entry = Entry(self.student_cont_frame, font=("Oswald", 14), highlightthickness=2,
                                              highlightbackground="#A51d23")
        self.search_student_bar_entry.place(x=595, y=85, width=200, height=35)

        search_student_btn = Button(self.student_cont_frame, bg="#A51d23", image=self.srch_btn_img,
                                    command=self.search_student)
        search_student_btn.photo = self.srch_btn_img
        search_student_btn.place(x=795, y=85, width=35, height=35)

        ref_search_btn = Button(self.student_cont_frame, bg="#A51d23", image=self.refresh_btn_img,
                                command=self.refresh_search)
        ref_search_btn.photo = self.refresh_btn_img
        ref_search_btn.place(x=835, y=85, width=35, height=35)

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
                                   text="  FEATURES", font=("Blinker", 15, "bold"))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.addstudentframe = Frame(self.student_cont_frame, bg="white", highlightbackground="#A51d23",
                                     highlightthickness=2)

    def add_student(self):
        self.heading_label.config(text="  ADD STUDENT")
        print("Student Added")

    def edit_student(self):
        self.heading_label.config(text="  EDIT STUDENT")
        print("Student Edited")

    def delete_student(self):
        print("")

    def search_student(self):
        if len(self.search_student_bar_entry.get()) == 0:
            messagebox.showerror("Error", "Please enter student id")
        else:
            print(self.search_student_bar_entry.get())

    def refresh_search(self):
        self.search_student_bar_entry.delete(0, END)
