from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun2():
    try:
        con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
        cur=con.cursor()
        cur.execute('select sum(Seates_booked) from booking_history group by Travelling_Date having Travelling_Date="{}"'.format(date.get()))
        resx=cur.fetchall()
        cur.execute("""select op.Name,b.type,b.capacity,b.fare,r.Seat_Available from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}" ;""".format(From.get(),to.get(),date.get()));
        a=cur.fetchall()
        if int(no.get())>int(a[0][4]-resx[0][0]):
            showerror('Seats Not Available','Sorry! Seats Are Limited')
        else:
            try:
                m=int(mobile.get())
                if len(name.get())==0:
                    showerror('Value Missing','Please Enter Name')
                elif len(no.get())==0:
                    showerror('Value Missing','Please Enter No. of Seats')
                elif m==0:
                    showerror('Value Missing','Please Enter Mobile Number')
                elif len(age.get())==0:
                    showerror('Value Missing','Please Enter Age')
                elif gender.get()=='Select Gender':
                    showerror('Value Missing', 'Please Select Gender')
                elif int(age.get())>150:
                    showerror('Wrong Entry', 'Please Enter Proper Age')
                elif len(mobile.get())>10 or len(mobile.get())<10:
                    showerror('Wrong Entry', 'Please Enter Proper Mobile Number')
                    
                    
                else:
                    con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
                    cur=con.cursor()
                    cur.execute("""select op.Name,b.type,r.Seat_Available,b.fare,r.Seat_Available,b.bus_id from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}" ;""".format(From.get(),to.get(),date.get()));
                    res1=cur.fetchall()
                    print(res1)
                    n=int(no.get())
                    cur.execute("""insert into booking_history(Name,Phone,Age,Gender,Boarding,Upto,Travelling_date,Booking_date,Seates_booked,Bus_Id,fare)values("{}",{},{},"{}","{}","{}","{}",current_date(),{},{},{})""".format(name.get(),mobile.get(),age.get(),gender.get(),From.get(),to.get(),date.get(),no.get(),res1[0][5],res1[0][3]*n))
                    total_fare=res1[0][3]*n;
                    con.commit()
                    con.close()
                    result=askquestion('Fare Confirm','Total amount to be paid Rs {}'.format(total_fare))
                    if result=='yes':
                        root.destroy()
                        import ticket
                    else:
                        root.destroy()
                        import Home
            except(ValueError):
                showerror('Invalid Input','Enter Correct Input')
    except(ValueError,IndexError):
        con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
        cur=con.cursor()
        cur.execute("""select op.Name,b.type,b.capacity,b.fare,r.Seat_Available from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}" ;""".format(From.get(),to.get(),date.get()));
        a=cur.fetchall()
        if int(no.get())>a[0][2]:
            showerror('Not Enough Seat','Sorry Seats Are Limited')
        else:
            try:
                m=int(mobile.get())
                if len(name.get())==0:
                    showerror('Value Missing','Please Enter Name')
                elif len(no.get())==0:
                    showerror('Value Missing','Please Enter No. of Seats')
                elif m==0:
                    showerror('Value Missing','Please Enter Mobile Number')
                elif len(age.get())==0:
                    showerror('Value Missing','Please Enter Age')
                elif gender.get()=='Select Gender':
                    showerror('Value Missing', 'Please Select Gender')
                elif int(age.get())>150:
                    showerror('Wrong Entry', 'Please Enter Proper Age')
                elif len(mobile.get())>10 or len(mobile.get())<10: 
                    showerror('Wrong Entry', 'Please Enter Proper Mobile Number')
                else:
                    con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
                    cur=con.cursor()
                    cur.execute("""select op.Name,b.type,r.Seat_Available,b.fare,r.Seat_Available,b.bus_id from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}" ;""".format(From.get(),to.get(),date.get()));
                    res1=cur.fetchall()
                    print(res1)
                    n=int(no.get())
                    total_fare=res1[0][3]*n;
                    result=askquestion('Fare Confirm','Total amount to be paid Rs {}'.format(total_fare))
                    if result=='yes':
                        cur.execute("""insert into booking_history(Name,Phone,Age,Gender,Boarding,Upto,Travelling_date,Booking_date,Seates_booked,Bus_Id,fare)values("{}",{},{},"{}","{}","{}","{}",current_date(),{},{},{})""".format(name.get(),mobile.get(),age.get(),gender.get(),From.get(),to.get(),date.get(),no.get(),res1[0][5],res1[0][3]*n))
                        root.destroy()
                        import ticket
                    else:
                        root.destroy()
                        import Home
            except(ValueError):
                showerror('Invalid Input','Enter Correct Input')
        con.commit()
        con.close()
        
def passenger():
    try:
        if bus_select.get()==0:
            showerror('Value Missing','Please Select Bus')
        else:
            Label(root,text='Fill Passenger Details to book the bus ticket',font='Arial 16 bold', bg='cadetblue1',fg='red').grid(row=9,column=1,columnspan=10,pady=20)
            Label(root,text='').grid(row=11,column=1)
            Label(root,text='Name').grid(row=11,column=1, padx=(50,0))
            name.grid(row=11,column=2)
            Label(root,text='Gender').grid(row=11,column=3)
            gender.set('Select Gender')
            opt=["Male","Female","other"]
            d_menu=OptionMenu(root,gender,*opt).grid(row=11,column=4)
            Label(root,text='No of seats').grid(row=11,column=5)
            no.grid(row=11,column=6)
            Label(root,text='Mobile No').grid(row=11,column=7)
            mobile.grid(row=11,column=8)
            Label(root,text='Age').grid(row=11,column=9)
            age.grid(row=11,column=10)
            Button(root,text='Book seat', bg='green2',command=fun2).grid(row=11,column=11)
    except(ValueError):
        showerror('Wrong Input', 'Enter Correct Value')

