from tkinter import *
from tkinter.messagebox import*
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()

def fun():
    root.destroy()
    import Home
def popup():
    if(len(capacity.get())==0 or len(fare.get())==0 or len(operator_id.get())==0 or len(root_id.get())==0):
        showerror('Value Missing',"Please Enter Details")
    elif(bus_type.get()=="Select Bus Type"):
        showerror('Value Missing',"Please Select Bus Type")
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
            cur=con.cursor()
            cur.execute('insert into bus(Bus_Id,Type,Capacity,Fare,Route_Id,Op_Id) values({},"{}",{},{},{},{})'.format(bid.get(),bus_type.get(),capacity.get(),fare.get(),root_id.get(),operator_id.get()))
            con.commit()
            con.close()
            showinfo('Action Completed','New Bus Added Successfully')
        except(mysql.connector.errors.IntegrityError):
            showerror('Error','Record Already Exists')
        except(ValueError):
            showerror('Error','Enter Valid Input')
def fun2():
    if(len(capacity.get())==0 or len(fare.get())==0 or len(operator_id.get())==0 or len(root_id.get())==0):
        showerror('Value Missing',"Please Enter Details")
    elif(bus_type.get()=="Select Bus Type"):
        showerror('Value Missing',"Please Select Bus Type")
    else:
        con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
        cur=con.cursor()
        cur.execute('update bus SET Type="{}",Capacity="{}",Fare={},Route_Id={},Op_Id={} where bus_id={}'.format(bus_type.get(),capacity.get(),fare.get(),root_id.get(),operator_id.get(),bid.get()))
        con.commit()
        con.close()
        showinfo('Action Completed','Bus Detail Updated Successfully')
        
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
Label(root,image=img).grid(row=0,column=1,columnspan=11,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=1,columnspan=11)
Label(root,text='Add Bus Details',font='Arial 14 bold',fg='green4').grid(row=2,column=1,columnspan=11,pady=20)

Label(root,text='Bus ID').grid(row=4,column=0,padx=(150,0),pady=40)
bid=Entry(root)
bid.grid(row=4,column=1,padx=10)

Label(root,text='Bus Type').grid(row=4,column=2)
bus_type=StringVar()
bus_type.set("Select Bus Type")
opt=["2x2","AC 2x2","3x2","AC 3x2"]
d_menu=OptionMenu(root,bus_type,*opt)
d_menu.bg='blue'
d_menu.grid(row=4,column=3)

Label(root,text='Capacity').grid(row=4,column=4)
capacity=Entry(root)
capacity.grid(row=4,column=5,padx=10)

Label(root,text='Fare Rs').grid(row=4,column=6)
fare=Entry(root)
fare.grid(row=4,column=7,padx=10)

Label(root,text='Operator ID').grid(row=4,column=8)
operator_id=Entry(root)
operator_id.grid(row=4,column=9,padx=10)

Label(root,text='Route ID').grid(row=4,column=10)
root_id=Entry(root)
root_id.grid(row=4,column=11,padx=10)

Button(root,text='Add Bus',bg='SpringGreen2',command=popup).grid(row=5,column=6)
Button(root,text='Edit Bus',bg='SpringGreen2',command=fun2).grid(row=5,column=7,padx=10)
Button(root,image=home,command=fun).grid(row=5,column=8)

