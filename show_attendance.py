
from tkinter import *
import new_attendance
from tkinter import filedialog




def main():
    root = Tk()
    root.title(" Attendance System")
    root.geometry("550x550")
    root.config(bg="#292626")



    def open():
        root.filename = filedialog.askopenfilename(initialdir="G:\ attendance system", title="Select file",
                                                     filetypes=(("xlsx  files", "*.xlsx "), ("all files", "*.*")))

    Label(root,text="_______________________________________________________________________________________________________________________________________________________________________________________",
                           width=80, font=("bold", 10), bg="#25f55c", fg="#25f55c").place(x=0,y=120)

    Label(root, text="Click Button below to open record!!", font=("bold", 14), bg="#fc5f53",fg="white").place(x=120,y=200)

    Button(root,text="Click Here",width=10,command=open,fg='blue',bg='#e0dfde',borderwidth=4).place(x=220,y=240)

    Label(root,text="_______________________________________________________________________________________________________________________________________________________________________________________",
                           width=80, font=("bold", 10), bg="#25f55c", fg="#25f55c").place(x=0,y=300)



    def exit(event):
        root.destroy()
    root.bind("<Return>",exit)


    # to go back to main Page.
    def goback():
        root.destroy()
        new_attendance.main()


    mybutton1 = Button(root, text="Main Page", fg='blue', width=12, command=goback, bg='#e0dfde',borderwidth=4)
    mybutton1.place(x=200, y=380)
    root.mainloop()
    root.mainloop()
if __name__ == '__main__':
    main()






