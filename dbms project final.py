import cx_Oracle as O
from tkinter import *
from tkinter import messagebox

def connection():
    con=O.connect('scott/pratyush@localhost:1521/orcl')
    cursor=con.cursor()
    return con,cursor

def display1():
      
    for widget in root.winfo_children():
        widget.destroy()
    root.geometry('600x600')
    con,c=connection()
    
    movie_id=Listbox(root,height=30,font='Calibri 14 bold')
    movie_id.place(x=0,y=0,height=400,width=200)
    
    seat_id=Listbox(root,height=30,font='Calibri 14 bold')
    seat_id.place(x=90,y=0,height=400,width=200)
    
    screen_id=Listbox(root,height=30,font='Calibri 14 bold')
    screen_id.place(x=190,y=0,height=400,width=200)

    mtype=Listbox(root,height=30,font='Calibri 14 bold')
    mtype.place(x=290,y=0,height=400,width=200)
    
    mydate=Listbox(root,height=30,font='Calibri 14 bold')
    mydate.place(x=400,y=0,height=400,width=200)
    
    movie_id.insert('end','MOVIE ID')
    seat_id.insert('end','SEAT ID')
    screen_id.insert('end','SCREEN ID')
    mtype.insert('end','MOVIE TYPE')
    mydate.insert('end','DATE ')

        
    for i in c.execute('select tmovie_id,seat_id,tscreen_id,type,dte from tickets'):
        movie_id.insert('end',i[0])
        seat_id.insert('end',i[1])
        screen_id.insert('end',i[2])
        mtype.insert('end',i[3])
        mydate.insert('end',i[4])
  
    con.close()


def display2():
      
    for widget in root.winfo_children():
        widget.destroy()
    con,c=connection()
    
    movieid=Listbox(root,height=10,font='Calibri 14 bold')
    movieid.place(x=0,y=0,height=200,width=400)
    moviename=Listbox(root,height=10,font='Calibri 14 bold')
    moviename.place(x=200,y=0,height=200,width=400)
    duration=Listbox(root,height=10,font='Calibri 14 bold')
    duration.place(x=400,y=0,height=200,width=400)
    language=Listbox(root,height=10,font='Calibri 14 bold')
    language.place(x=600,y=0,height=200,width=400)
    
    
    movieid.insert('end','MOVIE ID')
    moviename.insert('end','MOVIE NAME')
    duration.insert('end','DURATION')
    language.insert('end','LANGUAGE')

        
    for i in c.execute('select movie_id,movie_name,duration,language from movies'):
        movieid.insert('end',i[0])
        moviename.insert('end',i[1])
        duration.insert('end',i[2])
        language.insert('end',i[3])
        
    con.close()
    
def display3():
      
    for widget in root.winfo_children():
        widget.destroy()
    con,c=connection()
    root.geometry('800x800')

    screenid=Listbox(root,height=30,font='Calibri 14 bold')
    screenid.place(x=0,y=0,height=200,width=200)
    movieid=Listbox(root,height=30,font='Calibri 14 bold')
    movieid.place(x=100,y=0,height=200,width=200)
    showtime=Listbox(root,height=30,font='Calibri 14 bold')
    showtime.place(x=200,y=0,height=200,width=200)
    showdate=Listbox(root,height=30,font='Calibri 14 bold')
    showdate.place(x=350,y=0,height=200,width=200)
    moviename=Listbox(root,height=30,font='Calibri 14 bold')
    moviename.place(x=448,y=0,height=200,width=200)
    
    screenid.insert('end','SCREEN ID')
    movieid.insert('end','MOVIE ID')
    showtime.insert('end','SHOW TIME')
    showdate.insert('end','SHOW DATE')
    moviename.insert('end','MOVIE NAME')

        
    for i in c.execute('select screen_id,smovie_id,show_time,show_date,movie_name from scrndetails a,movies b where a.smovie_id=b.movie_id'):
        screenid.insert('end',i[0])
        movieid.insert('end',i[1])
        showtime.insert('end',i[2])
        showdate.insert('end',i[3])
        moviename.insert('end',i[4])

    con.close()



