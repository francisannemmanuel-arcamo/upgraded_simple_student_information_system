from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import SISdatabase

from AddCourse import AddCourse
from EditCourse import EditCourse
import displaytable as disp


class CoursesGUI:
    def __init__(self, frame):
        self.courses_cont_frame = frame

        self.search_course_id = StringVar()

        self.add_button_img = PhotoImage(file=r"images\addcourse.png").subsample(1, 1)
        self.edit_button_img = PhotoImage(file=r"images\editcourse.png").subsample(1, 1)
        self.delete_button_img = PhotoImage(file=r"images\deletecourse.png").subsample(1, 1)
        self.srch_img = PhotoImage(file=r"images\searchbuttonimg.png").subsample(1, 1)

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

        search_code_label = Label(self.courses_cont_frame, font=("Blinker", 11, "bold"), bg="#A51d23", fg="white",
                                  text="Course ID:")
        search_code_label.place(x=515, y=85, width=80, height=35)
        self.search_course_bar_entry = Entry(self.courses_cont_frame, textvariable=self.search_course_id,
                                             font=("Blinker", 15, "bold"), highlightthickness=2,
                                             highlightbackground="#A51d23")
        self.search_course_bar_entry.place(x=595, y=85, width=250, height=35)
        self.search_course_id.trace("w", lambda name, index, mode, sv=self.search_course_id: self.search_course())
        search_course_lbl = Label(self.courses_cont_frame, image=self.srch_img)
        search_course_lbl.photo = self.srch_img
        search_course_lbl.place(x=845, y=85, width=35, height=35)

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
        self.course_table.column("course_code", width=120)
        self.course_table.column("course", width=390)

        self.course_table.pack(fill=BOTH, expand=1)

        self.heading_label = Label(self.courses_cont_frame, bg="#A51d23", fg="white", anchor='w',
                                   text="", font=("Blinker", 15, "bold"))
        self.heading_label.place(x=10, y=140, width=340, height=30)

        self.features_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#A51d23",
                                    highlightthickness=2)
        self.add_course_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#A51d23",
                                      highlightthickness=2)
        self.edit_course_frame = Frame(self.courses_cont_frame, bg="white", highlightbackground="#A51d23",
                                       highlightthickness=2)

        self.default_layout()
        disp.display_course_table(self.course_table)

    def default_layout(self):
        self.heading_label.config(text="   FEATURES")
        self.hide_widgets()
        self.features_frame.place(x=10, y=170, width=340, height=370)

        add_button_nav = Button(self.features_frame, command=self.add_course,
                                activebackground="#A51d23", fg="white", activeforeground="#FA9412", bg="#A51d23",
                                text=" ADD COURSE", image=self.add_button_img, compound="left", anchor="w",
                                font=("Blinker", 20, "bold")
                                )
        add_button_nav.place(x=20, y=40, width=290, height=70)
        edit_button_nav = Button(self.features_frame, font=("Blinker", 20, "bold"), command=self.edit_course,
                                 activebackground="#A51d23", fg="white", activeforeground="#FA9412", bg="#A51d23",
                                 text=" EDIT COURSE", image=self.edit_button_img, compound="left", anchor="w",
                                 )
        edit_button_nav.place(x=20, y=120, width=290, height=70)
        delete_button_nav = Button(self.features_frame, command=self.delete_course,
                                   activebackground="#A51d23", fg="white", activeforeground="#FA9412", bg="#A51d23",
                                   text=" DELETE COURSE", image=self.delete_button_img, compound="left", anchor="w",
                                   font=("Blinker", 20, "bold")
                                   )
        delete_button_nav.place(x=20, y=200, width=290, height=70)

    def hide_widgets(self):
        self.features_frame.place_forget()
        self.add_course_frame.place_forget()
        self.edit_course_frame.place_forget()

    def add_course(self):
        self.heading_label.config(text="  ADD COURSE")
        self.hide_widgets()
        self.add_course_frame.place(x=10, y=170, width=340, height=370)
        AddCourse(self.add_course_frame, self.course_table)

    def edit_course(self):
        self.heading_label.config(text="  EDIT COURSE")
        self.hide_widgets()
        self.edit_course_frame.place(x=10, y=170, width=340, height=370)
        EditCourse(self.edit_course_frame, self.course_table)

    def delete_course(self):
        cursor_row = self.course_table.focus()
        contents = self.course_table.item(cursor_row)
        rows = contents['values']
        if rows == "":
            messagebox.showerror("Error", "Select course first")
            return
        else:
            if messagebox.askyesno("Delete Course", "Do you wish to delete this course? Some students might be enrolled"
                                                    " in this course."):
                if SISdatabase.delete_course_rec(rows[0]):
                    disp.display_course_table(self.course_table)
                    messagebox.showinfo("Success", "Course deleted in database")
                    self.default_layout()
                return
            else:
                return

    def search_course(self):
        result = SISdatabase.search_course_rec(self.search_course_id.get().upper())
        self.course_table.delete(*self.course_table.get_children())
        if not result:
            return
        else:
            for x in result:
                self.course_table.insert('', 0, values=(x[0], x[1]))
