from tkinter import *
from tkinter import messagebox
import pymysql

# This function executes an SQL command to insert data into the table and commit the changes.
def add_db():

    bid=id.get()
    btitle=title.get()
    bauthor=author.get()

    insertBooks= "insert into books values('" + bid +"','"+btitle+"','"+bauthor+"','YES');"
    print(insertBooks)

    try:
        cur.execute(insertBooks)
        db.commit()
        messagebox.showinfo('Success',"Book added Successfully")
    except:
        messagebox.showinfo("Error","Cannot add given book data into Database")
    
    print(bid,end=',')
    print(btitle,end=',')
    print(bauthor,end=',')
    


def addBooks():
    """This function connects to the MySql server and creates a window for accommodating
    new text fields. We fetch details of a new book from the user and then call
    bookRegister() function to register the books into the table."""

    global id,title,author,db,cur

    # Create window
    window=Tk()
    window.title("Ballot Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500+460+150")
    window.attributes("-toolwindow", True)

    # Connecting from the server
    db = pymysql.connect(host ="localhost",user = "root",password = '123maedeh',database='db')
    cur = db.cursor()
    
    # screen bg
    Canvas1 = Canvas(window)
    Canvas1.config(bg="#FFEC8B")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(window,bg="#C76114")
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='#FF8000', fg='black', font=('Showcard Gothic',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='#C76114')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    # Book ID label
    L = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.2, relheight=0.08)

    id = Entry(labelFrame)
    id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # Title label
    L = Label(labelFrame,text="Title : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.35, relheight=0.08)
        
    title = Entry(labelFrame)
    title.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    # Author label
    L = Label(labelFrame,text="Author : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.50, relheight=0.08)
        
    author = Entry(labelFrame)
    author.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='#00FF00',font=('Caveat',14, 'bold'), fg='black',command=add_db)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(window,text="Quit",bg='red', fg='black',font=('Caveat',14, 'bold'), command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()
    