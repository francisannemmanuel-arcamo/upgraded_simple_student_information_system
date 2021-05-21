from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class AddCourse:
    def __init__(self, frame):
        self.add_course_frame = frame

        self.course_id = StringVar()

        self.add_course_id_entry = Entry(self.add_course_frame, textvariable=self.course_id, highlightthickness=2,
                                         highlightbackground="#A51d23", font=("Bebas Neue", 18))
        self.add_course_text = Text(self.add_course_frame, highlightthickness=2, highlightbackground="#A51d23",
                                    font=("Bebas Neue", 18))

        course_id_label = Label(self.add_course_frame, text="COURSE ID", font=("Bebas Neue", 17),
                                bg="#A51d23", fg="white")
        course_id_label.place(x=10, y=50, width=80, height=35)
        self.add_course_id_entry.place(x=90, y=50, width=235, height=35)
        course_label = Label(self.add_course_frame, text="COURSE", font=("Bebas Neue", 17),
                             bg="#A51d23", fg="white")
        course_label.place(x=10, y=100, width=80, height=35)
        self.add_course_text.place(x=10, y=135, width=315, height=125)

        add_info_button = Button(self.add_course_frame, command='', text="ADD",
                                 bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                 font=("Bebas Neue", 15))
        add_info_button.place(x=175, y=300, width=70, height=30)
        clear_info_button = Button(self.add_course_frame, command=self.clear_data, text="CLEAR",
                                   bg="#A51d23", fg="white", activebackground="#A51d23", activeforeground="#FA9412",
                                   font=("Bebas Neue", 15))
        clear_info_button.place(x=255, y=300, width=70, height=30)

    def clear_data(self):
        self.add_course_id_entry.delete(0, END)
        self.add_course_text.delete(1.0, END)
