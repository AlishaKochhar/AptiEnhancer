
from tkinter import *
import tkinter as tk
import time
import sqlite3
import random

conn=sqlite3.connect('MinorProject.db')
c=conn.cursor()

c.execute("Select * from AptiQuestions")
data=c.fetchall()

#c.execute("CREATE TABLE UserRecord (UserName text, UserPassword text, UserScore int)")

k=1
list=[]
index=0

for i in range(0,len(data)-1):
    if(data[i][0]==data[i+1][0]):
        k=k+1
    
    else:
        list.append(k)
        k=1
        
list.append(k)


ques=[]
    
    
for i in range(0,35):
    t=random.randint(1,list[i])
    ques.append(data[t+index-1])
    index=index+list[i]


c.execute("Select * from AptiOptions")
data2=c.fetchall()

ans=[]
opt=[]

for i in range(0,35):
    c.execute("Select * from AptiOptions where QuestionId = ?",(ques[i][1],))
    opt.append(c.fetchall())
    c.execute("Select * from AptiAnswers where QuestionId = ?",(ques[i][1],))
    ans.append(c.fetchall())

dict={'A':'0','B':'1','C':'2','D':'3','E':'4'}

Oplen=[]
for i in range(0,35):
    Oplen.append(len(opt[i]))


section=['problems-on-trains','height-and-distance','simple-interest',
      'profit-and-loss','percentage','calendar','average','volume-and-surface-area',
      'numbers','problems-on-hcf-and-lcm','simplification','surds-and-indices',
      'chain-rule','boats-and-streams','logarithm','stocks-and-shares',
      'true-discount','odd-man-out-and-series','time-and-distance','time-and-work',
      'compound-interest','partnership','problems-on-ages','clock','area',
      'permutation-and-combination','problems-on-numbers','decimal-fraction',
      'square-root-and-cube-root','ratio-and-proportion','pipes-and-cistern',
      'alligation-or-mixture','races-and-games','probability','bankers-discount']

weak=[]



timeleft=60
LARGE_FONT=("Verdana",30)


state=True



timer=[]
timer.append(1)
timer.append(0)

pattern='{0:02d}:{1:02d}'

clicked=0

