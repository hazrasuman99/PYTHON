from tkinter import *
from PIL import Image
import sqlite3
from tkinter import messagebox
e1=''
e2=''
e3=0
e4=''
e5=''
e6=''
e7=''
e8=''
e9=''
e10=''
e11=''
e15=0
def create_table():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    cn.execute('CREATE TABLE criminal_rec (id text primary key not null,name text not null,age INTEGER not null,gender TEXT not null,doi DATE not null,dor DATE not null,img BLOB,img_name text not null)''')
    
    conn.commit()
def drop_table():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    cn.execute('DROP TABLE criminal_rec')
    cn.commit()

def add_data():
    
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    a=e1.get()
    y=e2.get()

    z=e3.get()
    k=e4.get()
    l=e5.get()
    m=e6.get()
    j=e7.get()
    i=open(j,'rb')
    idata=i.read()
    i.close()
    x=sqlite3.Binary(idata)
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    cn.execute("insert into criminal_rec values(?,?,?,?,?,?,?,?)",(a,y,int(z),k,l,m,x,j))
    conn.commit()
def deletei():
    master=Tk()
    master.title("Delete by Id")
    Label(master,text="Enter the id to delete").grid(row=0)
    global e10
    e10 = Entry(master)
    e10.grid(row=0,column=1)
    Button(master,text="submit",command=delete_id).grid(row=0,column=2)
    mainloop()
def deleten():
    master=Tk()
    master.title("Delete by Name")
    Label(master,text="Enter the name to delete").grid(row=0)
    global e11
    e11 = Entry(master)
    e11.grid(row=0,column=1)
    Button(master,text="submit",command=delete_name).grid(row=0,column=2)
    mainloop()
def delete_id():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e10
    i=e10.get()
    cn.execute("delete from criminal_rec where id='%s' "%i)
    conn.commit()
def delete_name():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e11
    i=e11.get()
    cn.execute("delete from criminal_rec where name='%s' "%i)
    conn.commit()
    
    
def search_name():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e9
    i=e9.get()
    res=()
    res=cn.execute("select id,name,age,gender,doi,dor,img_name from criminal_rec where name='%s' "%i)
    
    for j in res:
      master=Tk()
      scroll=Scrollbar(master)
      t=Text(master,height=20,width=50)
      t.pack(side=LEFT,fill=X)
      scroll.pack(side=RIGHT,fill=Y)
      scroll.config(command=t.yview)
      t.config(yscrollcommand=scroll.set)
      t.insert(END,"Id:")
      t.insert(END,j[0])
      t.insert(END,'\n')
      t.insert(END,"Name:")
      t.insert(END,j[1])
      t.insert(END,'\n')
      t.insert(END,"Age:")
      t.insert(END,j[2])
      t.insert(END,'\n')
      t.insert(END,"Gender:")
      t.insert(END,j[3])
      t.insert(END,'\n')
      t.insert(END,"Date of Imprisonment:")
      t.insert(END,j[4])
      t.insert(END,'\n')
      t.insert(END,"Date of Release:")
      t.insert(END,j[5])
      m=Image.open(j[6])
      m.show()
      mainloop()
def updaten():
      master=Tk()
      master.title("update name")
      Label(master,text="Enter the name").grid(row=0)
      Label(master,text="Enter the Id").grid(row=1)
      global e13,e14
      e13 = Entry(master)
      e14 = Entry(master)
      e13.grid(row=0,column=1)
      e14.grid(row=1,column=1)
      Button(master,text="submit",command=update_name).grid(row=2,column=0)
      mainloop()
def update_name():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e13,e14
    i=e13.get()
    s=e14.get()
    cn.execute("update criminal_rec set name='%s' where id='%s' "%(i,s))
    conn.commit()
    
def updatea():
    master=Tk()
    master.title("update age")
    Label(master,text="Enter the age").grid(row=0)
    Label(master,text="Enter the Id").grid(row=1)
    global e15,e16
    e15 = Entry(master)
    e16 = Entry(master)
    e15.grid(row=0,column=1)
    e16.grid(row=1,column=1)
    Button(master,text="submit",command=update_age).grid(row=2,column=0)
    mainloop()
