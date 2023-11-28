from tkinter import *

root=Tk()

root.geometry("244x344")

root.title("CAlCULATOR BY Abhijit Das")



# Function Define...

# .cget function use for extract text from widget or buttons..
# event.widget give use the buttons which we click..


def click(event):
    text=event.widget.cget("text")     
    if text== "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())   # convert in intiger..
        else:
            try:

                value=eval(screen.get())        # evel evaluated the number or string.. like 2*5=10
                
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



                       
                                        
# create tkinter variable..
scvalue=StringVar()

scvalue.set("")

# Create a Entry wedget...
screen=Entry(root , textvariable=scvalue ,bg="white" , font="lucida 20 bold")

screen.pack(fill=X ,ipadx=8 , ipady=10)





# Create a Frame...

f1=Frame(root , bg="red")
f1.pack()

# Create a Butoon..
b1=Button(f1 , text="7" , padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx=3 , pady=5)

# need to bind the button by click event..
b1.bind("<Button-1>" , click)


b1=Button(f1 , text="8" ,  padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx=3 , pady=5)

b1.bind("<Button-1>" , click)


b1=Button(f1 , text="9" ,    padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx=3 , pady=5)

b1.bind("<Button-1>" , click)




b1=Button(f1 , text="-" ,    padx=15 , pady=3,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)




# CREATE 4 , 5 , 6 , +  BUTTONS..

f1=Frame(root , bg="red")
f1.pack()

# Create a Butoon..
b1=Button(f1 , text="4" ,  padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 0.5, pady=2)

# need to bind the button by click event..
b1.bind("<Button-1>" , click)


b1=Button(f1 , text="5" ,    padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)


b1=Button(f1 , text="6" ,      padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)




b1=Button(f1 , text="+" ,  padx=15 , pady=3,  font="lucida 20 bold")
b1.pack(side=LEFT ,padx= 3, pady=5)

b1.bind("<Button-1>" , click)




#  CREATE 1 , 2 , 3 


f1=Frame(root , bg="red")
f1.pack()

# Create a Butoon..
b1=Button(f1 , text="1" , padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

# need to bind the button by click event..
b1.bind("<Button-1>" , click)


b1=Button(f1 , text="2" ,  padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)


b1=Button(f1 , text="3" ,   padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)



b1=Button(f1 , text="*" , padx=15 , pady=3,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)








# CREATE 0 , % , " . " 

f1=Frame(root , bg="red")
f1.pack()

# Create a Butoon..
b1=Button(f1 , text="0" , padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

# need to bind the button by click event..
b1.bind("<Button-1>" , click)


b1=Button(f1 , text="%" ,  padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)


b1=Button(f1 , text="." ,    padx=3 , pady=2,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)




b1=Button(f1 , text="/" , padx=15 , pady=3,  font="lucida 20 bold")
b1.pack(side=LEFT , padx= 3, pady=5)

b1.bind("<Button-1>" , click)





# CREATE / , = , C 

f1=Frame(root , bg="red")
f1.pack()


b1=Button(f1 , text="=" ,  padx=15 , pady=3,  font="lucida 20 bold")
b1.pack(side=LEFT , padx=8 , pady=10)

b1.bind("<Button-1>" , click)


b1=Button(f1 , text="C" ,    padx=15 , pady=3,  font="lucida 20 bold")
b1.pack(side=LEFT , padx=8 , pady=10)

b1.bind("<Button-1>" , click)







root.mainloop()


