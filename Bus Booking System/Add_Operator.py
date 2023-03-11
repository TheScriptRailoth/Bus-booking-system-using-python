from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun():
    if len(opeid.get())==0:
        showerror('Missing Value','Enter the Operator ID')
    elif len(name.get())==0:
        showerror('Missing Value','Enter the Name')
    elif len(address.get())==0:
        showerror('Missing Value','Enter the Address')
    elif len(phone.get())==0:
        showerror('Missing Value','Enter the Phone')
    elif len(email.get())==0:
        showerror('Missing Value','Enter the Email')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
            cur=con.cursor()
            cur.execute("""insert into operator(Op_Id,Name,Address,email,phone) values({},"{}","{}","{}",{})""".format(opeid.get(),name.get(),address.get(),email.get(),phone.get()));
            showinfo('Task Completed','Data Added Successfully')
            con.commit()
            con.close()
            a=opeid.get()
            Label(root,text=a).grid(row=5,column=3,pady=10)
            b=name.get()
            Label(root,text=b).grid(row=5,column=4)
            c=address.get()
            Label(root,text=c).grid(row=5,column=5)
            d=phone.get()
            Label(root,text=d).grid(row=5,column=6)
            e=email.get()
            Label(root,text=e).grid(row=5,column=7)
        except(mysql.connector.errors.IntegrityError):
            showerror('Error','Record Already Exists')
        except(ValueError):
            showerror('Error','Enter Valid Input')        
def fun1():
    if len(opeid.get())==0:
        showerror('Missing Value','Enter the Operator ID')
    elif len(name.get())==0:
        showerror('Missing Value','Enter the Name')
    elif len(address.get())==0:
        showerror('Missing Value','Enter the Address')
    elif len(phone.get())==0:
        showerror('Missing Value','Enter the Phone')
    elif len(email.get())==0:
        showerror('Missing Value','Enter the Email')
    else:
        try:
            a=int(opeid.get())
            Label(root,text=a).grid(row=5,column=4,pady=10)
            b=name.get()
            Label(root,text=b).grid(row=5,column=5)
            c=address.get()
            Label(root,text=c).grid(row=5,column=6)
            d=phone.get()
            Label(root,text=d).grid(row=5,column=7)
            e=email.get()
            Label(root,text=e).grid(row=5,column=8)
            con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
            cur=con.cursor()
            cur.execute("""update Operator SET Name='{}',Address='{}',Email='{}',Phone={} where Op_Id={}""".format(b,c,e,d,a))
            showinfo('Operator Entry Update','Operator details updated succesfully')
            con.commit()
            con.close()
        except(ValueError):
            showerror('Error','Enter Correct Value')
def home_fun():
    root.destroy()
    import Home
         
    
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
Label(root,image=img).grid(row=0,column=1,columnspan=11,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=1,columnspan=11)
Label(root,text='Add Bus Operator Details',font='Arial 14 bold',fg='green4').grid(row=2,column=1,columnspan=11,pady=20)
Label(root,text='Operator Id').grid(row=4,column=0,padx=(250,0),pady=40)
opeid=Entry(root)
opeid.grid(row=4,column=1,padx=10)
Label(root,text='Name').grid(row=4,column=2)
name=Entry(root)
name.grid(row=4,column=3,padx=10)
Label(root,text='Address').grid(row=4,column=4)
address=Entry(root)
address.grid(row=4,column=5,padx=10)
Label(root,text='Phone').grid(row=4,column=6)
phone=Entry(root)
phone.grid(row=4,column=7,padx=10)
Label(root,text='Email').grid(row=4,column=8)
email=Entry(root)
email.grid(row=4,column=9,padx=10)
Button(root,text='Add',bg='SpringGreen2',command=fun).grid(row=4,column=10)
Button(root,text='Edit',bg='SpringGreen2',command=fun1).grid(row=4,column=11,padx=10)
Button(root,image=home,command=home_fun).grid(row=6,column=11)