def cancel_ticket():
    for widget in root.winfo_children():
        widget.destroy()
    root.title('CANCELLING TICKET')
    con,c=connection()
    def cancel():
        
        seatid=str(sid_ent.get())
        movieid=int(mid_ent.get())
        movdt=str(dtent.get())
        temp=[seatid,movieid,movdt]
        for widget in root.winfo_children():
            widget.destroy()
        con,c=connection()
        c.execute('delete from tickets where seat_id=(:1) and tmovie_id=(:2) and dte=(:3)',temp)
        messagebox.showinfo("CANCEL TICKET", "TICKET CANCELLATION SUCCESSFUL")
        c.close()
        con.commit()
        con.close()
    
    s_id=Label(root,text='SEAT ID:',font='Calibri 14 bold')
    s_id.place(x=100,y=100)
    sid_ent=Entry(root,font='Calibri 14 bold')
    sid_ent.place(x=200,y=100)
    
    m_id=Label(root,text='MOVIE ID:',font='Calibri 14 bold')
    m_id.place(x=100,y=200)
    mid_ent=Entry(root,font='Calibri 14 bold')
    mid_ent.place(x=200,y=200)
    
    dt=Label(root,text='DATE:',font='Calibri 14 bold')
    dt.place(x=100,y=300)
    dtent=Entry(root,font='Calibri 14 bold')
    dtent.place(x=200,y=300)    
    
    ct=Button(root,text='CANCEL TICKET',font='Calibri 14 bold',bg='light blue',command=lambda:cancel())
    ct.place(x=250,y=400)


    con.close()
    

def book_ticket():
    for widget in root.winfo_children():
        widget.destroy()
        
    display3()
        
    root.title('BOOKING TICKETS')
    root.geometry('700x700')

    con,c=connection()
    l0=Label(root,text='THERE ARE TWO TICKET TYPES : ELITE & BUDGET',font='Calibri 14 bold')
    l0.place(x=120,y=240)
    l=Label(root,text='FOR ELITE CHOOSE ROW A-C , SEAT 1-10',font='Calibri 14 bold')
    l.place(x=130,y=270)
    l=Label(root,text='FOR BUDGET CHOOSE ROW D-J , SEAT 1-10',font='Calibri 14 bold')
    l.place(x=130,y=300)
    
    l1=Label(root,text='Movie id: ',font='Calibri 14 bold')
    l1.place(x=130,y=350)
    l1ent=Entry(root,font='Calibri 14 bold')
    l1ent.place(x=250,y=350)
    
    
    l2=Label(root,text='Seat id(s): ',font='Calibri 14 bold')
    l2.place(x=130,y=400)
    l2ent=Entry(root,font='Calibri 14 bold')
    l2ent.place(x=250,y=400)
    
    l3=Label(root,text='Screen id: ',font='Calibri 14 bold')
    l3.place(x=130,y=450)
    l3ent=Entry(root,font='Calibri 14 bold')
    l3ent.place(x=250,y=450)
    
    l4=Label(root,text='Type: ',font='Calibri 14 bold')
    l4.place(x=130,y=500)
    l4ent=Entry(root,font='Calibri 14 bold')
    l4ent.place(x=250,y=500)
    
    l5=Label(root,text='Date: ',font='Calibri 14 bold')
    l5.place(x=130,y=550)
    l5ent=Entry(root,font='Calibri 14 bold')
    l5ent.place(x=250,y=550)


    def insertticket():
        mid=int(l1ent.get())
        sid=str(l2ent.get())
        scrid=int(l3ent.get())
        typ=str(l4ent.get().lower())
        dte=str(l5ent.get())
        

            
        
        for widget in root.winfo_children():
            widget.destroy()
             
        if(typ=='elite'):
            lab=Label(root,text='Please pay 200/ticket for an Elite ticket\n from your UPI app.',font='Calibri 14 bold')
            lab.place(x=150,y=100)
        else:
            lab=Label(root,text='Please pay 150/ticket for a Budget ticket\n from your UPI app.',font='Calibri 14 bold')
            lab.place(x=150,y=100)
        
        btdone2=Button(root,text='Confirm Payment',bg='light pink',font='Calibri 14 bold',command=lambda:ins2())
        btdone2.place(x=200,y=250)        

        def ins2():

            con,c=connection() 
            a=[] 
            b=[]
            b=sid.split(',')
            x=len(b)
            c.execute(f"select seat_id from tickets where tmovie_id={mid} and tscreen_id={scrid}")
            rows=c.fetchall()
            for i in rows:
                a.append(i[0])
            c.close()
            con.commit()
            con.close()
            
          
            for i in range(x):
                if(b[i] in a):
                    messagebox.showerror("TICKET DETAILS","SEAT UNAVAILABLE. PLEASE CHOOSE ANOTHER SEAT.")
                else:
                    con,c=connection()
                    c.execute(f"insert into tickets values({mid},'{b[i]}',{scrid},'{typ}','{dte}')")
                    c.close()
                    con.commit()
                    con.close()
                    for widget in root.winfo_children():
                        widget.destroy()
                    
           
            messagebox.showinfo("TICKET DETAILS","BOOKING DONE SUCCESFULLY.")
           
    btdone=Button(root,text='Submit',bg='light pink',font='Calibri 14 bold',command=lambda:insertticket())
    btdone.place(x=300,y=600)
    
    con.close()


