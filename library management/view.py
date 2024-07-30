from tkinter import *
from tkinter import messagebox
import pymysql

# Connecting from the server
db = pymysql.connect(host ="localhost",user = "root",password = '123maedeh',database='db')
cur = db.cursor()

# This function is creates a window for displaying the records in the table   
def viewBooks():

    global id

    window = Tk()
    window.title("Ballot Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500+460+150")
    window.attributes("-toolwindow", True)

    Canvas1 = Canvas(window) 
    Canvas1.config(bg="#FFEC8B")
    Canvas1.pack(expand=True,fill=BOTH)
            
    headingFrame1 = Frame(window,bg="#C76114")
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='#FF8000', fg='black', font=('Showcard Gothic',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.64)
    x=0.25
    
    # Tabale head labale
    L = Label(labelFrame, text = "%-10s%-40s%-30s%-20s"%('BookID','Title','Author','Available'),bg='black',fg='white')
    L.place(relx=0.07,rely=0.1)

    L = Label(labelFrame, text = "=====================================================",bg='black',fg='white')
    L.place(relx=0.05,rely=0.2)

    sqlquery= "select * from books ;"# Get information from server
    print(sqlquery)

    # In order to handle any discrepancies, we place this code in a try-except block
    try:
        cur.execute(sqlquery)
        db.commit()

        for i in cur:
            L = Label(labelFrame, text = "%-10s%-40s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white')
            L.place(relx=0.07,rely=x)
            x += 0.1
    except:
        messagebox.showinfo("Error","Cannot Fetch data.")

    #Quit Button
    quitBtn = Button(window,text="Quit",bg='red',font=('Caveat',14, 'bold'), fg='black', command=window.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop() 
    