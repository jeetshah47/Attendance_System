
import show_attendance
import take_attend
import student_entry
import student_list
from tkinter import *
import tkinter.font as tkFont

def main():
   root = Tk()
   root.title("Attendance System")
   root.geometry("650x550")
   root.config(bg="#292626")

   def destroy():
      root.destroy()

   #Funtion to call  script(.py) name take_attend
   def attend():
      destroy()
      take_attend.main()

   # Funtion to call  script(.py) name student_entry
   def form():
      destroy()
      student_entry.main()

   # Funtion to call script (.py) name student_list
   def stud_list(event):
      destroy()
      student_list.main()
   root.bind("<KeyPress-1>",stud_list)


   # Funtion to call script (.py) name show_attendance
   def show_attend():
      destroy()
      show_attendance.main()


   title_font = tkFont.Font(family="Lucida Sans Unicode", size=20,weight="normal")
   title = Label(root, text="ATTENDANCE SYSTEM ", bg="#e30b4c", font=title_font,fg='white')
   title.place(x=180, y=60)

   label_5 = Label(root, text="1.List of Student", width=16, bg="#F55555", font=("bold", 12),fg='white')
   label_5.place(x=60, y=180)
   button_5 = Button(root, text="Open", width=8, command= lambda : stud_list(""), bg='#e0dfde', fg="#1a2cf0",borderwidth=4)
   button_5.place(x=220, y=180)

   label_6 = Label(root, text="2.Enter New Student", width=16, bg="#F55555", font=("bold", 12),fg='white')
   label_6.place(x=330, y=180)
   button_6 = Button(root, text="Open", width=8, command=form, bg='#e0dfde', fg="#1a2cf0",borderwidth=4)
   button_6.place(x=490, y=180)

   label_7 = Label(root, text="3.Take Attendance", width=16, bg="#F55555", font=("bold", 12),fg='white')
   label_7.place(x=60, y=230)
   button_7 = Button(root, text="Open", width=8, command=attend, bg='#e0dfde', fg="#1a2cf0",borderwidth=4)
   button_7.place(x=220, y=230)

   label_8 = Label(root, text="4.Show Attendance", width=16, bg="#F55555", font=("bold", 12),fg='white')
   label_8.place(x=330, y=230)
   button_8 = Button(root, text="Open", width=8, command=show_attend, bg='#e0dfde', fg="#1a2cf0",borderwidth=4)
   button_8.place(x=490, y=230)

   label_9 = Label(root,
                   text="_______________________________________________________________________________________________________________________________________________________________________________________",
                   width=80,height=4, font=("bold", 10), bg="#25f55c", fg="#25f55c")
   label_9.place(x=0, y=360)

   devloper_font=tkFont.Font(family="Consolas",size=14,weight="normal")
   Devloper_info=Label(root,text="Developed By ~ Pruthvi S. Patel",font=devloper_font,fg='red').place(x=160,y=380)


   root.mainloop()
if __name__ == '__main__':
    main()