def cancel_movie():
    for widget in root.winfo_children():
        widget.destroy()
    con,c=connection()

    def cancel():
        movieid=int(mid_ent.get())
        temp=[movieid]
        for widget in root.winfo_children():
            widget.destroy()
        con,c=connection()
        c.execute('delete from movies where movie_id=(:1)',temp)
        c.execute('delete from tickets where tmovie_id=(:1)',temp)
        c.execute('delete from scrndetails where smovie_id=(:1)',temp)
        c.close()
        con.commit()
        con.close()   
        messagebox.showinfo("CANCEL MOVIE", "Movie has been removed from all screens.")     
    
    m_id=Label(root,text='MOVIE ID',font='Calibri 14 bold')
    m_id.place(x=100,y=200)
    mid_ent=Entry(root,font='Calibri 14 bold')
    mid_ent.place(x=200,y=200)
    
    cm=Button(root,text='REMOVE MOVIE ',font='Calibri 14 bold',bg='light blue',command=lambda:cancel())
    cm.place(x=300,y=300)
    
    con.close()



def user(): 
    for widget in root.winfo_children():
        widget.destroy()
    root.title('USER details')
    root.geometry('600x600')
    con,c=connection()
    bt=Button(root,text='BOOK TICKET',bg='light green',font='Calibri 14 bold',command=lambda:book_ticket())
    bt.place(x=200,y=200)
    ct=Button(root,text='CANCEL TICKET',font='Calibri 14 bold',bg='light blue',command=lambda:cancel_ticket())
    ct.place(x=200,y=250)
    ds=Button(root,text='DISPLAY SCHEDULES',bg='red',font='Calibri 14 bold',command=lambda:display3())
    ds.place(x=200,y=300)

   
