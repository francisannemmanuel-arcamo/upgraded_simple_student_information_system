from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class DashboardGUI:
    def __init__(self, frame):
        self.dashboard_cont_frame = frame
        self.dashboard_cont_frame.place(x=20, y=100, width=900, height=570)

        self.student_count = Label(self.dashboard_cont_frame, text="None", font=("Merriweather", 24))
        self.student_count.place(x=20, y=20, width=250, height=120)

        self.course_count = Label(self.dashboard_cont_frame, text="None", font=("Merriweather", 24))
        self.course_count.place(x=290, y=20, width=250, height=120)

        stud_list_label = Label(self.dashboard_cont_frame, bg="#A51d23", fg="white",
                                text="  List of Students", font=("Bebas Neue", 15), anchor="w")
        self.stud_list_frame = Frame(self.dashboard_cont_frame, bg="white", highlightbackground="#A51d23",
                                     highlightthickness=2)
        stud_list_label.place(x=10, y=190, width=550, height=30)
        self.stud_list_frame.place(x=10, y=220, width=550, height=320)

        course_list_label = Label(self.dashboard_cont_frame, bg="#A51d23", fg="white",
                                  text="  List of Courses", font=("Bebas Neue", 15), anchor="w")
        self.course_list_frame = Frame(self.dashboard_cont_frame, bg="white", highlightbackground="#A51d23",
                                       highlightthickness=2)
        course_list_label.place(x=580, y=190, width=300, height=30)
        self.course_list_frame.place(x=580, y=220, width=300, height=320)

        scroll_x_stud_list = Scrollbar(self.stud_list_frame, orient=HORIZONTAL)
        scroll_y_stud_list = Scrollbar(self.stud_list_frame, orient=VERTICAL)

        scroll_x_course_list = Scrollbar(self.course_list_frame, orient=HORIZONTAL)
        scroll_y_course_list = Scrollbar(self.course_list_frame, orient=VERTICAL)
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

        self.course_table = ttk.Treeview(self.course_list_frame, xscrollcommand=scroll_x_course_list.set,
                                         yscrollcommand=scroll_y_course_list.set, columns=("course_code",
                                                                                           "course"))
        scroll_x_course_list.pack(side=BOTTOM, fill=X)
        scroll_y_course_list.pack(side=RIGHT, fill=Y)
        scroll_x_course_list.config(command=self.course_table.xview)
        scroll_y_course_list.config(command=self.course_table.yview)
        self.course_table.heading("course_code", text="Course Code")
        self.course_table.heading("course", text="Course")
        self.course_table['show'] = 'headings'
        self.course_table.column("course_code", width=50)
        self.course_table.column("course", width=100)

        self.course_table.pack(fill=BOTH, expand=1)