def update_age():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e15,e16
    i=e15.get()
    s=e16.get()
    cn.execute("update criminal_rec set age='%d' where id='%s' "%(int(i),s))
    conn.commit()
def updateg():
    master=Tk()
    master.title("update gender")
    Label(master,text="Enter the gender").grid(row=0)
    Label(master,text="Enter the Id").grid(row=1)
    global e17,e18
    e17 = Entry(master)
    e18 = Entry(master)
    e17.grid(row=0,column=1)
    e18.grid(row=1,column=1)
    Button(master,text="submit",command=update_gender).grid(row=2,column=0)
    mainloop()
def update_gender():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e17,e18
    i=e17.get()
    s=e18.get()
    cn.execute("update criminal_rec set gender='%s' where id='%s' "%(i,s))
    conn.commit()
def updatedoi():
    master=Tk()
    master.title("update date of imprisonment")
    Label(master,text="Enter the date of imprisonment").grid(row=0)
    Label(master,text="Enter the Id").grid(row=1)
    global e19,e20
    e19 = Entry(master)
    e20 = Entry(master)
    e19.grid(row=0,column=1)
    e20.grid(row=1,column=1)
    Button(master,text="submit",command=update_doi).grid(row=2,column=0)
    mainloop()
def update_doi():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e19,e20
    i=e19.get()
    s=e20.get()
    cn.execute("update criminal_rec set doi='%s' where id='%s' "%(i,s))
    conn.commit()
def updatedor():
    master=Tk()
    master.title("update date of release")
    Label(master,text="Enter the date of release").grid(row=0)
    Label(master,text="Enter the Id").grid(row=1)
    global e21,e22
    e21 = Entry(master)
    e22 = Entry(master)
    e21.grid(row=0,column=1)
    e22.grid(row=1,column=1)
    Button(master,text="submit",command=update_dor).grid(row=2,column=0)
    mainloop()
def update_dor():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e21,e22
    i=e21.get()
    s=e22.get()
    cn.execute("update criminal_rec set dor='%s' where id='%s' "%(i,s))
    conn.commit()
def searchi():
      master=Tk()
      master.title("search id")
      Label(master,text="Enter the id to search for").grid(row=0)
      global e8
      e8 = Entry(master)
      e8.grid(row=0,column=1)
      Button(master,text="submit",command=search_id).grid(row=0,column=2)
      mainloop()
def searchn():
      master=Tk()
      master.title("search name")
      Label(master,text="Enter the name to search for").grid(row=0)
      global e9
      e9 = Entry(master)
      e9.grid(row=0,column=1)
      Button(master,text="submit",command=search_name).grid(row=0,column=2)
      mainloop()
def search_id():
    conn=sqlite3.connect("C:\\Users\suman.hazra\Desktop\Criminal Record\crime.db")
    cn=conn.cursor()
    global e8
    i=e8.get()
    
    res=cn.execute("select id,name,age,gender,doi,dor,img_name from criminal_rec where id='%s' "%i)
    for j in res:
      master=Tk()
      

      scroll=Scrollbar(master)
      t=Text(master,height=20,width=50)
      t.pack(side=LEFT,fill=X)
      scroll.pack(side=RIGHT,fill=Y)
      scroll.config(command=t.yview)
      t.config(yscrollcommand=scroll.set)
      t.insert(END,"Id:")
      t.insert(END,j[0])
      t.insert(END,'\n')
      t.insert(END,"Name:")
      t.insert(END,j[1])
      t.insert(END,'\n')
      t.insert(END,"Age:")
      t.insert(END,j[2])
      t.insert(END,'\n')
      t.insert(END,"Gender:")
      t.insert(END,j[3])
      t.insert(END,'\n')
      t.insert(END,"Date of Imprisonment:")
      t.insert(END,j[4])
      t.insert(END,'\n')
      t.insert(END,"Date of Release:")
      t.insert(END,j[5])
      m=Image.open(j[6])
      m.show()
      mainloop()
