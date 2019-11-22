#! /usr/bin/env python

import sys


#Globals defined to user input fields throughout program
global username
global usertemp
global realtemp
global root
global count #tallies value of responses given by user
global country
global realcountry
global finalcountry
count = 0

try:
    import Tkinter as tk
    from tkinter import *
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def diagfunc():
    root = tk.Toplevel()
    top = diagWindow(root)
    root.mainloop()

def diagregfunc():
    root = tk.Toplevel()
    top = diagregWindow(root)
    root.mainloop()

def diagnofunc():
    root = tk.Toplevel()
    top = nodengueWindow(root)
    root.mainloop()

def vp_start_gui():
    root = tk.Toplevel()
    top = mainWindow(root)
    root.mainloop()



class mainWindow:

    def __init__(self,top):


        def check_null():  # THIS FUNCTION CHECKS FOR EMPTY VALUES
            from tkinter.messagebox import showerror, showinfo, showwarning

            a = str(eyeV.get())
            b = str(headV.get())
            c = str(jointV.get())

            d = str(vomitV.get())
            e = str(absV.get())
            f= str(bleedV.get())
            g=str(countvar.get())



            if len(nameText.get()) == 0:
                showerror(title="Error", message="Please Enter Your Name")

            elif len(tempText.get()) == 0:
                showerror(title="Error", message="Temperature Cannot Be Blank")
            elif (a == "None"):
                showerror(title="Error", message="Please Select All Radiobutton options")

            elif (b == "None"):
                showerror(title="Error", message="Please Select All Radiobutton options")

            elif (c == "None"):
                showerror(title="Error", message="Please Select All Radiobutton options")
            elif (d == "None"):
                showerror(title="Error", message="Please Select All Radiobutton options")

            elif (e == "None"):
                showerror(title="Error", message="Please Select All Radiobutton options")

            elif (f == "None"):
                showerror(title="Error", message="Please Select All Radiobutton options")
            elif (g == "" and len(countrytext.get())== 0):
                showerror(title="Error", message="A Country Must Be Selected")

            else:
                validation()

        def validation():  # THIS FUNCTION CHECKS TEMP BOX AND CONVERTS TO FAHRENEHIT
            global count
            global menu
            global finalcountry
            global countvar

            from tkinter.messagebox import showerror, showinfo, showwarning
            if len(countrytext.get()) != 0:
                country.append(countrytext.get())
                countvar = tk.StringVar()
                countvar.set(countrytext.get())
                menu.destroy()
                menu = tk.OptionMenu(Frame1, countvar, *country)
                menu.place(relx=0.560, rely=0.9, relheight=0.047, relwidth=0.101, width="40")
                menu.configure(background="#d9d9d9")
                menu.configure(font="TkFixedFont")
                menu.configure(foreground="#000000")
                finalcountry = countrytext.get()
            else:
                    finalcountry = countvar.get()



            #from tkinter.messagebox import showerror, showinfo, showwarning



            try:
                conventry = float(usertemp.get())

                if conventry >= 36 and conventry <= 44:


                    convtemp = round(conventry * 1.8 + 32,2) #rounds off to 2 decimal places
                    finaltemp = str(convtemp)
                    showinfo(title="Approve", message="Temperature Converted to Fahrenheit")
                    realtemp.configure(state='normal')
                    realtemp.delete(0,10) #removes previous output
                    realtemp.insert(0,finaltemp) #inserts new reading
                    realtemp.configure(state='readonly') #sets field back to readonly

                    if convtemp >= 104.0 :
                        count += 2
                    elif convtemp >= 90.0 and convtemp < 99.9:
                        count += 0
                    elif convtemp >= 100.0 and convtemp < 104.0:
                        count += 1

                    saveuser()
                else:
                    showerror(title="Error", message="Temperature must be between 36 and 44 degrees Celsius")
            except ValueError:
                showerror(title="Error", message="Invalid Temperature")

        def saveuser():
            global count

            from tkinter.messagebox import showerror, showinfo, showwarning

            with open("users.txt","a") as file:
                global finalcountry
                a = str(eyeV.get())
                b = str(headV.get())
                c = str(jointV.get())
                d = str(vomitV.get())
                e = str(absV.get())
                f = str(bleedV.get())
                username2 = str(username.get())
                usertemp2 = str(realtemp.get())

                if a == "Has Eye Ache":
                    count += 1
                if b == "Has Headache":
                    count += 1
                if c == "Has Joint Ache":
                    count += 2
                if d == "Is Vomitting":
                    count += 3
                if e == "Has Abdominal Pain":
                    count += 2
                if f == "Rashes On Skin":
                    count += 3

                inputstring = username2 + "\t" + usertemp2 + "\t" + a + "\t" + b + "\t" + c + "\t" + d + "\t" + e + "\t"\
                              + f + "\t" + finalcountry + "\n"

                try:
                    file.write(inputstring)
                    showinfo(title="Approve", message="Diagnosis Completed")
                    realcountry.delete(0, 30)
                    eyeV.set(None)
                    headV.set(None)
                    jointV.set(None)
                    absV.set(None)
                    bleedV.set(None)
                    vomitV.set(None)
                    username.delete(0,30)
                    usertemp.delete(0,10)
                    realtemp.configure(state='normal')
                    realtemp.delete(0, 10)  # removes previous outpu
                    realtemp.configure(state='readonly')  # sets field back to readonly

                    if count <= 4:
                        diagnofunc()
                    elif count >= 11:
                        diagfunc()
                    else:
                        diagregfunc()

                except AttributeError :
                    showerror(title="Approve", message="Error Saving User")




        #This class configures and populates window.
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        font10 = "-family {Segoe UI Light} -size 11 -weight bold " \
                 "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Light} -size 12 -weight bold " \
                 "-slant roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI Historic} -size 10 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Eras Demi ITC} -size 22 -weight normal " \
                "-slant italic -underline 0 -overstrike 0"

        top.geometry("800x650+391+84")
        top.title("Enter Details")
        top.configure(background="#d9d9d9")



        Frame1=tk.Frame(top)
        Frame1.place(relx=0.033, rely=0.089, relheight=0.833, relwidth=0.942)
        Frame1.configure(relief='groove')
        Frame1.configure(borderwidth="2")
        Frame1.configure(relief='groove')
        Frame1.configure(background="#d9d9d9")
        Frame1.configure(width=565)

        nameL = tk.Label(Frame1)
        nameL.place(relx=0.071, rely=0.133, height=21, width=110)
        nameL.configure(background="#d9d9d9")
        nameL.configure(disabledforeground="#a3a3a3")
        nameL.configure(foreground="#000000")
        nameL.configure(text='''What is your name?''')

        tempL = tk.Label(Frame1)
        tempL.place(relx=0.051, rely=0.24, height=21, width=225)
        tempL.configure(background="#d9d9d9")
        tempL.configure(disabledforeground="#a3a3a3")
        tempL.configure(foreground="#000000")
        tempL.configure(text='''Enter temperature in degrees Celsius ''')

        username = nameText = tk.Entry(Frame1)
        nameText.place(relx=0.372, rely=0.133,height=20, relwidth=0.29)
        nameText.configure(background="white")
        nameText.configure(disabledforeground="#a3a3a3")
        nameText.configure(font="TkFixedFont")
        nameText.configure(foreground="#000000")
        nameText.configure(insertbackground="black")

        usertemp = tempText = tk.Entry(Frame1)
        tempText.place(relx=0.452, rely=0.24,height=20, relwidth=0.131)
        tempText.configure(background="white")
        tempText.configure(disabledforeground="#a3a3a3")
        tempText.configure(font="TkFixedFont")
        tempText.configure(foreground="#000000")
        tempText.configure(insertbackground="black")
        tempText.configure(width=74)

        eyeL = tk.Label(Frame1)
        eyeL.place(relx=0.071, rely=0.347, height=21, width=218)
        eyeL.configure(background="#d9d9d9")
        eyeL.configure(disabledforeground="#a3a3a3")
        eyeL.configure(foreground="#000000")
        eyeL.configure(text='''Do you have any pain behind your eyes?''')

        Label4 = tk.Label(Frame1)
        Label4.place(relx=0.071, rely=0.453, height=21, width=157)
        Label4.configure(background="#d9d9d9")
        Label4.configure(disabledforeground="#a3a3a3")
        Label4.configure(foreground="#000000")
        Label4.configure(text='''Do you have any joint pains?''')
        Label4.configure(width=157)

        Label5 = tk.Label(Frame1)
        Label5.place(relx=0.071, rely=0.56, height=21, width=140)
        Label5.configure(background="#d9d9d9")
        Label5.configure(disabledforeground="#a3a3a3")
        Label5.configure(foreground="#000000")
        Label5.configure(text='''Do you have a headache?''')

        #Groups Radiobuttons
        eyeV = tk.StringVar()
        headV = tk.StringVar()
        jointV = tk.StringVar()
        bleedV = tk.StringVar()
        vomitV = tk.StringVar()
        absV = tk.StringVar()

        eyeV.set(None)
        headV.set(None)
        jointV.set(None)
        absV.set(None)
        bleedV.set(None)
        vomitV.set(None)

        radioEyeY = tk.Radiobutton(Frame1,variable=eyeV,value='Has Eye Ache')
        radioEyeY.place(relx=0.513, rely=0.347, relheight=0.067, relwidth=0.081)
        radioEyeY.configure(activebackground="#ececec")
        radioEyeY.configure(activeforeground="#000000")
        radioEyeY.configure(background="#d9d9d9")
        radioEyeY.configure(disabledforeground="#a3a3a3")
        radioEyeY.configure(foreground="#000000")
        radioEyeY.configure(highlightbackground="#d9d9d9")
        radioEyeY.configure(highlightcolor="black")
        radioEyeY.configure(justify='left')
        radioEyeY.configure(text='''Yes''')

        radioEyeN = tk.Radiobutton(Frame1,variable=eyeV,value='No Eye Ache')
        radioEyeN.place(relx=0.619, rely=0.347, relheight=0.067, relwidth=0.078)
        radioEyeN.configure(activebackground="#ececec")
        radioEyeN.configure(activeforeground="#000000")
        radioEyeN.configure(background="#d9d9d9")
        radioEyeN.configure(disabledforeground="#a3a3a3")
        radioEyeN.configure(foreground="#000000")
        radioEyeN.configure(highlightbackground="#d9d9d9")
        radioEyeN.configure(highlightcolor="black")
        radioEyeN.configure(justify='left')
        radioEyeN.configure(text='''No''')

        radioHeadY = tk.Radiobutton(Frame1,variable=headV,value='Has Headache')
        radioHeadY.place(relx=0.513, rely=0.56, relheight=0.067, relwidth=0.081)
        radioHeadY.configure(activebackground="#ececec")
        radioHeadY.configure(activeforeground="#000000")
        radioHeadY.configure(background="#d9d9d9")
        radioHeadY.configure(disabledforeground="#a3a3a3")
        radioHeadY.configure(foreground="#000000")
        radioHeadY.configure(highlightbackground="#d9d9d9")
        radioHeadY.configure(highlightcolor="black")
        radioHeadY.configure(justify='left')
        radioHeadY.configure(text='''Yes''')

        radioJointY = tk.Radiobutton(Frame1,variable=jointV,value='Has Joint Ache')
        radioJointY.place(relx=0.513, rely=0.453, relheight=0.067, relwidth=0.081)
        radioJointY.configure(activebackground="#ececec")
        radioJointY.configure(activeforeground="#000000")
        radioJointY.configure(background="#d9d9d9")
        radioJointY.configure(disabledforeground="#a3a3a3")
        radioJointY.configure(foreground="#000000")
        radioJointY.configure(highlightbackground="#d9d9d9")
        radioJointY.configure(highlightcolor="black")
        radioJointY.configure(justify='left')
        radioJointY.configure(text='''Yes''')

        radioJointN = tk.Radiobutton(Frame1,variable=jointV,value='No Joint Ache')
        radioJointN.place(relx=0.619, rely=0.453, relheight=0.067, relwidth=0.078)
        radioJointN.configure(activebackground="#ececec")
        radioJointN.configure(activeforeground="#000000")
        radioJointN.configure(background="#d9d9d9")
        radioJointN.configure(disabledforeground="#a3a3a3")
        radioJointN.configure(foreground="#000000")
        radioJointN.configure(highlightbackground="#d9d9d9")
        radioJointN.configure(highlightcolor="black")
        radioJointN.configure(justify='left')
        radioJointN.configure(text='''No''')

        radioHeadN = tk.Radiobutton(Frame1,variable=headV,value='No Headache')
        radioHeadN.place(relx=0.619, rely=0.56, relheight=0.067, relwidth=0.078)
        radioHeadN.configure(activebackground="#ececec")
        radioHeadN.configure(activeforeground="#000000")
        radioHeadN.configure(background="#d9d9d9")
        radioHeadN.configure(disabledforeground="#a3a3a3")
        radioHeadN.configure(foreground="#000000")
        radioHeadN.configure(highlightbackground="#d9d9d9")
        radioHeadN.configure(highlightcolor="black")
        radioHeadN.configure(justify='left')
        radioHeadN.configure(text='''No''')

        radioVomitY = tk.Radiobutton(Frame1, variable=vomitV, value='Is Vomitting')
        radioVomitY.place(relx=0.513, rely=0.667, relheight=0.067, relwidth=0.081)
        radioVomitY.configure(activebackground="#ececec")
        radioVomitY.configure(activeforeground="#000000")
        radioVomitY.configure(background="#d9d9d9")
        radioVomitY.configure(disabledforeground="#a3a3a3")
        radioVomitY.configure(foreground="#000000")
        radioVomitY.configure(highlightbackground="#d9d9d9")
        radioVomitY.configure(highlightcolor="black")
        radioVomitY.configure(justify='left')
        radioVomitY.configure(text='''Yes''')

        radioVomitN = tk.Radiobutton(Frame1, variable=vomitV, value='Not Vomitting')
        radioVomitN.place(relx=0.619, rely=0.667, relheight=0.067, relwidth=0.078)
        radioVomitN.configure(activebackground="#ececec")
        radioVomitN.configure(activeforeground="#000000")
        radioVomitN.configure(background="#d9d9d9")
        radioVomitN.configure(disabledforeground="#a3a3a3")
        radioVomitN.configure(foreground="#000000")
        radioVomitN.configure(highlightbackground="#d9d9d9")
        radioVomitN.configure(highlightcolor="black")
        radioVomitN.configure(justify='left')
        radioVomitN.configure(text='''No''')

        radioAbsY = tk.Radiobutton(Frame1, variable=absV, value="Has Abdominal Pain")
        radioAbsY.place(relx=0.513, rely=0.747, relheight=0.067, relwidth=0.081)
        radioAbsY.configure(activebackground="#ececec")
        radioAbsY.configure(activeforeground="#000000")
        radioAbsY.configure(background="#d9d9d9")
        radioAbsY.configure(disabledforeground="#a3a3a3")
        radioAbsY.configure(foreground="#000000")
        radioAbsY.configure(highlightbackground="#d9d9d9")
        radioAbsY.configure(highlightcolor="black")
        radioAbsY.configure(justify='left')
        radioAbsY.configure(text='''Yes''')

        radioBleedY = tk.Radiobutton(Frame1, variable=bleedV, value="Rashes On Skin")
        radioBleedY.place(relx=0.513, rely=0.827, relheight=0.067, relwidth=0.081)
        radioBleedY.configure(activebackground="#ececec")
        radioBleedY.configure(activeforeground="#000000")
        radioBleedY.configure(background="#d9d9d9")
        radioBleedY.configure(disabledforeground="#a3a3a3")
        radioBleedY.configure(foreground="#000000")
        radioBleedY.configure(highlightbackground="#d9d9d9")
        radioBleedY.configure(highlightcolor="black")
        radioBleedY.configure(justify='left')
        radioBleedY.configure(text='''Yes''')

        radioAbsN = tk.Radiobutton(Frame1, variable=absV, value="No Abdominal Pain")
        radioAbsN.place(relx=0.619, rely=0.747, relheight=0.067, relwidth=0.078)
        radioAbsN.configure(activebackground="#ececec")
        radioAbsN.configure(activeforeground="#000000")
        radioAbsN.configure(background="#d9d9d9")
        radioAbsN.configure(disabledforeground="#a3a3a3")
        radioAbsN.configure(foreground="#000000")
        radioAbsN.configure(highlightbackground="#d9d9d9")
        radioAbsN.configure(highlightcolor="black")
        radioAbsN.configure(justify='left')
        radioAbsN.configure(text='''No''')


        radioBleedN = tk.Radiobutton(Frame1, variable=bleedV, value="No Rashes On Skin")
        radioBleedN.place(relx=0.619, rely=0.827, relheight=0.067, relwidth=0.078)
        radioBleedN.configure(activebackground="#ececec")
        radioBleedN.configure(activeforeground="#000000")
        radioBleedN.configure(background="#d9d9d9")
        radioBleedN.configure(disabledforeground="#a3a3a3")
        radioBleedN.configure(foreground="#000000")
        radioBleedN.configure(highlightbackground="#d9d9d9")
        radioBleedN.configure(highlightcolor="black")
        radioBleedN.configure(justify='left')
        radioBleedN.configure(text='''No''')


        Label1 = tk.Label(top)
        Label1.place(relx=-0.083, rely=0.022, height=43, width=724)
        Label1.configure(background="#d9d9d9")
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font=font9)
        Label1.configure(foreground="#000000")
        Label1.configure(text='''DENGUE DETECTION EXPERT SYSTEM''')
        Label1.configure(width=724)

        realtemp = tempText_10 = tk.Entry(Frame1)
        tempText_10.place(relx=0.566, rely=0.24, height=20, relwidth=0.131)
        tempText_10.configure(background="white")
        tempText_10.configure(disabledbackground="#f0f0f0f0f0f0")
        tempText_10.configure(disabledforeground="#a3a3a3")
        tempText_10.configure(font="TkFixedFont")
        tempText_10.configure(foreground="#000000")
        tempText_10.configure(highlightbackground="#d9d9d9")
        tempText_10.configure(highlightcolor="black")
        tempText_10.configure(insertbackground="black")
        tempText_10.configure(selectbackground="#c4c4c4")
        tempText_10.configure(selectforeground="black")
        tempText_10.configure(state='readonly')


        Label5_1 = tk.Label(Frame1)
        Label5_1.place(relx=0.053, rely=0.667, height=21, width=250)
        Label5_1.configure(activebackground="#f9f9f9")
        Label5_1.configure(activeforeground="black")
        Label5_1.configure(background="#d9d9d9")
        Label5_1.configure(disabledforeground="#a3a3a3")
        Label5_1.configure(foreground="#000000")
        Label5_1.configure(highlightbackground="#d9d9d9")
        Label5_1.configure(highlightcolor="black")
        Label5_1.configure(text='''Have you experienced persistent vomitting?''')
        Label5_1.configure(width=250)

        Label5_2 = tk.Label(Frame1)
        Label5_2.place(relx=0.053, rely=0.747, height=21, width=200)
        Label5_2.configure(activebackground="#f9f9f9")
        Label5_2.configure(activeforeground="black")
        Label5_2.configure(background="#d9d9d9")
        Label5_2.configure(disabledforeground="#a3a3a3")
        Label5_2.configure(foreground="#000000")
        Label5_2.configure(highlightbackground="#d9d9d9")
        Label5_2.configure(highlightcolor="black")
        Label5_2.configure(text='''Do you have any abdominal pain?''')
        Label5_2.configure(width=200)

        Label5_3 = tk.Label(Frame1)
        Label5_3.place(relx=0.060, rely=0.827, height=21, width=170)
        Label5_3.configure(activebackground="#f9f9f9")
        Label5_3.configure(activeforeground="black")
        Label5_3.configure(background="#d9d9d9")
        Label5_3.configure(disabledforeground="#a3a3a3")
        Label5_3.configure(foreground="#000000")
        Label5_3.configure(highlightbackground="#d9d9d9")
        Label5_3.configure(highlightcolor="black")
        Label5_3.configure(text='''Are there rashes on your skin?''')
        Label5_3.configure(width=170)

        country = []
        country = ['Jamaica','Cuba','America','Canada','England']
        global countvar
        countvar = tk.StringVar()
       # countvar.set("Jamaica")

        global menu
        menu = tk.OptionMenu(Frame1,countvar,*country)

        menu.place(relx=0.560, rely=0.9, relheight=0.047, relwidth=0.101,width="40")
        menu.configure(background="#d9d9d9")
        menu.configure(font="TkFixedFont")
        menu.configure(foreground="#000000")

        realcountry= countrytext = tk.Entry(Frame1)
        countrytext.place(relx=0.413, rely=0.9, relheight=0.047, relwidth=0.101,width="40")
        countrytext.configure(background="white")
        countrytext.configure(disabledforeground="#a3a3a3")
        countrytext.configure(font="TkFixedFont")
        countrytext.configure(foreground="#000000")
        countrytext.configure(insertbackground="black")

        countryL = tk.Label(Frame1)
        countryL.place(relx=0.060, rely=0.890, height=21, width=170)
        countryL.configure(background="#d9d9d9")
        countryL.configure(disabledforeground="#a3a3a3")
        countryL.configure(foreground="#000000")
        countryL.configure(text='''What country are you from?''')

        submitBtn = tk.Button(Frame1,text='Submit',command = check_null)
        submitBtn.place(relx=0.803, rely=0.883, height=24, width=79)
        submitBtn.configure(activebackground="Red")
        submitBtn.configure(activeforeground="#000000")
        submitBtn.configure(background="Red")
        submitBtn.configure(disabledforeground="#a3a3a3")
        submitBtn.configure(foreground="#000000")
        submitBtn.configure(font="Bold")
        submitBtn.configure(highlightbackground="#d9d9d9")
        submitBtn.configure(highlightcolor="black")
        submitBtn.configure(pady="0")


