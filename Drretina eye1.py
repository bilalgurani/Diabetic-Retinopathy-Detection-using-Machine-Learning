import tkinter as tk
import tkinter.messagebox
import pandas as p
from tkinter import *

import mysql.connector

import mysql.connector as mysql

#from tkinter import filedialog as fd 
import tkinter.filedialog
from tkinter import ttk

from datetime import datetime
from dateutil import relativedelta

from PIL import ImageTk,Image  

import pandas as p
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from array import *
from pandas import DataFrame
import matplotlib.pyplot as plt

class NewWin():
    
   def __init__(self):
       self.win = tk.Tk()

       self.win.geometry("700x360+400+100");
       self.win.title("DR Retina Disease Prediction System")
       self.win.configure(bg="#912388")
       self.canvas = tk.Canvas(self.win, width = 700, height = 360)  
       self.canvas.place(x=0,y=0);


       self.img3 = ImageTk.PhotoImage(Image.open("drmain22.png"))  
       l22 = tk.Label(self.win, image=self.img3,width=700,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l22.place(x=00,y=0)


       self.img2 = ImageTk.PhotoImage(Image.open("drmain22.png"))  
       l11 = tk.Label(self.win, image=self.img2,width=700,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l11.place(x=0,y=0)

 #      self.l1 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
#       self.l1.place(x=0,y=00)

#       self.img3 = ImageTk.PhotoImage(Image.open("can3.jpg"))  
#       l33 = tk.Label(self.win, image=self.img3,width=450,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l33.place(x=0,y=150)

       self.b2 = tk.Button(self.win,text=" Select Data Set File  ",width=25,bg="#126732",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.callback)
       self.b2.place(x=320,y=150)
       
  #     self.l12 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
   #    self.l12.place(x=0,y=430)
       
       self.win.mainloop()

   def callback(self):
       self.name=tkinter.filedialog.askopenfilename()
       #name=fd.askopenfilename() 
       print(self.name)
       self.t1 = tk.Label(self.win,text="",width=22,relief="raised",bg="darkblue",fg="white",font=("cambria",14,"bold"))
       self.t1.place(x=320,y=220)
       self.t1.configure(text=self.name)

#       self.b1 = tk.Button(self.win,text=" Read Data Values  ",width=25,bg="red",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.loading)
 #      self.b1.place(x=320,y=280)
#       fname=self.name
 #      print("File Name="+fname)
  #     if(fname==""):       
   #        tkinter.messagebox.showinfo(" Air Pollution Analysis System "," Please Enter File Name....");
    #   else:
     #      tkinter.messagebox.showinfo(" Air Pollution Analysis System "," Data set of File="+fname+" is Loading ...Please Wait...");
       self.loading()
#             

   def loading(self):
       fname=self.name
       print("File Name="+fname)
       if(fname==""):       
           tkinter.messagebox.showinfo(" DR Retina Disease Prediction System "," Please Enter File Name....");
       else:
           tkinter.messagebox.showinfo(" DR Retina Disease Prediction System "," Data set of File="+fname+" is Loading ...Please Wait...");
           self.dataload()
#       self.win.destroy()
 #      app=Test()
 
   def dataload(self):
       tkinter.messagebox.showinfo(" DR Retina Disease Prediction System "," Data Loading Functio is Called...");
       fname=self.name
       data=p.read_csv(fname)
#       print(data);
       data.columns=[col.lower() for col in data];  # Makes all columns To Lower Case
#       print(data[['employee_name','ssn','dept','salary','doj','no_of_project_assigned','completed']]);
       n=data.shape
       print(" Total Record=")
       max=n[0]
       print(max)
       
  #     for i in range(max):
#           print(i)
 #          print("\t Record")
    
       rec=data.iloc[1];
       print(rec)
       print(rec[0])
       
       #[['employee name','gender','age','location']]);
       
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 
       #mdb=mysql.connector.connect(user="root",password="mj",database="crop",host="localhost",charset='utf8')
       #cursor=mdb.cursor()
       cursor.execute("delete from drdataset");
       mdb.commit()
#       sql="insert into emp values('jjj','222','Tester','12000','2015-2-2','40','25')";
 #      cursor.execute(sql);
 #      sql="select * from emp"



       for i in range(max):
           rec=data.iloc[i]
           f1=str(rec[0])
           f2=str(rec[1])
           f3=str(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           f6=str(rec[5])
           f7=str(rec[6])
           f8=str(rec[7])
           f9=str(rec[8])
           f10=str(rec[9])
           
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10);
           sql="insert into drdataset values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10));
           mdb.commit()
     
       print(" All Data Transfered And Stored in Data Base....");    
       tkinter.messagebox.showinfo(" DR Retina Eye Disease Prediction System "," All Patients Data Transfered And Stored in Data Base....");
       self.win.destroy()
       app=Load();
       
     #  rows=cursor.fetchall()
      # total=cursor.rowcount
      # print("\n Total Data Records=\t"+str(total));


 
 
class Load():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" DR Retina Disease Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from drdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Eye Patients Data Set Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#213473",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('10', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="PAT ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Gender")
       self.tv.heading("#4",text="Optic Distance")
       self.tv.heading("#5",text="Blood Vessel")
       self.tv.heading("#6",text="Blot Hemorrhages")
       self.tv.heading("#7",text="Exudates Area")
       self.tv.heading("#8",text="Macular Edema")
       self.tv.heading("#9",text="Bifurcation")
       self.tv.heading("#10",text="Shannon Entropy") 
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse And Predict Disease ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)

       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" DR Retina Disease Prediction System "," The Process of Analyse and Prediction of Disease Begins");
       self.load.destroy();
       app=Analysis();

