from tkinter import*

import mysql.connector


class invalid(Exception):
    def invalidlogin(self,username,password,root):
        self.username=username
        self.password=password
        result=messagebox.askquestion("error","THIS USERNAME DOES'NT EXIST \nDO U WANT TO REGISTER?")
        if result == 'yes':
            endProgam(root)
            entr()
        else:
            print("RE-login")
            
    
                    
#create new profile
def entr():
        tr1=Tk()
        tr1.title("NEW USER")
        c=Label(tr1,text="USER REGISTRATION").grid(row=1,column=25)
        tr1.configure(background="blue")
        tr1.geometry("400x400")
        n1=Label(tr1,text="username").grid(row=50,column=15)
        z1=Entry(tr1)
        z1.grid(row=50,column=20)
        n2=Label(tr1,text="Password").grid(row=80,column=15)
        z2=Entry(tr1,show='*')
        z2.grid(row=80,column=20)
        n3=Label(tr1,text="ADDRESS").grid(row=90,column=15)
        z3=Entry(tr1)
        z3.grid(row=90,column=20)
        y1=Button(tr1,text="SIGN UP!",command= lambda: enter(z1,z2,tr1))
        y1.grid(row=100,column=20)
        y1=Button(tr1,text="Bye now",command=lambda:endProgam(tr1))
        y1.grid(row=110,column=40)
       

def endProgam(z):
    z.destroy()


def enter(z1,z2,tr1):
    a=z1.get()
    b=z2.get()
    if len(a)>8 and len(b)>2:
        fo=open("check.txt","a")
        print("Name of the file is ",fo.name)
        fo.write(a)
        fo.write("\n")
        fo.write(b)
        fo.write("\n")
        print("SUCCESFULLY REGISTERED!")
        fo.close()
        result=messagebox.askquestion("done!","SUCCEFULLY REGISTERED!!\nLOG IN")
        if result == 'yes':
            endProgam(tr1)
            main()
        else:
            endProgam(tr1)
            entr()
            
    else:
        messagebox.showinfo("wrong input!","usernanme and password should have above 8 characters")

    
    
    

           
def login(e,e1,root):
            username=str(e.get())
            
            password=e1.get()
            print(username)
            print("---------------------LOGIN----------------------")
            try:
                fo=open("check.txt","r") 
                print("name of the file is ",fo.name)
                while 1:
                    line=fo.readline().strip('\n')
                    line2=fo.readline().strip('\n')
                    print(line2)
                    if(""==line):
                        print("wrong entry")
                        raise invalid()
                        break
                    elif username==line and password==line2:
                        print("SUCCESS!!")
                        flag=1
                        break
                       
                            
                                            
                fo.close()
                if flag==1:
                    details()
            except invalid as er:
                er.invalidlogin(username,password,root)
                  
#THE MENU, UPDATE, EXIT, NEW ENTRY
def details():
    root1=Tk()
    root1.title("ENTRY LOG")
    root1.geometry("400x400")
    root1.configure(background="green")
    l=Label(root1,text="PHARAMACY MANAGEMENT SYSTEM",bg="blue",fg="black",relief=RAISED).grid(row=1,column=50)
    b1=Button(root1,text="NEW MEDICINE ENTRY",command=click)
    b1.grid(row=2,column=50)
    b2= Button(root1,text="SEARCH THE MEDICINE TO KNOW THE STOCK VALUE",command=click1)
    b2.grid(row=3,column=50)
    b3=Button(root1,text="BILL",command=bill)
    b3.grid(row=4,column=50)
    b4=Button(root1,text="EXIT",command=lambda:endProgam(root1))
    b4.grid(row=5,column=50)
  



#bill system
def bill():
    bi=Tk()
    bi.title("BILLiNG SYSTEM")
    bi.geometry("400x400")
    bi.configure(background="grey")
    lN=Label(bi,text="WELCOME TO BILLINNG SYSTEM",bg="blue",fg="WHITE",relief=RAISED).grid(row=1,column=8)
    l1=Label(bi,text="ENTER THE MEDIICNE NAME",bg="white",fg="BLACK",relief=RAISED).grid(row=8,column=3)
    e1=Entry(bi)
    e1.grid(row=8,column=5)
    l2=Label(bi,text="QUANTITY NEEDED",bg="white",fg="BLACK",relief=RAISED).grid(row=9,column=3)
    e2=Entry(bi)
    e2.grid(row=9,column=5)
    #calculation of bill starts here
    bz=Button(bi,text="CALCULATE",command=lambda:sum(e1,e2))
    bz.grid(row=12,column=4)



