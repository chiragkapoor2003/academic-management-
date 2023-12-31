from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
from PIL import ImageTk,Image

db = Database("students.db")
root = Tk()
root.title("Academic Performance")
root.geometry("1920x1080+0+0")
root.config(bg="#13eb1e")

root.state("zoomed")

name = StringVar()
age = StringVar()
dob = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()
grade = StringVar()
percentage = StringVar()
branch= StringVar()

# Entries Frame
img=Image.open("emblemdark.png")
bg=ImageTk.PhotoImage(img)
entries_frame = Frame(root,bg="#10a33f")
entries_frame.pack(side=TOP, fill=X)

label1=Label(entries_frame, image=bg)
label1.image= bg
label1.place(relx=0.72,rely=0.6,anchor='ne')

title = Label(entries_frame, text="Academic Performance", font=("Cursive", 30, "bold"), bg="#f7faf8", fg="black")
title.grid(row=0, column=3,columnspan=2, padx=10, pady=20, sticky="w")



lblName = Label(entries_frame, text="Name", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 12), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 12), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lbldob = Label(entries_frame, text="D.O.B", font=("Calibri", 12), bg="#f7faf8", fg="black")
lbldob.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtDob = Entry(entries_frame, textvariable=dob, font=("Calibri", 12), width=30)
txtDob.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 12), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 12), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 12), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

txtAddress = Text(entries_frame, width=60, height=5, font=("Calibri", 12))
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

lblgrade = Label(entries_frame, text="grade", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblgrade.grid(row=1, column=4, padx=10, pady=10, sticky="w")
txtgrade = Entry(entries_frame, textvariable=grade, font=("Calibri", 12), width=30)
txtgrade.grid(row=1, column=5, padx=10, pady=10, sticky="w")

lblpercentage = Label(entries_frame, text="percentage", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblpercentage.grid(row=2, column=4, padx=10, pady=10, sticky="w")
txtpercentage = Entry(entries_frame, textvariable=percentage, font=("Calibri", 12), width=30)
txtpercentage.grid(row=2, column=5, padx=10, pady=10, sticky="w")

lblbranch = Label(entries_frame, text="section", font=("Calibri", 12), bg="#f7faf8", fg="black")
lblbranch.grid(row=3, column=4, padx=10, pady=10, sticky="w")
txtbranch = Entry(entries_frame, textvariable=branch
, font=("Calibri", 12), width=30)
txtbranch.grid(row=3, column=5, padx=10, pady=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    grade.set(row[7])
    percentage.set(row[8])
    branch.set(row[9])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[10])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_studentdetails():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtgrade.get()=="" or txtpercentage.get()=="" or txtbranch.get() =="" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtDob.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtgrade.get(), txtpercentage.get(), txtbranch
.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_studentdetails():
    if txtName.get() == "" or txtAge.get() == "" or txtDob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtgrade.get()=="" or txtpercentage.get()=="" or txtbranch.get()=="" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDob.get(), txtEmail.get(), comboGender.get(), txtContact.get(), txtgrade.get(),txtpercentage.get(), txtbranch
.get(), txtAddress.get(
             1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_studentdetails():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    dob.set("")
    gender.set("")
    email.set("")
    contact.set("")
    grade.set("")
    percentage.set("")
    branch.set("")
    txtAddress.delete(1.0, END)


btn_frame = Frame(entries_frame, bg="#f7faf8")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_studentdetails, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#66CD00", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_studentdetails, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#BF3EFF",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_studentdetails, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#FF3030",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style=ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
yscrollbar= Scrollbar(tree_frame)
yscrollbar.pack(side=RIGHT, fill=Y)
xscrollbar=Scrollbar(tree_frame,orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
tv = ttk.Treeview(tree_frame,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set,columns=(1, 2, 3, 4, 5, 6, 7, 8,9,10,11),style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.column("2", width=5)
tv.heading("3", text="Age")
tv.column("3", width=2)
tv.heading("4", text="D.O.B")
tv.column("4", width=8)
tv.heading("5", text="Email")
tv.column("5", width=6)
tv.heading("6", text="Gender")
tv.column("6", width=6)
tv.heading("7", text="Contact")
tv.column("7", width=10)
tv.heading("9", text="percentage")
tv.column("9", width=4)
tv.heading("8", text="grade")
tv.column("8", width=4)
tv.heading("10",text="section")
tv.column("10", width=10)
tv.heading("11",text="Address")
tv.column("11", width=10)

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(expand=1,fill=X)
tree_frame.pack(fill=X)
yscrollbar.config(command=tv.yview)
xscrollbar.config(command=tv.xview)
dispalyAll()

root.mainloop()
