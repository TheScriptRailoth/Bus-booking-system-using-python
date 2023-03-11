from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun1():
    root.destroy()
    import Add_Operator
def fun2():
    root.destroy()
    import Add_new_Bus
def fun3():
    root.destroy()
    import Add_New_Route
def fun4():
    root.destroy()
    import newrun
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=4,padx=(400,0),pady=10)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=4,padx=(400,0))
Label(root,text='Add New Details to DataBase',font='Arial 14 bold',fg='green4').grid(row=2,column=0,columnspan=4,padx=(400,0),pady=20)
Button(root,text='New Operator',bg='SpringGreen2', font='Arial 10',command=fun1).grid(row=3,column=0,padx=(400,50))
Button(root,text='New Bus',bg='orange red',font='Arial 10',command=fun2).grid(row=3,column=1,padx=60)
Button(root,text='New Route',bg='DodgerBlue3',font='Arial 10', command=fun3).grid(row=3,column=2,padx=60)
Button(root,text='New Run',bg='pink4',font='Arial 10',command=fun4).grid(row=3,column=3,padx=60)
