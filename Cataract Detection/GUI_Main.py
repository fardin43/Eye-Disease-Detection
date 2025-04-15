import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk


##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Cataract Disease Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('img.png')
image2 = image2.resize((w, h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Cataract Disease Detection",font=("Algerian", 20, ''),
                    background="Sky blue", fg="white", width=80, height=3)
label_l1.place(x=0, y=0)

label_l1 = tk.Label(root, text="",font=("Algerian", 20, ''),
                    background="Sky blue", fg="white", width=80, height=100)
label_l1.place(x=700, y=90)

image2 = Image.open('doctor_img.png')
image2 = image2.resize((700, 700), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=700, y=97)

label_l1 = tk.Label(root, text="About us",font=("Algerian", 25, ''),
                    background="#E6EBFF", fg="Dark blue", width=10, height=1)
label_l1.place(x=70, y=150)

label_l1 = tk.Label(root, text="In the realm of healthcare, technology isn't just a tool; it's a lifeline, \n empowering us to safeguard our most precious asset – our health",font=("Calibri", 14, ''),
                    background="#DBE9FA", fg="black", width=60, height=2)
label_l1.place(x=70, y=250)


# label_l1 = tk.Label(root, text="\n\n Predicting heart attacks isn't just about data;\n it's about saving lives. Harnessing the power\n of technology, we pave the way for early\n detection and prevention, ensuring\n healthier tomorrows",font=("Calibri",10, ''),
#                     background="#E6EBFF", fg="Sky blue", width=40, height=10)
# label_l1.place(x=60, y=450)

# image2 = Image.open('label_heart.png')
# image2 = image2.resize((50, 35), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=60, y=450)

label_l1 = tk.Label(root, text="\n\n Vision is a gift, and preserving it is paramount.\n   Through the lens of technology, we illuminate \n the path to early detection and treatment,\n safeguarding precious sight for \n generations to come",font=("Calibri", 10, ''),
                    background="#E6EBFF", fg="gray", width=40, height=10)
label_l1.place(x=60, y=450)

image2 = Image.open('label_eye.png')
image2 = image2.resize((50, 35), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=60, y=450)



label_l1 = tk.Label(root, text="\n\n Time is of the essence when it comes to \n emergencies.With just a click, bridge the gap\n between distress and assistance, ensuring swift\n intervention and saving precious moments\n that could mean the difference between\n life and loss",font=("Calibri", 10, ''),
                    background="#E6EBFF", fg="gray", width=40, height=10)
label_l1.place(x=400, y=450)

image2 = Image.open('label_help.png')
image2 = image2.resize((50, 35), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=400, y=450)


#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()




# button1 = tk.Button(root, text="SIGN IN", command=log, width=13, height=1, font=('Calibri', 10, ' '), bg="sky blue", fg="white")
# button1.place(x=1150, y=55)

# button1 = tk.Button(root, text="SIGN Up", command=reg, width=13, height=1, font=('Calibri', 10, ' '), bg="sky blue", fg="white")
# button1.place(x=1260, y=55)


button4 = tk.Button(root, text="SIGN IN", command=log, width=13, height=1,font=('times 12 bold '),bd=0,bg="sky blue", fg="white")
button4.place(x=1150, y=55)


button4 = tk.Button(root, text="SIGN UP", command=reg, width=13, height=1,font=('times 12 bold '),bd=0,bg="sky blue", fg="white")
button4.place(x=1260, y=55)



root.mainloop()