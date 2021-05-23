from tkinter import *

from DashboardGUI import DashboardGUI
from StudentsGUI import StudentGUI
from CoursesGUI import CoursesGUI
from AboutGUI import AboutGUI
import SISdatabase


class SISGUIApp:
    def __init__(self, frame):
        # creates database table for students and courses
        SISdatabase.student_data()
        SISdatabase.course_data()

        self.frame = frame
        self.frame.title("Student Information System")
        self.frame.geometry("1200x680+63+8")
        self.frame.resizable(False, False)
        self.frame.iconbitmap('logosis.ico')

        # background frames
        bg_frame = Frame(self.frame, bg="#A51d23")
        bg_frame.place(x=0, y=0, width=1200, height=680)

        # navigation frame
        self.nav_frame = Frame(bg_frame, bg="#A51d23")
        self.nav_frame.place(x=3, y=3, width=260, height=674)

        # contents frame
        self.right_frame = Frame(bg_frame, bg="#FA9412")
        self.right_frame.place(x=266, y=0, width=940, height=680)

        self.SISlogopic = PhotoImage(file=r"sislabellogo.png").subsample(2, 2)
        icon_pic_lbl = Label(self.nav_frame, image=self.SISlogopic)
        icon_pic_lbl.photo = self.SISlogopic
        icon_pic_lbl.place(x=5, y=10, width=250, height=180)

        self.dashboard_img = PhotoImage(file=r"dashboardimg.png")
        self.student_img = PhotoImage(file=r"studimg.png")
        self.course_img = PhotoImage(file=r"courseimg.png")
        self.about_img = PhotoImage(file=r"aboutimg.png")

        dashbrd_nav_button = Button(self.nav_frame, command=self.dashboard_frame_gui, relief=FLAT,
                                    activebackground="#A51d23", activeforeground="white", fg="#FA9412", bg="#A51d23",
                                    image=self.dashboard_img, text="   Dashboard",
                                    font=("Blinker", 17, "bold"), anchor="w", compound="left")
        dashbrd_nav_button.place(x=0, y=200, width=260, height=50)
        stud_nav_button = Button(self.nav_frame, command=self.student_frame_gui, relief=FLAT,
                                 activebackground="#A51d23", activeforeground="white", fg="#FA9412", bg="#A51d23",
                                 image=self.student_img, text="   Students",
                                 font=("Blinker", 17, "bold"), anchor="w", compound="left")
        stud_nav_button.place(x=0, y=250, width=260, height=50)
        course_nav_button = Button(self.nav_frame, command=self.courses_frame_gui, relief=FLAT,
                                   activebackground="#A51d23", activeforeground="white", fg="#FA9412", bg="#A51d23",
                                   image=self.course_img, text="   Courses",
                                   font=("Blinker", 17, "bold"), anchor="w", compound="left")
        course_nav_button.place(x=0, y=300, width=260, height=50)
        about_nav_button = Button(self.nav_frame, command=self.about_frame_gui, relief=FLAT,
                                  activebackground="#A51d23", activeforeground="white", fg="#FA9412", bg="#A51d23",
                                  image=self.about_img, text="   About",
                                  font=("Blinker", 17, "bold"), anchor="w", compound="left")
        about_nav_button.place(x=0, y=350, width=260, height=50)

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
                                   anchor="w", font=("Blinker", 20, "bold"))
        self.heading_lbldsgn = Label(self.right_frame, image=self.head_bldsgn_img, bg="#A51d23",
                                     fg="white", anchor='sw')
        self.heading_label.place(x=20, y=50, width=900, height=50)
        self.heading_lbldsgn.place(x=800, y=50, width=120, height=50)

        self.dashboard_frame_gui()

    def hide_widgets(self):
        self.dashboard_cont_frame.place_forget()
        self.student_cont_frame.place_forget()
        self.courses_cont_frame.place_forget()
        self.about_cont_frame.place_forget()

    def dashboard_frame_gui(self):
        self.heading_label.config(text="  DASHBOARD")
        self.hide_widgets()
        self.dashboard_cont_frame.place(x=20, y=100, width=900, height=570)
        DashboardGUI(self.dashboard_cont_frame)

    def student_frame_gui(self):
        self.heading_label.config(text="  STUDENTS")
        self.hide_widgets()
        self.student_cont_frame.place(x=20, y=100, width=900, height=570)
        StudentGUI(self.student_cont_frame)

    def courses_frame_gui(self):
        self.heading_label.config(text="  COURSES")
        self.hide_widgets()
        self.courses_cont_frame.place(x=20, y=100, width=900, height=570)
        CoursesGUI(self.courses_cont_frame)

    def about_frame_gui(self):
        self.heading_label.config(text="  ABOUT")
        self.hide_widgets()
        self.about_cont_frame.place(x=20, y=100, width=900, height=570)
        AboutGUI(self.about_cont_frame)


root = Tk()
ob = SISGUIApp(root)
root.mainloop()