def addmovies():
    for widget in root.winfo_children():
        widget.destroy()
        
    root.title('ADDING MOVIE..')
    root.geometry('600x600')
    con,c=connection()
    con.commit()
    con.close()
    
    l1=Label(root,text='Movie id: ',font='Calibri 14 bold')
    l1.place(x=120,y=150)
    l1ent=Entry(root,font='Calibri 14 bold')
    l1ent.place(x=270,y=150)
    
    
    l2=Label(root,text='Movie name: ',font='Calibri 14 bold')
    l2.place(x=120,y=200)
    l2ent=Entry(root,font='Calibri 14 bold')
    l2ent.place(x=270,y=200)
    
    l3=Label(root,text='Duration in mins: ',font='Calibri 14 bold')
    l3.place(x=120,y=250)
    l3ent=Entry(root,font='Calibri 14 bold')
    l3ent.place(x=270,y=250)
    
    l4=Label(root,text='Language: ',font='Calibri 14 bold')
    l4.place(x=120,y=300)
    l4ent=Entry(root,font='Calibri 14 bold')
    l4ent.place(x=270,y=300)
    
    def insertmovie():
        
        mid=int(l1ent.get())
        mnam=str(l2ent.get())
        dur=int(l3ent.get())
        lang=str(l4ent.get())  
        con,c=connection()   
        a=[]
        c.execute(f"select movie_id from movies")
        rows=c.fetchall()
        for i in rows:
            a.append(i[0])
        c.close()
        con.commit()
        con.close()
        
        if(mid in a):
            messagebox.showerror("ERROR!","MOVIE ID already exists")
        else:   
            con,c=connection() 
            c.execute(f"insert into movies values({mid},'{mnam}',{dur},'{lang}')")
            c.close()
            con.commit()
            con.close()
            for widget in root.winfo_children():
                widget.destroy()
            messagebox.showinfo("ADDING MOVIE","MOVIE ADDED SUCCESFULLY")
         
    btdone=Button(root,text='Submit',bg='light pink',font='Calibri 14 bold',command=lambda:insertmovie())
    btdone.place(x=300,y=400)
    
  

def addscrndet():
    for widget in root.winfo_children():
        widget.destroy()
    root.title('ADD SCREENING OPTIONS')
    root.geometry('500x500')
    con,c=connection() 
    
    l=Label(root,text='FOR SCREEN ID , CHOOSE FROM 1,2,3 ',font='Calibri 14 bold')
    l.place(x=50,y=50)
    
    st=Label(root,text='Show timings: ',font='Calibri 14 bold')
    st.place(x=70,y=100)
    ste=Entry(root,font='Calibri 14 bold')
    ste.place(x=240,y=100)

    sid=Label(root,text='Screen id: ',font='Calibri 14 bold')
    sid.place(x=70,y=150)
    side=Entry(root,font='Calibri 14 bold')
    side.place(x=240,y=150)

    mid=Label(root,text='Movie id: ',font='Calibri 14 bold')
    mid.place(x=70,y=200)
    mide=Entry(root,font='Calibri 14 bold')
    mide.place(x=240,y=200) 

    sd=Label(root,text='Date of show: ',font='Calibri 14 bold')
    sd.place(x=70,y=250)
    sde=Entry(root,font='Calibri 14 bold')
    sde.place(x=240,y=250) 
    
    
    def insertscrndet():
        showtime=str(ste.get())
        scrnid=int(side.get())
        movid=int(mide.get())
        showdate=str(sde.get())
        root.title('ADMIN OPTIONS')
        con,c=connection()   
        c.execute(f"insert into scrndetails values({scrnid},{movid},'{showtime}','{showdate}')")
        c.close()
        con.commit()
        con.close()
        for widget in root.winfo_children():
            widget.destroy()
        messagebox.showinfo("SCREENING DETAILS","ADDED SCREENING DETAILS SUCCESFULLY!")
        
    submitbtn=Button(root,text='Submit',bg='light green',font='Calibri 14 bold',command=lambda:insertscrndet())
    submitbtn.place(x=200,y=300)
    
