from tkinter import *
from tkinter import messagebox
import sys
from Graphs import *
import mysql.connector as m
from treeview_sql import *

c=m.connect(host="localhost",user="root",passwd="Ashwath03",database="buckstracker")
cur=c.cursor()

#Deletion of Account
def deleteaccfn():
    global username
    delete_win=Tk()
    delete_win.geometry('350x125')

    signdel=Label(delete_win,text="DELETE ACCOUNT",font=("Verdana",13,"bold"),fg="navy").grid(row=0,column=1,sticky="w")

    name=Label(delete_win,text="Enter username : ",font=("Verdana",10),fg="navy").grid(row=1,column=0)
    username=Entry(delete_win)
    username.grid(row=1,column=1)


    pswd=Label(delete_win,text="Enter password : ",font=("Verdana",10),fg="navy").grid(row=2,column=0)
    password=Entry(delete_win,show='*')
    password.grid(row=2,column=1)

    #Checking for correct username/password
    def checkdel():
        a=username.get()
        b=password.get()

        if a!="" and b!="":
            cur.execute("select * from login where username='"+ a +"'")
            data=cur.fetchall()

            # Verifying username, then password to delete acc
            if len(data)==0:
                messagebox.showerror("Notice","You have not entered a registered username")
            elif data[0][0]==a and data[0][1]==b:
                cur.execute("delete from login where username= '" +a+ "' and password= '" +b+ "'")
                c.commit()
                cur.execute("delete from income where name= '"+a+"'")
                c.commit()
                cur.execute("delete from expenditure where name= '" +a+"'")
                c.commit()
                messagebox.showinfo("Message","Successfully deleted account")
                delete_win.destroy()                
            else:
                messagebox.showerror("Notice","Your password or username is not entered correctly")
                
        elif a=="" and b=="":
            messagebox.showerror("Notice","You have not entered a username or password")

    label_dummy=Label(delete_win,text="").grid(row=4,column=0)

    button_del=Button(delete_win,text="DELETE ACCOUNT",font=("Calibre",12,"bold"),fg="navy",command= checkdel)
    button_del.grid(row=5,column=1,sticky="w")

#Login Screen
def loginwindow():
    global login,us
    login=Tk()
    login.geometry('400x175')
    login.title("LOGIN SCREEN")
    label1=Label(login,text="Do you want to login or signup or delete account ?",font=("Verdana",10)).place(x=50,y=0)
loginwindow()

#Login function
def signinfunc():
    global us,signin,login,mainname
    #us: String variable for username while mainame is value of us
    signin=Tk()
    signin.geometry("300x140")
    signin.title("SIGNIN SCREEN")

    sign=Label(signin,text="LOGIN",font=("Verdana",13,"bold"),fg="indian red").grid(row=0,column=1,sticky="w")

    name=Label(signin,text="Enter username : ",font=("Verdana",10),fg="indian red").grid(row=1,column=0)
    us=Entry(signin)
    us.grid(row=1,column=1)


    pswd=Label(signin,text="Enter password : ",font=("Verdana",10),fg="indian red").grid(row=2,column=0)
    password=Entry(signin,show='*')
    password.grid(row=2,column=1)

    empty=Label(signin,text="").grid(row=3,column=0)
    
    mainname=us.get()

    #Checking for correct username/password for login
    def checklogin():
        a=us.get()
        b=password.get()
        
        if a!="" and b!="":
            cur.execute("select * from login where username='"+ a +"'")
            data=cur.fetchall()
            
            if len(data)==0:
                messagebox.showerror("Notice","You have not entered a registered username")
            elif data[0][0]==a and data[0][1]==b:
                messagebox.showinfo("Message","Successfully logged into account")
                signin.destroy()
                loginin(a)
            else:
                messagebox.showerror("Notice","Your password or username is not entered correctly")
                
        elif a=="" and b=="":
            messagebox.showerror("Notice","You have not entered a username or password")



    button3=Button(signin,text="SIGN IN",font=("Calibre",12,"bold"),fg="indian red",command=checklogin)
    button3.grid(row=4,column=1,sticky="w")


