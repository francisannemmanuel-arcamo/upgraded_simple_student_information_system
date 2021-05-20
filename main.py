from tkinter import *

from DashboardGUI import DashboardGUI
from StudentsGUI import StudentGUI
from CoursesGUI import CoursesGUI
from AboutGUI import AboutGUI


class SISGUIApp:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title("Simple Student Information System")
        self.frame.geometry("1200x680+63+8")
        self.frame.resizable(False, False)

        # background frames
        bg_frame = Frame(self.frame, bg="#A51d23")
        bg_frame.place(x=0, y=0, width=1200, height=680)

        # navigation frame
        self.nav_frame = Frame(bg_frame, bg="#A51d23")
        self.nav_frame.place(x=3, y=3, width=260, height=674)

        # contents frame
        self.right_frame = Frame(bg_frame, bg="#FA9412")
        self.right_frame.place(x=266, y=0, width=940, height=680)

        icon_pic_lbl = Label(self.nav_frame, text="insert logo here")
        icon_pic_lbl.place(x=60, y=30, width=130, height=130)

        dashbrd_nav_button = Button(self.nav_frame, command=self.dashboard_frame_gui, text="   DASHBOARD",
                                    bg="#A51d23", fg="white",
                                    font=("Bebas Neue", 20), anchor="w")
        dashbrd_nav_button.place(x=0, y=180, width=260, height=50)
        stud_nav_button = Button(self.nav_frame, command=self.student_frame_gui, text="   STUDENTS", bg="#A51d23",
                                 fg="white", font=("Bebas Neue", 20), anchor="w")
        stud_nav_button.place(x=0, y=230, width=260, height=50)
        course_nav_button = Button(self.nav_frame, command=self.courses_frame_gui, text="   COURSES", bg="#A51d23",
                                   fg="white", font=("Bebas Neue", 20), anchor="w")
        course_nav_button.place(x=0, y=280, width=260, height=50)
        about_nav_button = Button(self.nav_frame, command=self.about_frame_gui, text="   ABOUT", bg="#A51d23",
                                  fg="white", font=("Bebas Neue", 20), anchor="w")
        about_nav_button.place(x=0, y=330, width=260, height=50)

        self.dashboard_cont_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                          highlightthickness=2)
        self.student_cont_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                        highlightthickness=2)
        self.courses_cont_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                        highlightthickness=2)
        self.about_cont_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                      highlightthickness=2)

        self.head_bldsgn_img = PhotoImage(file=r"label_design.png")
        self.heading_label = Label(self.right_frame, text="",
                                   bg="#A51d23", fg="white",
                                   anchor="w", font=("Bebas Neue", 20))
        self.heading_lbldsgn = Label(self.right_frame, image=self.head_bldsgn_img, bg="#A51d23",
                                     fg="white", anchor='sw', font=("Bebas Neue", 40))
        self.heading_label.place(x=20, y=50, width=900, height=50)
        self.heading_lbldsgn.place(x=800, y=50, width=120, height=50)

        self.dashboard_frame_gui()

    def hide_widgets(self):
        self.dashboard_cont_frame.place_forget()
        self.student_cont_frame.place_forget()
        self.courses_cont_frame.place_forget()
        self.about_cont_frame.place_forget()

    def dashboard_frame_gui(self):
        self.heading_label.config(text="  Dashboard")
        self.hide_widgets()
        DashboardGUI(self.dashboard_cont_frame)

    def student_frame_gui(self):
        self.heading_label.config(text="  Students")
        self.hide_widgets()
        StudentGUI(self.student_cont_frame)

    def courses_frame_gui(self):
        self.heading_label.config(text="  Courses")
        self.hide_widgets()
        CoursesGUI(self.courses_cont_frame)

    def about_frame_gui(self):
        self.heading_label.config(text="  About")
        self.hide_widgets()
        AboutGUI(self.about_cont_frame)


root = Tk()
ob = SISGUIApp(root)
root.mainloop()