class menuWindow:
    def start_menu(self):
        top = tk.Tk()


        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("300x175+391+84")
        top.title("MOH Dengue Agent")
        top.configure(background="#d9d9d9")

        Frame2 = tk.Frame(top)
        Frame2.place(relx=0.033, rely=0.089, relheight=0.833, relwidth=0.942)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief='groove')
        Frame2.configure(background="#d9d9d9")
        Frame2.configure(width=565)

        submitBtn2 = tk.Button(Frame2, text='Diagnose Patient',command=vp_start_gui)
        submitBtn2.place(relx=0.04, rely=0.07, height=24, width=100)
        submitBtn2.configure(activebackground="#ececec")
        submitBtn2.configure(background="#d9d9d9")
        submitBtn2.configure(disabledforeground="#a3a3a3")
        submitBtn2.configure(foreground="#000000")
        submitBtn2.configure(highlightbackground="#d9d9d9")
        submitBtn2.configure(highlightcolor="black")
        submitBtn2.configure(pady="0")

        submitBtn2 = tk.Button(Frame2, text='Exit Program', command=exit)
        submitBtn2.place(relx=0.51, rely=0.07, height=24, width=100)
        submitBtn2.configure(activebackground="#ececec")
        submitBtn2.configure(background="#d9d9d9")
        submitBtn2.configure(disabledforeground="#a3a3a3")
        submitBtn2.configure(foreground="#000000")
        submitBtn2.configure(highlightbackground="#d9d9d9")
        submitBtn2.configure(highlightcolor="black")
        submitBtn2.configure(pady="0")


        top.mainloop()


