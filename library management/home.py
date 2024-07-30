from tkinter import *
from turtle import bgcolor
import pymysql
from add import *
from delete import *
from issue import * 
from Return import *
from view import *

""""main.py :  which does function call to all other python files
    Add.py : To add the book
    View.py : To View the list of books in the library
    Delete.py : To Delete a book from library
    Issue.py : To Issue a book from library
    Return.py : To Return a book to the library"""

# Connecting from the server
db = pymysql.connect(host ="localhost",user = "root",password = '123maedeh',database='db')
cur = db.cursor()

# Creat table in server 
def creatTable():
    cur = db.cursor()
    cur.execute("create table books(bid varchar(10) primary key,title varchar(50) Not null,author varchar(50) Not null,available varchar(5) Default 'YES');")
    cur.execute("create table issue(bid varchar(10) primary key,studentName varchar(50) Not null,foreign key(bid) references books(bid));")

# Does the table exist on the server or not? 
# If it is exist, it will be displayed.
def fullTable():
    cur = db.cursor()
    cur.execute("SHOW TABLES")
    flag = True
    for i in cur:
        flag = False
        break
    if flag:
        return False
    else:
        return True

# If it does't exist, a table is created on the server.
if not fullTable():
    creatTable()  

# Create window
window=Tk()
window.title("Ballot Library")
window.minsize(width=400,height=400)
window.geometry("600x500+460+150")
window.attributes("-toolwindow", True)

Canvas1 = Canvas(window)
Canvas1.config(bg="#D2B48C")
Canvas1.pack(expand=True,fill=BOTH)

# Setting up the head frame
headingFrame1 = Frame(window,bg="#E3CF57",bd=4)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(window, text="*Welcome to Baloot Library*", fg='black',bg= "#D2B48C", font=('Caveat',34, 'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=0.4)


#-------------------Adding the Buttons------------------------
# Add Button
addbtn = Button(window,text="Add Book Details",bg='#CD8500', fg='black',font=('Eras Demi ITC',15), command = addBooks)
addbtn.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

# Delete Button    
deletebtn = Button(window,text="Delete Book",bg='#CD8500', fg='black',font=('Eras Demi ITC',15), command = deleteBooks)
deletebtn.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

# Issue Button
issuebtn = Button(window,text="Issue Book to Student",bg='#CD8500', fg='black',font=('Eras Demi ITC',15), command = issueBooks)
issuebtn.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)  

# Return Button
returnbtn = Button(window,text="Return Book",bg='#CD8500', fg='black',font=('Eras Demi ITC',15), command = returnBooks)
returnbtn.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

# View Button
viewbtn = Button(window,text="View Book List",bg='#CD8500', fg='black',font=('Eras Demi ITC',15), command=viewBooks)
viewbtn.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
window.mainloop()
