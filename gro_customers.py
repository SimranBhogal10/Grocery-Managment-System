from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import cx_Oracle
from tkinter import messagebox

class Store:
    def __init__(self, root):
      self.root=root
      self.root.title("Grocery Management System")
      self.root.geometry("1300x750")

      title=Label(self.root, text="Grocery Management System", font=("Helvetica",40,"bold"), bg="#00008b", fg="white", bd=5, relief=GROOVE)
      title.pack(side=TOP)

      self.cid=StringVar()
      self.cname=StringVar()
      self.cphone=StringVar()
      self.ccity=StringVar()
      self.cstate=StringVar()

      self.search_by=StringVar()
      self.search_txt=StringVar()


      # Frame to get the details.

      frame1=Frame(self.root, bd=4, relief=RIDGE, bg="#1e90ff")
      frame1.place(x=20,y=100, width=450, height=600)

      title1=Label(frame1, text="Customer Management", font=("Helvetica",20,"bold"), bg="#1e90ff")
      title1.grid(row=0, columnspan=2, pady=20)

      lbl_cid=Label(frame1, text="Customer ID", bg="#1e90ff", font=("Helvetica",12,"bold"))
      lbl_cid.grid(row=1, column=0, pady=10, padx=20, sticky="w")
      txt_cid=Entry(frame1, textvariable=self.cid, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_cid.grid(row=1, column=1, pady=10, padx=10, sticky="w", )

      lbl_cname=Label(frame1, text="Customer Name", bg="#1e90ff", font=("Helvetica",12,"bold"))
      lbl_cname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
      txt_cname=Entry(frame1, textvariable=self.cname, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_cname.grid(row=2, column=1, pady=10, padx=10, sticky="w",)

      lbl_cphone=Label(frame1, text="Customer Phone", bg="#1e90ff", font=("Helvetica",12,"bold"))
      lbl_cphone.grid(row=3, column=0, pady=10, padx=20, sticky="w")
      txt_cphone=Entry(frame1, textvariable=self.cphone, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_cphone.grid(row=3, column=1, pady=10, padx=10, sticky="w")

      lbl_ccity=Label(frame1, text="City", bg="#1e90ff", font=("Helvetica",12,"bold"))
      lbl_ccity.grid(row=4, column=0, pady=10, padx=20, sticky="w")
      txt_ccity=Entry(frame1, textvariable= self.ccity, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_ccity.grid(row=4, column=1, pady=10, padx=10, sticky="w")

      lbl_cstate=Label(frame1, text="State", bg="#1e90ff", font=("Helvetica",12,"bold"))
      lbl_cstate.grid(row=5, column=0, pady=10, padx=20, sticky="w")
      combo_cstate=ttk.Combobox(frame1, textvariable=self.cstate, font=("Helvetica",13), state='readonly')
      combo_cstate['values']=("Andhra Pradesh","Assam","Bihar","Chhattisgarh","Delhi","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Odisha","Punjab","Chandigarh","Rajasthan","Tamil Nadu","Telangana","Uttar Pradesh","Uttarakhand","West Bengal")
      combo_cstate.grid(row=5, column=1, pady=10, padx=10)
      
      btn_frame1=Frame(frame1, bg="#1e90ff")
      btn_frame1.place(x=20, y=390, width=400, height=200)
      add_btn=Button(btn_frame1, text="Add", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.add_customer).grid(row=6, column=1, padx=80, pady=6,)
      updt_btn=Button(btn_frame1, text="Update", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.update_customer).grid(row=7, column=1, padx=80, pady=6,)
      dlt_btn=Button(btn_frame1, text="Delete", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.delete_customer).grid(row=8, column=1, padx=80, pady=6,)
      clr_btn=Button(btn_frame1, text="Clear", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.clear).grid(row=9, column=1, padx=80, pady=6,)

      

      #Frame 2 to get the results or to display the records.

      frame2=Frame(self.root, bd=4, relief=RIDGE, bg="#1e90ff")
      frame2.place(x=500,y=100, width=850, height=600)

      lbl_search=Label(frame2, text="Search by", bg="#1e90ff", font=("Helvetica",20,"bold"))
      lbl_search.grid(row=0, column=0, pady=20, padx=10, sticky="w")
      combo_search=ttk.Combobox(frame2, textvariable=self.search_by, font=("Helvetica",13), state='readonly', width=17)
      combo_search['values']=("Customer Name","Customer ID","City", "State")
      combo_search.grid(row=0, column=1, pady=10, padx=10)

      txt_search=Entry(frame2,textvariable=self.search_txt, font=("Helvetica",15), bd=5, relief=GROOVE, width=15)
      txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")
      search_btn=Button(frame2, text="Search", width=15, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.search_prod).grid(row=0, column=3, padx=5, pady=10,)
      display_btn=Button(frame2, text="Show All", width=15, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.display).grid(row=0, column=4, padx=5, pady=10,)

      #table frame for displaying the records in a proper manner.

      frame3=Frame(frame2, bd=4, relief=RIDGE, bg="white")
      frame3.place(x=20, y=80, width=800, height=500)
      scroll_y=Scrollbar(frame3, orient=VERTICAL)
      self.Cust_table=ttk.Treeview(frame3, columns=("cid","cname","cphone","ccity","cstate"), yscrollcommand=scroll_y.set)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_y.config(command=self.Cust_table.yview)
      self.Cust_table.heading("cid", text="CID")
      self.Cust_table.heading("cname", text="Customer Name")
      self.Cust_table.heading("cphone", text="Phone No")
      self.Cust_table.heading("ccity", text="City")
      self.Cust_table.heading("cstate", text="State")
      self.Cust_table['show']='headings'
      self.Cust_table.column("cid", width=100)
      self.Cust_table.column("cname", width=250)
      self.Cust_table.column("cphone", width=150)
      self.Cust_table.column("ccity", width=125)
      self.Cust_table.column("cstate", width=150)
      self.Cust_table.pack(fill=BOTH, expand=1)
      self.Cust_table.bind("<ButtonRelease-1>", self.get_cursor)


      self.display()

    def add_customer(self):
        if self.cid.get()=="" or self.cname.get()=="":
          messagebox.showerror("Error","All fields are required!")
        else:
          con=cx_Oracle.connect('system/sim272')
          cur=con.cursor()
          cur.execute("INSERT INTO GROCUST1 VALUES(:cid, :cname, :cphone, :ccity, :cstate)", (self.cid.get(), self.cname.get(), self.cphone.get(), self.ccity.get(), self.cstate.get()))
          con.commit()
          self.display()
          self.clear()
          con.close()
          messagebox.showinfo("Success","Record insertion successful!")

    def display(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        cur.execute("select * from grocust1 order by cid")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Cust_table.delete(*self.Cust_table.get_children())
            for row in rows:
                self.Cust_table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row=self.Cust_table.focus()
        contents=self.Cust_table.item(cursor_row)
        row=contents['values']
        self.cid.set(row[0])
        self.cname.set(row[1])
        self.cphone.set(row[2])
        self.ccity.set(row[3])
        self.cstate.set(row[4])

    def update_customer(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        cur.execute("UPDATE GROCUST1 SET cname=:cname, cphone=:cphone, ccity=:ccity, cstate=:cstate where cid=:cid", (self.cname.get(), self.cphone.get(), self.ccity.get(), self.cstate.get(), self.cid.get()))
        con.commit()
        self.display()
        self.clear()
        con.close()

    def delete_customer(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        cur.execute("delete from grocust1 where cid="+ self.cid.get())
        con.commit()
        con.close()
        self.display()
        self.clear()
        
    def clear(self):
        self.cid.set("")
        self.cname.set("")
        self.cphone.set("")
        self.ccity.set("")
        self.cstate.set("")

    def search_prod(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        selected=self.search_by.get()
        if selected=="Customer Name":
            cur.execute("select * from grocust1 where cname=:1",(self.search_txt.get(), ))
        if selected=="Customer ID":
            cur.execute("select * from grocust1 where cid="+ self.search_txt.get())
        if selected=="City":
            cur.execute("select * from grocust1 where ccity=:1",(self.search_txt.get(), ))
        if selected=="State":
            cur.execute("select * from grocust1 where cstate=:1",(self.search_txt.get(), ))
        #searched=self.search_txt.get()
        #name=(searched,)
        #cur.execute(sql, name)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Cust_table.delete(*self.Cust_table.get_children())
            for row in rows:
                self.Cust_table.insert('',END,values=row)
            con.commit()
        con.close()
      
root=Toplevel()
img=Image.open("gro2.png")
bg= ImageTk.PhotoImage(img)
#bg=PhotoImage(file="gro2.png")
my_label=Label(root, image=bg)
my_label.place(x=0, y=0)
ob=Store(root)
root.mainloop()