def sum(e1,e2):
    medname=e1.get()
    quan=int(e2.get())
    conn = mysql.connector.connect(user="ashwantm",password='1454',database='asd')
    curs = conn.cursor()
    curs.execute('select * from medicine')
    df=curs.fetchall()
    for i in df:
        if i[0] == medname:
            val=int(i[1])
            val=val*quan
            ff=int(i[4])
            numb=ff-quan
            numb=str(numb)
            print(medname)
            curs.execute('update medicine set STOCK="'+numb+'" where Name="'+medname+'"')
            gene(val)
            conn.commit()
            conn.close()
    
    
    
    
#function to valuees into db
def click():
    root2=Tk()
    root2.title("NEW Entry")
    root2.geometry("400x400")
    root2.configure(background="white")
    k=Label(root2,text="MEDICINE DETAILS",bg="white",fg="blue",relief=RAISED).grid(row=3,column=8)
    l=Label(root2,text="ID",bg="white",fg="BLACK",relief=RAISED).grid(row=7,column=5)
    e=Entry(root2)
    e.grid(row=7,column=10)
    l1=Label(root2,text="MEDICINE NAME",bg="white",fg="BLACK",relief=RAISED).grid(row=8,column=5)
    e1=Entry(root2)
    e1.grid(row=8,column=10)
    l2=Label(root2,text="PRICE",bg="white",fg="BLACK",relief=RAISED).grid(row=9,column=5)
    e2=Entry(root2)
    e2.grid(row=9,column=10)
    l3=Label(root2,text="MFG. DATE",bg="white",fg="BLACK",relief=RAISED).grid(row=10,column=5)
    e3=Entry(root2)
    e3.grid(row=10,column=10)
    l4=Label(root2,text="EXP. DATE",bg="white",fg="BLACK",relief=RAISED).grid(row=11,column=5)
    e4=Entry(root2)
    e4.grid(row=11,column=10)
    l5=Label(root2,text="COMPANY",bg="white",fg="BLACK",relief=RAISED).grid(row=12,column=5)
    e5=Entry(root2)
    e5.grid(row=12,column=10)
    l11=Label(root2,text="SUPPLIER",bg="white",fg="BLACK",relief=RAISED).grid(row=18,column=5)
    e11=Entry(root2)
    e11.grid(row=18,column=10)
    l12=Label(root2,text="STOCK",bg="white",fg="BLACK",relief=RAISED).grid(row=19,column=5)
    e12=Entry(root2)
    e12.grid(row=19,column=10)
    bz=Button(root2,text="ENTER TO DATABASE",command=lambda:add(e1,e2,e4,e5,e11,e12,root2))
    bz.grid(row=20,column=8)
    by=Button(root2,text="close",command=lambda:endProgam(root2))
    by.grid(row=21,column=8)
    


def re(z):
    z.destroy()
    click()

    

#creating db and inserting values
def add(e1,e2,e4,e5,e11,e12,z):
    po=e1.get()
    op=e2.get()
    op1=e4.get()
    op2=e5.get()
    op4=e11.get()
    op3=e12.get()
    if len(po)!=0 or len(op)!=0 or len(op1)!=0 or len(op2)!=0 or len(op4)!=0 or len(op3)!=0:      
        z.destroy()
        conn = mysql.connector.connect(user="ashwantm",password='1454',database='asd')
        curs = conn.cursor()
        curs.execute('create table if not exists medicine(Name text,Price integer,EXP_Date date,Company text,STOCK text,Supplier text)')
        curs.execute('insert into medicine(Name,Price,EXP_Date,Company,STOCK,Supplier)values("'+po+'","'+op+'","'+op1+'","'+op2+'","'+op3+'","'+op4+'")')
        conn.commit()
        conn.close()
        result=messagebox.askquestion("updated","Enter next Stock info")
        if result =="yes":
            click()
        else:
            pass
    else:
        messagebox.showinfo("error","Fill in the details Correclty!")
        
        
