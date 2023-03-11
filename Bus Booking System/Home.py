from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun1():
    root.destroy()
    import Bus_Booking
def fun2():
    root.destroy()
    import Check_Booking
def fun3():
    root.destroy()
    import Add_Bus_Detail
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=1)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=1)
Label(root,text='').grid(row=2,column=1)
Label(root,text='').grid(row=3,column=1)
Button(root,text='Seat Booking',bg='green2',font='Arial 15',command=fun1).grid(row=4,column=0,padx=(350,100))
Button(root,text='Check Booked Seat', bg='green3',font='Arial 15',command=fun2).grid(row=4,column=1,padx=100)
Button(root,text='Add Bus Details', bg='green4',font='Arial 15',command=fun3).grid(row=4,column=3,padx=100)
Label(root,text='').grid(row=5,column=1)
Label(root,text='For admin only',fg='red').grid(row=6,column=3)
