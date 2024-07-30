from tkinter import *
from tkinter import messagebox
import pymysql

# This function primarily checks if the bid (book id) exists in the book table and
#  if it does, it executes the necessary command to remove it.
def delete_db():

    global id

    bid=id.get()
    
    # Connecting from the server
    db = pymysql.connect(host ="localhost",user = "root",password = '123maedeh',database='db')
    cur = db.cursor()
    
    print(bid,end='--')
    print("delete")

    sqlquery= "delete from books where bid='"+bid+"';"
    print(sqlquery)

    try:
        cur.execute(sqlquery)
        db.commit()
        messagebox.showinfo('Success',"Book deleted Successfully")
    except:
        messagebox.showinfo("Error","Book with given id does not exist")
        
    print("A book with  "+bid+" id was removed from the server")


# This function creates a window for accommodating a text input field.
# We fetch details of a book from the user and then call delete_db 
# function to delete the book record from the table.   
def deleteBooks():

    global id

    window = Tk()
    window.title("Ballot Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500+460+150")
    window.attributes("-toolwindow", True)
    
    Canvas1 = Canvas(window)
    
    Canvas1.config(bg="#FFEC8B")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(window,bg="#FFBB00")
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    # Delete Book labale    
    headingLabel = Label(headingFrame1, text="Delete Book", bg='#FF8000', fg='black', font=('Showcard Gothic',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='#C76114')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 

    # Book ID labale
    L = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.5)
        
    id = Entry(labelFrame)
    id.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    # Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='#00FF00',font=('Caveat',14, 'bold'), fg='black',command=delete_db)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(window,text="Quit",bg='red',font=('Caveat',14, 'bold'), fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()