def showbus():
    try:
        Label(root,text='Select Bus',fg='green4').grid(row=5,column=1, padx=(50,20),pady=10)
        Label(root,text='Operator',fg='green4').grid(row=5,column=2, pady=10)
        Label(root,text='Bus Type',fg='green4').grid(row=5,column=3, padx=20,pady=10)
        Label(root,text='Capacity',fg='green4').grid(row=5,column=4, pady=10)
        Label(root,text='Fare',fg='green4').grid(row=5,column=5, padx=20,pady=10)
        Label(root,text='Available',fg='green4').grid(row=5,column=6,padx=20,pady=10)
        con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
        cur=con.cursor()
        cur.execute("""select op.Name,b.type,b.capacity,b.fare,r.Seat_Available from Operator as op, Bus as b,runs as r, route as f,route as t where b.op_id=op.op_id and b.bus_id=r.bus_id and f.Route_id=b.Route_id and f.sname="{}" and t.sname="{}" and f.Route_id = t.route_id and F.s_id<T.s_id and r.date="{}" ;""".format(From.get(),to.get(),date.get()));
        a=cur.fetchall()
        print(a)
        try:
            cur.execute('select sum(Seates_booked) from booking_history group by Travelling_Date having Travelling_Date="{}"'.format(date.get()))
            resx=cur.fetchall()
        
            if a[0][4]-resx[0][0]==0:
                showerror('Bus Is FULL','Seats Are Not Available')
            else:
                Label(root,text=a[0][0],fg='Blue').grid(row=7,column=2)
                Label(root,text=a[0][1],fg='Blue').grid(row=7,column=3)
                Label(root,text=a[0][2],fg='Blue').grid(row=7,column=4)
                Label(root,text=a[0][3],fg='Blue').grid(row=7,column=5)
                Label(root,text=a[0][4]-resx[0][0],fg='Blue').grid(row=7,column=6)
                Radiobutton(root,text="Bus1",variable=bus_select,value=1).grid(row=7,column=1,padx=100)

                Label(root,text=a[1][0],fg='Blue').grid(row=8,column=2)
                Label(root,text=a[1][1],fg='Blue').grid(row=8,column=3)
                Label(root,text=a[1][2],fg='Blue').grid(row=8,column=4)
                Label(root,text=a[1][3],fg='Blue').grid(row=8,column=5)
                Label(root,text=a[1][4]-3,fg='Blue').grid(row=8,column=6)
                Radiobutton(root,text="Bus2",variable=bus_select,value=2).grid(row=8,column=1,padx=100)
                
                con.commit()
                con.close()
                Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7)
        except(IndexError,ValueError):
                    
            """if a[0][4]-resx[0][0]==0:
                showerror('Bus Is FULL','Seats Are Not Available')
            else:"""
            Label(root,text=a[0][0],fg='Blue').grid(row=7,column=2)
            Label(root,text=a[0][1],fg='Blue').grid(row=7,column=3)
            Label(root,text=a[0][2],fg='Blue').grid(row=7,column=4)
            Label(root,text=a[0][3],fg='Blue').grid(row=7,column=5)
            Label(root,text=a[0][4],fg='Blue').grid(row=7,column=6)
            Radiobutton(root,text="Bus1",variable=bus_select,value=1).grid(row=7,column=1,padx=100)
            
            Label(root,text=a[1][0],fg='Blue').grid(row=8,column=2)
            Label(root,text=a[1][1],fg='Blue').grid(row=8,column=3)
            Label(root,text=a[1][2],fg='Blue').grid(row=8,column=4)
            Label(root,text=a[1][3],fg='Blue').grid(row=8,column=5)
            Label(root,text=a[1][4]-3,fg='Blue').grid(row=8,column=6)
            Radiobutton(root,text="Bus2",variable=bus_select,value=2).grid(row=8,column=1,padx=100)
            
            Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7)
            
    except(ValueError,IndexError):
        showerror('No Route','No Bus Found')
    
def fun1():
    if len(to.get())==0:
        showerror('Value Missing','Please Enter Destination')
    elif len(From.get())==0:
        showerror('Value Missing','Please Enter From')
    elif len(date.get())==0:
        showerror('Value Missing','Please Enter Date')
    else:
        showbus()
def home_fun():
    root.destroy()
    import Home

bus_select=IntVar()
gender=StringVar()
no=Entry(root)
name=Entry(root)
mobile=Entry(root)
age=Entry(root)
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,text='                 ').grid(row=0,column=0)
Label(root,image=img).grid(row=0,column=2,columnspan=8)
Label(root,text='                 ').grid(row=1,column=0)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=2,columnspan=8)
Label(root,text='                 ').grid(row=3,column=0)
Label(root,text='').grid(row=2,column=1)
Label(root,text='Enter Journey Details',font='Arial 14 bold', bg='green2',fg='green4').grid(row=3,column=2,columnspan=8,pady=10)
Label(root,text='To').grid(row=4,column=1, padx=(300,0))
to=Entry(root)
to.grid(row=4,column=2)
Label(root,text='From').grid(row=4,column=3)
From=Entry(root)
From.grid(row=4,column=4)
Label(root,text='Journey Date').grid(row=4,column=5)
date=Entry(root)
date.grid(row=4,column=6)
home=PhotoImage(file='.//home.png')

Button(root,image=home,command=home_fun).grid(row=4,column=8,padx=30)  
Button(root,text='Show Bus', bg='springgreen4',command=fun1).grid(row=4,column=7,padx=30)
