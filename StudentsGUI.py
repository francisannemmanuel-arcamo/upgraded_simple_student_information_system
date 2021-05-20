from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class StudentGUI:
    def __init__(self, frame):
        self.student_cont_frame = frame
        self.student_cont_frame.place(x=20, y=100, width=900, height=570)

        self.stud_count = Label(self.student_cont_frame, text="None", font=("Merriweather", 15))
        self.stud_count.place(x=20, y=10, width=250, height=40)

        add_student_btn = Button(self.student_cont_frame, bg="#A51d23", text="Add")
        add_student_btn.place(x=20, y=80, width=40, height=40)

        edit_student_btn = Button(self.student_cont_frame, bg="#A51d23", text="Edit")
        edit_student_btn.place(x=65, y=80, width=40, height=40)

        delete_student_btn = Button(self.student_cont_frame, bg="#A51d23", text="Delete")
        delete_student_btn.place(x=110, y=80, width=40, height=40)

        self.search_student_bar_entry = Entry(self.student_cont_frame, font=("Oswald", 14), highlightthickness=2,
                                              highlightbackground="#A51d23")
        self.search_student_bar_entry.place(x=585, y=80, width=200, height=40)

        search_student_btn = Button(self.student_cont_frame, bg="#A51d23", text="Search")
        search_student_btn.place(x=785, y=80, width=40, height=40)
        ref_search_btn = Button(self.student_cont_frame, bg="#A51d23", text="Refresh")
        ref_search_btn.place(x=830, y=80, width=40, height=40)

        stud_list_label = Label(self.student_cont_frame, bg="#A51d23", fg="white",
                                text="   List of Students", font=("Bebas Neue", 18), anchor='w')
        stud_list_label.place(x=20, y=130, width=850, height=40)

        self.stud_list_frame = Frame(self.student_cont_frame, bg="white", highlightbackground="#A51d23",
                                     highlightthickness=2)
        self.stud_list_frame.place(x=20, y=170, width=850, height=370)

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
        self.student_table.heading("course_code", text="Course Code")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("gender", text="Gender")
        self.student_table['show'] = 'headings'
        self.student_table.column("id_no", width=70)
        self.student_table.column("name", width=190)
        self.student_table.column("course_code", width=100)
        self.student_table.column("year", width=70)
        self.student_table.column("gender", width=70)

        self.student_table.pack(fill=BOTH, expand=1)
