Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lblmobile=Label(Cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lblmobile.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblName=Label(Cust_Frame,text="Customer Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblName.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.textName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("arial",11,"bold"),width=24)
        self.textName.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblEmail=Label(Cust_Frame,text="Email",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.textEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("arial",11,"bold"),width=24)
        self.textEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