class Analysis():
   def __init__(self):

       self.ana = tk.Tk()
       self.ana.geometry("700x380+300+100");
       self.ana.title(" DR Retina Disease Prediction System ")
       self.ana.configure(bg="black")
                          
       self.canvas = tk.Canvas(self.ana, width = 700, height = 380, bg="black")  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("drmain33.png"))  
       l1 = tk.Label(self.ana, image=self.img1,width=700,relief="ridge",fg="black",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)

#       l2 = tk.Label(self.ana,text=" DR Retina  Data Analysis for Disease Prediction  ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=200,y=30)

       
       b1 = tk.Button(self.ana,text=" Extract Featured Attribute  ",width=30,bg="black",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.featureextraction)
       b1.place(x=110,y=150)
       
#       b2 = tk.Button(self.ana,text=" Classification ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.classify)
#       b2.place(x=220,y=180)

#       b3 = tk.Button(self.ana,text=" Prediction Of Crop ",width=30,bg="#c82210",fg="yellow",relief="groove",font=("cambria",12,"bold"),command=self.prediction)
 #      b3.place(x=150,y=180)

       b4 = tk.Button(self.ana, text=" Exit ",width=30,bg="black",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
       b4.place(x=110,y=240)

       self.ana.mainloop()

   def featureextraction(self):
       tkinter.messagebox.showinfo(" DR Retina Disease Prediction System "," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Load1()
       
 #  def classify(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
   #    self.ana.destroy()
  #     app=Classification()

   def prediction(self):
#       tkinter.messagebox.showinfo(" Employee Payroll"," Extraction of Required Data from Oveall Data Set Information...")
       self.ana.destroy()
       app=Load()

   def exit(self):
       self.ana.destroy()



class Load1():
   def __init__(self):
       self.load1 = tk.Tk()
       self.load1.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load1.configure(bg="#985676")
       self.load1.title(" DR Retina Disease Prediction System ")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select optic_distance,blood_vessel,Exudates_area,Macular_edema,bifurcation,shannon_entropy from drdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Extracted Featured Attributes Details Of Patients ",width=50,relief="raised",bg="#235687",fg="white",font=("cambria",14,"bold"))
       l1.place(x=250,y=20)
       
 
       self.tv=ttk.Treeview(self.load1,column=(1,2,3,4,5,6),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="black",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('6', minwidth=50, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
       self.tv.heading("#1",text="Optic Distance")
       self.tv.heading("#2",text="Blood Vessel")
       self.tv.heading("#3",text="Exudates Area")
       self.tv.heading("#4",text="Macular Edema")
       self.tv.heading("#5",text="Bifurcation")
       self.tv.heading("#6",text="Shannon Entropy") 
 
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Predict DR Retina Disease  ",width=40,relief="raised",bg="#235687",fg="white",font=("cambria",14,"bold"),command=self.loading)
       b1.place(x=500,y=14)

       self.load1.mainloop()
 
   def loading(self):
       self.load1.destroy()
       app=Prediction()



class Prediction():
   def __init__(self):
       self.prediction = tk.Tk()
       self.prediction.geometry("401x103+400+200");
       self.prediction.title(" DR Retina Eye Disease Prediction System ")
#       self.prediction.configure(bg="#232342")

       self.canvas = tk.Canvas(self.prediction, width = 400, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("drpre1.png"))  
#       l1 = tk.Label(self.prediction, image=self.img1,width=400,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
#       l1.place(x=0,y=00)

#       l2 = tk.Label(self.prediction,text=" Prediction of Disease   ",width=50,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=30,y=30)

       
       b1 = tk.Button(self.prediction,image=self.img1,width=400,bg="darkblue",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.croppred)
       b1.place(x=0,y=0)
       

#       b4 = tk.Button(self.prediction, text=" Exit ",width=35,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=150,y=200)

       self.prediction.mainloop()

   def croppred(self):
       tkinter.messagebox.showinfo(" DR Retina Eye Disease Prediction "," Disease Prediction Begins...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       cursor.execute("delete from drdisease");
       sql="select * from drdataset"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           id=str(row[0])
           age=str(row[1])
           gen=str(row[2])
           od=float(row[3])
           bv=float(row[4])
           bh=float(row[5])
           ea=float(row[6])
           me=float(row[7])
           bif=float(row[8])
           se=float(row[9])
          
           print("BV=",bv); 
 #          if(od>925):
  #             disease=" Normal "
  #         elif((od<925)):
  #             disease=" Mild"
  #         elif(bv>37230.56 and bv<38500.79):
  #             disease=" Normal "
  #         elif((bv>33000.00 and bv<37229.00) or (bv>38500.00)):
  ##             disease=" Mild Retinopathy"
   #        elif((bif>305 and bif<332)):
   #            disease=" Mild Retinopathy"
   #        elif((bif>=332)):
   #            disease=" Normal"
   #        elif((bh>85000 and bif<91000)):
   #            disease=" Mild Retinopathy"
   #        elif((bh <85000)):
   #            disease=" Normal"
   ##        elif((ea>1015.23 and ea<1051.36)):
     #          disease=" Mild Retinopathy"
    ##       elif((ea==0)):
      #         disease=" Normal"
      #     elif((se>5.5 and se<6.352)):
      #         disease=" Mild Retinopathy"
      #     elif((se>=6.36)):
      #         disease=" Normal"
      #     elif((me>85000)):
      #         disease=" Mild Retinopathy"
      #     elif((me<85000)):
      #         disease=" Normal"
           if(od<925 and ((bv>33000 and bv<37229) or (bv>38500)) and (bif>=305 and bif<332) and (bh>85000 and bh<91000) and (ea>1015 and ea<1051) and (se>5.5 and se<6.3) and (me>85000)):
               disease=" Proliferative DR "
           elif(((bv>33000 and bv<37229) or (bv>38500)) and (bh>85000 and bh<91000) and (ea>1015 and ea<1051) and (me>85000)):
               disease=" Proliferative DR "
           elif(((bv>33000 and bv<37229) or (bv>38500)) and (bh>85000 and bh<91000) and (ea>1015 and ea<1051)):
               disease=" Sever DR "
           elif(((bv>33000 and bv<37229) or (bv>38500)) or (bh>85000 and bh<91000) or (ea>1015 and ea<1051) or (me>85000)):
                disease=" Moderate DR"
           elif((bh>85000 and bh<91000) or (ea>1015 and ea<1051) or (me>85000)):
                disease=" Mild DrR "
           elif((od<925 or (bif>=305 and bif<332) or (se>5.5 and se<6.3))):
                disease=" Mild DR "
           elif((bv<33000) or (bh<85000) or (ea<1015) or (me<85000)):
               #or od<925 or (bif>=305 and bif<332) or (se>5.5 and se<6.3)):
                disease=" No DR "
           else:
               disease=" No DR "
           
            
#               Mild Retinopathy
#                No DR 1 - Mild 2 - Moderate 3 - Severe 4 - Proliferative DR
 
 #              Moderate Retinopathy
  #             Severe Retinopathy
   #            Proliferative Retinopathy
   
           sql="insert into drdisease values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(id,age,gen,od,bv,bh,ea,me,bif,se,disease));
           mdb.commit()
     
       tkinter.messagebox.showinfo(" DR Retina Eye Disease Prediction "," DR Retina Patient Disease Completed ....");
       self.prediction.destroy()
       app=Load2()
       
   def exit(self):
       self.prediction.destroy()
       app=Analysis()

class Load2():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" DR Retina Eye Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from drdisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Eye Disease Predicted Result Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="black",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('11', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="PAT ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Gender")
       self.tv.heading("#4",text="Optic Distance")
       self.tv.heading("#5",text="Blood Vessel")
       self.tv.heading("#6",text="Blot Hemorrhages")
       self.tv.heading("#7",text="Exudates Area")
       self.tv.heading("#8",text="Macular Edema")
       self.tv.heading("#9",text="Bifurcation")
       self.tv.heading("#10",text="Shannon Entropy") 
       self.tv.heading("#11",text="Disease Result") 
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse The Result ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)
 
       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" DR Retina Eye Disease Prediction System "," The Process of Analyzation of Disease Begins");
       self.load.destroy();
       app=Classification();


class Classification():
   def __init__(self):
       
       self.classify = tk.Tk()
       self.classify.geometry("800x465+300+100");
       self.classify.title(" DR Retina Disease Prediction System ")
       self.classify.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.classify, width = 800, height = 380)  
       self.canvas.place(x=0,y=0);

       self.img2 = ImageTk.PhotoImage(Image.open("drclass.png"))  
       l2 = tk.Label(self.classify, image=self.img2,width=800,relief="groove",fg="#323223",font=("cambria",14,"bold"))
       l2.place(x=0,y=00)

#       self.img1 = ImageTk.PhotoImage(Image.open("air1.jpg"))  
 #      l1 = tk.Label(self.classify, image=self.img1,width=500,relief="groove",fg="#323223",font=("cambria",14,"bold"))
  #     l1.place(x=500,y=00)

#       l2 = tk.Label(self.classify,text=" DR Retina Disease Data Analyse On Different Criteria  ",width=60,height=2,relief="groove",bg="#092193",fg="yellow",font=("cambria",14,"bold"))
 #      l2.place(x=100,y=30)

 
       b1 = tk.Button(self.classify,text=" DR Disease Class  ",width=27,bg="#122137",fg="yellow",relief="groove",font=("cambria",13,"bold"),command=self.diseaseclass)
       b1.place(x=70,y=300)
       
       b3 = tk.Button(self.classify,text=" Gender ",width=27,bg="#122137",fg="yellow",relief="groove",font=("cambria",13,"bold"),command=self.gender)
       b3.place(x=440,y=300)

       b2 = tk.Button(self.classify,text=" Age ",width=27,bg="#122137",fg="yellow",relief="groove",font=("cambria",13,"bold"),command=self.age)
       b2.place(x=440,y=380)

       b4 = tk.Button(self.classify,text=" Exit ",width=27,bg="#122137",fg="yellow",relief="groove",font=("cambria",13,"bold"),command=self.exit)
       b4.place(x=70,y=380)

#       b4 = tk.Button(self.classify, text=" Overall Analysis Of Air Polllution ",width=30,bg="#c82210",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
 #      b4.place(x=120,y=390)
       

       self.classify.mainloop()

   def diseaseclass(self):
       tkinter.messagebox.showinfo(" DR Retina Disease Data Analysis ","DR Retina Disease Patient Data Analysis On Disease Class ...")
       self.classify.destroy()
       app=DiseaseClass()
       
   def gender(self):
       tkinter.messagebox.showinfo(" DR Retina Disease Data Analysis ","DR Retina Disease Patient Data Analysis On Gender ...")
       self.classify.destroy()
       app=Gender()

   def age(self):
       tkinter.messagebox.showinfo(" DR Retina Disease Data Analysis ","DR Retina Disease Patient Data Analysis On Age ...")
       self.classify.destroy()
       app=Age()

   def exit(self):
#       tkinter.messagebox.showinfo(" Mushroom Disease Prediction"," Classficaation of Data Based On Location...")
       self.classify.destroy()
      
#   def exit(self):
 #      self.classify.destroy()
  #      app=Analysis()


class Gender():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" DR Retina Disease  Data Analysis Based on Gender  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select gender,res,count(*) from drdisease group by gender,res";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease Data Analysis Based on Gender Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('3', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Gender")
       self.tv.heading("#2",text="Disease Stage")
       self.tv.heading("#3",text="No of Patients")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyze Data Using Graph ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=260,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=30,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" DR Retina Disease Data Data Analysis "," DR Retina Disease Data Processing on Gender Processing classification Begins ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select gender,res,count(*) from drdisease group by gender,res order by age"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       for rec in rows:
           gender=str(rec[0])
           res=str(rec[1])
           cnt=int(rec[2])
           sc=gender+"-"+res        
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()
           
       self.load.destroy()
       app=OverallGenderGraph88()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

       
       
class OverallGenderGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Gender Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease Data Analysis Based On Gender Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=10)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=12, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas3.place(x=650,y=70);
#       self.canvas.pack();

#       figure3 = plt.Figure(figsize=(10,7), dpi=100)
 #      ax1 = figure3.add_subplot(221)

   
       figure3 = plt.Figure(figsize=(13,9), dpi=70)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e", "#d62728", "#8c564b","#982363","red","#ff7f0e"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
     #  autopct='%1i%%', shadow=True, startangle=140)
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
#       ax1.Legend()
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
     #  app=DeptGraph881()
       app=Classification()


#       self.load.mainloop()       
       

class Age():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" DR Retina Disease  Data Analysis Based on Age  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select patid,age,res from drdisease ";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('3', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Patient ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Disease Stage")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Classify Age Group ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=260,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=30,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" DR Retina Disease Data Data Analysis "," DR Retina Disease Data Processingn on Age Group Processing classification Begins ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from temp");

       sql="select patid,age,res from drdisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       for rec in rows:
           id=str(rec[0])
           age=int(rec[1])
           res=str(rec[2])
           
           if(age>10 and age<20):
               ageclass="Age(10-20) Class"
           elif(age>20 and age<30):
               ageclass="Age(20-30) Class"
           elif(age>30 and age<40):
               ageclass="Age(30-40) Class"
           elif(age>40 and age<50):
               ageclass="Age(40-50) Class"
           elif(age>50 and age<60):
               ageclass="Age(50-60) Class"
           else:
               ageclass="Age(>60) Class"
        
           sql="insert into temp values(%s,%s)"
           cursor.execute(sql,(ageclass,res));
           mdb.commit()
           
       self.load.destroy()
       app=Age1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

       
       
class Age1():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" DR Retina Disease  Data Analysis Based on Age Group  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select age,count(*) from temp group by age";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="5")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Age")
       self.tv.heading("#2",text="No OF Patients")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" DR Retina Disease Data Analysis "," DR Retina  Disease Data Analysis Using Graphical Representation ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select age,count(*) from temp group by age order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           age=str(row[0])
           cnt=int(row[1])
#           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(age,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
           
#       self.load.destroy()
 #      app=OverallLoc1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def selected(self,a):
       print(" Item Clicke");
       self.data=self.tv.item(self.tv.selection())
       print(self.data)
       item=self.tv.selection()[0]
       print(item)
       self.age=str(self.tv.item(item)['values'][0])
       print(self.age)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select age,res,count(*) from temp where age='"+self.age+"' group by age,res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
 

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallAgeGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Age Group Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease Data Analysis Based On Age Group Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=10)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=12, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       self.canvas3.place(x=650,y=70);
#       self.canvas.pack();

#       figure3 = plt.Figure(figsize=(10,7), dpi=100)
 #      ax1 = figure3.add_subplot(221)

   
       figure3 = plt.Figure(figsize=(13,9), dpi=70)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
     #  autopct='%1i%%', shadow=True, startangle=140)
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
#       ax1.Legend()
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
     #  app=DeptGraph881()
       app=Classification()


       self.load.mainloop()       


class DiseaseClass():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" DR Retina Disease Data Analysis Based on Disease Class  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select res,count(*) from drdisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease Data Analysis Based on Disease Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Disease Class")
       self.tv.heading("#2",text=" Total Patient ")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" DR Retina Disease Data Analysis "," DR Retina Disease Data Analysis Using Graphical Representation ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select res,count(*) from drdisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           res=str(row[0])
           cnt=int(row[1])
           sc=res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallLocGraph88()
           
