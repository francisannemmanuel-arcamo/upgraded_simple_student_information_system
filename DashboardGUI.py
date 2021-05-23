from tkinter import *
from tkinter import ttk

import displaytable as disp
import SISdatabase


class DashboardGUI:
    def __init__(self, frame):
        self.dashboard_cont_frame = frame

        self.student_dshbrd_img = PhotoImage(file=r"dashboardstud.png")
        student_count_dash = Label(self.dashboard_cont_frame, image=self.student_dshbrd_img)
        student_count_dash.photo = self.student_dshbrd_img
        student_count_dash.place(x=20, y=20, width=250, height=120)
        self.student_count = Label(self.dashboard_cont_frame, text="1000", font=("Blinker", 40, "bold"),
                                   fg="#A51d23", bg="#FA9412")
        self.student_count.place(x=20, y=20, width=140, height=77)

        self.course_dshbrd_img = PhotoImage(file=r"dashboardcourse.png")
        course_count_dash = Label(self.dashboard_cont_frame, image=self.course_dshbrd_img)
        course_count_dash.photo = self.course_dshbrd_img
        course_count_dash.place(x=290, y=20, width=250, height=120)
        self.course_count = Label(self.dashboard_cont_frame, text="0", font=("Blinker", 40, "bold"),
                                  bg="#A51d23", fg="#FA9412")
        self.course_count.place(x=290, y=20, width=140, height=77)

        self.bg_frame = Frame(self.dashboard_cont_frame, bg="white")

        self.stud_list_label = Label(self.dashboard_cont_frame, bg="#A51d23", fg="white",
                                     text="  LIST OF STUDENTS", font=("Blinker", 15, "bold"), anchor="w")
        self.stud_list_frame = Frame(self.dashboard_cont_frame, bg="white", highlightbackground="#A51d23",
                                     highlightthickness=2)

        self.course_label = Label(self.dashboard_cont_frame, bg="#A51d23", fg="white",
                                  text="  LIST OF COURSES", font=("Blinker", 15, "bold"), anchor="w")
        self.course_list_frame = Frame(self.dashboard_cont_frame, bg="white", highlightbackground="#A51d23",
                                       highlightthickness=2)

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
        self.course_table.column("course", width=200)

        self.course_table.pack(fill=BOTH, expand=1)

        self.max_student_img = PhotoImage(file=r"max.png").subsample(5, 5)
        self.max_course_img = PhotoImage(file=r"max.png").subsample(5, 5)
        self.max_student_button = Button(self.dashboard_cont_frame, command=self.max_student_table, relief=FLAT,
                                         bg="#A51d23", activebackground="#A51d23", image=self.max_student_img)
        self.max_course_button = Button(self.dashboard_cont_frame, command=self.max_course_table, relief=FLAT,
                                        bg="#A51d23", activebackground="#A51d23", image=self.max_course_img)

        self.min_image = PhotoImage(file=r"min.png").subsample(5, 5)
        self.min_button = Button(self.dashboard_cont_frame, command=self.default_layout, relief=FLAT,
                                 fg="white", bg="#A51d23", activeforeground="white", activebackground="#A51d23",
                                 image=self.min_image)
        self.min_button.photo = self.min_image

        self.default_layout()
        self.count_data()
        disp.display_student_table(self.student_table)
        disp.display_course_table(self.course_table)

    def default_layout(self):
        self.min_button.place_forget()
        self.max_student_button.place(x=530, y=190, height=30, width=30)
        self.max_course_button.place(x=840, y=190, height=30, width=30)
        self.bg_frame.place(x=10, y=190, height=350, width=880)
        self.stud_list_label.place_configure(x=20, y=190, width=550, height=30)
        self.stud_list_frame.place_configure(x=20, y=220, width=550, height=320)
        self.course_label.place_configure(x=580, y=190, width=300, height=30)
        self.course_list_frame.place_configure(x=580, y=220, width=300, height=320)

    def count_data(self):
        self.student_count.config(text=len(SISdatabase.view_student_rec()))
        self.course_count.config(text=len(SISdatabase.view_course_rec()))

    def max_student_table(self):
        self.hide_widgets()
        self.stud_list_label.place_configure(x=20, y=190, width=860, height=30)
        self.stud_list_frame.place_configure(x=20, y=220, width=860, height=320)
        self.min_button.place(x=840, y=190, height=30, width=30)

    def max_course_table(self):
        self.hide_widgets()
        self.course_label.place_configure(x=20, y=190, width=860, height=30)
        self.course_list_frame.place_configure(x=20, y=220, width=860, height=320)
        self.min_button.place(x=840, y=190, height=30, width=30)

    def hide_widgets(self):
        self.stud_list_label.place_forget()
        self.stud_list_frame.place_forget()
        self.max_student_button.place_forget()
        self.max_course_button.place_forget()
        self.course_list_frame.place_forget()
        self.course_label.place_forget()
