from tkinter import *

import new_attendance
import xlsxwriter


def main():
    root = Tk()
    root.title("Attendance System")
    root.geometry("650x650")
    root.config(bg="#292626")
    global var6
    var6 = StringVar()


    #To Store Data in Excle (.xlxs) File
    def add_excle():#


        w1 = var1.get()
        w2 = var2.get()
        w3 = var3.get()
        w4 = var4.get()
        w5 = var5.get()
        w6 = ''
        if len(var6.get()) != 0:
            w6 = var6.get()

        date = entry_2.get()
        filename_1 = "attendance " + date
        extension = ".xlsx"
        filename_2 = filename_1 + extension
        workbook = xlsxwriter.Workbook(filename_2)


        worksheet = workbook.add_worksheet(date)
        if w6 == '':
            record = (
                ["P/A(With Name)", "Date"],
                [w1, date],
                [w2, date],
                [w3, date],
                [w4, date],
                [w5, date],

            )
        else:
            record = (
                ["P/A(With Name)", "Date"],
                [w1, date],
                [w2, date],
                [w3, date],
                [w4, date],
                [w5, date],
                [w6, date],
            )
        row = 0
        col = 0
        for pa, date in (record):
            worksheet.write(row, col, pa)
            worksheet.write(row, col + 1, date)
            row += 1

        Label(root, text="Attendance is been downloaded!!", fg="Red", font=("bold", 12)).place(x=40, y=540)

        workbook.close()


    #Show the attendance summary after the attendance is taken.
    def show():
        root = Tk()
        root.title("Attendance System")
        root.geometry("650x650")
        root.config(bg="#292626")

        attend_summary = Label(root, text="Attendance Summary", font=("italic", 30), bg="#e30b4c", fg="white")
        attend_summary.place(x=130, y=50)

        attendsum_line = Label(root,
                               text="_______________________________________________________________________________________________________________________________________________________________________________________",
                               width=80, font=("bold", 10), bg="#81f046", fg="#81f046")
        attendsum_line.place(x=0, y=120)

        mylable1 = Label(root, text=var1.get(), font=("bold", 16), bg="#faf8a2", width=25)
        mylable1.place(x=190, y=200)

        mylable2 = Label(root, text=var2.get(), font=("bold", 16), bg="#f7da8f", width=25)
        mylable2.place(x=190, y=240)

        mylable3 = Label(root, text=var3.get(), font=("bold", 16), bg="#faf8a2", width=25)
        mylable3.place(x=190, y=280)

        mylable4 = Label(root, text=var4.get(), font=("bold", 16), bg="#f7da8f", width=25)
        mylable4.place(x=190, y=320)

        mylable5 = Label(root, text=var5.get(), font=("bold", 16), bg="#faf8a2", width=25)
        mylable5.place(x=190, y=360)
        global var6
        if len(var6.get()) !=0 :
            mylable6 = Label(root, text=var6.get(), font=("bold", 16), bg="#faf8a2", width=25)
            mylable6.place(x=190, y=400)


    #Dynamically add checkbutton
    def add_obj():
        global create


        global var6
        var6 = StringVar()

        create=Checkbutton(root, text=entry_1.get(), bg="#e19ef0",variable=var6,
                                 onvalue=entry_1.get() + " is present", offvalue=entry_1.get() + " is absent", width=25,
                                 font=("bold", 12))
        create.deselect()
        create.place(x=180, y=400 )

    attend_line = Label(root,
                        text="_______________________________________________________________________________________________________________________________________________________________________________________",
                        width=80,height=3, font=("bold", 10), bg="#25f55c", fg="#25f55c")
    attend_line.place(x=0, y=20)

    attend_title = Label(root, text="Attendance list", font=('bold', 20), width=15,fg="white",bg="#e30b4c")
    attend_title.place(x=200, y=30)


    name_label = Label(root, text="Name:", font=('bold', 12), fg="white", bg="#292626").place(x=0, y=130)
    entry_1 = Entry(root, width=22,bg="#ebe4d1") #To take value to create dynamic check button
    entry_1.place(x=58, y=135)
    entry_1.insert(0, 'Sr.no and Name')

    b1 = Button(root, text='Add', width=8,borderwidth=3, fg='blue', command=add_obj) #This Button call the add_obj function to create dynamic checkbutton
    b1.place(x=200, y=130)


    #To mention date.
    date_label = Label(root, text="Date:", font=('bold', 12), fg="white",bg="#292626").place(x=470, y=125)
    entry_2 = Entry(root, width=18,bg="#ebe4d1")
    entry_2.place(x=520, y=125)
    entry_2.insert(0, 'dd/mm/yyyy')

    Label(root,text="*Date is complusory",font=("Bold",8),fg="red").place(x=488,y=155)


    #Static way to create button.
    var1 = StringVar()
    c1 = Checkbutton(root, text="1.Anisha Patel", bg="#e19ef0", variable=var1,
                     onvalue="1.Anisha is present", offvalue="1.Anisha is absent", width=25,
                     font=("bold", 12))
    c1.deselect()
    c1.place(x=180, y=200)

    var2 = StringVar()
    c2 = Checkbutton(root, text="2.Aseem Shah", bg="#e19ef0", variable=var2, onvalue="2.Aseem Shah is present",
                     offvalue="2.Aseem Shah is absent", width=25, font=("bold", 12))
    c2.deselect()
    c2.place(x=180, y=240)

    var3 = StringVar()
    c3 = Checkbutton(root, text="3.Ishaan Agrawal", bg="#e19ef0", variable=var3, onvalue="3.Ishaan Agrawal is present",
                     offvalue="3.Ishaan Agrawal is absent", width=25, font=("bold", 12))
    c3.deselect()
    c3.place(x=180, y=280)

    var4 = StringVar()
    c4 = Checkbutton(root, text="4.Jason Panchal", bg="#e19ef0", variable=var4, onvalue="4.Jason Panchal is present",
                     offvalue="4.Jason Panchal is absent", width=25, font=("bold", 12))
    c4.deselect()
    c4.place(x=180, y=320)

    var5 = StringVar()
    c5 = Checkbutton(root, text="5.Suresh Parmar", bg="#e19ef0", variable=var5, onvalue="5.Suresh Parmar is present",
                     offvalue="5.Suresh Parmar is absent", width=25, font=("bold", 12))
    c5.deselect()
    c5.place(x=180, y=360)

    note = Label(root, text="Note- For now we can add only 1 student at time", bg="#f27168", width=50,
                 font=("bold", 16))
    note.place(x=20, y=600)

    mybutton = Button(root, text="Submit", fg='blue', width=15, command=show, bg='#e0dfde',borderwidth=4)
    mybutton.place(x=260, y=500)

    add_button = Button(root, text=" Get Attendance", fg='blue', width=15, command=add_excle, bg='#e0dfde',borderwidth=4)
    add_button.place(x=120, y=500)

    dc = StringVar()
    Label(root, text="enter name")

    #to go back to main Page.
    def goback():
        root.destroy()
        new_attendance.main()

    mybutton1 = Button(root, text="Main Page", fg='blue', width=15, command=goback, bg='#e0dfde',borderwidth=4)
    mybutton1.place(x=400, y=500)
    root.mainloop()


if __name__ == "__main__":
    main()