#function to search medicine
def click1():
    root3=Tk()
    root3.geometry("400x400")
    root3.configure(background="blue")
    k=Label(root3,text="WELCOME TO MEDICINE SEARCH",bg="white",fg="BLACK",relief=RAISED).grid(row=3,column=1)
    l=Label(root3,text="ENTER THE MEDICINE NAME ",bg="white",fg="BLACK",relief=RAISED).grid(row=4,column=1)
    er=Entry(root3)
    er.grid(row=5,column=1)
    re=er
    er.delete(0,"end") 
    bz=Button(root3,text="SEARCH THE DATABASE",command=lambda:add2(re))
    bz.grid(row=5,column=2)
   
    by=Button(root3,text="Close",command=lambda:endProgam(root3))
    by.grid(row=15,column=3)



#bill print out
def gene(val):
    bii=Tk()
    bii.title("THE BILL")
    bii.geometry("400x400")
    bii.configure(background="grey")
    lN=Label(bii,text="THE TOTAL AMOUNT TO BE PAID IS",bg="blue",fg="WHITE",relief=RAISED).grid(row=1,column=4)
    L4=Label(bii,text="TOTAL AMOUNT",relief=RAISED).grid(row=10,column=3)
    t3=StringVar()
    t3=Entry(bii)
    t3.delete(0,"end")   
    t3.grid(row=11,column=4)
    t3.insert(0,val)


#the search result
def stoc(li):
    ii=Tk()
    ii.title("THE SEARCH RESULT")
    ii.geometry("400x400")
    ii.configure(background="grey")
    L3=Label(ii,text="MEDICINE NAME",relief=RAISED).grid(row=11,column=3)
    t3=Entry(ii)
    t3.delete(0,"end")   
    t3.grid(row=11,column=4)
    t3.insert(0,li[0][0])

    L4=Label(ii,text="MEDICINE RATE",relief=RAISED).grid(row=12,column=3)
    t4=Entry(ii)
    t4.delete(0,"end")   
    t4.grid(row=12,column=4)
    t4.insert(0,li[0][1])

    L5=Label(ii,text="TOTAL STOCK",relief=RAISED).grid(row=13,column=3)
    t5=Entry(ii)
    t5.delete(0,"end")   
    t5.grid(row=13,column=4)
    t5.insert(0,li[0][4])

    bz=Button(ii,text="close",command=lambda:endProgam(ii))
    bz.grid(row=15,column=5)


#from click1
def add2(er):
    neww=er.get()
    conn = mysql.connector.connect(user="ashwantm",password='1454',database='asd')
    curs = conn.cursor()
    curs.execute('select * from medicine')
    vb=curs.fetchall()
    break1=0
    for i in vb:
        if neww==i[0]:
            print("Medicine found")
            curs.execute('select * from medicine where Name="'+neww+'"')
            li=curs.fetchall()
            print(li[0][1])
            stoc(li)
            print(li)
            break1=1
    if break1==0:
        messagebox.showinfo("EMPTY","NO STOCK AVAILABLE \n GO BACK AND ADD THE MEDECINE")
        print("NO STOCK AVAILABILITY")
    conn.commit()
    conn.close()



def end(z):
    z.destroy()
    exit()

def main():
    root=Tk()
    root.title("WELCOME TO LOGIN PAGE!")
    root.configure(background="HOTPINK")
    root.geometry("400x600")
    l=Label(text="PHARAMCY MANAGEMENT SYSTEM",bg="BLUE",fg="black",relief=RAISED).grid(row=1,column=20)
    l1=Label(text="LOGIN PAGE",bg="white",fg="black",relief=RAISED).grid(row=3,column=20)
    l2=Label(root,text="USERNAME ").grid(row=50,column=15)
    e=Entry(root)
    e.grid(row=50,column=20)
    l3=Label(text="PASSWORD").grid(row=80,column=15)
    e1=Entry(root,show='*')
    e1.grid(row=80,column=20)
    b=Button(text="LOG IN",command=lambda: login(e,e1,root))
    b.grid(row=100,column=20)
    b5=Button(root,text="EXIT",command=lambda:end(root))
    b5.grid(row=101,column=20)
   
main()

