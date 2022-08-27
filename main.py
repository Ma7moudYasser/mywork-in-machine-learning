# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from tkinter import *
from tkinter import ttk

pro = Tk()
pro.title('LOGIN SYSTEM')
pro.geometry('500x500')
pro.resizable(False, False)
pro.config(background='#D5DBDB')
pro.iconbitmap('key.ico')
# The title of the project
title = Label(pro, text = 'LOGIN SYSTEM', font = ('Couriere', 15), bg = 'black', fg = 'white')
title.pack(fill = X)
# Making Frame for the app
fr1 = Frame(pro,width= '300', height='350', bg = 'whitesmoke')
fr1.pack(pady=30)
#------------Image
photo = PhotoImage(file = "encrypted.png")
panel1 = Label(pro, image=photo)
panel1.place(x = 200, y=60)
#-----------Label1----------

lb1 = Label(fr1, text = 'USERNAME :', font=('Courier', 15), bg='whitesmoke')
lb1.place(x = 10, y= 140)
lb2 = Label(fr1, text = 'PASSWORD :', font= ('Courier', 15), bg='whitesmoke')
lb2.place(x = 10, y = 180)

#-------------Entry ---------
en1 = Entry(fr1)
en1.place(x= 140, y = 145 )
en2 = Entry(fr1)
en2.place(x= 140, y= 185)


#----------Buttons------------
bt1 = Button(fr1, text = 'LOGIN', font = ('Courier', 15), bg = '#76D7C4', width = 11)
bt1.place(x = 15, y = 260)

bt2 = Button(fr1, text = 'SIGN IN', font=('Courier', 15), bg = '#CD6155' , width = 11)
bt2.place(x = 155, y = 260 )

#-----------Checkbox -------------
c1 = Checkbutton(fr1, text = 'Forget password !', font=('Courier', 15),bg = 'whitesmoke' )
c1.place(x = 40, y = 220)
pw = Label(fr1, text = 'Developed By M.YASSER @2022', font = ('Courier', 9), bg = 'whitesmoke')
pw.place(x=60, y = 320)



pro.mainloop()