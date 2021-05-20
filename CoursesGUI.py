from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class CoursesGUI:
    def __init__(self, frame):
        self.courses_cont_frame = frame

        self.courses_cont_frame.place(x=20, y=100, width=900, height=570)

        self.course_count = Label(self.courses_cont_frame, text="None", font=("Merriweather", 15))
        self.course_count.place(x=20, y=10, width=250, height=40)

        add_course_btn = Button(self.courses_cont_frame, bg="#A51d23", text="Add")
        add_course_btn.place(x=20, y=80, width=40, height=40)

        edit_course_btn = Button(self.courses_cont_frame, bg="#A51d23", text="Edit")
        edit_course_btn.place(x=65, y=80, width=40, height=40)

        delete_course_btn = Button(self.courses_cont_frame, bg="#A51d23", text="Delete")
        delete_course_btn.place(x=110, y=80, width=40, height=40)

        self.search_course_bar_entry = Entry(self.courses_cont_frame, font=("Oswald", 14), highlightthickness=2,
                                             highlightbackground="#A51d23")
        self.search_course_bar_entry.place(x=585, y=80, width=200, height=40)

        search_course_btn = Button(self.courses_cont_frame, bg="#A51d23", text="Search")
        search_course_btn.place(x=785, y=80, width=40, height=40)
        ref_search_btn = Button(self.courses_cont_frame, bg="#A51d23", text="Refresh")
        ref_search_btn.place(x=830, y=80, width=40, height=40)

        courselist_label = Label(self.courses_cont_frame, bg="#A51d23", fg="white",
                                 text="   List of Courses",
                                 font=("Bebas Neue", 18), anchor='w')
        courselist_label.place(x=20, y=130, width=850, height=40)

        self.course_list_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#A51d23",
                                       highlightthickness=2)
        self.course_list_frame.place(x=20, y=170, width=850, height=370)

        scroll_x_course_list = Scrollbar(self.course_list_frame, orient=HORIZONTAL)
        scroll_y_course_list = Scrollbar(self.course_list_frame, orient=VERTICAL)
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
        self.course_table.column("course", width=150)

        self.course_table.pack(fill=BOTH, expand=1)
