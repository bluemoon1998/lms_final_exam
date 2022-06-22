from tkinter import * 
from PIL import ImageTk, Image #PIL
import sqlite3
from tkinter import messagebox

db_name = "new_database"

def bookRegister():
    bid = entry_bookID.get()
    title = entry_booktitle.get()
    author = entry_bookauthor.get()
    status = entry_bookstatus.get().lower()
    isbn = entry_isbn.get()
    phonenumber =entry_phonenumber.get()
    issuedate = entry_issuedate.get()
    duedate = entry_duedate.get()
    returndate = entry_returndate.get()
    
    insert_book_mysql ="insert into " + table_name + " values ('" + bid + "','" + isbn+ "','" + title + "','" + author + "','" + status + "','" + phonenumber+ "'," + str(issuedate)+ "," + str(duedate) + "," + str(returndate)+ ")"
    print(insert_book_mysql)
    
    try:
        cursor.execute(insert_book_mysql)
        connection.commit()
        connection.close()
        messagebox.showinfo('Success', "Book added successfully")

    except:
        messagebox.showinfo('Error', "Can't add book to database")

    print(bid)
    print(title)
    print(author)
    print(status)
    print(isbn)
    print(phonenumber)
    print(issuedate)
    print(duedate)
    print(returndate)
    
    app.destroy()

def addBook():
    global canvas, cursor, connection, table_name, app,entry_bookID,entry_booktitle,entry_bookauthor,entry_bookstatus,entry_isbn,entry_phonenumber,entry_issuedate,entry_duedate,entry_returndate
    app = Tk()
    my_name = "Yonsei" #put your name here
    library_name = my_name+" Library"
    app.title(library_name)
    app.minsize(width=400, height=600)
    app.geometry("600x600")

    connection = sqlite3.connect(db_name+".db")
    cursor = connection.cursor()

    #enter table names here
    table_name = "bookTable"
    
    #create the canvas for info
    canvas = Canvas(app)
    canvas.config(bg="#ace5ee")
    canvas.pack(expand=True, fill=BOTH)

    #add a heading frame
    headingFrame = Frame(app, bg="#FFBB00", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = Label(headingFrame, text = "Add Books", bg="white", fg="black", font=('Courier', 15))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    #frame for form
    LabelFrame = Frame(app, bg="gray")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.6)

    #book ID
    label_bookID = Label(LabelFrame, text = "Book ID: ", bg="gray", fg="white")
    label_bookID.place(relx=0.05, rely=0.05, relheight=0.04)
    #entry label for book ID
    entry_bookID = Entry(LabelFrame)
    entry_bookID.place(relx=0.3, rely=0.05, relwidth=0.62, relheight=0.04)
    
    #title
    label_title = Label(LabelFrame, text = "Title: ", bg="gray", fg="white")
    label_title.place(relx=0.05, rely=0.1, relheight=0.04)
    #entry for title
    entry_booktitle = Entry(LabelFrame)
    entry_booktitle.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.04)
    
    #author
    label_author = Label(LabelFrame, text = "Author: ", bg="gray", fg="white")
    label_author.place(relx=0.05, rely=0.15, relheight=0.04)
    #entry for author
    entry_bookauthor = Entry(LabelFrame)
    entry_bookauthor.place(relx=0.3, rely=0.15, relwidth=0.62, relheight=0.04)
    
    #status
    label_status = Label(LabelFrame, text = "Status: ", bg="gray", fg="white")
    label_status.place(relx=0.05, rely=0.2, relheight=0.04)
    #entry for status
    entry_bookstatus = Entry(LabelFrame)
    entry_bookstatus.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.04)

    #isbn
    label_isbn = Label(LabelFrame, text = "ISBN: ", bg="gray", fg="white")
    label_isbn.place(relx=0.05, rely=0.25, relheight=0.04)
    #entry for isbn
    entry_isbn = Entry(LabelFrame)
    entry_isbn.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.04)

    #phonenumber
    label_phonenumber = Label(LabelFrame, text = "Phone Number: ", bg="gray", fg="white")
    label_phonenumber.place(relx=0.05, rely=0.3, relheight=0.04)
    #entry for phonenumber
    entry_phonenumber = Entry(LabelFrame)
    entry_phonenumber.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.04)

    #issue date
    label_issuedate = Label(LabelFrame, text = "Issue Date: ", bg="gray", fg="white")
    label_issuedate.place(relx=0.05, rely=0.35, relheight=0.04)
    #entry for issue date
    entry_issuedate = Entry(LabelFrame)
    entry_issuedate.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.04)

    #due date
    label_duedate = Label(LabelFrame, text = "Due Date: ", bg="gray", fg="white")
    label_duedate.place(relx=0.05, rely=0.4, relheight=0.04)
    #entry for due date
    entry_duedate = Entry(LabelFrame)
    entry_duedate.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.04)

#    #return date
    label_returndate = Label(LabelFrame, text = "Return Date: ", bg="gray", fg="white")
    label_returndate.place(relx=0.05, rely=0.45, relheight=0.04)
    #entry for return date
    entry_returndate = Entry(LabelFrame)
    entry_returndate.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.04)


    #submit Button
    SubmitButton = Button(app, text="SUBMIT", bg="#d1ccc0", fg="black", command=bookRegister)
    SubmitButton.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    #Quit button
    QuitButton = Button(app, text="Quit", bg="#f7f1e3", fg="black", command=app.destroy)
    QuitButton.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
    app.mainloop()