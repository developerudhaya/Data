import pymysql
import time

# Global database connection
mydb=pymysql.connect(
    user="root",
    password="",
    host="localhost",
    database="bankdata"

    )

#Bank Class 
class Bank:
    def Introduction(self,bankname):
        print("*********Welcome to "+bankname+"**********\n")
        print("1.withdraw")
        print("2.deposit")
        print("3.balance enquiry")
    def withdraw(self, w_amt, m_amt):
        result=m_amt-w_amt;
        query="update bank set main_amount="+str(result)+" where id='1001'";
        
        cursor.execute(query)
        mydb.commit()
    def deposit(self, d_amy, m_amy):
        pass
    def balance_enquiry(self,bankname, flag):
        pass

#Main Function 
if __name__== "__main__":
    b_name="ICICI"
    sbi=Bank()
    flag=0
    sbi.Introduction(b_name)

    cursor=mydb.cursor()
    cursor.execute("select * from bank;")
    fetch=cursor.fetchone();
    pin=list(fetch)[2]
    user_pin=int(input("Enter the pin number :"))
    if(int(pin)==user_pin):
       user_input=int(input("\nchoose option to prooced :"))
    if(user_input==1):
        w_amt=int(input("Enter your Amount:"))
        cursor.execute("select * from bank;")
        fetch=cursor.fetchone();
        m_amt=int(list(fetch)[3])
        sbi.withdraw(w_amt, m_amt)
        flag=1
        user_rp=str(input("Do You Want Receipt or Not(y/N):"))
        if(user_rp=="Y"):
            sbi.Balance_enquiry(b_name,flag)
            
            

       

     
    
    
