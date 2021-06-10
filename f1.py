from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import cx_Oracle
from tkinter import messagebox

root=Tk()
root.title("Grocery Management System")
root.geometry("1300x750")
img=Image.open("gro2.png")
bg= ImageTk.PhotoImage(img)
#bg= PhotoImage(file="gro5.png")
my_label=Label(root, image=bg)
my_label.place(x=0, y=0)
frame= LabelFrame(root, text="Login/Register", font=("Times","24","italic") ,padx=25, pady=25, bg="darkgrey", bd=10, relief=RIDGE)
frame.pack(padx=100, pady=200)

#my_label=Label(root, text="Hello World")
#my_label.pack()

def login():
        global username
        global password
        username="admin"
        password="123"
        if e1.get()==username and e2.get()==password:
            sec_win()
            
        else:
            response=messagebox.showinfo("Error","You entered wrong username or password, kindly check and retry!!")
            Label(root, text=response).pack()
                
                

def popup():
        response=messagebox.askyesno("Exit", "Are you sure you want to exit?")
        Label(root, text=response).pack()
        if response==True:
                root.destroy()
        #else:
                #login()



l1= Label(frame,text="Enter UserName",font=("Helvetica",18), padx=5, pady=5, bg="darkgrey")
l1.grid(row=0,column=0,padx=10,pady=10)
l2= Label(frame,text="Enter Password",font=("Helvetica",18),padx=5, pady=5, bg="darkgrey")
l2.grid(row=1,column=0,pady=15,padx=15)
e1=Entry(frame,font=("Helvetica",14,"bold"))
e1.grid(row=0,column=1)
e2=Entry(frame,show="*", font=("Helvetica",14))
e2.grid(row=1,column=1,pady=20)
button_login=Button(frame, text="Login",relief=SUNKEN, padx=15, pady=5, bg='grey', font=("Helvetica","18","bold"), command=login)
can_but=Button(frame,text="Cancel", relief=SUNKEN, padx=15, pady=5, bg='grey', font=("Helvetica","18","bold"),command= popup)
#can_but.pack()
#button_register=Button(frame, text="Register",relief=SUNKEN, padx=10, pady=10, bg='#bdb76b', font=("Helvetica","25","bold"), command=register)

button_login.grid(row=3, column=0, padx=25, pady=25)
can_but.grid(row=3,column=1,padx=25, pady=25)
#button_register.grid(row=1, column=0, padx=50, pady=50)
#my_label.pack()


def sec_win():
    from PIL import ImageTk, Image
    root1=Toplevel()
    root1.geometry("1300x750")
    img=Image.open("gro2.png")
    bg= ImageTk.PhotoImage(img)
    my_label=Label(root1, image=bg)
    my_label.place(x=0, y=0)
    frame1=Frame(root1, padx=85, pady=80, bg="#1e90ff", bd=5, relief=RIDGE)
    frame1.place(x=300,y=225, width=350, height=250)
    prod_page_btn=Button(frame1, text="Product Management", relief=SUNKEN, padx=15,pady=30, bg="darkblue", fg="white", font=("Helvetica","10","bold"), command=product)
    prod_page_btn.grid(row=0, column=0,padx=0,pady=3)
    frame2=Frame(root1, padx=85, pady=80, bg="#1e90ff", bd=5, relief=RIDGE)
    frame2.place(x=750,y=225, width=350, height=250)
    cust_page_btn=Button(frame2, text="Customer Management", relief=SUNKEN, padx=15,pady=30, bg="darkblue", fg="white",font=("Helvetica","10","bold"), command=customer)
    cust_page_btn.grid(row=0, column=0,padx=0,pady=3)
    root1.mainloop()

#def destroy():
#    root.destroy()
   
def product():
    import gro272
    #os.system("python gro272.py")


def customer():
    import gro_customers
    #os.system("python gro_customers.py")

    
root.mainloop()