def delscrndet():   
    for widget in root.winfo_children():
        widget.destroy()
    con,c=connection()

    def dele():
        movieid=int(mid_ent.get())
        screenid=int(scrid_ent.get())
        sdate=str(showdate_ent.get())
        temp=[movieid,screenid,sdate]
        for widget in root.winfo_children():
            widget.destroy()
        con,c=connection()
        c.execute('delete from scrndetails where smovie_id=(:1) and screen_id=(:2) and show_date=(:3)',temp)
        c.close()
        con.commit()
        con.close()   
        messagebox.showinfo("REMOVE SCREENING DETAILS", "Screening details have been deleted.")     
    
    movieid=Label(root,text='MOVIE ID:',font='Calibri 14 bold')
    movieid.place(x=100,y=100)
    mid_ent=Entry(root,font='Calibri 14 bold')
    mid_ent.place(x=220,y=100)
    
    screenid=Label(root,text='SCREEN ID:',font='Calibri 14 bold')
    screenid.place(x=100,y=200)
    scrid_ent=Entry(root,font='Calibri 14 bold')
    scrid_ent.place(x=220,y=200)
    
    sdate=Label(root,text='SHOW DATE:',font='Calibri 14 bold')
    sdate.place(x=100,y=300)
    showdate_ent=Entry(root,font='Calibri 14 bold')
    showdate_ent.place(x=220,y=300)
    
    cm=Button(root,text='REMOVE SCREENING DETAILS ',font='Calibri 14 bold',bg='light blue',command=lambda:dele())
    cm.place(x=150,y=350)
    
    con.close()       
        
           
def admin():
    for widget in root.winfo_children():
        widget.destroy()
    root.title('ADMIN OPTIONS')
    root.geometry('500x500')
    con,c=connection()  
    
    a1=Label(root,text='PASSWORD: ',font='Calibri 14 bold')
    a1.place(x=100,y=100)
    a1e=Entry(root,font='Calibri 14 bold',show='*')
    a1e.place(x=230,y=100)
    
    def user2():
        for widget in root.winfo_children():
            widget.destroy()
        bt1=Button(root,text=' ADD  MOVIES  ',bg='light green',font='Calibri 14 bold',command=lambda:addmovies())
        bt1.place(x=90,y=100)
        bt2=Button(root,text=' REMOVE MOVIES',bg='light green',font='Calibri 14 bold',command=lambda:cancel_movie())
        bt2.place(x=300,y=100)
        bt3=Button(root,text=' VIEW  TICKET   \nDETAILS',bg='light green',font='Calibri 14 bold',command=lambda:display1())
        bt3.place(x=90,y=150)
        bt4=Button(root,text='VIEW SCREENING \nDETAILS',bg='light green',font='Calibri 14 bold',command=lambda:display3())
        bt4.place(x=300,y=150)
        bt5=Button(root,text='ADD  SCREENING\nDETAILS',bg='light green',font='Calibri 13 bold',command=lambda:addscrndet())
        bt5.place(x=90,y=230)
        bt6=Button(root,text='    VIEW MOVIE     \nDETAILS',bg='light green',font='Calibri 14 bold',command=lambda:display2())
        bt6.place(x=300,y=230)
        bt7=Button(root,text='DEL  SCREENING \nDETAILS',bg='light green',font='Calibri 14 bold',command=lambda:delscrndet())
        bt7.place(x=190,y=320)
    
    bts=Button(root,text='Submit',bg='light green',font='Calibri 14 bold',command=lambda:pwcheck())
    bts.place(x=200,y=200)
    def pwcheck():
        if(a1e.get()=='admin123'):
            user2()
        else:
            messagebox.showinfo("Wrong PW","Wrong password entered.\nPlease try again.")
    
       
con,c=connection()
root=Tk()
root.title('LOGIN AS..')
root.geometry('900x500')


userbutton=Button(root,text='  USER  ',bg='blue',font='Calibri 14 bold',command=lambda:user())
userbutton.place(x=700,y=300)
adminbutton=Button(root,text='ADMIN',font='Calibri 14 bold',bg='light blue',command=lambda:admin())
adminbutton.place(x=700,y=350)
root.mainloop()