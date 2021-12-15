# Modules
import datetime
import time
from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import webbrowser
import csv

login_entry_file = open("User_Data.csv", "a", newline="")
data = csv.writer(login_entry_file)
list = []

# GUI second Window
root1 = Tk()


# For day
def myday():
    local_time = time.asctime(time.localtime(time.time()))
    current_day = local_time[:3]
    return current_day


# For date
def mydate():
    current_day = datetime.date.today()
    int_date = current_day.day
    int_month = current_day.month
    date = (str(int_date).zfill(2), "/", str(int_month).zfill(2), "/", current_day.year)
    return date


# Linking
linking = myday()
if linking == "Mon":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "09:30 - 10:30",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "12:30 - 01:00",
        "01:00 - 02:00",
        "02:00 - 03:00",
        "Chemistry",
        "Chemistry",
        "Sports",
        "Recess",
        "PPS",
        "PPS",
        "Nidhi Ma'am",
        "Nidhi Ma'am",
        " ----- ",
        " ----- ",
        "Rashmi Ma'am",
        "Rashmi Ma'am",
    )

if linking == "Tue":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "08:00 - 08:40",
        "08:50 - 09:30",
        "09:40 - 10:20",
        "10:20 - 11:00",
        "11:10 - 11:50",
        "12:00 - 12:40",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
    )

if linking == "Wed":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "09:30 - 10:30",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "12:30 - 01:00",
        "01:00 - 02:00",
        "02:00 - 03:00",
        "Maths",
        "Maths",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
        "Amit Sir",
        "Amit Sir",
        " ----- ",
        " ----- ",
        " ----- ",
        " ----- ",
    )
    """Time1, Time2, Time3, Time4, Time5, Time6, Subject1, Subject2, Subject3, Subject4, Subject5, Subject6, Teacher1, Teacher2, Teacher3, Teacher4, Teacher5, Teacher6 = "09:30 - 10:30", "10:30 - 11:30", "11:30 - 12:30", "12:30 - 01:00", "01:00 - 02:00", "02:00 - 03:00", "Maths", "Chemistry", "WT", "Recess", "PPS", "English", "Amit Sir", "Nidhi Ma'am", "Sandeep Sir", " ----- ", "Rashmi Ma'am", "Nivedita Ma'am" """


if linking == "Thu":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "09:30 - 10:30",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "12:30 - 01:00",
        "01:00 - 02:00",
        "02:00 - 03:00",
        "Chemistry",
        "PPS",
        "PPS",
        "Recess",
        "Chemistry",
        "WT",
        "Nidhi Ma'am",
        "Rashmi Ma'am",
        "Rashmi Ma'am",
        " ----- ",
        "Nidhi Ma'am",
        "Sandeep Sir",
    )

if linking == "Fri":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "09:30 - 10:30",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "12:30 - 01:00",
        "01:00 - 02:00",
        "02:00 - 03:00",
        "Chemistry",
        "Maths",
        "PPS",
        " ----- ",
        " ----- ",
        " ----- ",
        "Nidhi Ma'am",
        "Amit Sir",
        "Rashmi Ma'am",
        " ----- ",
        " ----- ",
        " ----- ",
    )

if linking == "Sat":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "09:30 - 10:30",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "12:30 - 01:00",
        "01:00 - 02:00",
        "02:00 - 03:00",
        "Chemistry",
        "Chemistry",
        "English",
        "Recess",
        "English",
        "WT",
        "Nidhi Ma'am",
        "Nidhi Ma'am",
        "Nivedita Ma'am",
        " ----- ",
        "Nivedita Ma'am",
        "Sandeep Sir",
    )

if linking == "Sun":
    (
        Time1,
        Time2,
        Time3,
        Time4,
        Time5,
        Time6,
        Subject1,
        Subject2,
        Subject3,
        Subject4,
        Subject5,
        Subject6,
        Teacher1,
        Teacher2,
        Teacher3,
        Teacher4,
        Teacher5,
        Teacher6,
    ) = (
        "09:30 - 10:30",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "12:30 - 01:00",
        "01:00 - 02:00",
        "02:00 - 03:00",
        "Chemistry",
        "Chemistry",
        "Sports",
        "Recess",
        "PPS",
        "PPS",
        "Nidhi Ma'am",
        "Nidhi Ma'am",
        " ----- ",
        " ----- ",
        "Rashmi Ma'am",
        "Rashmi Ma'am",
    )