def update_timeText():
    if(clicked==1):
        print("clicked")
    else:
        for t in range(900, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            #print("sf")
            #print(sf)
            time_str.set(sf)
            root.update()
            if(sf=="00:00"):
                timeup()
            time.sleep(1)


def timeup():
    score=0
    for i in range(0,35):
        if(marked[i]==dict[ans[i][0][2]]):
            score=score+1
        else :
            weak.append(str(section[i]))
    print(weak)
    weakarea='\n'.join(weak)
    Newframe=Toplevel(fs37,height=400,width=600)
    Newframe.configure()
    wkarea=Label(Newframe,text="Your Weak Areas are:",fg="red",font="20,bold").grid(row=30,column=0)
    lr1=Label(Newframe,text="Enter Name : ",fg="green",font=20).grid(row=20,column=20)
    er1=Entry(Newframe,bd=1,textvariable=ev1,font=20).grid(row=30,column=20)
    lr2=Label(Newframe,text="Enter Password : ",fg="green",font=20).grid(row=40,column=20)
    er2=Entry(Newframe,bd=1,textvariable=ev2,font=20).grid(row=50,column=20)

    def saver():
        c.execute("INSERT INTO UserRecord values(?,?,?)",(ev1.get(),ev2.get(),score))
        conn.commit()
        messagebox.showinfo("Saved")
        fs1.tkraise()
    br1=Button(Newframe,text="Save Result",command=saver,font=30,fg="black",bg="pink").grid(row=60,column=20)
    
     
    sc=StringVar()
    ws=StringVar()
    msg=Message(Newframe,textvariable=sc,relief=RAISED,font="20,bold",fg="blue")
    x="SCORE IS : "+str(score)+"(/35)"
    sc.set(x)
    msg2=Message(Newframe,textvariable=ws,relief=RAISED,font=10,fg="green")
    ws.set(weakarea)
    msg.grid(row=20,column=0)
    msg2.grid(row=60,column=0)
    print("Done")
    
           
    

def starttimer():
    global state
    state=True
    update_timeText()

def raise_frame1(frame):
    fs3.tkraise()
    starttimer()


def raise_frame2(frame):
    frame.tkraise()

    

def clicks():
    clicked=1
    score=0
    for i in range(0,35):
        if(marked[i]==dict[ans[i][0][2]]):
            score=score+1
        else :
            weak.append(str(section[i]))
    print(weak)
    weakarea='\n'.join(weak)
    Newframe=Toplevel(fs37)
    wkarea=Label(Newframe,text="Your Weak Areas are:",fg="red",font="20,bold").grid(row=40,column=0)
    lr1=Label(Newframe,text="Enter Name : ",fg="green",font=20).grid(row=20,column=20)
    er1=Entry(Newframe,bd=1,textvariable=ev1,font=20).grid(row=30,column=20)
    lr2=Label(Newframe,text="Enter Password : ",fg="green",font=20).grid(row=40,column=20)
    er2=Entry(Newframe,bd=1,textvariable=ev2,font=20).grid(row=50,column=20)

    def saver():
        c.execute("INSERT INTO UserRecord values(?,?,?)",(ev1.get(),ev2.get(),score))
        conn.commit()
        messagebox.showinfo("Saved")
        fs1.tkraise()
    br1=Button(Newframe,text="Save Result",command=saver,font=30,fg="black",bg="pink").grid(row=60,column=20)
    
     
    sc=StringVar()
    ws=StringVar()
    msg=Message(Newframe,textvariable=sc,relief=RAISED,font="20,bold",fg="blue")
    x="SCORE IS : "+str(score)+"(/35)"
    sc.set(x)
    msg2=Message(Newframe,textvariable=ws,relief=RAISED,font=10,fg="green")
    ws.set(weakarea)
    msg.grid(row=20,column=0)
    msg2.grid(row=60,column=0)
    
    print("Done")

   
    


root=Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


fs1=Frame(root)
fs2=Frame(root)
fs3=Frame(root)
fs4=Frame(root)
fs5=Frame(root)
fs6=Frame(root)
fs7=Frame(root)
fs8=Frame(root)
fs9=Frame(root)
fs10=Frame(root)
fs11=Frame(root)
fs12=Frame(root)
fs13=Frame(root)
fs14=Frame(root)
fs15=Frame(root)
fs16=Frame(root)
fs17=Frame(root)
fs18=Frame(root)
fs19=Frame(root)
fs20=Frame(root)
fs21=Frame(root)
fs22=Frame(root)
fs23=Frame(root)
fs24=Frame(root)
fs25=Frame(root)
fs26=Frame(root)
fs27=Frame(root)
fs28=Frame(root)
fs29=Frame(root)
fs30=Frame(root)
fs31=Frame(root)
fs32=Frame(root)
fs33=Frame(root)
fs34=Frame(root)
fs35=Frame(root)
fs36=Frame(root)
fs38=Frame(root)
fs39=Frame(root)
fs40=Frame(root)
fs37=Frame(root)
fs41=Frame(root)

fall=[fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8,fs9,fs10,fs11,fs12,fs13,fs14,fs15,fs16,fs17,fs18,fs19,fs20,fs21,fs22,fs23,fs24,fs25,fs26,fs27,fs28,fs29,fs30,fs31,fs32,fs33,fs34,fs35,fs36,fs37,fs38,fs39,fs40]

f=[fs3,fs4,fs5,fs6,fs7,fs8,fs9,fs10,fs11,fs12,fs13,fs14,fs15,fs16,fs17,fs18,fs19,fs20,fs21,fs22,fs23,fs24,fs25,fs26,fs27,fs28,fs29,fs30,fs31,fs32,fs33,fs34,fs35,fs36,fs37,fs38,fs39,fs40]
root.configure()
for frame in fall:
     frame.grid(row=0,column=0,sticky='news')
     frame.configure()



time_str =StringVar()
label_font = ('helvetica', 40)


v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
v7=StringVar()
v8=StringVar()
v9=StringVar()
v10=StringVar()
v11=StringVar()
v12=StringVar()
v13=StringVar()
v14=StringVar()
v15=StringVar()
v16=StringVar()
v17=StringVar()
v18=StringVar()
v19=StringVar()
v20=StringVar()
v21=StringVar()
v22=StringVar()
v23=StringVar()
v24=StringVar()
v25=StringVar()
v26=StringVar()
v27=StringVar()
v28=StringVar()
v29=StringVar()
v30=StringVar()
v31=StringVar()
v32=StringVar()
v33=StringVar()
v34=StringVar()
v35=StringVar()


v1.set("Q1. "+ques[0][2])
v2.set("Q2. "+ques[1][2])
v3.set("Q3. "+ques[2][2])
v4.set("Q4. "+ques[3][2])
v5.set("Q5. "+ques[4][2])
v6.set("Q6. "+ques[5][2])
v7.set("Q7. "+ques[6][2])
v8.set("Q8. "+ques[7][2])
v9.set("Q9. "+ques[8][2])
v10.set("Q10. "+ques[9][2])
v11.set("Q11. "+ques[10][2])
v12.set("Q12. "+ques[11][2])
v13.set("Q13. "+ques[12][2])
v14.set("Q14. "+ques[13][2])
v15.set("Q15. "+ques[14][2])
v16.set("Q16. "+ques[15][2])
v17.set("Q17. "+ques[16][2])
v18.set("Q18. "+ques[17][2])
v19.set("Q19. "+ques[18][2])
v20.set("Q20. "+ques[19][2])
v21.set("Q21. "+ques[20][2])
v22.set("Q22. "+ques[21][2])
v23.set("Q23. "+ques[22][2])
v24.set("Q24. "+ques[23][2])
v25.set("Q25. "+ques[24][2])
v26.set("Q26. "+ques[25][2])
v27.set("Q27. "+ques[26][2])
v28.set("Q28. "+ques[27][2])
v29.set("Q29. "+ques[28][2])
v30.set("Q30. "+ques[29][2])
v31.set("Q31. "+ques[30][2])
v32.set("Q32. "+ques[31][2])
v33.set("Q33. "+ques[32][2])
v34.set("Q34. "+ques[33][2])
v35.set("Q35. "+ques[34][2])

ev1=StringVar()
ev2=StringVar()
res1=StringVar()

def showres():
    Newframe=Toplevel(fs2)
    userres1=[]
    c.execute("SELECT * FROM UserRecord where UserName = ? and UserPassword = ?",(ev1.get(),ev2.get()))
    userres=c.fetchall()
    for i in range(0,len(userres)):
        userres1.append(userres[i][2])
        
   
    Msg=Message(Newframe,textvariable=res1,relief=RAISED,fg="red",font=("Helvetica", 10))
    Msg2=Message(Newframe,text="Your Scores are : ",relief=RAISED,fg="red",font=("Helvetica", 10))
    res1.set(userres1)
    Msg2.grid(row=60,column=20)
    Msg.grid(row=70,column=20)
    print(userres)

def viewresult():
    Newframe=Toplevel(fs2)
    lr1=Label(Newframe,text="Enter Name : ",fg="red",font=30).grid(row=0,column=20)
    er1=Entry(Newframe,bd=1,textvariable=ev1,fg="red",font=30).grid(row=10,column=20)
    lr2=Label(Newframe,text="Enter Password : ",fg="red",font=30).grid(row=40,column=20)
    er2=Entry(Newframe,bd=1,textvariable=ev2,fg="red",font=30).grid(row=50,column=20)
    br1=Button(Newframe,text="Show Result",command=showres,bg="blue",fg="black",font=30).grid(row=60,column=20)


lt1=Label(fs1,text="Welcome to Aptitude Enhancer",bg="black",font=("Helvetica", 30),fg="blue").grid(row=1,column=2)
#bt1=Button(fs1,text="PROCEED",fg="black",font=("Helvetica", 10),command=lambda:raise_frame2(fs2)).grid(row=5,column=2)
#Bt3=Button(fs3, text=' Start Quiz', font=("Helvetica", 10),command=lambda:raise_frame1(fs3)).grid(row=0,column=0)
#lt2=Label(fs2,text="Choose your section",font=("Helvetica", 15),fg="blue").grid(row=1,column=3)
bt2a=Button(fs1,text="TAKE QUIZ",font=("Helvetica", 20),command=lambda:raise_frame1(fs3),bg="red",fg="black").place(x=600,y=100)
bt2b=Button(fs1,text="VIEW RESULT",font=("Helvetica", 20),command=viewresult,bg="red",fg="black").place(x=575,y=200)

for t in f:
    Button1=Button(t,text='Q01',bg="blue",fg="white",command=lambda:raise_frame2(fs3)).place(x=100,y=100)
    Button2=Button(t,text='Q02',bg="blue",fg="white",command=lambda:raise_frame2(fs4)).place(x=130,y=100)
    Button3=Button(t,text='Q03',bg="blue",fg="white",command=lambda:raise_frame2(fs5)).place(x=160,y=100)
    Button4=Button(t,text='Q04',bg="blue",fg="white",command=lambda:raise_frame2(fs6)).place(x=190,y=100)
    Button5=Button(t,text='Q05',bg="blue",fg="white",command=lambda:raise_frame2(fs7)).place(x=220,y=100)
    Button6=Button(t,text='Q06',bg="blue",fg="white",command=lambda:raise_frame2(fs8)).place(x=250,y=100)
    Button7=Button(t,text='Q07',bg="blue",fg="white",command=lambda:raise_frame2(fs9)).place(x=280,y=100)
    Button8=Button(t,text='Q08',bg="blue",fg="white",command=lambda:raise_frame2(fs10)).place(x=100,y=130)
    Button9=Button(t,text='Q09',bg="blue",fg="white",command=lambda:raise_frame2(fs11)).place(x=130,y=130)
    Button10=Button(t,text='Q10',bg="blue",fg="white",command=lambda:raise_frame2(fs12)).place(x=160,y=130)
    Button11=Button(t,text='Q11',bg="blue",fg="white",command=lambda:raise_frame2(fs13)).place(x=190,y=130)
    Button12=Button(t,text='Q12',bg="blue",fg="white",command=lambda:raise_frame2(fs14)).place(x=220,y=130)
    Button13=Button(t,text='Q13',bg="blue",fg="white",command=lambda:raise_frame2(fs15)).place(x=250,y=130)
    Button14=Button(t,text='Q14',bg="blue",fg="white",command=lambda:raise_frame2(fs16)).place(x=280,y=130)
    Button15=Button(t,text='Q15',bg="blue",fg="white",command=lambda:raise_frame2(fs17)).place(x=100,y=160)
    Button16=Button(t,text='Q16',bg="blue",fg="white",command=lambda:raise_frame2(fs18)).place(x=130,y=160)
    Button17=Button(t,text='Q17',bg="blue",fg="white",command=lambda:raise_frame2(fs19)).place(x=160,y=160)
    Button18=Button(t,text='Q18',bg="blue",fg="white",command=lambda:raise_frame2(fs20)).place(x=190,y=160)
    Button19=Button(t,text='Q19',bg="blue",fg="white",command=lambda:raise_frame2(fs21)).place(x=220,y=160)
    Button20=Button(t,text='Q20',bg="blue",fg="white",command=lambda:raise_frame2(fs22)).place(x=250,y=160)
    Button21=Button(t,text='Q21',bg="blue",fg="white",command=lambda:raise_frame2(fs23)).place(x=280,y=160)
    Button22=Button(t,text='Q22',bg="blue",fg="white",command=lambda:raise_frame2(fs24)).place(x=100,y=190)
    Button23=Button(t,text='Q23',bg="blue",fg="white",command=lambda:raise_frame2(fs25)).place(x=130,y=190)
    Button24=Button(t,text='Q24',bg="blue",fg="white",command=lambda:raise_frame2(fs26)).place(x=160,y=190)
    Button25=Button(t,text='Q25',bg="blue",fg="white",command=lambda:raise_frame2(fs27)).place(x=190,y=190)
    Button26=Button(t,text='Q26',bg="blue",fg="white",command=lambda:raise_frame2(fs28)).place(x=220,y=190)
    Button27=Button(t,text='Q27',bg="blue",fg="white",command=lambda:raise_frame2(fs29)).place(x=250,y=190)
    Button28=Button(t,text='Q28',bg="blue",fg="white",command=lambda:raise_frame2(fs30)).place(x=280,y=190)
    Button29=Button(t,text='Q29',bg="blue",fg="white",command=lambda:raise_frame2(fs31)).place(x=100,y=220)
    Button30=Button(t,text='Q30',bg="blue",fg="white",command=lambda:raise_frame2(fs32)).place(x=130,y=220)
    Button31=Button(t,text='Q31',bg="blue",fg="white",command=lambda:raise_frame2(fs33)).place(x=160,y=220)
    Button32=Button(t,text='Q32',bg="blue",fg="white",command=lambda:raise_frame2(fs34)).place(x=190,y=220)
    Button33=Button(t,text='Q33',bg="blue",fg="white",command=lambda:raise_frame2(fs35)).place(x=220,y=220)
    Button34=Button(t,text='Q34',bg="blue",fg="white",command=lambda:raise_frame2(fs36)).place(x=250,y=220)
    Button35=Button(t,text='Q35',bg="blue",fg="white",command=lambda:raise_frame2(fs37)).place(x=280,y=220)
    



L1=Message(fs3, textvariable=v1, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L2=Message(fs4, textvariable=v2, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L3=Message(fs5, textvariable=v3, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L4=Message(fs6, textvariable=v4, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L5=Message(fs7, textvariable=v5, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
  
L6=Message(fs8, textvariable=v6, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L7=Message(fs9, textvariable=v7, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L8=Message(fs10, textvariable=v8, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
   
L9=Message(fs11, textvariable=v9, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L10=Message(fs12, textvariable=v10, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L11=Message(fs13, textvariable=v11, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
   
L12=Message(fs14, textvariable=v12, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L13=Message(fs15, textvariable=v13, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L14=Message(fs16, textvariable=v14, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
    
L15=Message(fs17, textvariable=v15, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L16=Message(fs18, textvariable=v16, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L17=Message(fs19, textvariable=v17, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
 
L18=Message(fs20, textvariable=v18, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L19=Message(fs21, textvariable=v19, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L20=Message(fs22, textvariable=v20, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L21=Message(fs23, textvariable=v21, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L22=Message(fs24, textvariable=v22, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L23=Message(fs25, textvariable=v23, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
   
L24=Message(fs26, textvariable=v24, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L25=Message(fs27, textvariable=v25, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L26=Message(fs28, textvariable=v26, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L27=Message(fs29, textvariable=v27, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L28=Message(fs30, textvariable=v28, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L29=Message(fs31, textvariable=v29, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L30=Message(fs32, textvariable=v30, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)

L31=Message(fs33, textvariable=v31, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L32=Message(fs34, textvariable=v32, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L33=Message(fs35, textvariable=v33, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
L34=Message(fs36, textvariable=v34, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)
 
L35=Message(fs37, textvariable=v35, bg='white', 
         fg='blue', relief='raised').place(x=350,y=100)


for t in f:
    timeText = tk.Label(t, textvariable=time_str, font=("Helvetica", 30),fg='blue')
    
    #timeText.grid(row=1,column=0)
    timeText.place(x=50,y=0)


#radiotext=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]


i=17
v=StringVar()

#marked=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

marked=[]

for i in range(0,35):
    marked.append('5')

def click1():
    marked[0]=v.get()

def click2():
    marked[1]=v.get()

def click3():
    marked[2]=v.get()

def click4():
    marked[3]=v.get()

def click5():
    marked[4]=v.get()

def click6():
    marked[5]=v.get()

def click7():
    marked[6]=v.get()

def click8():
    marked[7]=v.get()

def click9():
    marked[8]=v.get()

def click10():
    marked[9]=v.get()

def click11():
    marked[10]=v.get()

def click12():
    marked[11]=v.get()

def click13():
    marked[12]=v.get()

def click14():
    marked[13]=v.get()

def click15():
    marked[14]=v.get()

def click16():
    marked[15]=v.get()

def click17():
    marked[16]=v.get()

def click18():
    marked[17]=v.get()

def click19():
    marked[18]=v.get()

def click20():
    marked[19]=v.get()

def click21():
    marked[20]=v.get()

def click22():
    marked[21]=v.get()

def click23():
    marked[22]=v.get()

def click24():
    marked[23]=v.get()

def click25():
    marked[24]=v.get()

def click26():
    marked[25]=v.get()

def click27():
    marked[26]=v.get()

def click28():
    marked[27]=v.get()

def click29():
    marked[28]=v.get()

def click30():
    marked[29]=v.get()

def click31():
    marked[30]=v.get()

def click32():
    marked[31]=v.get()

def click33():
    marked[32]=v.get()

def click34():
    marked[33]=v.get()

def click35():
    marked[34]=v.get()
    print(marked)
    

v.set(5)

optdict={0:'A.  ',1:'B.  ',2:'C.  ',3:'D.  ',4:'E.  '}

yval=50
for k in range(0,Oplen[0]):
        r1=Radiobutton(fs3,fg="red",text=optdict[k]+opt[0][k][2],variable=v,value=k,command=click1)
        r1.place(x=650,y=yval)
        yval=yval+70
       

yval=50
for k in range(0,Oplen[1]):
        r2=Radiobutton(fs4,fg="red",text=optdict[k]+opt[1][k][2],variable=v,value=k,command=click2)
        r2.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[2]):
        r3=Radiobutton(fs5,fg="red",text=optdict[k]+opt[2][k][2],variable=v,value=k,command=click3)
        r3.place(x=650,y=yval)
        yval=yval+70

yval=50    
for k in range(0,Oplen[3]):
        r4=Radiobutton(fs6,fg="red",text=optdict[k]+opt[3][k][2],variable=v,value=k,command=click4)
        r4.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[4]):
        r5=Radiobutton(fs7,fg="red",text=optdict[k]+opt[4][k][2],variable=v,value=k,command=click5)
        r5.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[5]):
        r6=Radiobutton(fs8,fg="red",text=optdict[k]+opt[5][k][2],variable=v,value=k,command=click6)
        r6.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[6]):
        r7=Radiobutton(fs9,fg="red",text=optdict[k]+opt[6][k][2],variable=v,value=k,command=click7)
        r7.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[7]):
        r8=Radiobutton(fs10,fg="red",text=optdict[k]+opt[7][k][2],variable=v,value=k,command=click8)
        r8.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[8]):
        r9=Radiobutton(fs11,fg="red",text=optdict[k]+opt[8][k][2],variable=v,value=k,command=click9)
        r9.place(x=650,y=yval)
        yval=yval+70

yval=50        
for k in range(0,Oplen[9]):
        r10=Radiobutton(fs12,fg="red",text=optdict[k]+opt[9][k][2],variable=v,value=k,command=click10)
        r10.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[10]):
        r11=Radiobutton(fs13,fg="red",text=optdict[k]+opt[10][k][2],variable=v,value=k,command=click11)
        r11.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[11]):
        r12=Radiobutton(fs14,fg="red",text=optdict[k]+opt[11][k][2],variable=v,value=k,command=click12)
        r12.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[12]):
        r13=Radiobutton(fs15,fg="red",text=optdict[k]+opt[12][k][2],variable=v,value=k,command=click13)
        r13.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[13]):
        r14=Radiobutton(fs16,fg="red",text=optdict[k]+opt[13][k][2],variable=v,value=k,command=click14)
        r14.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[14]):
        r15=Radiobutton(fs17,fg="red",text=optdict[k]+opt[14][k][2],variable=v,value=k,command=click15)
        r15.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[15]):
        r16=Radiobutton(fs18,fg="red",text=optdict[k]+opt[15][k][2],variable=v,value=k,command=click16)
        r16.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[16]):
        r17=Radiobutton(fs19,fg="red",text=optdict[k]+opt[16][k][2],variable=v,value=k,command=click17)
        r17.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[17]):
        r18=Radiobutton(fs20,fg="red",text=optdict[k]+opt[17][k][2],variable=v,value=k,command=click18)
        r18.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[18]):
        r19=Radiobutton(fs21,fg="red",text=optdict[k]+opt[18][k][2],variable=v,value=k,command=click19)
        r19.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[19]):
        r20=Radiobutton(fs22,fg="red",text=optdict[k]+opt[19][k][2],variable=v,value=k,command=click20)
        r20.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[20]):
        r21=Radiobutton(fs23,fg="red",text=optdict[k]+opt[20][k][2],variable=v,value=k,command=click21)
        r21.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[21]):
        r22=Radiobutton(fs24,fg="red",text=optdict[k]+opt[21][k][2],variable=v,value=k,command=click22)
        r22.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[22]):
        r23=Radiobutton(fs25,fg="red",text=optdict[k]+opt[22][k][2],variable=v,value=k,command=click23)
        r23.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[23]):
        r24=Radiobutton(fs26,fg="red",text=optdict[k]+opt[23][k][2],variable=v,value=k,command=click24)
        r24.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[24]):
        r25=Radiobutton(fs27,fg="red",text=optdict[k]+opt[24][k][2],variable=v,value=k,command=click25)
        r25.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[25]):
        r26=Radiobutton(fs28,fg="red",text=optdict[k]+opt[25][k][2],variable=v,value=k,command=click26)
        r26.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[26]):
        r27=Radiobutton(fs29,fg="red",text=optdict[k]+opt[26][k][2],variable=v,value=k,command=click27)
        r27.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[27]):
        r28=Radiobutton(fs30,fg="red",text=optdict[k]+opt[27][k][2],variable=v,value=k,command=click28)
        r28.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[28]):
        r29=Radiobutton(fs31,fg="red",text=optdict[k]+opt[28][k][2],variable=v,value=k,command=click29)
        r29.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[29]):
        r30=Radiobutton(fs32,fg="red",text=optdict[k]+opt[29][k][2],variable=v,value=k,command=click30)
        r30.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[30]):
        r31=Radiobutton(fs33,fg="red",text=optdict[k]+opt[30][k][2],variable=v,value=k,command=click31)
        r31.place(x=650,y=yval)
        yval=yval+70
        
yval=50
for k in range(0,Oplen[31]):
        r32=Radiobutton(fs34,fg="red",text=optdict[k]+opt[31][k][2],variable=v,value=k,command=click32)
        r32.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[32]):
        r33=Radiobutton(fs35,fg="red",text=optdict[k]+opt[32][k][2],variable=v,value=k,command=click33)
        r33.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[33]):
        r34=Radiobutton(fs36,fg="red",text=optdict[k]+opt[33][k][2],variable=v,value=k,command=click34)
        r34.place(x=650,y=yval)
        yval=yval+70

yval=50
for k in range(0,Oplen[34]):
        r35=Radiobutton(fs37,fg="red",text=opt[34][k][2],variable=v,value=k,command=click35)
        r35.place(x=650,y=yval)
        yval=yval+70



for t in f:
    btlast=Button(t,text="SUBMIT",command=clicks,font=("Helvetica", 20),bg="green",fg="black")
    btlast.place(x=250,y=270)

logo = PhotoImage(file="quiz.png")
w1 = Label(fs1, image=logo).grid(row=5,column=1)

raise_frame2(fs1)
root.mainloop()