class diagWindow:
    def __init__(self,top):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Light} -size 11 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Light} -size 12 -weight bold " \
        "-slant roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI Historic} -size 10 -weight normal " \
        "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Eras Demi ITC} -size 22 -weight normal " \
        "-slant italic -underline 0 -overstrike 0"
        top.geometry("600x450+397+119")
        top.title("Patient Diagnosis")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.diagnosis = tk.Label(top)
        self.diagnosis.place(relx=0.083, rely=0.244, height=21, width=194)
        self.diagnosis.configure(activebackground="#f9f9f9")
        self.diagnosis.configure(activeforeground="black")
        self.diagnosis.configure(background="#d9d9d9")
        self.diagnosis.configure(disabledforeground="#a3a3a3")
        self.diagnosis.configure(font=font10)
        self.diagnosis.configure(foreground="#000000")
        self.diagnosis.configure(highlightbackground="#d9d9d9")
        self.diagnosis.configure(highlightcolor="#000000")
        self.diagnosis.configure(text='''Patient has severe Dengue''')
        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=-0.017, rely=0.044, height=43, width=634)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''DENGUE DETECTION EXPERT SYSTEM''')
        self.Label1_2.configure(width=634)
        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.067, rely=0.444, height=21, width=254)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font11)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''The Expert System Recommends''')
        self.Label1_3.configure(width=254)
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.083, rely=0.556, height=23, width=207)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''1)   avoid medicines with aspirin''')
        self.Label2.configure(width=207)
        self.Label2_4 = tk.Label(top)
        self.Label2_4.place(relx=0.067, rely=0.644, height=23, width=287)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#d9d9d9")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font12)
        self.Label2_4.configure(foreground="#000000")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''2)   use pain relievers with acetaminophen''')
        self.Label2_4.configure(width=287)
        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.067, rely=0.733, height=23, width=157)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font12)
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''3)   see your doctor''')
        self.Label2_5.configure(width=157)


class diagregWindow:
    def __init__(self,top):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Light} -size 11 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Light} -size 12 -weight bold " \
        "-slant roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI Historic} -size 10 -weight normal " \
        "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Eras Demi ITC} -size 22 -weight normal " \
        "-slant italic -underline 0 -overstrike 0"

        top.geometry("600x450+397+119")
        top.title("Patient Diagnosis")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.diagnosis = tk.Label(top)
        self.diagnosis.place(relx=0.083, rely=0.244, height=21, width=194)
        self.diagnosis.configure(activebackground="#f9f9f9")
        self.diagnosis.configure(activeforeground="black")
        self.diagnosis.configure(background="#d9d9d9")
        self.diagnosis.configure(disabledforeground="#a3a3a3")
        self.diagnosis.configure(font=font10)
        self.diagnosis.configure(foreground="#000000")
        self.diagnosis.configure(highlightbackground="#d9d9d9")
        self.diagnosis.configure(highlightcolor="#000000")
        self.diagnosis.configure(text='''Patient has regular Dengue''')

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=-0.017, rely=0.044, height=43, width=634)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''DENGUE DETECTION EXPERT SYSTEM''')
        self.Label1_2.configure(width=634)

        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.067, rely=0.444, height=21, width=254)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font11)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''The Expert System Recommends''')
        self.Label1_3.configure(width=254)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.067, rely=0.556, height=23, width=207)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''1)   drink plenty of fluids''')
        self.Label2.configure(width=207)

        self.Label2_4 = tk.Label(top)
        self.Label2_4.place(relx=0.067, rely=0.644, height=23, width=287)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#d9d9d9")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font12)
        self.Label2_4.configure(foreground="#000000")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''2)   use pain relievers with acetaminophen''')
        self.Label2_4.configure(width=287)

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.067, rely=0.733, height=23, width=157)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font12)
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''3)   get adequate rest''')
        self.Label2_5.configure(width=157)


