import os
import pickle
from datetime import datetime
dtobj=datetime.now()

#user defined function to create Bank Accounts
def BANK():
    f1=open("Bank.dat",'ab')
    bank={}
    while True:
        a=int(input("Enter the Account Number:"))
        if len(str(a))!=16:
            print("-----INCORRECT ACCOUNT NUMBER-----")
            break
        an=input("Enter the Account Name:")
        pin=None
        dob=input("Eter your Date of Birth(dd-mm-yyyy):")
        ad=input("Enter the Address:")
        ah=int(input("Enter your Aadhar Number:"))
        if len(str(ah))!=12:
            print("-----INCORRECT AADHAR NUMBER-----")
            break
        ph=int(input("Enter your Mobile Number:"))
        if len(str(ph))!=10:
            print("-----INCORRECT MOBILE NUMBER-----")
            break
        s=float(input("Enter the Amount deposited:"))
        print()
        print("-"*100)
        print("ACCOUNT TYPE MENU")
        print("-"*100)
        print("Select your Account Type:\n1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
        print("-"*100)
        ch=int(input("Enter your choice[1-4]:"))
        if ch==1:
            x="Savings"
        elif ch==2:
            x="Current"
        elif ch==3:
            x="CC/Deposit"
        elif ch==4:
            x="Loan"
        else:
            print("-----INVALID CHOICE-----")
            break
        if ch in [1,2,3,4]:
            t=x
        v=[an,pin,dob,ad,ah,ph,s,t]
        bank={a:v}
        pickle.dump(bank,f1)
        print("\n-----ACCOUNT CREATED SUCCESSFULLY-----")
        ans=input("\nDo you want to enter more records[Y/N]?")
        if ans=="N":
            break
        else:
            print()
    f1.close()
    print()

#user defined funtion to display Acc Number, PIN Number, Total Balance and Acc Type of details stored in 'Bank.dat'
def DISPLAY_BANK():
    f=open("Bank.dat",'rb')
    print("-"*100)
    print("ACC_NO\t\t\tPIN\t\tAMOUNT\t\tTYPE")
    print("-"*100)
    while True:
        try:
            data=pickle.load(f)
            for i in data:
                print(i,"\t",data[i][1],"\t\t",data[i][6],"\t\t",data[i][7])
        except EOFError:
            break
    f.close()
    print()
    
#user defined funtion to display PIN Number, Acc Number, Total Balance and Acc Type of details stored in 'ATM.dat'
def DISPLAY_ATM():
    f=open("ATM.dat",'rb')
    print("-"*100)
    print("PIN\tACC_NO\t\t\tAMOUNT\t\tTYPE")
    print("-"*100)
    while True:
        try:
            data=pickle.load(f)
            for i in data:
                print(i,"\t",data[i][0],"\t",data[i][1],"\t\t",data[i][2])
        except EOFError:
            break
    f.close()
    print()
    
#user defined fuction to create an ATM Card
def ATM():
    ATM={}
    f3=open("Bank.dat",'rb')
    f0=open("temp1.dat","wb")
    a=int(input("Enter your Account Number:"))       
    while True:
        if len(str(a))!=16:
            print("Incorrect Account Number")
            break
        else:
            y=check(a)
            if y==True:
                p=int(input("Enter your PIN Number:"))
                if len(str(p))!=4:
                    print("-----INCORRECT PIN NUMBER-----")
                    break
                else:
                    print()
                    f=0
                    while True:
                        try:
                            data=pickle.load(f3)
                            for i in data:
                                if i==a and data[i][1]==None:
                                    f=1
                                    data[i][1]=p
                                pickle.dump(data,f0)
                        except EOFError:
                            break
                    f3.close()
                    f0.close()
                    os.remove("Bank.dat")
                    os.rename("temp1.dat","Bank.dat")
                    f1=open("ATM.dat",'ab')
                    f3=open("Bank.dat",'rb')
                    if f==1:
                        while True:
                            try:
                                c=pickle.load(f3)
                                for j in c:
                                    if j==a and c[j][1]!=None:
                                        x=j
                                        y=c[j][1]
                                        z=c[j][6]
                                        w=c[j][7]
                                        v=[x,z,w]
                                        ATM={y:v}
                                        pickle.dump(ATM,f1)
                                        print("-----ATM CARD CREATED SUCCESSFULLY-----")
                            except EOFError:
                                break
                        f1.close()
                        f3.close()
                    else:
                        print("-----ATM CARD ALREADY EXISTS-----")
                    break
            else:
                print()
                print("-----ERROR-----")
                print("-----ACCOUNT DOESN'T EXIST-----")
                break
            print()
            
#user defined function to return the Balance Amount of a given PIN Number
def BALANCE_INQUIRY():
    while True:
        p=int(input("Enter your PIN Number:"))
        if len(str(p))!=4:
            print("-----INCORRECT PIN NUMBER-----")
            break
        else:
            y=acc(p)
            if y==True:
                f8=open("ATM.dat",'rb')
                print()
                print("-"*100)
                print("ACCOUNT TYPE MENU")
                print("-"*100)
                print("Select your Account Type:\n1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
                ch=int(input("Enter your choice[1-4]:"))
                if ch==1:
                    x="Savings"
                elif ch==2:
                    x="Current"
                elif ch==3:
                    x="CC/Deposit"
                elif ch==4:
                    x="Loan"
                else:
                    print("-----INVALID CHOICE-----")
                    break
                print()
                print("*"*100)
                print("DATE:",dtobj.strftime("%d-%m-%y"))
                while True:
                    try:
                        data=pickle.load(f8)
                        for i in data:
                            if i==p and data[i][2]==x:
                                a=str(data[i][0])
                                print("Account Number: ************",a[-4:])
                                print("Remaining Balance:",data[i][1])
                            elif i==p and data[i][2]!=x:
                                print("-----ACCOUNT DOESN'T EXIST-----")
                    except EOFError:
                        break
                f8.close()
                print("*"*100)
            else:
                print("-----PIN NUMBER DOESN'T EXIST-----")
        break
    
#user defined function to withdraw amount from an Account using a menu of amounts from which the user can choose
def FAST_CASH():
    process="WITHDRAWAL"
    while True:
        p=int(input("Enter your PIN Number:"))
        if len(str(p))!=4:
            print("-----INCORRECT PIN NUMBER-----")
            break
        else:
            y=acc(p)
            if y==True:
                print()
                print("-"*100)
                print("ACCOUNT TYPE MENU")
                print("-"*100)
                print("Select your Account Type:\n1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
                ch=int(input("Enter your choice[1-4]:"))
                if ch==1:
                    x="Savings"
                elif ch==2:
                    x="Current"
                elif ch==3:
                    x="CC/Deposit"
                elif ch==4:
                    x="Loan"
                else:
                    print("-----INVALID CHOICE-----")
                    break
                print()
                print("-"*100)
                print("AMOUNT TRASACTION MENU")
                print("-"*100)
                print("Select Amount to be withdrawn:\n1) Rs. 1000\n2) Rs. 2000\n3) Rs. 3000\n4) Rs. 4000\n5) Rs. 5000")
                n=int(input("Enter your choice[1-5]:"))
                if n==1:
                    ch=1000
                elif n==2:
                    ch=2000
                elif n==3:
                    ch=3000
                elif n==4:
                    ch=4000
                elif n==5:
                    ch=5000
                else:
                    n=0
                    print("-----INVALID CHOICE-----")
                    break
                print()
                f4=open("ATM.dat",'rb')
                f6=open("temp1.dat",'wb')
                print("_PLEASE WAIT_")
                print("_YOUR TRANSACTION IS BEING PROCESSED_\n")
                while True:
                    try:
                        data=pickle.load(f4)
                        for i in data:
                            if i==p and data[i][1]>=ch and data[i][2]==x:
                                data[i][1]=data[i][1]-ch
                                print("-----CASH WITHDRAWAL SUCESSFUL-----")
                            elif i==p and data[i][1]<ch and data[i][2]==x:
                                print("-----CASH WITHDRAWAL UNSUCCESSFUL-----")
                                print("-----RE-CHECK CASH BALANCE-----")
                            elif i==p and data[i][1]>=ch and data[i][2]!=x:
                                print("-----CASH WITHDRAWAL UNSUCCESSFUL-----")
                                print("-----ACCOUNT DOESN'T EXIST-----")
                            pickle.dump(data,f6)
                    except EOFError:
                            break
                f4.close()
                f6.close()
                os.remove("ATM.dat")
                os.rename("temp1.dat","ATM.dat")
                f5=open("Bank.dat",'rb')
                f7=open("temp2.dat",'wb')
                while True:
                    try:
                        b=pickle.load(f5)
                        for j in b:
                            if b[j][1]==p and b[j][6]>=ch and b[j][7]==x:
                                b[j][6]=b[j][6]-ch
                            pickle.dump(b,f7)
                    except EOFError:
                        break
                f5.close()
                f7.close()
                os.remove("Bank.dat")
                os.rename("temp2.dat","Bank.dat")
                print()
                print("Do you want a printed reciept:")
                print("1. YES\n2. NO")
                r=int(input("Select your choice[1/2]:"))
                if r==1:
                    f0=open("ATM.dat",'rb')
                    while True:
                        try:
                            data=pickle.load(f0)
                            for i in data:
                                if i==p:
                                    ac=data[i][0]
                                    tot=data[i][1]
                        except EOFError:
                            break
                    f0.close()
                    RECEIPT(process,ac,ch,tot)
                elif r!=2:
                    print("-----INVALID CHOICE-----")
                    break
                break
            else:
                print("-----PIN NUMBER DOESN'T EXIST-----")
                break
            
#user defined function to withdraw a particular amount specified by the user from an Account
def WITHDRAWAL():
    process="WITHDRAWAL"
    while True:
        p=int(input("Enter your PIN Number:"))
        if len(str(p))!=4:
            print("Incorrect PIN Number")
            break
        else:
            y=acc(p)
            if y==True:
                f9=open("ATM.dat",'rb')
                f10=open("Bank.dat",'rb')
                f11=open("temp1.dat",'wb')
                f12=open("temp2.dat",'wb')
                print()
                print("-"*100)
                print("ACCOUNT TYPE MENU")
                print("-"*100)
                print("Select your Account Type:\n1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
                ch=int(input("Enter your choice[1-4]:"))
                if ch==1:
                    x="Savings"
                elif ch==2:
                    x="Current"
                elif ch==3:
                    x="CC/Deposit"
                elif ch==4:
                    x="Loan"
                else:
                    print("-----INVALID CHOICE-----")
                    break
                a=float(input("\nEnter the amount to be withdrawn:"))
                print()
                print("_PLEASE WAIT_")
                print("_YOUR TRANSACTION IS BEING PROCESSED_\n")
                while True:
                    try:
                        data=pickle.load(f9)
                        for i in data:
                            if i==p and data[i][1]>=a and data[i][2]==x:
                                data[i][1]-=a
                                print("-----CASH WITHDRAWAL SUCCESSFUL-----")
                            elif i==p and data[i][1]<a and data[i][2]==x:
                                print("-----CASH WITHDRAWAL UNSUCCESSFUL-----")
                                print("-----RE-CHECK CASH BALANCE-----")
                            elif i==p and data[i][1]>=ch and data[i][2]!=x:
                                print("-----CASH WITHDRAWAL UNSUCCESSFUL-----")
                                print("-----ACCOUNT DOESN'T EXIST-----")
                            pickle.dump(data,f11)
                    except EOFError:
                        break
                f9.close()
                f11.close()
                os.remove("ATM.dat")
                os.rename("temp1.dat","ATM.dat")
                while True:
                    try:
                        b=pickle.load(f10)
                        for j in b:
                            if b[j][1]==p and b[j][6]>=a and b[j][7]==x:
                                b[j][6]-=a
                            pickle.dump(b,f12)
                    except EOFError:
                        break
                f10.close()
                f12.close()
                os.remove("Bank.dat")
                os.rename("temp2.dat","Bank.dat")
                print()
                print("Do you want a printed reciept:")
                print("1. YES\n2. NO")
                r=int(input("Enter your choice[1/2]:"))
                if r==1:
                    f0=open("ATM.dat",'rb')
                    while True:
                        try:
                            data=pickle.load(f0)
                            for i in data:
                                if i==p:
                                    ac=data[i][0]
                                    tot=data[i][1]
                        except EOFError:
                            break
                    f0.close()
                    RECEIPT(process,ac,a,tot)
                elif r!=2:
                    print("-----INVALID CHOICE-----")
                    break
                break
            else:
                print("-----PIN NUMBER DOESN'T EXIST-----")
                break
           
#user defined function to change the PIN Number of an ATM Card 
def PIN_CHANGE():
    while True:
        rp=int(input("Enter your registered PIN Number:"))
        if len(str(rp))!=4:
            print("-----INCORRECT PIN NUMBER-----")
            break
        else:
            y=acc(rp)
            if y==True:
                np1=int(input("Enter your new PIN number:"))
                np2=int(input("Re-Enter to confirm your new PIN number:"))
                if np1==np2 and len(str(np1))==4:
                    np=np1
                    print()
                    print("-"*100)
                    print("ACCOUNT TYPE MENU")
                    print("-"*100)
                    print("Select your Account Type:\n1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
                    ch=int(input("Enter your choice[1-4]:"))
                    if ch==1:
                        x="Savings"
                    elif ch==2:
                        x="Current"
                    elif ch==3:
                        x="CC/Deposit"
                    elif ch==4:
                        x="Loan"
                    else:
                        print("-----INVALID CHOICE-----")
                        break
                    print()
                    f14=open("Bank.dat",'rb')
                    f16=open("temp2.dat",'wb')
                    while True:
                        try:
                            b=pickle.load(f14)
                            for j in b:
                                if b[j][1]==rp and b[j][7]==x:
                                    b[j][1]=np
                                    print("-----PIN NUMBER CHANGED SUCCESSFULLY-----")
                                elif b[j][1]==rp and b[j][7]!=x:
                                    print("-----PIN CHANGING UNSUCCESSFUL-----")
                                    print("-----ACCOUNT DOESN'T EXIST-----")
                                pickle.dump(b,f16)
                        except EOFError:
                            break
                    f14.close()
                    f16.close()
                    os.remove("Bank.dat")
                    os.rename("temp2.dat","Bank.dat")
                    f13=open("ATM.dat",'rb')
                    f15=open("temp1.dat",'wb')
                    while True:
                        try:
                            b=pickle.load(f13)
                            for j in b:
                                if j==rp:
                                    v=b[j]
                                    j=np
                                    b={j:v}
                                pickle.dump(b,f15)
                        except EOFError:
                            break
                    f13.close()
                    f15.close()
                    os.remove("ATM.dat")
                    os.rename("temp1.dat","ATM.dat")
                    break
            else:
                print("-----PIN NUMBER DOESN'T EXIST-----")
                break
        break

#user defined function to transfer money from one Account to another
def FUND_TRANSFER():
    process="FUND TRANSFER"
    while True:
        p=int(input("Enter your PIN Number:"))
        if len(str(p))!=4:
            print("-----INCORRECT PIN NUMBER-----")
            break
        else:
            y=acc(p)
            if y==True:
                print()
                print("-"*100)
                print("ACCOUNT BASED TRANSFER")
                print("-"*100)
                print("SELECT YOUR TO ACCOUNT TYPE:")
                print("1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
                ch1=int(input("Enter your choice:"))
                if ch1==1:
                    d="Savings"
                elif ch1==2:
                    d="Current"
                elif ch1==3:
                    d="CC/Deposit"
                elif ch1==4:
                    d="Loan"
                else:
                    print("-----INVALID CHOICE-----")
                    break
                print()
                if ch1 in [1,2,3,4]:
                    ans1=int(input("Enter your To Account Number:"))
                    ans2=int(input("Re-Enter your To Account Number:"))
                    print()
                    if ans1!=ans2:
                        print("-----INCONGRUENT ACCOUNT NUMBER-----")
                        break
                    else:
                        ans=ans1
                        z=check(ans)
                        if z==True:
                            a=float(input("Enter the amount to transfer:  Rs."))
                            print("\nSELECT YOUR FROM ACCOUNT TYPE:")
                            print("1.Savings\n2.Current")
                            ch2=int(input("Enter your choice:"))
                            print()
                            print("_PLEASE WAIT_")
                            print("_YOUR TRANSACTION IS BEING PROCESSED_\n")
                            print("*"*100)
                            print("TRANSACTION SCREEN")
                            print("*"*100)
                            if ch2==1:
                                f="Savings"
                                print("From Acc Type: Savings")
                                print("To Acc Number:",ans)
                                print("Transfer Amount:",a)
                                print()
                                f17=open("ATM.dat",'rb')
                                f19=open("temp1.dat",'wb')
                                while True:
                                    try:
                                        data=pickle.load(f17)
                                        for i in data:
                                            if i==p and data[i][1]>=a and data[i][2]=="Savings":
                                                data[i][1]=data[i][1]-a
                                            elif i==p and data[i][1]<a and data[i][2]=="Savings":
                                                print("-----TRANSACTION UNSUCCESSFUL-----")
                                                print("-----RE-CHECK CASH BALANCE-----")
                                            elif i==p and data[i][1]>=a and data[i][2]!="Savings":
                                                print("-----TRANSACTION UNSUCCESSFUL-----")
                                                print("-----SENDER'S ACCOUNT NOT FOUND-----")
                                            pickle.dump(data,f19)
                                    except EOFError:
                                        break
                                f17.close()
                                f19.close()
                                os.remove("ATM.dat")
                                os.rename("temp1.dat","ATM.dat")
                                f18=open("Bank.dat",'rb')
                                f20=open("temp2.dat",'wb')
                                while True:
                                    try:
                                        c=pickle.load(f18)
                                        for j in c:
                                            if c[j][1]==p and c[j][6]>=a and c[j][7]=="Savings":
                                                c[j][6]=c[j][6]-a
                                            pickle.dump(c,f20)
                                    except EOFError:
                                        break
                                f18.close()
                                f20.close()
                                os.remove("Bank.dat")
                                os.rename("temp2.dat","Bank.dat")
                                f17=open("ATM.dat",'rb')
                                f19=open("temp1.dat",'wb')
                                while True:
                                    try:
                                        data=pickle.load(f17)
                                        for i in data:
                                            if data[i][0]==ans and data[i][2]==d:
                                                data[i][1]=data[i][1]+a
                                                print("-----TRANSACTION SUCCESSFUL-----")
                                            elif data[i][0]==ans and data[i][2]!=d:
                                                print("-----TRANSACTION UNSUCCESSFUL-----")
                                                print("-----RECEIVER'S ACCOUNT NOT FOUND-----")
                                            pickle.dump(data,f19)
                                    except EOFError:
                                        break
                                f17.close()
                                f19.close()
                                os.remove("ATM.dat")
                                os.rename("temp1.dat","ATM.dat")
                                f18=open("Bank.dat",'rb')
                                f20=open("temp2.dat",'wb')
                                while True:
                                    try:
                                        c=pickle.load(f18)
                                        for j in c:
                                            if j==ans and c[j][7]==d:
                                                c[j][6]=c[j][6]+a
                                            pickle.dump(c,f20)
                                    except EOFError:
                                        break
                                f18.close()
                                f20.close()
                                os.remove("Bank.dat")
                                os.rename("temp2.dat","Bank.dat")
                            elif ch2==2:
                                f="Current"
                                print("From Acc Type: Current")
                                print("To Acc Number:",ans)
                                print("Transfer Amount:",a)
                                print()
                                f17=open("ATM.dat",'rb')
                                f19=open("temp1.dat",'wb')
                                while True:
                                    try:
                                        data=pickle.load(f17)
                                        for i in data:
                                            if i==p and data[i][1]>=a and data[i][2]=="Current":
                                                data[i][1]=data[i][1]-a
                                            elif i==p and data[i][1]<a and data[i][2]=="Current":
                                                print("-----TRANSACTION UNSUCCESSFUL-----")
                                                print("-----RE-CHECK CASH BALANCE-----")
                                            elif i==p and data[i][1]>=a and data[i][2]!="Current":
                                                print("-----TRANSACTION UNSUCCESSFUL-----")
                                                print("-----SENDER'S ACCOUNT NOT FOUND-----")
                                            pickle.dump(data,f19)
                                    except EOFError:
                                        break
                                f17.close()
                                f19.close()
                                os.remove("ATM.dat")
                                os.rename("temp1.dat","ATM.dat")
                                f18=open("Bank.dat",'rb')
                                f20=open("temp2.dat",'wb')
                                while True:
                                    try:
                                        c=pickle.load(f18)
                                        for j in c:
                                            if c[j][1]==p and c[j][6]>=a and c[j][7]=="Current":
                                                c[j][6]=c[j][6]-a
                                            pickle.dump(c,f20)
                                    except EOFError:
                                        break
                                f18.close()
                                f20.close()
                                os.remove("Bank.dat")
                                os.rename("temp2.dat","Bank.dat")
                                f17=open("ATM.dat",'rb')
                                f19=open("temp1.dat",'wb')
                                while True:
                                    try:
                                        data=pickle.load(f17)
                                        for i in data:
                                            if data[i][0]==ans and data[i][2]==d:
                                                data[i][1]=data[i][1]+a
                                                print("-----TRANSACTION SUCCESSFUL-----")
                                            elif data[i][0]==ans and data[i][2]!=d:
                                                print("-----RECEIVER'S ACCOUNT NOT FOUND-----")
                                            pickle.dump(data,f19)
                                    except EOFError:
                                        break
                                f17.close()
                                f19.close()
                                os.remove("ATM.dat")
                                os.rename("temp1.dat","ATM.dat")
                                f18=open("Bank.dat",'rb')
                                f20=open("temp2.dat",'wb')
                                while True:
                                    try:
                                        c=pickle.load(f18)
                                        for j in c:
                                            if j==ans and c[j][7]==d:
                                                c[j][6]=c[j][6]+a
                                            pickle.dump(c,f20)
                                    except EOFError:
                                        break
                                f18.close()
                                f20.close()
                                os.remove("Bank.dat")
                                os.rename("temp2.dat","Bank.dat")
                            else:
                                print("Invalid choice")
                                break
                            print()
                            print("Do you want a printed reciept:")
                            print("1. YES\n2. NO")
                            r=int(input("Enter your choice[1/2]:"))
                            if r==1:
                                f0=open("ATM.dat",'rb')
                                while True:
                                    try:
                                        data=pickle.load(f0)
                                        for i in data:
                                            if i==p and data[i][2]==f:
                                                ac=data[i][0]
                                                tot=data[i][1]
                                                l=0
                                    except EOFError:
                                        break
                                f0.close()
                                RECEIPT(process,ac,a,tot)
                            elif r!=2:
                                print("-----INVALID CHOICE-----")
                                break
                            break
                        else:
                            print("-----PIN NUMBER DOESN'T EXIST-----")
                            break
        break
    
#user defined function to deposit a particular amount specified by the user from an Account
def DEPOSIT():
    process="DEPOSITION"
    while True:
        p=int(input("Enter your PIN Number:"))
        if len(str(p))!=4:
            print("-----INCORRECT PIN NUMBER-----")
            break
        else:
            y=acc(p)
            if y==True:
                f21=open("ATM.dat",'rb')
                f22=open("Bank.dat",'rb')
                f23=open("temp1.dat",'wb')
                f24=open("temp2.dat",'wb')
                print()
                print("-"*100)
                print("ACCOUNT TYPE MENU")
                print("-"*100)
                print("Select your Account Type:\n1. Savings\n2. Current\n3. CC/Deposit\n4. Loan")
                ch=int(input("Enter your choice[1-4]:"))
                if ch==1:
                    x="Savings"
                elif ch==2:
                    x="Current"
                elif ch==3:
                    x="CC/Deposit"
                elif ch==4:
                    x="Loan"
                else:
                    print("-----INVALID CHOICE-----")
                    break
                print()
                a=float(input("Enter the amount to be deposited:"))
                print()
                print("_PLEASE WAIT_")
                print("_YOUR TRANSACTION IS BEING PROCESSED_\n")
                while True:
                    try:
                        data=pickle.load(f21)
                        for i in data:
                            if i==p and data[i][2]==x:
                                data[i][1]=data[i][1]+a
                                print("-----CASH DEPOSITION SUCCESSFUL-----")
                            elif i==p and data[i][2]!=x:
                                print("-----CASH DEPOSITION SUCCESSFUL-----")
                                print("-----ACCOUNT DOESN'T EXIST-----")
                            pickle.dump(data,f23)
                    except EOFError:
                        break
                f21.close()
                f23.close()
                os.remove("ATM.dat")
                os.rename("temp1.dat","ATM.dat")
                while True:
                    try:
                        b=pickle.load(f22)
                        for j in b:
                            if b[j][1]==p:
                                b[j][6]=b[j][6]+a
                            pickle.dump(b,f24)
                    except EOFError:
                        break
                f22.close()
                f24.close()
                os.remove("Bank.dat")
                os.rename("temp2.dat","Bank.dat")
                print()
                print("Do you want a printed reciept:")
                print("1. YES\n2. NO")
                r=int(input("Enter your choice[1/2]:"))
                if r==1:
                    f0=open("ATM.dat",'rb')
                    while True:
                        try:
                            data=pickle.load(f0)
                            for i in data:
                                if i==p:
                                    ac=data[i][0]
                                    tot=data[i][1]
                        except EOFError:
                            break
                    f0.close()
                    RECEIPT(process,ac,a,tot)
                elif r!=2:
                    print("-----INVALID CHOICE-----")
                    break
                break
            else:
                print("-----PIN NUMBER DOESN'T EXIST-----")
                break
            
#user defined function to print Receipt
def RECEIPT(t,u,v,w):
    print()
    print("*"*60)
    print("\t\tRECEIPT")
    print("*"*60)
    print("DATE\t\tTIME\t\tATM ID")
    print(dtobj.strftime("%d-%m-%y"),"\t",dtobj.strftime("%H:%M:%S"),"\t","00720001")
    print()
    print("\t\t",t)
    print()
    a=str(u)
    print("FR A/C # :",a[:3],"************",a[-4:])
    print("TXN AMOUNT : RS  ",v)
    print("LEDG BAL : RS  ",w)
    print("AVAIL BAL : RS  ",w)
    
#user defined function to check whether a PIN Number exists using 'ATM.dat'
def acc(pin):                       
    x=open('ATM.dat',"rb")         
    flag=False                      
    while True:
        try:                                        
            d1=pickle.load(x)
            d2=d1.keys()
            if pin in d2:           
                flag=True           
        except  EOFError:
            return flag 
            break
        
#user defined function to check whether an Account exists using 'Bank.dat'
def check(acc):                       
    x=open('Bank.dat',"rb")         
    flag=False
    while True:
        try:                                        
            d1=pickle.load(x)
            d2=d1.keys()
            if acc in d2:           
                flag=True           
        except  EOFError:
            return flag 
            break
        
#Driver Function
while True:
    print("OPERATION MENU\n1. Create account\n2. Create ATM Card\n3. Fast Cash\n4. Withdrawal\n5. Change PIN Number\n6. Fund Transfer\n7. Deposit\n8. Balance Inquiry\n9. Display All Bank Accounts\n10. Display All ATM Accounts\n11. Exit")
    ch=int(input("\nEnter your choice:"))
    print()
    if ch==1:
        n=3
        while n>0:
            psswrd=input("Enter the password:")
            if psswrd=="BANK@123":
                print()
                BANK()
                break
            else:
                print("Incorrect password...",end="")
                n-=1
                if n==0:
                    print()
                    break
                else:
                    print("Please try again!!!")
                    print(n,"tries left")
                    print()
    elif ch==2:
        n=3
        while n>0:
            psswrd=input("Enter the password:")
            if psswrd=="ATM@123":
                print()
                ATM()
                break
            else:
                print("Incorrect password...",end="")
                n-=1
                if n==0:
                    break
                else:
                    print("Please try again!!!")
                    print(n,"tries left")
                    print()
    elif ch==3:
        FAST_CASH()
    elif ch==4:
        WITHDRAWAL()
    elif ch==5:
        PIN_CHANGE()
    elif ch==6:
        FUND_TRANSFER()
    elif ch==7:
        DEPOSIT()
    elif ch==8:
        BALANCE_INQUIRY()
    elif ch==9:
        n=3
        while n>0:
            psswrd=input("Enter the password:")
            if psswrd=="BANK@123":
                print()
                DISPLAY_BANK()
                break
            else:
                print("Incorrect password...",end="")
                n-=1
                if n==0:
                    break
                else:
                    print("Please try again!!!")
                    print(n,"tries left")
                    print()
    elif ch==10:
        n=3
        while n>0:
            psswrd=input("Enter the password:")
            if psswrd=="ATM@123":
                print()
                DISPLAY_ATM()
                break
            else:
                print("Incorrect password...",end="")
                n-=1
                if n==0:
                    break
                else:
                    print("Please try again!!!")
                    print(n,"tries left")
                    print()
    elif ch==11:
        exit(0)
    else:
        print("-----INVALID CHOICE-----")
    print()
    ans=input("Do you want to continue[Y/N]?:")
    if ans=="N":
        break
    else:
        print()

