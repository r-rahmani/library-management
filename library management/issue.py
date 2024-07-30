from tkinter import *
from tkinter import messagebox
import pymysql

def issue_db():

    global id,StudentName

    bid=id.get()
    bStudentName=StudentName.get()

    # Connecting from the server
    db = pymysql.connect(host ="localhost",user = "root",password = '123maedeh',database='db')
    cur = db.cursor()
    
    print(bid,end='--')
    print(bStudentName,end='--')
    print("issue")

    try:
        checkavailability=" select * from books where available='YES';"
        print(checkavailability)
        cur.execute(checkavailability)

        flag=0

        for i in cur:
            print(i[0])
            if(i[0]==bid):
                flag=1
                break;
        
        if flag==1:     
            updatequery="update books set available='NO' where bid='"+bid +"';"
            print(updatequery)
            cur.execute(updatequery)
            db.commit()

            sqlquery= "insert into issue values('" + bid +"','" +bStudentName+"' );"
            print(sqlquery)

            cur.execute(sqlquery)
            db.commit()

            messagebox.showinfo('Success',"Book issued Successfully")
        else:
            messagebox.showinfo("Error","Required Book is not available")
    except:
        messagebox.showinfo("Error","Cannot issue given book ")    
    
def issueBooks():

    global id,StudentName

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

    # Issue Book labale    
    headingLabel = Label(headingFrame1, text="Issue Book", bg='#FF8000', fg='black', font=('Showcard Gothic',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='#C76114')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # Book ID label
    L = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.2)
        
    id = Entry(labelFrame)
    id.place(relx=0.3,rely=0.2, relwidth=0.62)

    # Student Name labale
    L = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    L.place(relx=0.05,rely=0.4)
        
    StudentName = Entry(labelFrame)
    StudentName.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    # Submit Button
    SubmitBtn = Button(window,text="SUBMIT",bg='#00FF00',font=('Caveat',14, 'bold'), fg='black',command=issue_db)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    # Quit Button
    quitBtn = Button(window,text="Quit",bg='red',font=('Caveat',14, 'bold'), fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    window.mainloop()
    