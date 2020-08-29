from tkinter import *
import new_attendance






def main():
    root = Tk()
    root.title("Attendance System")
    root.geometry('650x500')
    root.config(bg="#292626")

    stud_list_title = Label(root, text="List of Student", width=20, font=("bold", 20), bg="#e30b4c",fg="white")
    stud_list_title.place(x=140, y=40)

    stud_list_line = Label(root,
                           text="_______________________________________________________________________________________________________________________________________________________________________________________",
                           width=80, font=("bold", 10), bg="#25f55c", fg="#25f55c")
    stud_list_line.place(x=0, y=100)






    stud_name = ["First name", " Last name ", " ID.No "]
    # Use of ITERATOR

   #To read from .txt File
    f1 = open('data_store/first_name.txt', 'r')
    f_name = f1.readlines()

    f1.close()
    f2 = open('data_store/last_name.txt', 'r')
    l_name = f2.readlines()
    f2.close()

    f3 = open('data_store/id.txt', 'r')
    id = f3.readlines()
    f3.close()


    #To Display the data from .txt file
    def data():

        val1 = iter(stud_name)
        a = 0
        r = 0

        while val1:

            try:

                head = next(val1)
                Label(frame, text=head, font=('Arial', 12), fg='black',bg="#d06ad4").grid(row=0, column=a + 1)
                a += 1
                r += 1

            except StopIteration:
                break

        for i in range(len(f_name)):
            Label(frame, text=f_name[i], font=('Arial', 12),bg="#d06ad4").grid(row=i+1 , column=1)
            Label(frame, text=l_name[i], font=('Arial', 12),bg="#d06ad4").grid(row=i+1 , column=2)
            Label(frame, text=id[i], font=('Arial', 12),bg="#d06ad4").grid(row=i+1 , column=3)



    def scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=300, height=300,bg="#d06ad4")



    #To set scroll bar
    myframe = Frame(root, relief=GROOVE, width=50, height=100, bd=1)
    myframe.place(x=140, y=160)

    canvas = Canvas(myframe)
    frame = Frame(canvas,bg='#d06ad4')
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')

    frame.bind("<Configure>", scroll)

    data()

    # to go back to main Page.
    def goback():
        root.destroy()
        new_attendance.main()

    mybutton1 = Button(root, text="Main Page", fg='blue', width=10, command=goback, bg='#e0dfde',borderwidth=4)
    mybutton1.place(x=240, y=470)

    root.mainloop()

if __name__ == "__main__":
    main()