class nodengueWindow:
    def __init__(self,top):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Light} -size 11 -weight bold " \
        "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI Light} -size 12 -weight bold " \
        "-slant roman -underline 1 -overstrike 0"
        font12 = "-family {Segoe UI Historic} -size 10 -weight normal " \
        "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Eras Demi ITC} -size 22 -weight normal " \
        "-slant italic -underline 0 -overstrike 0"
        top.geometry("600x450+397+119")
        top.title("Patient Diagnosis")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.diagnosis = tk.Label(top)
        self.diagnosis.place(relx=0.083, rely=0.244, height=21, width=294)
        self.diagnosis.configure(activebackground="#f9f9f9")
        self.diagnosis.configure(activeforeground="black")
        self.diagnosis.configure(background="#d9d9d9")
        self.diagnosis.configure(disabledforeground="#a3a3a3")
        self.diagnosis.configure(font=font10)
        self.diagnosis.configure(foreground="#000000")
        self.diagnosis.configure(highlightbackground="#d9d9d9")
        self.diagnosis.configure(highlightcolor="#000000")
        self.diagnosis.configure(text='''Patient does not have Dengue''')
        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=-0.017, rely=0.044, height=43, width=634)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font9)
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''DENGUE DETECTION EXPERT SYSTEM''')
        self.Label1_2.configure(width=634)
        self.Label1_3 = tk.Label(top)
        self.Label1_3.place(relx=0.067, rely=0.444, height=21, width=254)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#d9d9d9")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font11)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''The Expert System Recommends''')
        self.Label1_3.configure(width=254)
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.083, rely=0.556, height=23, width=207)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''1)   get some rest''')
        self.Label2.configure(width=207)


main1 = menuWindow()
main1.start_menu()