# Thought of the Day

thought_variable = random.randrange(1, 11)

if thought_variable == 1:
    thought = "Many People failed, not because they don't have the Ability\n but they don't have the adversity to go throught the process "

if thought_variable == 2:
    thought = "    Make a Plan , Dive in it , Achive Results   "

if thought_variable == 3:
    thought = "Time beats Speed and Precision beats Power"

if thought_variable == 4:
    thought = "The day You become independent \n Things will become easier for You"

if thought_variable == 5:
    thought = "Take responsibilities of your failure and work on it  "

if thought_variable == 6:
    thought = "A champion does'nt become a champion in a Ring \n the Becoming happen in it's daily routine"

if thought_variable == 7:
    thought = (
        "Small Amount of Intense work when Applied Consistently \n CAN CHANGE THE WORLD"
    )

if thought_variable == 8:
    thought = "   Don't Love What you DO, BE Addicted  to it           "

if thought_variable == 9:
    thought = "Have Courage to Accecpt Mistake and Power to Correct it \n and BOUNCE BACK as A MORE STRONG Character"

if thought_variable == 10:
    thought = "Never be afraid of Giving and Asking for help to anyone"


# Information Function
def submit():

    if (
        intro_name.get().upper() == "NEERAJ ARORA"
        or intro_name.get().upper() == "LAVISHA GUPTA"
        or intro_name.get().upper() == "POOJA GUPTA"
        or intro_name.get().upper() == "VAIBHAV RAJ PANDAY"
        or intro_name.get().upper() == "ANAND PRATAP SINGH"
    ):
        if intro_branch.get().upper() == "CSE":
            if intro_semester.get().upper() == "1":
                if (
                    intro_password.get() == "neeraj@123"
                    or intro_password.get() == "lavisha@123"
                    or intro_password.get() == "pooja@123"
                    or intro_password.get() == "vaibhav@123"
                    or intro_password.get() == "anand@123"
                ):
                    messagebox.showinfo(
                        "Successful", "Welcome " + "ADMIN - " + intro_name.get().upper()
                    )
                    print(f"{intro_name.get()}")
                    # create file to save credientials in specific folder
                    # calling NEW Window
                    window_2_admin()
                else:
                    messagebox.showerror("Incorrect Details", "Wrong Password ")
            else:
                messagebox.showerror("Incorrect Details", "Wrong Semester")

        else:
            messagebox.showerror("Incorrect Details", "Wrong Branch")

    elif (
        intro_name.get().upper() == ""
        or intro_branch.get() == ""
        or intro_semester.get().upper() == ""
        or intro_password.get() == ""
    ):
        messagebox.showerror("Error", "not mentioned proper data !")

    elif (
        intro_name.get().upper() != "NEERAJ ARORA"
        or intro_branch.get() != "12"
        or intro_semester.get().upper() != "A"
        or intro_password.get() != "8316"
    ):
        messagebox.showinfo("Successful", "Welcome " + intro_name.get().upper())
        admin_name_f = f"{intro_name.get()}"
        admin_class_f = f"{intro_branch.get()}"
        admin_section_f = f"{intro_semester.get()}"
        admin_adm_number_f = f"{intro_password.get()}"

        while True:
            datalst = [admin_name_f, admin_class_f, admin_section_f, admin_adm_number_f]
            list.append(datalst)
            break
        for i in list:
            data.writerow(i)
        login_entry_file.close()

        # create file to save credientials in specific folder
        # calling NEW Window
        window_2_user()

    else:
        messagebox.showerror("Error", "Not in Database")


