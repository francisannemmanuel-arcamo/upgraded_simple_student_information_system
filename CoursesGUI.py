from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class CoursesGUI:
    def __init__(self, frame):
        self.courses_cont_frame = frame

        self.course_count = Label(self.courses_cont_frame, text="None", font=("Blinker", 15))
        self.course_count.place(x=595, y=10, width=250, height=40)

        self.add_button_img = PhotoImage(file=r"addcourse.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"editcourse.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"deletecourse.png").subsample(1, 1)
        self.srch_btn_img = PhotoImage(file=r"searchbuttonimg.png").subsample(1, 1)
        self.refresh_btn_img = PhotoImage(file=r"refreshbutton.png").subsample(1, 1)

        add_course_btn = Button(self.courses_cont_frame, image=self.add_button_img,
                                bg="#A51d23", command=self.add_course)
        add_course_btn.photo = self.add_button_img
        add_course_btn.place(x=10, y=50, width=70, height=70)

        edit_course_btn = Button(self.courses_cont_frame, image=self.edit_button_img, bg="#A51d23",
                                 command=self.edit_course)
        edit_course_btn.photo = self.edit_button_img
        edit_course_btn.place(x=85, y=50, width=70, height=70)

        delete_course_btn = Button(self.courses_cont_frame, image=self.delete_button_img, bg="#A51d23",
                                   command=self.delete_course)
        delete_course_btn.photo = self.delete_button_img
        delete_course_btn.place(x=160, y=50, width=70, height=70)

        self.search_course_bar_entry = Entry(self.courses_cont_frame, font=("Oswald", 14), highlightthickness=2,
                                             highlightbackground="#A51d23")
        self.search_course_bar_entry.place(x=595, y=85, width=200, height=35)
        search_course_btn = Button(self.courses_cont_frame, bg="#A51d23", fg="white", font=("Bebas Neue", 20),
                                   command=self.search_course,
                                   image=self.srch_btn_img)
        search_course_btn.photo = self.srch_btn_img
        search_course_btn.place(x=795, y=85, width=35, height=35)

        ref_search_btn = Button(self.courses_cont_frame, bg="#A51d23", image=self.refresh_btn_img,
                                command=self.refresh_search)
        ref_search_btn.photo = self.refresh_btn_img
        ref_search_btn.place(x=835, y=85, width=35, height=35)

        courselist_label = Label(self.courses_cont_frame, bg="#A51d23", fg="white",
                                 text="   LIST OF COURSES",
                                 font=("Blinker", 15, "bold"), anchor='w')
        courselist_label.place(x=370, y=140, width=510, height=30)

        self.course_list_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#A51d23",
                                       highlightthickness=2)
        self.course_list_frame.place(x=370, y=170, width=510, height=370)

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
        self.course_table.column("course_code", width=40)
        self.course_table.column("course", width=150)

        self.course_table.pack(fill=BOTH, expand=1)

        self.heading_label = Label(self.courses_cont_frame, bg="#A51d23", fg="white", anchor='w',
                                   text="  FEATURES", font=("Blinker", 15, "bold"))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.add_course_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#A51d23",
                                      highlightthickness=2)

    def add_course(self):
        self.heading_label.config(text="  ADD COURSE")
        print("Course added")

    def edit_course(self):
        self.heading_label.config(text="  EDIT COURSE")
        print("Course edited")

    def delete_course(self):
        print("Course deleted")

    def search_course(self):
        if len(self.search_course_bar_entry.get()) == 0:
            messagebox.showerror("Error", "Please enter course id")
        else:
            print(self.search_course_bar_entry.get())

    def refresh_search(self):
        self.search_student_bar_entry.delete(0, END)