#       self.load.destroy()
 #      app=OverallLoc1()

            
#       self.load.destroy()
#       app=DeptAllLoad2()

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallLocGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Disease Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" DR Retina Disease Data Analysis Based On Disease Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="drretina",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'NoofPat': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['NoofPat','dc'])
       df2 = df2[['NoofPat','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=10, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas3.place(x=700,y=70);
#       self.canvas.pack();

#       figure3 = plt.Figure(figsize=(10,7), dpi=100)
 #      ax1 = figure3.add_subplot(221)

   
       figure3 = plt.Figure(figsize=(8,6), dpi=100)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
     #  autopct='%1i%%', shadow=True, startangle=140)
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  
#       ax1.Legend()
       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
     #  app=DeptGraph881()
       app=Classification()





class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry("1000x600+300+100");
       self.root.title(" DR Retina Disease Prediction System ")
       self.root.configure(bg="darkblue")
       self.canvas = tk.Canvas(self.root, width = 1000, height = 600)  
       self.canvas.place(x=0,y=0);


       self.img1 = ImageTk.PhotoImage(Image.open("drmain11.png"))  
#       l1 = tk.Label(self.root, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l1.place(x=0,y=00)



       b1 = tk.Button(self.root,image=self.img1,width=1000,height=600,bg="darkblue",fg="white",relief="raised",font=("cambria",14,"bold"),command=self.createNewWindow)
       b1.place(x=0,y=0) 
       
       #b2 = tk.Button(self.root, text=" Exit ",width=25,bg="#782323",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.exit)
      # b2.place(x=50,y=200)

       self.root.mainloop()

   def createNewWindow(self):
       self.root.destroy()
       app=NewWin()
       

   def exit(self):
       self.root.destroy()



#app=OverallLocGraph88()()          
#pp=Classification()          

app=Test()
#app=Analysis()
#app=DayGraph88()
#app=OverallLocGraph88()