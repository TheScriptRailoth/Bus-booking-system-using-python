from tkinter import*
root=Tk()
root.geometry('1366x768')
img=PhotoImage(file='.\\Bus_for_project.png')
def close(e=0):
    root.destroy()
    import Home
Label(root,image=img).  pack()
Label(root,text="Online Bus Booking System",font='Arial 25 bold',bg='light blue',fg='Red').pack()
Label(root,text="").pack()
Label(root,text="Name : Ashutosh Mishra", font='Arial 13 bold',fg='Blue').pack()
Label(root,text="").pack()
Label(root,text="Enrollment Number: 211B073", font='Arial 13 bold',fg='Blue').pack()
Label(root,text="").pack()
Label(root,text="Mobile: 8423979654", font='Arial 13 bold',fg='Blue').pack()
Label(root,text="").pack()
Label(root,text="Submitted To: Dr. Mahesh Kumar", font='Arial 13 bold',bg='sky blue',fg='red').pack()
Label(root,text="Project Based Learning", font='Arial 9 bold',fg='red').pack()
root.bind('<KeyPress>',close)

