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

      self.pid=StringVar()
      self.pname=StringVar()
      self.pstock=StringVar()
      self.pprice=StringVar()
      self.ptype=StringVar()

      self.search_by=StringVar()
      self.search_txt=StringVar()


      # Frame to get the details.

      frame1=Frame(self.root, bd=4, relief=RIDGE, bg="#1e90ff")
      frame1.place(x=20,y=100, width=450, height=600)

      title1=Label(frame1, text="Product Management", font=("Helvetica",20,"bold"), bg="#1e90ff")
      title1.grid(row=0, columnspan=2, pady=20)

      lbl_pid=Label(frame1, text="Product ID", bg="#1e90ff", font=("Helvetica",15,"bold"))
      lbl_pid.grid(row=1, column=0, pady=10, padx=20, sticky="w")
      txt_pid=Entry(frame1, textvariable=self.pid, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_pid.grid(row=1, column=1, pady=10, padx=10, sticky="w", )

      lbl_pname=Label(frame1, text="Product Name", bg="#1e90ff", font=("Helvetica",15,"bold"))
      lbl_pname.grid(row=2, column=0, pady=10, padx=20, sticky="w")
      txt_pname=Entry(frame1, textvariable=self.pname, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_pname.grid(row=2, column=1, pady=10, padx=10, sticky="w",)

      lbl_pstock=Label(frame1, text="Product Stock", bg="#1e90ff", font=("Helvetica",15,"bold"))
      lbl_pstock.grid(row=3, column=0, pady=10, padx=20, sticky="w")
      txt_pstock=Entry(frame1, textvariable=self.pstock, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_pstock.grid(row=3, column=1, pady=10, padx=10, sticky="w")

      lbl_pprice=Label(frame1, text="Product Price", bg="#1e90ff", font=("Helvetica",15,"bold"))
      lbl_pprice.grid(row=4, column=0, pady=10, padx=20, sticky="w")
      txt_pprice=Entry(frame1, textvariable=self.pprice, font=("Helvetica",15), bd=5, relief=GROOVE)
      txt_pprice.grid(row=4, column=1, pady=10, padx=10, sticky="w")

      lbl_ptype=Label(frame1, text="Product Type", bg="#1e90ff", font=("Helvetica",15,"bold"))
      lbl_ptype.grid(row=5, column=0, pady=10, padx=20, sticky="w")
      combo_ptype=ttk.Combobox(frame1, textvariable=self.ptype, font=("Helvetica",13), state='readonly')
      combo_ptype['values']=("Solid","Liquid","Other")
      combo_ptype.grid(row=5, column=1, pady=10, padx=10)
      
      btn_frame1=Frame(frame1, bg="#1e90ff")
      btn_frame1.place(x=20, y=390, width=400, height=200)
      add_btn=Button(btn_frame1, text="Add", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.add_product).grid(row=6, column=1, padx=80, pady=6,)
      updt_btn=Button(btn_frame1, text="Update", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.update_product).grid(row=7, column=1, padx=80, pady=6,)
      dlt_btn=Button(btn_frame1, text="Delete", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.delete_product).grid(row=8, column=1, padx=80, pady=6,)
      clr_btn=Button(btn_frame1, text="Clear", width=30, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.clear).grid(row=9, column=1, padx=80, pady=6,)

      

      #Frame 2 to get the results or to display the records.

      frame2=Frame(self.root, bd=4, relief=RIDGE, bg="#1e90ff")
      frame2.place(x=500,y=100, width=850, height=600)

      lbl_search=Label(frame2, text="Search by", bg="#1e90ff", font=("Helvetica",20,"bold"))
      lbl_search.grid(row=0, column=0, pady=20, padx=10, sticky="w")
      combo_search=ttk.Combobox(frame2, textvariable= self.search_by, font=("Helvetica",13), state='readonly', width=17)
      combo_search['values']=("Product Name","Product ID","Product Type")
      combo_search.grid(row=0, column=1, pady=10, padx=10)

      txt_search=Entry(frame2, textvariable=self.search_txt, font=("Helvetica",15), bd=5, relief=GROOVE, width=15)
      txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")
      search_btn=Button(frame2, text="Search", width=15, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.search_prod).grid(row=0, column=3, padx=5, pady=10,)
      display_btn=Button(frame2, text="Show All", width=15, bd=5, bg="dark blue", fg="white", padx=2, pady=2, command=self.display).grid(row=0, column=4, padx=5, pady=10,)

      #table frame for displaying the records in a proper manner.

      frame3=Frame(frame2, bd=4, relief=RIDGE, bg="white")
      frame3.place(x=20, y=80, width=800, height=500)
      scroll_y=Scrollbar(frame3, orient=VERTICAL)
      self.Prod_table=ttk.Treeview(frame3, columns=("pid","pname","pstock","pprice","ptype"), yscrollcommand=scroll_y.set)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_y.config(command=self.Prod_table.yview)
      self.Prod_table.heading("pid", text="PID")
      self.Prod_table.heading("pname", text="Product Name")
      self.Prod_table.heading("pstock", text="Product Stock")
      self.Prod_table.heading("pprice", text="Price")
      self.Prod_table.heading("ptype", text="Product Type")
      self.Prod_table['show']='headings'
      self.Prod_table.column("pid", width=100)
      self.Prod_table.column("pname", width=250)
      self.Prod_table.column("pstock", width=150)
      self.Prod_table.column("pprice", width=125)
      self.Prod_table.column("ptype", width=150)
      self.Prod_table.pack(fill=BOTH, expand=1)
      self.Prod_table.bind("<ButtonRelease-1>", self.get_cursor)


      self.display()

    def add_product(self):
        if self.pid.get=="" or self.pname.get()=="":
          messagebox.showerror("Error","All fields are required!")
        else:
          con=cx_Oracle.connect('system/sim272')
          cur=con.cursor()
          cur.execute("INSERT INTO GROPROD1 VALUES(:pid, :pname, :pstock, :pprice, :ptype)", (self.pid.get(), self.pname.get(), self.pstock.get(), self.pprice.get(), self.ptype.get()))
          con.commit()
          self.display()
          self.clear()
          con.close()
          messagebox.showinfo("Success","Record has been inserted!")
    def display(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        cur.execute("select * from groprod1 order by pid")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Prod_table.delete(*self.Prod_table.get_children())
            for row in rows:
                self.Prod_table.insert('',END,values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row=self.Prod_table.focus()
        contents=self.Prod_table.item(cursor_row)
        row=contents['values']
        self.pid.set(row[0])
        self.pname.set(row[1])
        self.pstock.set(row[2])
        self.pprice.set(row[3])
        self.ptype.set(row[4])

    def update_product(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        cur.execute("UPDATE GROPROD1 SET pname=:pname, pstock=:pstock, pprice=:pprice, ptype=:ptype where pid=:pid", (self.pname.get(), self.pstock.get(), self.pprice.get(), self.ptype.get(),self.pid.get()))
        con.commit()
        self.display()
        self.clear()
        con.close()

    def delete_product(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        cur.execute("delete from groprod1 where pid="+ self.pid.get())
        con.commit()
        con.close()
        self.display()
        self.clear()
        
    def clear(self):
        self.pid.set("")
        self.pname.set("")
        self.pstock.set("")
        self.pprice.set("")
        self.ptype.set("")

    def search_prod(self):
        con=cx_Oracle.connect('system/sim272')
        cur=con.cursor()
        selected=self.search_by.get()
        if selected=="Product Name":
            cur.execute("select * from groprod1 where pname=:1",(self.search_txt.get(), ))
        if selected=="Product ID":
            cur.execute("select * from groprod1 where pid="+ self.search_txt.get())
        if selected=="Product Type":
            cur.execute("select * from groprod1 where ptype=:1",(self.search_txt.get(), ))
        #searched=self.search_txt.get()
        #name=(searched,)
        #cur.execute(sql, name)
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Prod_table.delete(*self.Prod_table.get_children())
            for row in rows:
                self.Prod_table.insert('',END,values=row)
            con.commit()
        con.close()
root=Toplevel()
img=Image.open("gro2.png")
bg= ImageTk.PhotoImage(img)
#bg= PhotoImage(file="gro.png")
my_label=Label(root, image=bg)
my_label.place(x=0, y=0)
ob=Store(root)
root.mainloop()
