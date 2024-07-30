from tkinter import *
from tkinter import messagebox
import pymysql

def return_db():

    global id

    bid=id.get()

    # Connecting from the server
    db = pymysql.connect(host ="localhost",user = "root",password = '123maedeh',database='db')
    cur = db.cursor()
    
    print(bid,end='--')
    print("return")

    try:
        checkavailability=" select * from books where available='NO';"
        print(checkavailability)
        cur.execute(checkavailability)

        flag=0

        for i in cur:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='YES' where bid='"+bid +"';"
            print(updatequery)
            cur.execute(updatequery)
            db.commit()

            sqlquery= "delete from issue where bid='" + bid +"';"
            print(sqlquery)

            cur.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success',"Book returned Successfully")
        else:
            messagebox.showinfo("Error","Invalid Book id")
    except:
        messagebox.showinfo("Error","Cannot return given book ")
    
def returnBooks():

    global id

    window = Tk()
    window.title("Ballot Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500+460+150")
    window.attributes("-toolwindow", True)
    
    Canvas1 = Canvas(window)
    
    Canvas1.config(bg="#FFEC8B")
    Canvas1.pack(expand=True,fill=BOTH) 

    headingFrame1 = Frame(window,bg="#C76114",)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    # Return Book labale    
    headingLabel = Label(headingFrame1, text="Return Book", bg='#FF8000', fg='black', font=('Showcard Gothic',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='#C76114')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5) 

    # Book ID labale
    L = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.5)
        
    id = Entry(labelFrame)
    id.place(relx=0.3,rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='#00FF00',font=('Caveat',14, 'bold'), fg='black',command=return_db)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(window,text="Quit",bg='red',font=('Caveat',14, 'bold'), fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop() 