def about():
      master=Tk()
      master.title("About")
      scroll=Scrollbar(master)
      t=Text(master,height=300,width=300)
      t.pack(side=LEFT,fill=X)
      scroll.pack(side=RIGHT,fill=Y)
      scroll.config(command=t.yview)
      t.config(yscrollcommand=scroll.set)
      t.insert(END,"CRM version 1.0 developed by Suman Hazra.2020 All rights reserved")
def help():
      master=Tk()
      master.title("help")
      scroll=Scrollbar(master)
      t=Text(master,height=300,width=300)
      t.pack(side=LEFT,fill=X)
      scroll.pack(side=LEFT,fill=X)
      scroll.pack(side=RIGHT,fill=Y)
      scroll.config(command=t.yview)
      t.config(yscrollcommand=scroll.set)
      t.insert(END,"operations:insert->to insert criminal details")
      t.insert(END,'\n')
      t.insert(END,"operations:update->to alter a criminal particular information of criminal")
      t.insert(END,'\n')
      t.insert(END,"operations:delete->to delete a particular row from a table")
      t.insert(END,'\n')
      t.insert(END,"search:search_name->to search a particular criminal by name")
      t.insert(END,'\n')
      t.insert(END,"search:search_id->to search a particular criminal by id")
      t.insert(END,'\n')
      t.insert(END,"exit:to exit from the application")
def menu():
 master=Tk()
 master.title("insert")
 Label(master, text="Id").grid(row=0)
 Label(master, text="Name").grid(row=1)
 Label(master, text="Age").grid(row=2)
 Label(master, text="Gender").grid(row=3)
 Label(master,text="date of Imprisonment").grid(row=4)
 Label(master,text="date of release").grid(row=5)
 Label(master,text="image name").grid(row=6)
 global e1,e2,e3,e4,e5,e6,e7
 e1= Entry(master)
 e2= Entry(master)
 e3= Entry(master)
 e4= Entry(master)
 e5= Entry(master)
 e6= Entry(master)
 e7= Entry(master)

 e1.grid(row=0,column=1)
 e2.grid(row=1,column=1)
 e3.grid(row=2,column=1)
 e4.grid(row=3,column=1)
 e5.grid(row=4,column=1)
 e6.grid(row=5,column=1)
 e7.grid(row=6,column=1)
 
 Button(master,text="submit",command=add_data).grid(row=7,column=0)
 mainloop()  

master=Tk()
master.title("Criminal Record Mnagement System")
C = Canvas(master, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\suman.hazra\Desktop\Criminal Record\criminal.png")
background_label = Label(master, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

menubar=Menu(master)
menubar.add_command(label="create",command=create_table)
menubar.add_command(label="drop",command=drop_table)
filemenu=Menu(menubar)
filemenu.add_command(label="insert",command=menu)
menubar.add_cascade(label="operations",menu=filemenu)
fm=Menu(filemenu)
fm.add_command(label="name",command=updaten)
fm.add_command(label="Age",command=updatea)
fm.add_command(label="Gender",command=updateg)
fm.add_command(label="date of imprisonment",command=updatedoi)
fm.add_command(label="date of release",command=updatedor)
filemenu.add_cascade(label="update",menu=fm)
fm1=Menu(filemenu)
fm1.add_command(label="By name",command=deleten)
fm1.add_command(label="By Id",command=deletei)
filemenu.add_cascade(label="delete",menu=fm1)
filemenu1=Menu(menubar)
filemenu1.add_command(label="search by name",command=searchn)
filemenu1.add_command(label="search by id",command=searchi)
menubar.add_cascade(label="search",menu=filemenu1)
menubar.add_command(label="help",command=help)
menubar.add_command(label="about",command=about)
menubar.add_command(label="exit",command=master.quit)
master.config(menu=menubar)
mainloop()
