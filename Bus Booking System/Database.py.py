import sqlite3
con = sqlite3.Connection('Python_bus.db')
cur=con.cursor()
cur.execute('create table Operator(Op_Id int PRIMARY KEY, Name varchar(20), Address varchar(20), Email varchar(50), Phone numeric(20));')
cur.execute('create table Route(Route_Id int(10), S_Id int(10), Sname varchar(10), PRIMARY KEY(Route_Id,S_Id));')
cur.execute('create table Bus(Bus_Id int PRIMARY KEY, Type varchar(10),Capacity int(5),Fare int(10),Route_Id int(10),Op_Id int(10),CONSTRAINT fk_route FOREIGN KEY(Route_Id) REFERENCES Route(Route_Id),CONSTRAINT fk_opID FOREIGN KEY(Op_Id) REFERENCES operator(op_Id));')
cur.execute('create table Runs(Bus_Id int(10),Date varchar(10), Seat_Available int(5),CONSTRAINT fk_bus FOREIGN KEY(bus_Id) REFERENCES BUS(Bus_Id));')
cur.execute('create table Booking_history(Reference_Id int auto_increment Primary Key,Name varchar(20),Phone numeric(11),Age int(10),Gender varchar(10),Boarding varchar(10),Upto varchar(10),Travelling_Date date,Booking_date date, Seates_booked int(10),Bus_Id int(10),fare numeric(10))')

cur.execute('insert into Operator values(01,"Kamla","Jhansi","kamlatravel@gmail.com",884531259);');
cur.execute('insert into Operator values(02,"Hans","Kanpur","Hanstravel@gmail.com",963258741)');

cur.execute('insert into Route values(31,1,"Guna");')
cur.execute('insert into Route values(31,2,"Jaypee");')
cur.execute('insert into Route values(31,3,"Binagarh")')
cur.execute('insert into Route values(31,4,"Biaora");')
cur.execute('insert into Route values(31,5,"Bhopal");')

cur.execute('insert into Route values(32,1,"Bhopal");')
cur.execute('insert into Route values(32,2,"Biaora");')
cur.execute('insert into Route values(32,3,"Binagarh");')
cur.execute('insert into Route values(32,4,"Jaypee");')
cur.execute('insert into Route values(32,5,"Guna");')

cur.execute('insert into Bus values(21,"AC 2x2",50,1000,31,01);')
cur.execute('insert into Bus values(22,"2x2",60,800,32,02);')

cur.execute('insert into Runs values(21,"27/11/22",50);')
cur.execute('insert into Runs values(22,"28/11//22",60);')
con.commit()
con.close()
