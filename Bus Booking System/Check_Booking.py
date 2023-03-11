import mysql.connector
from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def home_fun():
    root.destroy()
    import Home
def fun():
    if len(check.get())==0:
        showerror('Missing Value','Please Enter Mobile Number')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='1234',database='python_bus')
            cur=con.cursor()
            cur.execute('select Name,Phone,Age,Gender,Boarding,Upto,Travelling_Date,Booking_date,Seates_booked,Bus_Id,fare,reference_id from booking_history where phone="{}"'.format(check.get()))
            res=cur.fetchall()
            print(res)
            final = LabelFrame(root)
            final.grid(row=6,columnspan=8,column=0,padx=300)
            Label(final, text = "Passenger: {}".format(res[0][0])).grid(row =8, column=0)
            Label(final, text = "No of seats: {}".format(res[0][8])).grid(row =9, column=0)
            Label(final, text = "Age: {}".format(res[0][2])).grid(row =10, column=0)
            Label(final, text = "Booking Ref. {}".format(res[0][11])).grid(row =11, column=0)
            Label(final, text = "Travels on: {}".format(res[0][6])).grid(row =12, column=0)
            Label(final, text = "Gender: {}".format(res[0][3])).grid(row =8, column=1)
            Label(final, text = "Phone: {}".format(res[0][1])).grid(row =9, column=1)
            Label(final, text = "Fare Rs: {}".format(res[0][10])).grid(row =10, column=1)
            Label(final, text = "Booked On: {}".format(res[0][7])).grid(row =11, column=1)
            Label(final, text = "Boarding Point: {}".format(res[0][4])).grid(row =12, column=1)
            Label(final, text = "").grid(row =13,column=1)
            Label(final, text = "Total amount Rs {} to be paid at the time of boarding the bus".format(res[0][10]),fg='grey').grid(row =14, column=0,columnspan=2)
            con.commit()
            con.close()
        except(IndexError,ValueError):
            showerror('Value Error','No Ticket Found!')
            
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file=".\\home.png")
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=(450,0),pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=3,padx=(450,0))
Label(root,text='Check Your Booking',font='Arial 14 bold', bg='green2',fg='green4').grid(row=2,column=0,pady=20,columnspan=3,padx=(450,0))
Label(root,text='Enter Your Mobile Number:').grid(row=4,column=0,padx=(450,0))
check=Entry(root)
check.grid(row=4,column=1,padx=50)
Button(root,text='Check Booking',command=fun).grid(row=4,column=2,padx=(10,100))
Button(root,image=home,command=home_fun).grid(row=4,column=3,padx=(0,100))








