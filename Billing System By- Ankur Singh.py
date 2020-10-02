"""
    
 *****Developer Info ****
 Name :     Ankur Singh
 Email :    as797007@gmail.com
 contact :  7000098854
 Date :     02/10/2020

"""

from tkinter import *
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x700+0+0")
        self.root.title("Billing Software| by ankur singh")
        bg_color="#074463"

        title=Label(self.root,text="Billing Software By Ankur Singh",bd=12,relief=GROOVE,fg="white"
        ,bg=bg_color,font=("times new roman",30,"bold"),pady=2).pack(fill="x")
         
        #VARIABLES-----

        #Cosmetics

        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.lotion=IntVar()
        #Grocery

        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #Cold Drinks

        self.maza=IntVar()
        self.coke=IntVar()
        self.limca=IntVar()
        self.mountain_dew=IntVar()
        self.thumbsup=IntVar()
        self.frooti=IntVar()
        
        #Total Product price and text variable
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #CUSTOMER

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()


        #Customer Detail Frame

        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,bg=bg_color,font=("times new roman",15,"bold"),
        fg="gold")
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cname_lbl.grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,font="arial 15",bg="lightyellow",textvariable=self.c_name)
        cname_txt.grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cphn_lbl.grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,font="arial 15",bg="lightyellow",textvariable=self.c_phon)
        cphn_txt.grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl=Label(F1,text="Customer Bill No.",bg=bg_color,fg="white",font=("times new roman",15,"bold"))
        cbill_lbl.grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,font="arial 15",bg="lightyellow",textvariable=self.search_bill)
        cbill_txt.grid(row=0,column=5,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,font="arial 12 bold",fg="white",bg="green",bd=2,relief=GROOVE)
        bill_btn.grid(row=0,column=6,padx=10,pady=5)

       # COSMETICS FRAME

        F2=LabelFrame(self.root,bd=10,relief=GROOVE ,bg=bg_color,text="Cosmetics",fg="gold",font=("times new roman",15,"bold"))
        F2.place(x=5,y=180,width=325,height=380)
         
      
        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        bath_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,bg="lightyellow",textvariable=self.soap,font=("times new roman",16,"bold"),relief=SUNKEN)
        bath_txt.grid(row=0,column=1,padx=10,pady=10)

        Face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        Face_w_lbl.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt=Entry(F2,width=10,bg="lightyellow",textvariable=self.face_wash,font=("times new roman",16,"bold"),relief=SUNKEN)
        Face_w_txt.grid(row=1,column=1,padx=10,pady=10)

        
        Face_c_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        Face_c_lbl.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_c_txt=Entry(F2,width=10,bg="lightyellow",textvariable=self.face_cream,font=("times new roman",16,"bold"),relief=SUNKEN)
        Face_c_txt.grid(row=2,column=1,padx=10,pady=10)
        
        hair_s_lbl=Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        hair_s_lbl.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,bg="lightyellow",textvariable=self.spray,font=("times new roman",16,"bold"),relief=SUNKEN)
        hair_s_txt.grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl=Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        hair_g_lbl.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=10,bg="lightyellow",textvariable=self.gell,font=("times new roman",16,"bold"),relief=SUNKEN)
        hair_g_txt.grid(row=4,column=1,padx=10,pady=10)
        
        Body_lbl=Label(F2,text="Body spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        Body_lbl.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_txt=Entry(F2,width=10,bg="lightyellow",textvariable=self.lotion,font=("times new roman",16,"bold"),relief=SUNKEN)
        Body_txt.grid(row=5,column=1,padx=10,pady=10)
        
        
       
        #GROCERY FRAME

        F3=LabelFrame(self.root,bd=10,relief=GROOVE ,bg=bg_color,text="Groceries",fg="gold",font=("times new roman",15,"bold"))
        F3.place(x=340,y=180,width=325,height=380)
         
      
        G1_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        G1_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        G1_txt=Entry(F3,width=10,bg="lightyellow",textvariable=self.rice,font=("times new roman",16,"bold"),relief=SUNKEN)
        G1_txt.grid(row=0,column=1,padx=10,pady=10)

        G2_lbl=Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        G2_lbl.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        G2_txt=Entry(F3,width=10,bg="lightyellow",textvariable=self.food_oil,font=("times new roman",16,"bold"),relief=SUNKEN)
        G2_txt.grid(row=1,column=1,padx=10,pady=10)

        
        G3_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        G3_lbl.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        G3_txt=Entry(F3,width=10,bg="lightyellow",textvariable=self.daal,font=("times new roman",16,"bold"),relief=SUNKEN)
        G3_txt.grid(row=2,column=1,padx=10,pady=10)
        
        G4_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        G4_lbl.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        G4_txt=Entry(F3,width=10,bg="lightyellow",textvariable=self.wheat,font=("times new roman",16,"bold"),relief=SUNKEN)
        G4_txt.grid(row=3,column=1,padx=10,pady=10)

        G5_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        G5_lbl.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        G5_txt=Entry(F3,width=10,bg="lightyellow",textvariable=self.sugar,font=("times new roman",16,"bold"),relief=SUNKEN)
        G5_txt.grid(row=4,column=1,padx=10,pady=10)
        
        G6_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        G6_lbl.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        G6_txt=Entry(F3,width=10,bg="lightyellow",textvariable=self.tea,font=("times new roman",16,"bold"),relief=SUNKEN)
        G6_txt.grid(row=5,column=1,padx=10,pady=10)


          
        #COLD DRINK FRAME

        F4=LabelFrame(self.root,bd=10,relief=GROOVE ,bg=bg_color,text="Cold Drinks",fg="gold",font=("times new roman",15,"bold"))
        F4.place(x=670,y=180,width=325,height=380)
         
      
        C1_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        C1_lbl.grid(row=0,column=0,padx=10,pady=10,sticky="w")
        C1_txt=Entry(F4,width=10,bg="lightyellow",textvariable=self.maza,font=("times new roman",16,"bold"),relief=SUNKEN)
        C1_txt.grid(row=0,column=1,padx=10,pady=10)

        C2_lbl=Label(F4,text="Coke",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        C2_lbl.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        C2_txt=Entry(F4,width=10,bg="lightyellow",textvariable=self.coke,font=("times new roman",16,"bold"),relief=SUNKEN)
        C2_txt.grid(row=1,column=1,padx=10,pady=10)

        
        C3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        C3_lbl.grid(row=2,column=0,padx=10,pady=10,sticky="w")
        C3_txt=Entry(F4,width=10,bg="lightyellow",textvariable=self.frooti,font=("times new roman",16,"bold"),relief=SUNKEN)
        C3_txt.grid(row=2,column=1,padx=10,pady=10)
        
        C4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        C4_lbl.grid(row=3,column=0,padx=10,pady=10,sticky="w")
        C4_txt=Entry(F4,width=10,bg="lightyellow",textvariable=self.thumbsup,font=("times new roman",16,"bold"),relief=SUNKEN)
        C4_txt.grid(row=3,column=1,padx=10,pady=10)

        C5_lbl=Label(F4,text="Mountain Dew",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        C5_lbl.grid(row=4,column=0,padx=10,pady=10,sticky="w")
        C5_txt=Entry(F4,width=10,bg="lightyellow",textvariable=self.mountain_dew,font=("times new roman",16,"bold"),relief=SUNKEN)
        C5_txt.grid(row=4,column=1,padx=10,pady=10)
        
        C6_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen")
        C6_lbl.grid(row=5,column=0,padx=10,pady=10,sticky="w")
        C6_txt=Entry(F4,width=10,bg="lightyellow",textvariable=self.limca,font=("times new roman",16,"bold"),relief=SUNKEN)
        C6_txt.grid(row=5,column=1,padx=10,pady=10)


        #BILL AREA

        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=280,height=380)

        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        
        #Scroll Bar
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set) 

        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)



        #BUTTON FRAME
       
        F6=LabelFrame(self.root,bd=10,relief=GROOVE ,bg=bg_color,text="Bill Menu",fg="gold",font=("times new roman",15,"bold"))
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1=Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        m1.grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bg="lightyellow")
        m1_txt.grid(row=0,column=1,padx=10,pady=1)

        
        m2=Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        m2.grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bg="lightyellow")
        m2_txt.grid(row=1,column=1,padx=10,pady=1)

        
        m3=Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        m3.grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bg="lightyellow")
        m3_txt.grid(row=2,column=1,padx=10,pady=1)
         
        

        c1=Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        c1.grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bg="lightyellow")
        c1_txt.grid(row=0,column=3,padx=10,pady=1)

        
        c2=Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        c2.grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.grocery_tax,bg="lightyellow")
        c2_txt.grid(row=1,column=3,padx=10,pady=1)

        
        c3=Label(F6,text="Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold"))
        c3.grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,font="arial 10 bold",textvariable=self.cold_drink_tax,bg="lightyellow")
        c3_txt.grid(row=2,column=3,padx=10,pady=1)
         
        #FRAME FOR BUTTONS

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=500,height=105)
        
        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=3,pady=15,width=10,font="arial 11 bold")
        total_btn.grid(row=0,column=0,padx=5,pady=5)
        GBill_btn=Button(btn_F,text="Generate \nBill",command=self.bill_area,bg="cadetblue",fg="white",bd=3,pady=15,width=10,font="arial 11 bold")
        GBill_btn.grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=3,pady=15,width=10,font="arial 11 bold")
        Clear_btn.grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=3,pady=15,width=10,font="arial 11 bold")
        Exit_btn.grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.lotion.get()*180
        self.total_cosmetic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hs_p+
                                    self.c_hg_p+
                                    self.c_bl_p     
                                   )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
            
        self.g_r_p=self.rice.get()*80
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*240
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
        
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))

        self.d_m_p=self.maza.get()*60
        self.d_c_p=self.coke.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_l_p=self.limca.get()*70
        self.d_d_p=self.mountain_dew.get()*75
        self.d_t_p=self.thumbsup.get()*70
        self.total_drinks_price=float(
                                   self.d_m_p+
                                   self.d_c_p+
                                   self.d_f_p+
                                   self.d_l_p+
                                   self.d_d_p+
                                   self.d_t_p
                                   
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))

        self.Total_Bill=float(self.total_cosmetic_price+
                               self.total_grocery_price+
                               self.total_drinks_price+
                               self.c_tax+
                               self.g_tax+
                               self.d_tax
                            )

    def welcome_bill(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\tWelcome To Retail\n")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()} ")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()} ")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phon.get()}")
        self.textarea.insert(END,f"\n-----------------------------")
        self.textarea.insert(END,f"\n Products\t\tQty\tPrice")
        self.textarea.insert(END,f"\n-----------------------------")




    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer details are compulsary")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Has Been Purchased")
        else:    
            self.welcome_bill()
            #Cosmetics
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t{self.c_s_p}")
            if self.face_cream.get()!=0:
                self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t{self.c_fc_p}")
            if self.face_wash.get()!=0:
                self.textarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t{self.c_fw_p}")
            if self.spray.get()!=0:
                self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t{self.c_hs_p}")        
            if self.gell.get()!=0:
                self.textarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t{self.c_hg_p}")
            if self.lotion.get()!=0:
                self.textarea.insert(END,f"\n Body Spray\t\t{self.lotion.get()}\t{self.c_bl_p}")


            #Grocery
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t{self.g_r_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t{self.g_f_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t{self.g_d_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t{self.g_w_p}")        
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t{self.g_s_p}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t{self.g_t_p}")

            #Cold_Drinks
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t{self.d_m_p}")
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t{self.d_c_p}")
            if self.frooti.get()!=0:
                self.textarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t{self.d_f_p}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n Thumbsup\t\t{self.thumbsup.get()}\t{self.d_t_p}")        
            if self.mountain_dew.get()!=0:
                self.textarea.insert(END,f"\n Mountain Dew\t\t{self.mountain_dew.get()}\t{self.d_d_p}")
            if self.limca.get()!=0:
                self.textarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t{self.d_l_p}")

            self.textarea.insert(END,f"\n=============================")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cosmetic Tax\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")
                self.textarea.insert(END,f"\n Total Bill : \t\t Rs. {self.Total_Bill}")
                self.textarea.insert(END,f"\n=============================")
                self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Your Bill Has been Saved Successfully")
        else:
            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")        
    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear the Data?")
        if op>0:
        
            #Cosmetics

            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.lotion.set(0)
            #Grocery

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #Cold Drinks

            self.maza.set(0)
            self.coke.set(0)
            self.limca.set(0)
            self.mountain_dew.set(0)
            self.thumbsup.set(0)
            self.frooti.set(0)
            
            #Total Product price and text variable
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #CUSTOMER

            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()




root=Tk()
obj=Bill_App(root)
root.mainloop()