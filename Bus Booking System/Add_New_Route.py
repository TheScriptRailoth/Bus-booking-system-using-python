from tkinter import *
from tkinter.messagebox import*
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun1():
    if len(rid.get())==0 or len(station.get())==0 or len(sid.get())==0:
        showerror('Value Missing','Enter Detail')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
            cur=con.cursor()
            cur.execute("""insert into Route(Route_Id, S_Id, Sname)values({},{},'{}')""".format(rid.get(),sid.get(),station.get()))
            con.commit()
            con.close()
            showinfo('Action Completed','Route Added Successfully')
        except(mysql.connector.errors.IntegrityError):
            showerror('Error','Record Already Exists')
        except(ValueError):
            showerror('Error','Enter Valid Input')
def fun2():
    if len(rid.get())==0 or len(station.get())==0 or len(sid.get())==0:
        showerror('Value Missing','Enter Detail')
    else:
        con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
        cur=con.cursor()
        cur.execute('delete from Route where Route_Id={} and S_Id={} and SName="{}"'.format(rid.get(),sid.get(),station.get()))
        con.commit()
        con.close()
        showinfo('Action Completed','Route Deleted Successfully')
def fun():
    root.destroy()
    import Home
    
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
Label(root,image=img).grid(row=0,column=1,columnspan=11,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=1,columnspan=11)
Label(root,text='Add Bus Route Details',font='Arial 14 bold',fg='green4').grid(row=2,column=1,columnspan=11,pady=20)
Label(root,text='Route Id').grid(row=4,column=0,padx=(250,0),pady=40)
rid=Entry(root)
rid.grid(row=4,column=1,padx=10)

Label(root,text='Station Name').grid(row=4,column=2)
station=Entry(root)
station.grid(row=4,column=3,padx=10)

Label(root,text='Station Id').grid(row=4,column=4)
sid=Entry(root)
sid.grid(row=4,column=5,padx=10)

Label(root,text='').grid(row=4,column=6)
Label(root,text='').grid(row=4,column=7,padx=10)
Label(root,text='').grid(row=4,column=8)
Label(root,text='').grid(row=4,column=9,padx=10)
Button(root,text='Add Route',bg='SpringGreen2',command=fun1).grid(row=4,column=10)
Button(root,text='Delete Route',bg='SpringGreen2',fg='red',command=fun2).grid(row=4,column=11,padx=10)
Button(root,image=home,command=fun).grid(row=5,column=8)
