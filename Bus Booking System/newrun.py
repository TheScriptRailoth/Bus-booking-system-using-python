from tkinter import *
from tkinter.messagebox import*
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
def fun1():
    if len(bid.get())==0 or len(rdate.get())==0 or len(seat.get())==0:
        showerror('Value Missing','Please Enter Details')
    else:
        try:
            con=mysql.connector.connect(user='root',host='localhost',password='1234',database='python_bus')
            cur=con.cursor()
            cur.execute('insert into Runs(Bus_Id,Date,Seat_Available)values({},"{}",{})'.format(int(bid.get()),rdate.get(),int(seat.get())))
            con.commit()
            con.close()
            showinfo('Task Completed','Details Added Successfully')
        except(mysql.connector.errors.IntegrityError):
            showerror('Error','Record Already Exists')
        except(ValueError):
            showerror('Error','Enter Valid Input')

def fun2():
    if len(bid.get())==0 or len(rdate.get())==0 or len(seat.get())==0:
        showerror('Value Missing','Please Enter Details')
    else:
        con=mysql.connector.connect(user='root',host='localhost',password='1234',database='python_bus')
        cur=con.cursor()
        cur.execute('delete from Runs where Bus_Id={} and Date="{}" and Seat_Available={}'.format(int(bid.get()),rdate.get(),int(seat.get())))
        con.commit()
        con.close()
        showinfo('Task Completed','Details Deleted Successfully')
        
def home_fun():
    root.destroy()
    import Home
    
home=PhotoImage(file='home.png')
Label(root,image=img).grid(row=0,column=1,columnspan=11,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=1,columnspan=11)
Label(root,text='Add Bus Running Details',font='Arial 14 bold',fg='green4').grid(row=2,column=1,columnspan=11,pady=20)

Label(root,text='Bus Id').grid(row=4,column=0,padx=(350,0),pady=40)
bid=Entry(root)
bid.grid(row=4,column=1,padx=10)

Label(root,text='Running Date').grid(row=4,column=2)
rdate=Entry(root)
rdate.grid(row=4,column=3,padx=10)

Label(root,text='Seat Available').grid(row=4,column=4)
seat=Entry(root)
seat.grid(row=4,column=5,padx=10)

Button(root,text='Add Run',bg='SpringGreen2',command=fun1).grid(row=4,column=6)
Button(root,text='Delete Run',bg='SpringGreen2',command=fun2).grid(row=4,column=7,padx=10)
Button(root,image=home,command=home_fun).grid(row=5,column=6)
