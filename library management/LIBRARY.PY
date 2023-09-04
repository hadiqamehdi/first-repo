from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import datetime
import tkinter

class libraryManagement:
    def __init__(self,root):
        self.root=root
        self.root.title(" library management system")
        self.root.geometry("1590x850+0+0")


        #-------------------------variable---------------------
        # self.number=StringVar()
        self.member=StringVar()
        self.prnno=StringVar()
        
        self.member=StringVar()
        self.firstname=StringVar()
        self.lastname=StringVar()
        self.address=StringVar()
        self.postcode=StringVar()
        self.phno=StringVar()
        self.bookid=StringVar()
        self.booktitle=StringVar()
        self.authername=StringVar()
        self.dateborrowed=StringVar()
        self.fine=StringVar()
        self.datedue=StringVar()
        self.dateoverdue=StringVar()
        self.actualprice=StringVar()
        

        lb_title=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM", bg="dark red",fg="white",relief=RIDGE, font=("times new roman",50,"bold"),padx=2,pady=6)
        lb_title.pack(side=TOP,fill=X)
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="Light grey")
        frame.place(x=0,y=130,width=1590,height=400)
        #--------DATAFRAMELEFT-----------
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBERSHIP INFORMATION", bg="Light grey",fg="BLACK",relief=RIDGE, font=("arial",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        a=self.number()
        llb_number=Label(DataFrameLeft,bg="Light grey", fg="black",text=" ENTRY NUMBER:",font=("times new roman",15,"bold"),padx=2,pady=6)
        llb_number.grid(row=0,column=0,sticky=W)
        txtno = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.numberr,width=29, state='disabled')
        txtno.grid(row=0,column=1,)


        lb_member=Label(DataFrameLeft,bg="Light grey", fg="black",text="MEMBER TYPE:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_member.grid(row=1,column=0,sticky=W)

        commember=ttk.Combobox(DataFrameLeft,font=("times new roman",15,"bold"),textvariable= self.member,width=27,state="readonly")
        commember["value"]=("Admin staff","Student","Lecturer")
        commember.grid(row=1,column=1)


        lb_prno=Label(DataFrameLeft,bg="Light grey", fg="black",text="PRN NUMBER:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_prno.grid(row=2,column=0,sticky=W)
        txtprno = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.prnno,width=29)
        txtprno.grid(row=2,column=1,)

        # lb_idno=Label(DataFrameLeft,bg="dark blue", fg="white",text="ID NUMBER:",font=("times new roman",15,"bold"),padx=2,pady=6)
        # lb_idno.grid(row=3,column=0,sticky=W)
        # txtidno = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.id,width=29)
        # txtidno.grid(row=3,column=1,)

        lb_Fname=Label(DataFrameLeft,bg="Light grey", fg="black",text="FIRST NAME:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_Fname.grid(row=3,column=0,sticky=W)
        txtfname = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.firstname,width=29)
        txtfname.grid(row=3,column=1,)

        lb_LNAME=Label(DataFrameLeft,bg="Light grey", fg="black",text="LAST NAME: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_LNAME.grid(row=4,column=0,sticky=W)
        txtLN = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.lastname,width=29)
        txtLN.grid(row=4,column=1,)

        lb_ADDRESS=Label(DataFrameLeft,bg="Light grey", fg="black",text="ADDRESS:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_ADDRESS.grid(row=5,column=0,sticky=W)
        txtADD = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.address,width=29)
        txtADD.grid(row=5,column=1,)

        lb_SCODE=Label(DataFrameLeft,bg="Light grey", fg="black",text="POST CODE:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_SCODE.grid(row=6,column=0,sticky=W)
        txtSCODE = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.postcode,width=29)
        txtSCODE.grid(row=6,column=1,)

        lb_no=Label(DataFrameLeft,bg="Light grey", fg="black",text="PHONE  NUMBER:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_no.grid(row=7,column=0,sticky=W)
        txtno = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.phno,width=29)
        txtno.grid(row=7,column=1,)

        lb_ID=Label(DataFrameLeft,bg="Light grey", fg="black",text="BOOK ID:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_ID.grid(row=0,column=2,sticky=W)
        txtID = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.bookid,width=29)
        txtID.grid(row=0,column=3,)


        lb_BNAME=Label(DataFrameLeft,bg="Light grey", fg="black",text="BOOK NAME:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_BNAME.grid(row=1,column=2,sticky=W)
        txtBNAME = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.booktitle,width=29)
        txtBNAME.grid(row=1,column=3,)

        lb_AN=Label(DataFrameLeft,bg="Light grey", fg="black",text="AUTHER NAME:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_AN.grid(row=2,column=2,sticky=W)
        txtAN = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.authername,width=29)
        txtAN.grid(row=2,column=3,)

        lb_DA=Label(DataFrameLeft,bg="Light grey", fg="black",text="DATE BORROWED:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_DA.grid(row=3,column=2,sticky=W)
        txtDA = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.dateborrowed,width=29)
        txtDA.grid(row=3,column=3,)

        lb_FINE=Label(DataFrameLeft,bg="Light grey", fg="black",text="FINE: ",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_FINE.grid(row=4,column=2,sticky=W)
        txtFINE= Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.fine,width=29)
        txtFINE.grid(row=4,column=3,)

        lb_DUE=Label(DataFrameLeft,bg="Light grey", fg="black",text="DATE DUE:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_DUE.grid(row=5,column=2,sticky=W)
        txtDUE = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.datedue,width=29)
        txtDUE.grid(row=5,column=3,)

        lb_DOD=Label(DataFrameLeft,bg="Light grey", fg="black",text="DATE OVER DUE:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_DOD.grid(row=6,column=2,sticky=W)
        txtDOD = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.dateoverdue,width=29)
        txtDOD.grid(row=6,column=3,)

        lb_AC=Label(DataFrameLeft,bg="Light grey", fg="black",text="ACTUAL PRICE:",font=("times new roman",15,"bold"),padx=2,pady=6)
        lb_AC.grid(row=7,column=2,sticky=W)
        txtAC = Entry(DataFrameLeft, font=("times new roman", 15, "bold"),textvariable=self.actualprice,width=29)
        txtAC.grid(row=7,column=3,)
   
       #====================DATA FRAME RIGHT=============================
        DataFrameRight=LabelFrame(frame,text="BOOK DETAILS", bg="Light grey",fg="BLACK",relief=RIDGE, font=("arial",12,"bold"),padx=2,pady=6)
        DataFrameRight.place(x=910,y=5,width=620,height=350)

        self.txtbox=Text(DataFrameRight,font=("red",12,"bold"),width =32,height=15,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)
        lstscrollbar=Scrollbar(DataFrameRight)
        lstscrollbar.grid(row=0,column=1,sticky="ns")
         #-------------book--------------
        a=self.fetchdatabook()
        b=self.booksrow()
        
        # print("hhhhhhhhhhhhhhhhhhhhhhhh",b)
        # for i in b:
        #     print("hhhhhhhhhhhhhhhhhhhaaaaaaaaaaaaa,",i)
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM books")
        rows = my_cursor.fetchall()
        bookdetails=[]
        for row in rows:
            bookdetails.append(row)
        print("list me hogya",bookdetails)
        for i in bookdetails:
            print("hogyaaaaaaa",i)
        def selectbook(event=""):
            selected_indices = listbox.curselection()
            if len(selected_indices) > 0:
                index = selected_indices[0]  # Get the first selected index
                value = listbox.get(index)  # Get the value at the selected index
                print("ye horahaaa he print",value)
                # if value == "tfios":
                    # self.bookid.set("hadiqa")
                for i in bookdetails:
                    print(i)
                    if value in i:
                        print("kya krri hu baji",value)
                    # if "tfios" in i:
                        print(bookdetails[0])
                        self.bookid.set(i[0])
                        self.booktitle.set(i[1])
                        self.authername.set(i[2])
                        self.actualprice.set(i[4])
                        self.fine.set(i[3])
                        d1=datetime.date.today()
                        print(d1)
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed.set(d1)
                        self.datedue.set(d3)
                        self.dateoverdue.set("no")

            
            
        
        
        listboks=list(a)
        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width =30,height=15)
        listbox.bind("<<ListboxSelect>>",selectbook)
        listbox.grid(row=0,column=0,padx=4)
        lstscrollbar.config(command=listbox.yview)
        
        

        for item in listboks:
            listbox.insert(END,item)

        self.booksrow()
       # ==========================================BUTTONS FRAME========
        frame_BUTTON=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="Light grey")
        frame_BUTTON.place(x=0,y=530,width=1560,height=70)

        btnadddata=Button(frame_BUTTON,command=self.adddata,text="ADD DATA",font=("arial",12,"bold"),width =24,bg="dark red",fg="white")
        btnadddata.grid(row=0,column=0)

        btnsdata=Button(frame_BUTTON,command=self.showdata,text="SHOW DATA",font=("arial",12,"bold"),width =24,bg="dark red",fg="white")
        btnsdata.grid(row=0,column=1)

        btnupdata=Button(frame_BUTTON,command=self.updatemember,text="UPDATE",font=("arial",12,"bold"),width =24,bg="dark red",fg="white")
        btnupdata.grid(row=0,column=2)

        btndeldata=Button(frame_BUTTON,command=self.delete,text="DELETE",font=("arial",12,"bold"),width =24,bg="dark red",fg="white")
        btndeldata.grid(row=0,column=3)

        btnresdata=Button(frame_BUTTON,command=self.reset,text="RESET",font=("arial",12,"bold"),width =24,bg="dark red",fg="white")
        btnresdata.grid(row=0,column=4)

        btnexitdata=Button(frame_BUTTON,command=self.exit,text="EXIT",font=("arial",12,"bold"),width =24,bg="darkred",fg="white")
        btnexitdata.grid(row=0,column=5)

        # ==========================================INFORMATION FRAME========
        frame_INFO=Frame(self.root,bd=12,relief=RIDGE,padx=30,bg="light grey")
        frame_INFO.place(x=0,y=600,width=1590,height=230)

        table_frame= Frame(frame_INFO,bd=6,relief=RIDGE,bg="light grey")
        table_frame.place(x=0,y=2,width=1510,height=200)
        xscroll=ttk.Scrollbar( table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar( table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(table_frame,column=("ENTRY NUMBER","MEMBER TYPE","PRN NUMBER","FIRST NAME","LAST NAME","ADDRESS","POSTCODE","PHONE NUMBER","BOOK ID","BOOK NAME","AUTHER NAME","DATE BORROWED","FINE","DATE DUE","DATE OVER DUE","ACTUAL PRICE"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("ENTRY NUMBER",text="ENTRY NUMBER")
        self.library_table.heading("MEMBER TYPE",text="MEMBER TYPE")
        self.library_table.heading("PRN NUMBER",text="PRN NUMBER")
        # self.library_table.heading("ID NUMBER",text="ID NUMBER")
        self.library_table.heading("FIRST NAME",text="FIRST NAME")
        self.library_table.heading("LAST NAME",text="LAST NAME")
        self.library_table.heading("ADDRESS",text="ADDRESS")
        self.library_table.heading("POSTCODE",text="POSTCODE")
        self.library_table.heading("PHONE NUMBER",text="PHONE NUMBER")
        self.library_table.heading("BOOK ID",text="BOOK ID")
        self.library_table.heading("BOOK NAME",text="BOOK NAME")
        self.library_table.heading("AUTHER NAME",text="AUTHER NAME")
        self.library_table.heading("DATE BORROWED",text="DATE BORROWED")
        self.library_table.heading("FINE",text="FINE")
        self.library_table.heading("DATE DUE",text="DATE DUE")
        self.library_table.heading("DATE OVER DUE",text="DATE OVER DUE")
        self.library_table.heading("ACTUAL PRICE",text="ACTUAL PRICE")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("ENTRY NUMBER",width=100)
        self.library_table.column("MEMBER TYPE",width=100)
        self.library_table.column("PRN NUMBER",width=100)
        # self.library_table.column("ID NUMBER",width=100)
        self.library_table.column("FIRST NAME",width=100)
        self.library_table.column("LAST NAME",width=100)
        self.library_table.column("ADDRESS",width=100)
        self.library_table.column("POSTCODE",width=100)
        self.library_table.column("PHONE NUMBER",width=100)
        self.library_table.column("BOOK ID",width=100)
        self.library_table.column("BOOK NAME",width=100)
        self.library_table.column("AUTHER NAME",width=100)
        self.library_table.column("DATE BORROWED",width=100)
        self.library_table.column("FINE",width=100)
        self.library_table.column("DATE DUE",width=100)
        self.library_table.column("DATE OVER DUE",width=100)
        self.library_table.column("ACTUAL PRICE",width=100)
        self.fetchdata()
        self.library_table.bind("<ButtonRelease-1>",self.getdata)


    def new_method(self, selectbook):
        return selectbook
    def adddata(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="hadiqa123",database="new_schema")
        # my_cursor=conn.cursor()
        # my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( self.number.get(),self.member.get()
        #                                                                                                ,self.prnno.get()
                                                                                                       
        #                                                                                                , self.firstname.get()
        #                                                                                                , self.lastname.get()
        #                                                                                                 ,self.address.get()
        #                                                                                                 ,self.postcode.get()
        #                                                                                                 ,self.phno.get()
        #                                                                                                 ,self.bookid.get()
        #                                                                                                 ,self.booktitle.get()
        #                                                                                                , self.authername.get()
        #                                                                                                 ,self.dateborrowed.get()
        #                                                                                                 ,self.fine.get()
        #                                                                                                 ,self.datedue.get()
        #                                                                                                 ,self.dateoverdue.get()
        #                                                                                                 ,self.actualprice.get() ) )
        
        # rows=my_cursor.fetchall()
        # myy_cursor=conn.cursor()
        # myyy_cursor=conn.cursor()
        # myyy_cursor.execute("select firstname from ")
        # rows=my_cursor.fetchall()
        # myy_cursor.execute("insert into members values(%s,%s,%s,%s,%s,%s,%s)",( self.member.get()
        #                                                                                                ,self.prnno.get()
                                                                                                       
        #                                                                                                , self.firstname.get()
        #                                                                                                , self.lastname.get()
        #                                                                                                 ,self.address.get()
        #                                                                                                 ,self.postcode.get()
        #                                                                                                 ,self.phno.get()))
        self.memberid()
        messagebox.showinfo("success","member inserterd successfully")
        conn.commit()
        self.fetchdata()
        conn.close()
        # messagebox.showinfo("success","member inserterd successfully")

    def fetchdata(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="hadiqa123",database="new_schema")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()
        # print(rows,"ye araha ")
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,value=i)
            conn.commit()
        conn.close()
    def getdata(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item( cursor_row)
        row=content['values']  
        self.numberr.set(row[0])
        self.member.set(row[1])
        self.prnno.set(row[2])
        
        self.firstname.set(row[3])
        self.lastname.set(row[4])
        self.address.set(row[5])
        self.postcode.set(row[6])
        self.phno.set(row[7])
        self.bookid.set(row[8])
        self.booktitle.set(row[9])
        self.authername.set(row[10])
        self.dateborrowed.set(row[11])
        self.fine.set(row[12])
        self.datedue.set(row[13])
        self.dateoverdue.set(row[14])
        self.actualprice.set(row[15])
    



    def fetchdatabook(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="hadiqa123",database="new_schema")
        my_cursor=conn.cursor()
        my_cursor.execute("select bookname from books")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            i=rows
            result = tuple(item[0] for item in i)
            print(result)
            return (result)
            
        conn.commit()
        conn.close()
    def booksrow(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM books")
        rows = my_cursor.fetchall()
        for i in range(4):
            for row in rows:
                return(row)
                print(row)
            
            

        conn.commit()
        conn.close()
    def showdata(self):
        self.txtbox.insert(END,"Memeber Type: \t\t"+self.member.get()+"\n")
        self.txtbox.insert(END,"id: \t\t"+self.firstname.get()+"\n")
        self.txtbox.insert(END,"date borrowed: \t\t"+self.dateborrowed.get()+"\n")
        self.txtbox.insert(END,"book: \t\t"+self.booktitle.get()+"\n")
        self.txtbox.insert(END,"auther name: \t\t"+self.authername.get()+"\n")
        self.show_detail()
    def reset(self):
        b=self.numberr.get()
        b=int(b)
        self.numberr.set(b+1)
        self.member.set(""),
        self.prnno.set(""),
        
        self.member.set(""),
        self.firstname.set(""),
        self.lastname.set(""),
        self.address.set(""),
        self.postcode.set(""),
        self.phno.set(""),
        self.bookid.set(""),
        self.booktitle.set(""),
        self.authername.set(""),
        self.dateborrowed.set(""),
        self.fine.set(""),
        self.datedue.set(""),
        self.dateoverdue.set(""),
        self.actualprice.set(""),
        self.txtbox.delete("1.0",END)
        

    def exit(self):
        iexit=tkinter.messagebox.askyesno("library management system","do you want to exit")
        if iexit>0:
            self.root.destroy()
            return
    # def update(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute()
    def number(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
       
        my_cursor.execute("select idlib from library")
        rows=my_cursor.fetchall()
        print (rows)
        if len (rows)==0:
            self.numberr=StringVar()
            self.numberr.set("1")
        else:
            self.numberr=StringVar()
            self.numberr.set(len(rows)+1)
        conn.commit()
        conn.close()
    def memberid(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
       
        my_cursor.execute("select prnnumber from members")
        rows=my_cursor.fetchall()
        print ("hellllo brother",rows)
        if int(self.prnno.get())not in rows:
            myy_cursor=conn.cursor()
            myy_cursor.execute("insert into members values(%s,%s,%s,%s,%s,%s,%s,%s)",( self.member.get()
                                                                                                       ,self.prnno.get()
                                                                                                       
                                                                                                       , self.firstname.get()
                                                                                                       , self.lastname.get()
                                                                                                        ,self.address.get()
                                                                                                        ,self.postcode.get()
                                                                                                        ,self.phno.get(),
                                                                                                        self.bookid.get()))
        else:
            messagebox.showinfo("success","member inserterd successfully")
        conn.commit()
        self.fetchdata()
        conn.close()
    def show_detail(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( self.numberr.get(),self.member.get()
                                                                                                       ,self.prnno.get()
                                                                                                       
                                                                                                       , self.firstname.get()
                                                                                                       , self.lastname.get()
                                                                                                        ,self.address.get()
                                                                                                        ,self.postcode.get()
                                                                                                        ,self.phno.get()
                                                                                                        ,self.bookid.get()
                                                                                                        ,self.booktitle.get()
                                                                                                       , self.authername.get()
                                                                                                        ,self.dateborrowed.get()
                                                                                                        ,self.fine.get()
                                                                                                        ,self.datedue.get()
                                                                                
                                                                                                        ,self.dateoverdue.get()
                                                                                                        ,self.actualprice.get() ) )
        conn.commit()
        self.fetchdata()
        conn.close()
        
    def update(self):
        a=self.prnno.get()
        b=int(a)
        id=self.numberr.get()
        id=int(id)
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
       
        my_cursor.execute("update library set member=%s,prnnumber=%s,first=%s,last=%s,address=%s,postcode=%s,phonenumber=%s,bookid=%s,booktitle=%s,authername=%s,dateborrowed=%s,fine=%s,datedue=%s,dateoverdue=%s,actualprice=%s where idlib=%s",( self.member.get()
                                                                                                        ,b
                                                                                                        
                                                                                                        , self.firstname.get()
                                                                                                        , self.lastname.get()
                                                                                                            ,self.address.get()
                                                                                                            ,self.postcode.get()
                                                                                                            ,self.phno.get()
                                                                                                            ,self.bookid.get()
                                                                                                            ,self.booktitle.get()
                                                                                                        , self.authername.get()
                                                                                                            ,self.dateborrowed.get()
                                                                                                            ,self.fine.get()
                                                                                                            ,self.datedue.get()
                                                                                    
                                                                                                            ,self.dateoverdue.get()
                                                                                                            ,self.actualprice.get(),
                                                                                                             id ) )
        conn.commit()
        self.fetchdata()
        self.reset()
        conn.close()
    
        # messagebox.showinfo("Success", "Member has been updated")

    def updatemember(self):
        a=self.prnno.get()
        b=int(a)
        print(type(self.postcode.get()))

        print("ye hai uski value",a)
        conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
        my_cursor = conn.cursor()
        
        my_cursor.execute("UPDATE members SET membertype=%s, firstname=%s, lastname=%s, address=%s, postcode=%s, phoneno=%s, bookid=%s WHERE prnnumber=%s",
                  (self.member.get(), self.firstname.get(), self.lastname.get(), self.address.get(), self.postcode.get(), self.phno.get(), self.bookid.get(), b))
        self.update()
        messagebox.showinfo("success","Member has been updated")

        self. number()
        
        conn.commit()
        self.fetchdata()
        
        self.reset()
        self.adddata()
        self. show_detail()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated")

    def delete(self):
        if self.numberr.get()=="":
            messagebox.showerror("error,first select the member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="hadiqa123", database="new_schema")
            my_cursor = conn.cursor()
            query="delete from library  where idlib=%s"
            value=(self.numberr.get())
            value=int(value)
            value=(value,)
            my_cursor.execute(query,value)
            conn.commit()
            self.fetchdata()
            self.reset()
            conn.close()
            messagebox.showinfo("success","member as been deleted")
root=Tk()
obj=libraryManagement(root)
root.mainloop()
