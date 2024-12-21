from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("BILLING SOFTWARE")

        #=============variables=======================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,10000)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.Product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.Sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        

        #product Categories List
        self.categary=('sellect option','Clothing','Lifestyle','Mobiles')
        self.SubCatClothing=['Pant','T-Shirt','Shirt']
        self.pant=['Levis','Mufti','Spykar']
        self.price_levis=900
        self.price_Mufti=1200
        self.price_Spykar=1500

        self.T_shirt=['polo','Roadstar','Jack&Jones']
        self.price_polo=1700
        self.price_Roadstar=2900
        self.price_Jack=2800

        self.Shirt=['Peter','louis','Park Avenue']
        self.price_peter=1603
        self.price_louis=3900
        self.price_ParkAvenue=2002

        #subcatLifestyle
        self.SubCatLifestyle=["Bath Soap","Face cream","Hair Oil"]
        self.Bath_soap=['lifeBuy','Lux','Santoor','pearl']
        self.price_lifeBuy=30
        self.price_Lux=60
        self.price_Santoor=45
        self.price_pearl=76

        self.Face_Cream=['Ponds','olay','Garnier','Fair&Lovely']
        self.price_Ponds=80
        self.price_olay=120
        self.price_Garnier=160
        self.price_Fair=90

        self.Hair_oil=['Parachute','Jashmin','Bajaj']
        self.price_Parachute=180
        self.price_Jashmin=200
        self.price_Bajaj=240

       # subMobiles
        self.SubCatMobiles=["Iphone","Sumsung","Xione","Realme","One+"]
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_Iphone_x=40000
        self.price_Iphone_11=60000
        self.price_Iphone_12=70000


        self.Sumsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_Sam16=45000
        self.price_sam12=66000
        self.price_sam21=47000
        
        self.price_xiome=['Red11','Redme-12','Redmepro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.Realme=['Realme 11','Realme-12','Realme pro']
        self.price_rel11=25000
        self.price_rel12=30000
        self.price_relpro=40000

        self.onepluse=['onepluse1','onepluse2','onepluse3']
        self.price_one1=70000
        self.price_one2=75000
        self.price_one3=90000
        
        
  
        # Title bannar
        lbltiitle=Label(self.root,text="BILLING SOFTWARE",bg="powder blue",fg="green",bd=40,relief=RIDGE,font=("times new roman",50,"bold"),padx=10,pady=20)
        lbltiitle.pack(side=TOP ,fill=X)
        

        # frame
        Main_Frame =Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        # customer lable frame
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

        # product lable frame
        Pro_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Pro_Frame.place(x=370,y=5,width=620,height=140)

        #categary
        self.lblcategary=Label(Pro_Frame,text="Select Category",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblcategary.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_categary=ttk.Combobox(Pro_Frame,value=self.categary,font=("arial",10,"bold"),width=24,state="readonly")
        self.combo_categary.current(0)
        self.combo_categary.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_categary.bind("<<ComboboxSelected>>",self.Categories)

        #Subcategary
        self.lblSubcategary=Label(Pro_Frame,text="SubCategory",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubcategary.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.comboSubcategary=ttk.Combobox(Pro_Frame,value=[''],font=("arial",10,"bold"),width=24,state="readonly")
        self.comboSubcategary.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.comboSubcategary.bind("<<ComboboxSelected>>", self.Product_Name)




        #product name
        self.lblproduct=Label(Pro_Frame,text="Product Name",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.comboproduct=ttk.Combobox(Pro_Frame,textvariable=self.Product,font=("arial",10,"bold"),width=24,state="readonly")
        self.comboproduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.comboproduct.bind("<<ComboboxSelected>>", self.price)



         #price
        self.lblprice=Label(Pro_Frame,text="Price",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.comboprice=ttk.Combobox(Pro_Frame,textvariable=self.prices,font=("arial",10,"bold"),width=24,state="readonly")
        self.comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)


        #Qty
        self.lblQty=Label(Pro_Frame,text="Qty",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.comboQty = ttk.Entry(Pro_Frame, textvariable=self.qty, font=("arial", 10, "bold"), width=24)
        self.comboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #middle frame for Images
        Middle_Frame=Frame(Main_Frame,bd=10)
        Middle_Frame.place(x=10,y=150,width=980,height=340)

        #images
        lbltiitle=Label(Middle_Frame,text="WELCOME  TO  A  MART",bg="powder blue",fg="black",bd=40,relief=RIDGE,font=("times new roman",50,"bold"),padx=10,pady=20,height=40)
        lbltiitle.pack(side=TOP ,fill=X)


       
      
        #search Bill number  area

        search_Frame=Frame(Main_Frame,bd=2,bg="white")
        search_Frame.place(x=1020,y=13,width=450,height=40)

        self.lblBill=Label(search_Frame,text="Bill Number",font=("arial",12,"bold"),bg="red",fg="white")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=2)

        self.text_Enterysearch=ttk.Entry(search_Frame,textvariable=self.search_bill,font=("arial",10,"bold"),width=24)
        self.text_Enterysearch.grid(row=0,column=1,sticky=W,padx=2)

        self.Btn_Search=Button(search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",width=16,cursor="hand2")
        self.Btn_Search.grid(row=0,column=2)

        # Right fream bill area

        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)


        # Scroll bar Right  side bill area
        Scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=Scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        Scroll_y.pack(side=RIGHT,fill=Y)
    
        self.textarea.pack(fill=BOTH,expand=1)


         # Bill counter lable frame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1500,height=120)

        self.lblSubtotal=Label(Bottom_Frame,text="Sub Total",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblSubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entrySubtotal=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.entrySubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)


        self.lbltax=Label(Bottom_Frame,text=" Gov Tax",font=("arial",12,"bold"),bg="white",bd=4)
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.text_tax=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.text_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)


        self.lblAmmount=Label(Bottom_Frame,text="Total Ammount",font=("arial",12,"bold"),bg="white",bd=4)
        self.lblAmmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.text_ammount=ttk.Entry(Bottom_Frame,font=("arial",10,"bold"),width=24)
        self.text_ammount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddtocart = Button(Btn_Frame, command=self.AddIteam, height=2, text="Add To Cart", font=("arial", 15, "bold"), bg="orangered", fg="white", width=15, cursor="hand2")
        self.BtnAddtocart.grid(row=0, column=0)

        self.Btnganerate=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnganerate.grid(row=0,column=1)

        self.Btnsave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnsave.grid(row=0,column=3)


        self.Btnprint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnprint.grid(row=0,column=5)

        self.Btnclear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnclear.grid(row=0,column=7)


        self.Btnexit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",width=15,cursor="hand2")
        self.Btnexit.grid(row=0,column=9)
        self.welcome()

        self.l=[]

    #==========Function Declaration=======
    def welcome(self):
       self.textarea.delete(1.0,END)
       self.textarea.insert(END,"\t Welcome to A Mart ")
       self.textarea.insert(END,f"\n Bill  Number:{self.bill_no.get()}")
       self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
       self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
       self.textarea.insert(END,f"\n Customer Email :{self.c_email.get()}")

       self.textarea.insert(END,"\n==================*******========================")
       self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
       self.textarea.insert(END,"\n==================*******=========================\n")
      


    def AddIteam(self):
      print("AddItem method called")  # Check if the method is being called
      print("Product:", self.Product.get())
      print("Price:", self.prices.get())
      print("Quantity:", self.qty.get())  
      Tax = 1
      price = self.prices.get()
      qty = self.qty.get()
      total_price = price * qty
      self.l.append(total_price)

      if self.Product.get() == "":
            messagebox.showerror("Error", "Please Select Product Name")
      else:
            self.textarea.insert(END, f"\n {self.Product.get()}\t\t{qty}\t\t{total_price}")
            self.Sub_total.set(sum(self.l))
            self.tax_input.set((((sum(self.l)) - price) * Tax) / 1000)
            self.total.set(((sum(self.l)) + ((((sum(self.l)) - price) * Tax) / 100)))
    def gen_bill(self):
       if not self.l:
        messagebox.showerror("Error", "No items in the cart. Please add items.")
        return
       self.textarea.delete("1.0", END)
       self.welcome()
       
        # Loop through the list of items and insert them into the text area
       for item in self.l:
          self.textarea.insert(END, f"\n {self.Product.get()}\t\t{self.qty.get()}\t\t{item}")
          subtotal = sum(self.l)
          self.Sub_total.set(subtotal)
          tax = 0.1 * subtotal
          self.tax_input.set(tax)
          self.entrySubtotal.delete(0, END)
          self.entrySubtotal.insert(0, subtotal)

          # Calculate government tax (assuming 10% tax)
          gov_tax = 0.1 * subtotal
          self.text_tax.delete(0, END)
          self.text_tax.insert(0, gov_tax)
    
    
    # Calculate total amount (subtotal + tax)
          total_amount = subtotal + tax
          self.text_ammount.delete(0, END)
          self.text_ammount.insert(0, total_amount)
          self.total.set(total_amount)
    
    # Insert subtotal, tax, and total amount into the bill area
          self.textarea.insert(END, "\n==================*******=========================")
          self.textarea.insert(END, f"\n Sub Total:\t\t\t{subtotal} ")
          self.textarea.insert(END, f"\n Tax Amount:\t\t\t{tax} ")
          self.textarea.insert(END, f"\n Total Amount:\t\t\t{total_amount} ")
          self.textarea.insert(END, "\n==================*******=========================")
    def save_bill(self):
       op=messagebox.askyesno("Save Bill","Do you want save the bill")
       if op>0:
          self.bill_data=self.textarea.get(1.0,END)
          f1=open('bills/'+str(self.bill_no.get())+"txt",'w')
          f1.write(self.bill_data)
          op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()}saved successfully")
          f1.close()
    def iprint(self):
       content = self.textarea.get(1.0, "end-1c")
    
    # Create a temporary file with a .txt extension
       with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
        temp_file.write(content.encode('utf-8'))  # Write content to the file
    
        # Get the file path
       filename = temp_file.name
    
    # Print the file
       os.startfile(filename, "print")

    def find_bill(self):
       found="no"
       for i in os.listdir("bills/"):
          if i.split('.')[0]==self.search_bill.get():
             f1=open(f'bills/{i}','r')
             self.textarea.delete(1.0,END)
             for d in f1:
                self.textarea.insert(END,d)
             f1.close()
             found="Yes"
       if found=="no":
          messagebox.showerror("Error","Invalid Bill No.")
    def clear(self):
       self.textarea.delete(1.0,END)
       self.c_name.set("")
       self.c_phone.set("")
       self.bill_no.set("")
       z=random.randint(1000,10000)
       self.bill_no.set(str(X))
       self.c_email.set("")
       self.search_bill.set("")
       self.Product.set("")
       self.prices.set("")
       self.qty.set("")
       self.Sub_total.set("")
       self.l=[0]
       self.tax_input.set("")
       self.total.set("")
       self.welcome()
       
            
    def Categories(self, event=""):
        selected_category = self.combo_categary.get()
        if selected_category == "Clothing":
            self.comboSubcategary.config(values=self.SubCatClothing)
        elif selected_category == "Lifestyle":
            self.comboSubcategary.config(values=self.SubCatLifestyle)
        elif selected_category == "Mobiles":
            self.comboSubcategary.config(values=self.SubCatMobiles)
        else:
            self.comboSubcategary.config(values=[])  # If none selected or 'sellect option'

        self.comboSubcategary.current(0)  # Set default selection

    def Product_Name(self,event=""):
        print("Product_Name method called")  # Add this line for debugging
        selected_subcategory = self.comboSubcategary.get()
        if selected_subcategory == "Pant":
            print("Pant:", self.pant)
            self.comboproduct.config(values=self.pant)
            self.comboproduct.current(0)
        elif selected_subcategory == "T-Shirt":
            print("T-Shirt:", self.T_shirt)
            self.comboproduct.config(values=self.T_shirt)
            self.comboproduct.current(0)
        elif selected_subcategory == "Shirt":
            print("Shirt:", self.Shirt)
            self.comboproduct.config(values=self.Shirt)
            self.comboproduct.current(0)
        #lifestyle
         # For Lifestyle category
        elif selected_subcategory == "Bath Soap":
           self.comboproduct.config(values=self.Bath_soap)
           self.comboproduct.current(0)
        elif selected_subcategory == "Face cream":
           self.comboproduct.config(values=self.Face_Cream)
           self.comboproduct.current(0)
        elif selected_subcategory == "Hair Oil":
           self.comboproduct.config(values=self.Hair_oil)
           self.comboproduct.current(0)

    # For Mobiles category
        elif selected_subcategory == "Iphone":
            self.comboproduct.config(values=self.Iphone)
            self.comboproduct.current(0)
        elif selected_subcategory == "Sumsung":
            self.comboproduct.config(values=self.Sumsung)
            self.comboproduct.current(0)
        elif selected_subcategory == "Xione":
            self.comboproduct.config(values=self.xiome)
            self.comboproduct.current(0)
        elif selected_subcategory == "Realme":
            self.comboproduct.config(values=self.Realme)
            self.comboproduct.current(0)
        elif selected_subcategory == "One+":
            self.comboproduct.config(values=self.onepluse)
            self.comboproduct.current(0)

    def price(self, event=""):
    # pant
      if self.comboproduct.get() == "Levis":
        self.comboprice.set(self.price_levis)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)
      
      if self.comboproduct.get() == "Mufti":
        self.comboprice.set(self.price_Mufti)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Spykar":
        self.comboprice.set(self.price_Spykar)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      # T-shirt
      if self.comboproduct.get() == "polo":
        self.comboprice.set(self.price_polo)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Roadstar":
        self.comboprice.set(self.price_Roadstar)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Jack&Jones":
        self.comboprice.set(self.price_Jack)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      # shirt

      if self.comboproduct.get() == "Peter":
        self.comboprice.set(self.price_peter)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "louis":
        self.comboprice.set(self.price_louis)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Park Avenue":
        self.comboprice.set(self.price_ParkAvenue)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      #soap

      if self.comboproduct.get() == "lifeBuy":
        self.comboprice.set(self.price_lifeBuy)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Pear":
        self.comboprice.set(self.price_pearl)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Lux":
        self.comboprice.set(self.price_Lux)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Santoor":
        self.comboprice.set(self.price_Santoor)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      #Face_Cream=['Ponds','olay','Garnier','Fair&Lovely']

      if self.comboproduct.get() == "Ponds":
        self.comboprice.set(self.price_Ponds)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "olay":
        self.comboprice.set(self.price_olay)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Garnier":
        self.comboprice.set(self.price_Garnier)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Fair&Lovely":
        self.comboprice.set(self.price_Fair)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      # Hair oil==['Parachute','Jashmin','Bajaj']
      if self.comboproduct.get() == "Parachute":
        self.comboprice.set(self.price_Parachute)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Jashmin":
        self.comboprice.set(self.price_Jashmin)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Bajaj":
        self.comboprice.set(self.price_Bajaj)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      #Iphone=['Iphone_X','Iphone_11','Iphone_12']

      if self.comboproduct.get() == "Iphone_X":
        self.comboprice.set(self.price_Iphone_x)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Iphone_11":
        self.comboprice.set(self.price_Iphone_11)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Iphone_12":
        self.comboprice.set(self.price_Iphone_12)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      #samsung=['Samsung M16 ','Samsung M12','Samsung M21']


      if self.comboproduct.get() == "Samsung M16":
        self.comboprice.set(self.price_Sam16)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Samsung M12":
        self.comboprice.set(self.price_sam12)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Samsung M21":
        self.comboprice.set(self.price_sam21)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)
      
      #self.price_xiome=['Red11','Redme-12','Redmepro']
    
      if self.comboproduct.get() == "Red11":
        self.comboprice.set(self.price_r11)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Redme-12":
        self.comboprice.set(self.price_r12)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Redmepro":
        self.comboprice.set(self.price_rpro)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

       #self.Realme=['Realme 11','Realme-12','Realme pro']

      if self.comboproduct.get() == "Realme 11":
        self.comboprice.set(self.price_rel11)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Realme-12":
        self.comboprice.set(self.price_rel12)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "Realme pro":
        self.comboprice.set(self.price_relpro)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      #self.onepluse=['onepluse1','onepluse2','onepluse3']


      if self.comboproduct.get() == "onepluse1":
        self.comboprice.set(self.price_one1)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "onepluse2":
        self.comboprice.set(self.price_one2)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)

      if self.comboproduct.get() == "onepluse3":
        self.comboprice.set(self.price_one3)
        self.comboprice.current(0)
      self.comboQty.config(state="normal") 
      self.qty.set(1)




















      












      












if __name__=="__main__":
    root=Tk()
    obj=Bill_app(root)
    root.mainloop()