#Sign up function
def signupfunc():
    global signup,login
    
    signup=Tk()
    signup.geometry("310x160")
    signup.title("SIGNUP SCREEN")
    
    sign=Label(signup,text="SIGN UP",font=("Verdana",13,"bold"),fg="steel blue").grid(row=0,column=1,sticky="w")


    name=Label(signup,text="Enter username : ",font=("Verdana",10),fg="steel blue").grid(row=1,column=0)
    user_signup=Entry(signup)
    user_signup.grid(row=1,column=1)

    pswd=Label(signup,text="Enter password : ",font=("Verdana",10),fg="steel blue").grid(row=2,column=0)
    password_signup=Entry(signup,show='*')
    password_signup.grid(row=2,column=1)

    cpswd=Label(signup,text="Confirm password : ",font=("Verdana",10),fg="steel blue").grid(row=3,column=0)
    cpass_signup=Entry(signup,show="*")
    cpass_signup.grid(row=3,column=1)
    
    empty=Label(signup,text="").grid(row=4,column=0)
   
    #Adding account to SQL
    def uploadsignup():
        A=user_signup.get()
        B=password_signup.get()
        C=cpass_signup.get()
        
        if B==C and C!=None and A!=None:
            cur.execute("select * from login where username='"+A+"'")
            d=cur.fetchall()

            if len(d)==0:
                messagebox.showinfo("Message","Successfully created an account. Please proceed to Login")
                cur.execute("insert into login values('"+ A +"','"+ B +"')")
                c.commit()
                signup.destroy()
            else:
                messagebox.showerror("Notice","This Username already exists")

        else:
            messagebox.showerror("Notice","Your password or username is not entered correctly")
    
    button3=Button(signup,text="SIGN UP",font=("Calibre",12,"bold"),fg="steel blue",command=uploadsignup)
    button3.grid(row=5,column=1,sticky="w")

# Final buttons performing given functions
button1=Button(login,text=" LOGIN  ",font=("Calibre",12,"bold"),fg="blue",command=signinfunc).pack(pady=22)
button2=Button(login,text="SIGNUP",font=("Calibre",12,"bold"),fg="green",command=signupfunc).pack(pady=4)
button3=Button(login,text="DELETE ACCOUNT",font=("Calibre",12,"bold"),fg="red",command=deleteaccfn).pack(pady=15)


