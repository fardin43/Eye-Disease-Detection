import tkinter as tk
#from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import numpy

##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Heart Disease and Catract Disease")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('1.jpg')
image2 = image2.resize((950,900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=600, y=0)  # , relwidth=1, relheight=1)


label_l1 = tk.Label(root, text="Heart Disease and Catract Disease",font=("Times New Roman", 30, 'bold'),
                    background="#607B8B", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)





######################### For Registration form #####################################################################

Tp = tk.StringVar()
Cp = tk.StringVar()




# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS data"
               "(Tp TEXT, Cp TEXT)")
db.commit()




def insert():
    TropI = Tp.get()
    Cpknb = Cp.get()
    

    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    
    # # validation
    if (TropI.isdigit() or (TropI == "")):
        ms.showinfo("Message", "please enter TP")
    elif (Cpknb == ""):
        ms.showinfo("Message", "Please Enter CP")
   
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO data(Tp, Cp) VALUES(?,?)',
                (TropI, Cpknb))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Data Added Successfully !')
            window.destroy()
            
            from subprocess import call
            call(["python", "Log.py"])
            window.destroy()

#####################################################################################################################################################

# ------------------------- For Registration Frame 


frame_alpr = tk.LabelFrame(root, text=" --Form-- ", width=600, height=702, bd=5, font=('times', 14, ' bold '),fg="white",bg="#607B8B")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=0, y=90)








l4 = tk.Label(frame_alpr, text="Trop I :", width=12, font=("Times new roman", 15, "bold"), bd=5,fg="black")
l4.place(x=100, y=300)
t3 = tk.Entry(frame_alpr, textvar=Tp, width=20, font=('', 15))
t3.place(x=300, y=300)
# that is for label 4()

l9 = tk.Label(frame_alpr, text="Cp knb :", width=12, font=("Times new roman", 15, "bold"),bd=5, fg="black")
l9.place(x=100, y=350)
t8 = tk.Entry(frame_alpr, textvar=Cp, width=20, font=('', 15), show="")
t8.place(x=300, y=350)





btn = tk.Button(frame_alpr, text="Submit", bg="#FAEBD7",font=("times new roman",20,"bold"),fg="black", width=9, height=1, bd=5,command=insert)
btn.place(x=220, y=470)

 # ------------------------------------------------------------
 
 # ------------------ Function for button
 
def log():
    from subprocess import call
    call(["python","Log.py"])
    root.destroy()
    
def con():
    from subprocess import call
    call(["python","GUI_main.py"])
    root.destroy()

def window():
  root.destroy()
  
    
button1 = tk.Button(root, text="HOME", command=con, width=12, height=1,font=('times 15 bold underline'),bd=0, bg="#3CB371", fg="white")
button1.place(x=635, y=350)



button4 = tk.Button(root, text="EXIT", command=window, width=12, height=1,font=('times 15 bold underline'),bd=0,bg="#FF4500", fg="white")
button4.place(x=635, y=450)




# label_l1 = tk.Label(root, text="**Exam Video Suspicious Activity Detection @ 2023 by **",font=("Times New Roman", 10, 'bold'),
#                     background="black", fg="white", width=250, height=2)
# label_l1.place(x=0, y=800)


root.mainloop()