def window_2_admin():
    def window_4_user():

        # Global Images

        global tt_bg_image
        global back_main_tt_image
        root4 = Toplevel(root2)
        root4.geometry(f"{root1.winfo_screenwidth()}x{root1.winfo_screenheight()}+0+0")
        root4.title("Complete Time Table")

        # Images

        back_main_tt_image = PhotoImage(
            file="C:\\Python Project\\ZEITPLAN\\images\\BACK_tt.png"
        )
        tt_bg_image = PhotoImage(
            file="C:\\Python Project\\ZEITPLAN\\images\\FULL_TIMETABEL.png"
        )  # Back Ground Images
        tt_bg_label_image = Label(root4, image=tt_bg_image)
        tt_bg_label_image.pack()

        # Back Button

        back_root4_button = Button(
            root4,
            borderwidth=2,
            image=back_main_tt_image,
            bg="black",
            compound=LEFT,
            font="ariel 16 bold",
            text="",
            command=root4.destroy,
        )

        back_root4_button.place(x=10, y=10)

        # Exit Button
        exit_root_button = Button(
            root4,
            borderwidth=2,
            image=exit_image,
            bg="black",
            compound=LEFT,
            font="ariel 16 bold",
            text="",
            command=root1.destroy,
        )

        exit_root_button.place(x=1280, y=25)

    # Global Images
    global back_image
    global exit_image
    global back_main_image
    global bg_admin
    global header_frame
    global idea_image
    global mini_logo_user

    # Real Time Clock
    def mytime():
        local_time = time.asctime(time.localtime(time.time()))
        current_time = (
            local_time[11:13] + ":" + local_time[14:16] + ":" + local_time[17:19]
        )
        current_time = str(current_time)
        time_Label["text"] = current_time
        root2.after(800, mytime)

    # Creating New Window
    root2 = Toplevel(root1)

    # Geometry and Title
    root2.geometry(f"{root2.winfo_screenwidth()}x{root1.winfo_screenheight()}+0+0")
    root2.title("Time Table of admin window")

    # Images
    back_main_image = PhotoImage(
        file="C:\\Python Project\\ZEITPLAN\\images\\BACK_main.png"
    )
    idea_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\IDEA.png")
    mini_logo_user = PhotoImage(
        file="C:\\Python Project\\ZEITPLAN\\images\\mini_logo.png"
    )
    bg_admin = PhotoImage(
        file="C:\\Python Project\\ZEITPLAN\\images\\PURPLE.png"
    )  # Back Ground Image

    # Background image ADMIN
    bg_admin_label = Label(root2, image=bg_admin)
    bg_admin_label.place(x=0, y=0)

    # Frames

    admin_exit_button_frame = Frame(root2, bg="#441c74", borderwidth=6)
    admin_exit_button_frame.pack(side=TOP, anchor="ne", padx=10, pady=10)

    date_frame = Frame(root2, bg="#441c74", borderwidth=0)
    date_frame.place(x=20, y=100)

    day_frame = Frame(root2, bg="#441c74", borderwidth=0)
    day_frame.place(x=20, y=155)

    time_frame = Frame(root2, bg="#441c74", borderwidth=0)
    time_frame.place(x=20, y=210)

    main_frame = Frame(root2, bg="#441c74", borderwidth=5, relief=GROOVE)
    main_frame.place(x=360, y=190)

    # BUTTONS

    admin_exit_button = Button(
        admin_exit_button_frame,
        borderwidth=5,
        relief=FLAT,
        image=exit_image,
        font="ariel 16 bold",
        bg="#441c74",
        command=root1.destroy,
    )
    admin_exit_button.pack(padx=0, pady=0)

    admin_back_button = Button(
        root2,
        borderwidth=5,
        relief=FLAT,
        image=back_main_image,
        font="ariel 16 bold",
        bg="#441c74",
        command=root2.destroy,
    )
    admin_back_button.place(x=20, y=20)

    # MENUBAR of admin window

    menubar = Menu(root2)

    st = Menu(menubar, tearoff=0)
    st.add_command(label="Attendance detail")
    st.add_command(label="Time table")
    st.add_command(label="Assignment")
    st.add_separator()
    st.add_command(label="fee enquiry")
    root2.config(menu=menubar)
    menubar.add_cascade(label="Student info..", menu=st)

    sr = Menu(menubar, tearoff=0)
    sr.add_command(label="Books")
    sr.add_command(label="PPT")
    sr.add_separator()
    sr.add_command(label="video lecture")
    root2.config(menu=menubar)
    menubar.add_cascade(label="Study resources", menu=sr)

    s1 = Menu(menubar, tearoff=0)
    s1.add_command(label="Reset password")
    s1.add_separator()
    s1.add_command(label="Make admin")
    s1.add_command(label="Remove admin")
    root2.config(menu=menubar)
    menubar.add_cascade(label="Setting", menu=s1)

    h1 = Menu(menubar, tearoff=0)
    h1.add_command(label="?Help")
    h1.add_command(label="Check for Updates..")
    h1.add_separator()
    h1.add_command(label="About us")
    root2.config(menu=menubar)
    menubar.add_cascade(label="Help", menu=h1)

    # LABELS

    thought_Label = Label(
        root2,
        text=thought,
        image=idea_image,
        borderwidth=0,
        compound=LEFT,
        font=("Mangal", 20, "bold"),
        bg="#441c74",
        fg="white",
    )
    thought_Label.place(x=320, y=110)

    date_Label = Label(
        date_frame, text=mydate(), font="Jokerman 20 bold", bg="#441c74", fg="White"
    )
    date_Label.pack(side=TOP, anchor="nw")

    # Current Day

    current_day = myday()
    if current_day == "Mon":
        day_Label = Label(
            day_frame,
            text=myday() + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Tue":
        day_Label = Label(
            day_frame,
            text=myday() + "es" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Wed":
        day_Label = Label(
            day_frame,
            text=myday() + "nes" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Thu":
        day_Label = Label(
            day_frame,
            text=myday() + "rs" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Fri":
        day_Label = Label(
            day_frame,
            text=myday() + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Sat":
        day_Label = Label(
            day_frame,
            text=myday() + "ur" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Sun":
        day_Label = Label(
            day_frame,
            text=myday() + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    # TIME LABEL

    time_Label = Label(time_frame, font="SweetyRasty 20 bold", bg="#441c74", fg="White")
    time_Label.pack(side=TOP, anchor="nw")

    time_Label0 = Label(
        main_frame,
        text="Time",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label0.grid(row=0, column=0)

    time_Label1 = Label(
        main_frame,
        text=Time1,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label1.grid(row=1, column=0)

    time_Label2 = Label(
        main_frame,
        text=Time2,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label2.grid(row=2, column=0)

    time_Label3 = Label(
        main_frame,
        text=Time3,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label3.grid(row=3, column=0)

    time_Label4 = Label(
        main_frame,
        text=Time4,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label4.grid(row=4, column=0)

    time_Label5 = Label(
        main_frame,
        text=Time5,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label5.grid(row=5, column=0)

    time_Label6 = Label(
        main_frame,
        text=Time6,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label6.grid(row=6, column=0)

    # lINKS of WEBSITES
    def open_chemistry():
        pass

    def open_physics():
        pass

    def open_maths():
        pass

    def open_computerScience():
        pass

    def open_physical_education():
        pass

    def open_english():
        pass

    def open_recess():
        pass

    time_Label0 = Label(
        main_frame,
        text="Subject",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label0.grid(row=0, column=1)

    # SUBJECT 1

    if Subject1 == "WT":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Chemistry":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Maths":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "PPS":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Sports":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "English":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Recess":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=20,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

        # SUBJECT 2

    if Subject2 == "Physics":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=68,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    # SUBJECT 2

    if Subject2 == "WT":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Chemistry":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Maths":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "PPS":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Sports":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "English":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Recess":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    # SUBJECT 3

    if Subject3 == "WT":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Chemistry":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Maths":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "PPS":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Sports":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "English":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Recess":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    # SUBJECT 4

    if Subject4 == "WT":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Chemistry":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Maths":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "PPS":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Sports":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "English":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Recess":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    # SUBJECT 5

    if Subject5 == "WT":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Chemistry":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Maths":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "PPS":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Sports":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "English":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Recess":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    # SUBJECT 6

    if Subject6 == "WT":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Chemistry":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Maths":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "PPS":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Sports":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "English":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Recess":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    Teacher_Label0 = Label(
        main_frame,
        text=" Teacher ",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label0.grid(row=0, column=2)

    Teacher_Label1 = Label(
        main_frame,
        text=Teacher1,
        font="Jokerman 20",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label1.grid(row=1, column=2)

    Teacher_Label2 = Label(
        main_frame,
        text=Teacher2,
        font="Jokerman 20",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label2.grid(row=2, column=2)

    Teacher_Label3 = Label(
        main_frame,
        text=Teacher3,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label3.grid(row=3, column=2)

    Teacher_Label4 = Label(
        main_frame,
        text=Teacher4,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label4.grid(row=4, column=2)

    Teacher_Label5 = Label(
        main_frame,
        text=Teacher5,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label5.grid(row=5, column=2)

    Teacher_Label6 = Label(
        main_frame,
        text=Teacher6,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label6.grid(row=6, column=2)

    mytime()


def window_2_user():
    def window_5_user():

        # Global Images

        global tt_bg_image
        global back_main_tt_image
        root5 = Toplevel(root3)
        root5.geometry(f"{root1.winfo_screenwidth()}x{root1.winfo_screenheight()}+0+0")
        root5.title("Complete Time Table")

        # Images

        back_main_tt_image = PhotoImage(
            file="C:\\Python Project\\ZEITPLAN\\images\\BACK_tt.png"
        )
        tt_bg_image = PhotoImage(
            file="C:\\Python Project\\ZEITPLAN\\images\\FULL_TIMETABEL.png"
        )  # Back Ground Images
        tt_bg_label_image = Label(root5, image=tt_bg_image)
        tt_bg_label_image.pack()

        # Back Button

        back_root4_button = Button(
            root5,
            borderwidth=2,
            image=back_main_tt_image,
            bg="black",
            compound=LEFT,
            font="ariel 16 bold",
            text="",
            command=root5.destroy,
        )

        back_root4_button.place(x=10, y=10)

        # Exit Button
        exit_root_button = Button(
            root5,
            borderwidth=2,
            image=exit_image,
            bg="black",
            compound=LEFT,
            font="ariel 16 bold",
            text="",
            command=root1.destroy,
        )

        exit_root_button.place(x=1280, y=25)

    # Global Images
    global back_image
    global exit_image
    global back_main_image
    global bg_user
    global idea_image
    global mini_logo_user

    # Real Time Clock
    def mytime():
        local_time = time.asctime(time.localtime(time.time()))
        current_time = (
            local_time[11:13] + ":" + local_time[14:16] + ":" + local_time[17:19]
        )
        current_time = str(current_time)
        time_Label["text"] = current_time
        root1.after(800, mytime)

    # Creating New Window
    root3 = Toplevel(root1)

    # Geometry and Title
    root3.geometry(f"{root3.winfo_screenwidth()}x{root1.winfo_screenheight()}+0+0")
    root3.title("Time Table")

    # Images
    back_main_image = PhotoImage(
        file="C:\\Python Project\\ZEITPLAN\\images\\BACK_main.png"
    )
    idea_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\IDEA.png")
    mini_logo_user = PhotoImage(
        file="C:\\Python Project\\ZEITPLAN\\images\\mini_logo.png"
    )
    bg_user = PhotoImage(
        file="C:\\Python Project\\ZEITPLAN\\images\\PURPLE.png"
    )  # Back Ground Image

    # Background image USER
    bg_user_label = Label(root3, image=bg_user, bd=0)
    bg_user_label.place(x=0, y=0)

    # Frames

    user_exit_button_frame = Frame(root3, bg="#441c74", borderwidth=6)
    user_exit_button_frame.pack(side=TOP, anchor="ne", padx=10, pady=10)

    date_frame = Frame(root3, bg="#441c74", borderwidth=0)
    date_frame.place(x=20, y=100)

    day_frame = Frame(root3, bg="#441c74", borderwidth=0)
    day_frame.place(x=20, y=155)

    time_frame = Frame(root3, bg="#441c74", borderwidth=0)
    time_frame.place(x=20, y=210)

    main_frame = Frame(root3, bg="#441c74", borderwidth=5, relief=GROOVE)
    main_frame.place(x=360, y=190)

    # BUTTONS

    user_exit_button = Button(
        user_exit_button_frame,
        borderwidth=5,
        relief=FLAT,
        image=exit_image,
        bg="#441c74",
        font="ariel 16 bold",
        command=root1.destroy,
    )
    user_exit_button.pack(padx=0, pady=0)

    user_back_button = Button(
        root3,
        borderwidth=5,
        relief=FLAT,
        image=back_main_image,
        font="ariel 16 bold",
        bg="#441c74",
        command=root3.destroy,
    )
    user_back_button.place(x=20, y=20)

    FULL_TT_button = Button(
        root3,
        borderwidth=0,
        text="",
        image=mini_logo_user,
        bg="#441c74",
        compound=LEFT,
        font="ariel 16 bold",
        command=window_5_user,
    )
    FULL_TT_button.place(x=650, y=680)

    # MENUBAR OF USER WINDOW

    mymenu = Menu(root3)
    mymenu.add_command(label="Change password")

    mymenu.add_command(label="Log out")

    mymenu.add_command(label="Exit")
    root3.config(menu=mymenu)

    # DASHBOARD BUTTON

    Learnings = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Learnings",
    )
    Learnings.place(x=100, y=20)

    Online_class = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Online class",
    )
    Online_class.place(x=240, y=20)

    Announcement = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        # image=back_main_image,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Announcement",
    )
    Announcement.place(x=400, y=20)

    Attendance = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        # image=back_main_image,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Attendance"
        # command=root3.destroy,
    )
    Attendance.place(x=590, y=20)

    Event_calender = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        # image=back_main_image,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Event calender"
        # command=root3.destroy,
    )
    Event_calender.place(x=750, y=20)

    Assignments = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        # image=back_main_image,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Assignments"
        # command=root3.destroy,
    )
    Assignments.place(x=950, y=20)

    class_diary = Button(
        root3,
        borderwidth=5,
        relief=SUNKEN,
        # image=back_main_image,
        font="ariel 16 bold",
        bg="red",
        fg="white",
        text="Class Diary"
        # command=root3.destroy,
    )
    class_diary.place(x=1130, y=20)

    # LABELS

    thought_Label = Label(
        root3,
        text=thought,
        image=idea_image,
        borderwidth=0,
        compound=LEFT,
        font=("Mangal", 20, "bold"),
        fg="White",
        bg="#441c74",
    )
    thought_Label.place(x=400, y=110)

    date_Label = Label(
        date_frame, text=mydate(), font="Jokerman 20 bold", bg="#441c74", fg="White"
    )
    date_Label.pack(side=TOP, anchor="nw")

    # Current Day

    current_day = myday()
    if current_day == "Mon":
        day_Label = Label(
            day_frame,
            text=myday() + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Tue":
        day_Label = Label(
            day_frame,
            text=myday() + "es" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Wed":
        day_Label = Label(
            day_frame,
            text=myday() + "nes" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Thu":
        day_Label = Label(
            day_frame,
            text=myday() + "rs" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Fri":
        day_Label = Label(
            day_frame,
            text=myday() + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Sat":
        day_Label = Label(
            day_frame,
            text=myday() + "ur" + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    if current_day == "Sun":
        day_Label = Label(
            day_frame,
            text=myday() + "day",
            font="Jokerman 20 bold",
            bg="#441c74",
            fg="White",
        )
        day_Label.pack(side=TOP, anchor="nw")

    # TIME LABEL
    time_Label = Label(time_frame, font="SweetyRasty 20 bold", bg="#441c74", fg="White")
    time_Label.pack(side=TOP, anchor="nw")

    time_Label0 = Label(
        main_frame,
        text="Time",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label0.grid(row=0, column=0)

    time_Label1 = Label(
        main_frame,
        text=Time1,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label1.grid(row=1, column=0)

    time_Label2 = Label(
        main_frame,
        text=Time2,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label2.grid(row=2, column=0)

    time_Label3 = Label(
        main_frame,
        text=Time3,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label3.grid(row=3, column=0)

    time_Label4 = Label(
        main_frame,
        text=Time4,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label4.grid(row=4, column=0)

    time_Label5 = Label(
        main_frame,
        text=Time5,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label5.grid(row=5, column=0)

    time_Label6 = Label(
        main_frame,
        text=Time6,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label6.grid(row=6, column=0)

    """
    time_Label = Label(time_frame, font="SweetyRasty 20 bold", bg="#441c74", fg="White")
    time_Label.pack(side=TOP, anchor="nw")

    time_Label0 = Label(
        main_frame,
        text="Time",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label0.grid(row=0, column=0)

    time_Label1 = Label(
        main_frame,
        text=Time1,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label1.grid(row=1, column=0)

    time_Label2 = Label(
        main_frame,
        text=Time2,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label2.grid(row=2, column=0)

    time_Label3 = Label(
        main_frame,
        text=Time3,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label3.grid(row=3, column=0)

    time_Label4 = Label(
        main_frame,
        text=Time4,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label4.grid(row=4, column=0)

    time_Label5 = Label(
        main_frame,
        text=Time5,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label5.grid(row=5, column=0)

    time_Label6 = Label(
        main_frame,
        text=Time6,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label6.grid(row=6, column=0)
    """
    # lINKS of WEBSITES
    def open_chemistry():
        webbrowser.open("https://classroom.google.com/u/1/c/MTE0Nzg3NDEzODUy")

    def open_physics():
        webbrowser.open("https://classroom.google.com/u/1/c/MTM3MTU3ODk2NTc4")

    def open_maths():
        webbrowser.open("https://classroom.google.com/u/1/c/MTA4NTA1MjIxNzEy")

    def open_computerScience():
        webbrowser.open("https://classroom.google.com/u/1/c/MTA1NzE4Mjk4NTk0")

    def open_physical_education():
        webbrowser.open("https://classroom.google.com/u/1/c/MTIxMTM1NzMwMjE1")

    def open_english():
        webbrowser.open("https://classroom.google.com/u/1/c/MTE0ODU0Njc2NDgy")

    def open_recess():
        webbrowser.open(
            "https://www.youtube.com/results?search_query=eye+exercise+for+relaxation+"
        )

    time_Label0 = Label(
        main_frame,
        text="Subject",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    time_Label0.grid(row=0, column=1)

    # SUBJECT 1

    if Subject1 == "WT":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Chemistry":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Maths":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "PPS":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Sports":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "English":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

    if Subject1 == "Recess":
        Subject_button1 = Button(
            main_frame,
            text=Subject1,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=20,
            bg="#441c74",
            fg="White",
        )
        Subject_button1.grid(row=1, column=1)

        # SUBJECT 2

    if Subject2 == "Physics":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=68,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    # SUBJECT 2

    if Subject2 == "WT":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Chemistry":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Maths":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "PPS":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Sports":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "English":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    if Subject2 == "Recess":
        Subject_button2 = Button(
            main_frame,
            text=Subject2,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button2.grid(row=2, column=1)

    # SUBJECT 3

    if Subject3 == "WT":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Chemistry":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Maths":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "PPS":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Sports":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "English":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    if Subject3 == "Recess":
        Subject_button3 = Button(
            main_frame,
            text=Subject3,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button3.grid(row=3, column=1)

    # SUBJECT 4

    if Subject4 == "WT":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Chemistry":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Maths":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "PPS":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Sports":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "English":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    if Subject4 == "Recess":
        Subject_button4 = Button(
            main_frame,
            text=Subject4,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button4.grid(row=4, column=1)

    # SUBJECT 5

    if Subject5 == "WT":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Chemistry":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Maths":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "PPS":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Sports":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "English":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    if Subject5 == "Recess":
        Subject_button5 = Button(
            main_frame,
            text=Subject5,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button5.grid(row=5, column=1)

    # SUBJECT 6

    if Subject6 == "WT":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_physics,
            padx=95,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Chemistry":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_chemistry,
            padx=55,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Maths":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_maths,
            padx=79,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "PPS":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_computerScience,
            padx=88,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Sports":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_physical_education,
            padx=77,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "English":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_english,
            padx=72,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    if Subject6 == "Recess":
        Subject_button6 = Button(
            main_frame,
            text=Subject6,
            font="Jokerman 20 italic",
            command=open_recess,
            padx=70,
            bg="#441c74",
            fg="White",
        )
        Subject_button6.grid(row=6, column=1)

    Teacher_Label0 = Label(
        main_frame,
        text=" Teacher ",
        font="Jokerman 20 bold",
        pady=20,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label0.grid(row=0, column=2)

    Teacher_Label1 = Label(
        main_frame,
        text=Teacher1,
        font="Jokerman 20",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label1.grid(row=1, column=2)

    Teacher_Label2 = Label(
        main_frame,
        text=Teacher2,
        font="Jokerman 20",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label2.grid(row=2, column=2)

    Teacher_Label3 = Label(
        main_frame,
        text=Teacher3,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label3.grid(row=3, column=2)

    Teacher_Label4 = Label(
        main_frame,
        text=Teacher4,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label4.grid(row=4, column=2)

    Teacher_Label5 = Label(
        main_frame,
        text=Teacher5,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label5.grid(row=5, column=2)

    Teacher_Label6 = Label(
        main_frame,
        text=Teacher6,
        font="Jokerman 20 ",
        pady=10,
        padx=20,
        bg="#441c74",
        fg="White",
    )
    Teacher_Label6.grid(row=6, column=2)

    mytime()


# Geometry and Title
root1.geometry(f"{root1.winfo_screenwidth()}x{root1.winfo_screenheight()}+0+0")
# root1.geometry("1366x768+0+0")
root1.title("Welcome")


# Images
logo_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\Logo_3.png")
men_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\MEN.png")
lock_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\LOCK.png")
number_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\NUMBERS.png")
stream_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\STREAM.png")
back_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\BACK.png")
exit_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\EXIT.png")
submit_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\SUBMIT .png")
background_image = PhotoImage(file="C:\\Python Project\\ZEITPLAN\\images\\PURPLE.png")


# my_photo_intro = Image.open("C:\\Python Project\\ZEITPLAN\\images\\WHITE.jpg")     # Backgound Image
# admin_bg_image = ImageTk.PhotoImage(my_photo_intro)   # Backgound Image
# admin_bg_label_image = Label(image=admin_bg_image)    # Backgound Image
# admin_bg_label_image.pack()                           # Backgound Image


# VARIABLES
intro_name = StringVar()
intro_branch = StringVar()
intro_semester = StringVar()
intro_password = StringVar()

# Background Image (White)
intro_background_image = Label(root1, image=background_image, bd=0).place(x=0, y=0)
# background_image_intro.grid(row=0, columnspan=2, pady=0)


# FRAMES
intro_exit_button_frame = Frame(root1, bg="#441c74", borderwidth=6, relief=FLAT)
intro_exit_button_frame.pack(side=TOP, anchor="ne", padx=10, pady=10)

info_frame = Frame(root1, bg="#441c74", borderwidth=6, relief=FLAT)
info_frame.pack(side=TOP, anchor="center", pady=10)


# EXIT BUTTONS
intro_exit_button = Button(
    intro_exit_button_frame,
    borderwidth=10,
    relief=FLAT,
    image=exit_image,
    bg="#441c74",
    font="ariel 16 bold",
    command=root1.destroy,
)
intro_exit_button.pack(padx=0, pady=0)
# exit_root_button.place(x=1800, y=40)
# exit_root_button.grid(row=0, column=70)

# ZIETPLAN logo
intro_logo = Label(info_frame, image=logo_image, bd=0)  # labeling LOGO (HEAD) image
intro_logo.grid(row=0, columnspan=2, pady=50)  # labeling LOGG (HEAD) image


# labeling admin_name image and admin_name
intro_name_label = Label(
    info_frame,
    text="Name",
    image=men_image,
    compound=LEFT,
    font="ariel 10 bold",
    fg="white",
    bg="#441c74",
)
intro_name_label.grid(row=1, column=0)
# creating "entering" blank for username
intro_name_entry = Entry(
    info_frame, bd=5, textvariable=intro_name, relief=GROOVE, font="Arial 15 "
)
intro_name_entry.grid(row=1, column=1, padx=20)


# labeling Number image and class
intro_branch_label = Label(
    info_frame,
    text="Branch",
    image=number_image,
    compound=LEFT,
    font="ariel 10 bold",
    fg="white",
    bg="#441c74",
)
intro_branch_label.grid(row=2, column=0)
# creating "entering" blank for class
intro_branch_entry = Entry(
    info_frame, bd=5, textvariable=intro_branch, relief=GROOVE, font="Arial 15 "
)
intro_branch_entry.grid(row=2, column=1, padx=20)


# labeling Stream image and Section
intro_semester_label = Label(
    info_frame,
    text="Semester",
    image=stream_image,
    compound=LEFT,
    font="ariel 10 bold",
    fg="white",
    bg="#441c74",
)
intro_semester_label.grid(row=3, column=0)
# creating "entering" blank for class
intro_semester_entry = Entry(
    info_frame, bd=5, textvariable=intro_semester, relief=GROOVE, font="Arial 15 "
)
intro_semester_entry.grid(row=3, column=1, padx=20)


# labeling Numbers_1 image and Admission_Number
intro_password_label = Label(
    info_frame,
    text="Password",
    image=lock_image,
    compound=LEFT,
    font="ariel 10 bold",
    fg="white",
    bg="#441c74",
)
intro_password_label.grid(row=4, column=0)
# creating "entering" blank for class
intro_password_entry = Entry(
    info_frame,
    bd=5,
    textvariable=intro_password,
    show="*",
    relief=GROOVE,
    font="Arial 15 ",
)
intro_password_entry.grid(row=4, column=1, padx=20)


# SUBMIT Button
Submit_Button = Button(
    info_frame,
    text="",
    borderwidth=0,
    font="ariel 14 bold",
    image=submit_image,
    command=submit,
    compound=LEFT,
    bg="#441c74",
    fg="red",
)
Submit_Button.grid(row=5, columnspan=2, pady=10)

# width_value = root1.winfo_screenwidth()
# height_value = root1.winfo_screenheight()
# print(width_value)
# print(height_value)
# can not use pack and grid in same frame or class
root1.mainloop()