def calculate_tax():
    try:
        age = int(age_entry.get())
        gross_salary = int(gross_salary_entry.get())
        other_income = int(other_income_entry.get())
        interest_income = int(interest_income_entry.get())
        rental_income = int(rental_income_entry.get())
        home_loan_self_occupied = int(home_loan_self_occupied_entry.get())
        home_loan_let_out = int(home_loan_let_out_entry.get())

        basic_deduction = int(basic_deduction_entry.get())
        nps_contribution = int(nps_contribution_entry.get())
        medical_premium = int(medical_premium_entry.get())
        charity_donation = int(charity_donation_entry.get())
        education_loan_interest = int(education_loan_interest_entry.get())
        saving_interest = int(saving_interest_entry.get())

        total_income = gross_salary + other_income + interest_income + rental_income - home_loan_self_occupied - home_loan_let_out

        total_deductions = basic_deduction + nps_contribution + medical_premium + charity_donation + education_loan_interest + saving_interest

        net_income = total_income - total_deductions

        # Apply Tax Slabs
        if age >= 80:
            tax_free_limit = 500000
        elif age >= 60:
            tax_free_limit = 300000
        else:
            tax_free_limit = 300000

        if net_income <= tax_free_limit:
            tax = 0
        elif net_income <= 700000:
            tax = (net_income - tax_free_limit) * 0.05
        elif net_income <= 1000000:
            tax = 20000 + (net_income - 700000) * 0.1
        elif net_income <= 1200000:
            tax = 50000 + (net_income - 1000000) * 0.15
        elif net_income <= 1500000:
            tax = 80000 + (net_income - 1200000) * 0.2
        else:
            tax = 140000 + (net_income - 1500000) * 0.3

        tax_output.config(text=f"Calculated Tax: Rs. {round(tax, 2)}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def tax_window():
    # Create a new window for the Income Tax Calculator
    tax_window = Tk()
    tax_window.title("Income Tax Calculator")
    tax_window.geometry("800x800")

    # Labels and Entries for Income Data
    Label(tax_window, text="Age").grid(row=0, column=0)
    global age_entry
    age_entry = Entry(tax_window)
    age_entry.grid(row=0, column=1)

    Label(tax_window, text="Gross Salary Income").grid(row=1, column=0)
    global gross_salary_entry
    gross_salary_entry = Entry(tax_window)
    gross_salary_entry.grid(row=1, column=1)

    Label(tax_window, text="Annual Income from Other Sources").grid(row=2, column=0)
    global other_income_entry
    other_income_entry = Entry(tax_window)
    other_income_entry.grid(row=2, column=1)

    Label(tax_window, text="Annual Income from Interest").grid(row=3, column=0)
    global interest_income_entry
    interest_income_entry = Entry(tax_window)
    interest_income_entry.grid(row=3, column=1)

    Label(tax_window, text="Rental Income").grid(row=4, column=0)
    global rental_income_entry
    rental_income_entry = Entry(tax_window)
    rental_income_entry.grid(row=4, column=1)

    Label(tax_window, text="Interest Paid on Home Loan (Self-Occupied)").grid(row=5, column=0)
    global home_loan_self_occupied_entry
    home_loan_self_occupied_entry = Entry(tax_window)
    home_loan_self_occupied_entry.grid(row=5, column=1)

    Label(tax_window, text="Interest Paid on Home Loan (Let-Out)").grid(row=6, column=0)
    global home_loan_let_out_entry
    home_loan_let_out_entry = Entry(tax_window)
    home_loan_let_out_entry.grid(row=6, column=1)

    # Labels and Entries for Deductions
    Label(tax_window, text="Basic Deductions u/s 80C").grid(row=7, column=0)
    global basic_deduction_entry
    basic_deduction_entry = Entry(tax_window)
    basic_deduction_entry.grid(row=7, column=1)

    Label(tax_window, text="Contribution to NPS u/s 80CCD(1B)").grid(row=8, column=0)
    global nps_contribution_entry
    nps_contribution_entry = Entry(tax_window)
    nps_contribution_entry.grid(row=8, column=1)

    Label(tax_window, text="Medical Insurance Premium u/s 80D").grid(row=9, column=0)
    global medical_premium_entry
    medical_premium_entry = Entry(tax_window)
    medical_premium_entry.grid(row=9, column=1)

    Label(tax_window, text="Donations to Charity u/s 80G").grid(row=10, column=0)
    global charity_donation_entry
    charity_donation_entry = Entry(tax_window)
    charity_donation_entry.grid(row=10, column=1)

    Label(tax_window, text="Interest on Educational Loan u/s 80E").grid(row=11, column=0)
    global education_loan_interest_entry
    education_loan_interest_entry = Entry(tax_window)
    education_loan_interest_entry.grid(row=11, column=1)

    Label(tax_window, text="Interest on Savings u/s 80TTA/TTB").grid(row=12, column=0)
    global saving_interest_entry
    saving_interest_entry = Entry(tax_window)
    saving_interest_entry.grid(row=12, column=1)

    # Button to Calculate Tax
    Button(tax_window, text="Calculate Tax", command=calculate_tax).grid(row=13, column=0, pady=20)

    # Label for displaying calculated tax
    global tax_output
    tax_output = Label(tax_window, text="Calculated Tax: Rs. 0.00")
    tax_output.grid(row=13, column=1)

    tax_window.mainloop()



#Information Options :  Graph Reports or Income or Expense Data or Logout
def loginin(mainname_1):
    global signin,signup,login
    root=Toplevel()
    root.geometry('550x100')
    root.title("Buckstracker")
    label=Label(root,text="Buckstracker",anchor=CENTER,font=("Calibre",15,"bold"),fg="magenta3").grid(row=0,column=2)


    b1=Button(root,text="Income",anchor=CENTER,font=("Calibre",12,"bold"),fg="green",command= lambda: Income_Tree(mainname_1))
    b1.grid(row=1,column=1)
    b2=Button(root,text="Expense",anchor=CENTER,font=("Calibre",12,"bold"),fg="red",command= lambda: Expense_Tree(mainname_1))
    b2.grid(row=1,column=2)
    b3=Button(root,text="Graph Reports",anchor=CENTER,font=("Calibre",12,"bold"),fg="blue",command= lambda : graphreports(mainname_1))
    b3.grid(row=1,column=3)

    b4 = Button(root, text="Income_Tax", anchor=CENTER, font=("Calibre", 12, "bold"), fg="blue",command=tax_window)
    b4.grid(row=1, column=4)

    
    def logout(root,win):
        root.destroy()
        # function to logout and open Buckstracker Login window if it had been closed previously
        if win.state()!="normal":
            loginwindow()
            
    Label_Space=Label(root,text="      ")
    Label_Space.grid(row=1,column=4)

    b4=Button(root,text="LOGOUT",anchor=CENTER,font=("Calibre",12,"bold"),fg="navy",command= lambda: logout(root,login))
    b4.grid(row=1,column=5)

    root.mainloop()

login.mainloop()





    
    

    

