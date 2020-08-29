
from tkinter import *
import new_attendance



def main():
    root = Tk()
    root.title("Attendance System")
    root.geometry("650x650")
    root.config(bg="#292626")

    #To store data in .txt File
    def add_info():
        f1 = open("data_store/first_name.txt", "a+")
        f_name = entry_2.get()
        f1.write("\n" + f_name)
        f1.close()

        f2 = open("data_store/last_name.txt", "a+")
        l_name = entry_3.get()
        f2.write("\n" + l_name)
        f2.close()

        f3 = open("data_store/id.txt", "a+")
        id_get = entry_4.get()
        f3.write("\n" + id_get)
        f3.close()

        Label(root, text="Data is added!!", font=("Bold", 12), fg="red").place(x=260, y=440)




    label_1 = Label(root, text="Add Student detail", width=20, font=("bold", 20), bg="#e30b4c")
    label_1.place(x=160, y=80)

    form_line = Label(root,
                      text="_______________________________________________________________________________________________________________________________________________________________________________________",
                      width=80, font=("bold", 10), bg="#25f55c",height=3 ,fg="#25f55c")
    form_line.place(x=0, y=480)

    label_2 = Label(root, text="First Name", width=15, font=("bold", 10), bg="#f7da8b")
    label_2.place(x=180, y=200)

    entry_2 = Entry(root,bg="#bdb8ac")
    entry_2.place(x=340, y=200)

    label_3 = Label(root, text="Last Name", width=15, font=("bold", 10), bg="#f7da8b")
    label_3.place(x=180, y=258)

    entry_3 = Entry(root,bg="#bdb8ac")
    entry_3.place(x=340, y=258)

    label_4 = Label(root, text="ID.NO", width=15, font=("bold", 10), bg="#f7da8b")
    label_4.place(x=180, y=310)

    entry_4 = Entry(root,bg="#bdb8ac")
    entry_4.place(x=340, y=310)

    button_1 = Button(root, text="Add", width=10, command=add_info,borderwidth=3, bg="#e0dfde", fg="#1a2cf0")
    button_1.place(x=260, y=400)



    def form_gen():
        # Use of generator
        yield "Note -"
        yield "ID.No should be 4 digit only"


    value = form_gen()

    gen_label1 = Label(root, text=value.__next__(), font=("bold", 16), fg="red",bg="#25f55c")
    gen_label2 = Label(root, text=value.__next__(), font=("bold", 14), fg="red",bg="#25f55c")


    gen_label1.place(x=200, y=490)
    gen_label2.place(x=265, y=490)


    # to go back to main Page.
    def goback():
        root.destroy()
        new_attendance.main()

    mybutton1 = Button(root, text="Main Page", fg='blue', width=15, command=goback, bg='#e0dfde',borderwidth=4)
    mybutton1.place(x=460, y=600)
    root.mainloop()

    root.mainloop()

if __name__ == '__main__':
    main()