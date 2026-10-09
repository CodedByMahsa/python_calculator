# tkinter : this is going to be our graphical user interface library 
# math : this library performs mathmetical operations such as square root
import tkinter
import math
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]
# for indentifying later we separate the lists!
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count= len(button_values)#5
column_count=len(button_values[0])#4

color_cherry_red="#C24641"
color_black="#1C1C1C"
color_dark_gray="#505050"
color_red="#990012"
color_white="#FFFFFF"

#window_setup
window = tkinter.Tk() #create the window
window.title("calculator")
window.resizable(False,False)
# here we need to specify the parent we are basically placing the frame inside the window
frame = tkinter.Frame(window)
# also we specify frame here as the parent
#anchore is for alignment!
#width=column_count keeps buttons width consistent as the nubmer of columns changes!
label = tkinter.Label(frame,text="0", font=("Arial",45),background=color_black,
                      foreground=color_white,anchor="e", width=column_count)

#in Tkinter pack() is a layout inside its parent window and decide where/how it should be placed!
# we in sticky refers to east and west and we  also have north and south
label.grid(row=0,column=0, columnspan=column_count,sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value=button_values[row][column]
        button=tkinter.Button(frame, text=value, font=("Arial",30),
                              width=column_count-1,height=1,
                              command=lambda value=value: button_clicked(value)) 
        if value in top_symbols:
            button.config(foreground=color_black, background=color_cherry_red)
        elif value in right_symbols:
            button.config(foreground=color_white,background=color_red)
        else:
            button.config(foreground=color_white,background=color_dark_gray)    
        button.grid(row=row+1,column=column)

frame.pack()

A="0"
operator=None
B=None

def clear_all():
   global A, B, operator
   A="0"
   operator=None
   B=None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num=int(num)
    return str(num)    

def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B=label["text"]
                numA=float(A)
                numB=float(B)

                if operator == "+":
                    label["text"]=remove_zero_decimal(numA+numB)
                elif operator == "-":
                    label["text"]=remove_zero_decimal(numA-numB)
                elif operator == "×":
                    label["text"]=remove_zero_decimal(numA*numB)
                elif operator == "÷":
                    label["text"]=remove_zero_decimal(numA/numB)

                clear_all()
        elif value in "+-×÷":
            if operator is None:
                A=label["text"]
                label["text"]="0"
                B="0"
            operator = value        
    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"]="0" 
        elif value =="+/-":
           result=float(label["text"])*-1
           label["text"]=remove_zero_decimal(result)
        elif value == "%":
            result=float(label["text"])/100
            label["text"]=remove_zero_decimal(result)   

    else: #digits or . or √
        if value == ".":
            if value not in label["text"]:
                label["text"]+=value
        elif value in "0123456789":
            if label["text"] =="0":
                label["text"]=value #replace 0
            else:
                label["text"]+=value#append digit  
        elif value == "√":
            if value not in label["text"]:
                number=float(label["text"])
                result=math.sqrt(number)
                label["text"]=remove_zero_decimal(result)

#center the window
window.update()#update window with the new size dimensions
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))
#format "(w)*(h)+(x)+(y)"

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#cuz i want the window to continue running i use this main loop!
window.mainloop()