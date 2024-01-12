from tkinter import *

# Initialize the expression variable
expression = ""

# Function to update expression in the text entry box
def press(item):
  global expression
  if item == "=":
      try:
          total = str(eval(expression))
          equation.set(total)
          expression = total
      except:
          equation.set("error")
          expression = ""
  elif item == "c":
      expression = ""
      equation.set("")
  elif item == "<-":
      expression = expression[:-1]
      equation.set(expression)
  else:
      expression += str(item)
      equation.set(expression)

# Driver code
if __name__ == "__main__":
 # Create a GUI window
 gui = Tk()
 # Set the background color of GUI window
 gui.configure(background="black")
 # Set the title of GUI window
 gui.title("Simple Calculator")
 # Set the configuration of GUI window
 gui.geometry("300x300")
 # Center the window
 gui.eval('tk::PlaceWindow . center')
 # StringVar() is the variable class
 # We create an instance of this class
 equation = StringVar()
 # Create the text entry box for showing the expression
 expression_field = Entry(gui, textvariable=equation, bg="white", fg="black")
 expression_field.grid(columnspan=4, ipadx=70)

 # Create a Buttons and place at a particular location inside the root window
 # When user press the button, the command or function affiliated to that button is executed
 for num in range(9):
    Button(gui, text=str(num+1), fg='black', bg='white', command=lambda num=num: press(num+1), height=1, width=7).grid(row=(num//3)+3, column=num%3)

 Button(gui, text=' 0 ', fg='black', bg='white', command=lambda: press(0), height=1, width=7).grid(row=6, column=1)

 # Backspace button
 Button(gui, text='<-', fg='black', bg='white', command=lambda: press("<-"), height=1, width=7).grid(row=6, column=2)

 # Decimal point button
 Button(gui, text=' . ', fg='black', bg='white', command=lambda: press('.'), height=1, width=7).grid(row=5, column=3)

 # Power function button
 Button(gui, text=' ^ ', fg='black', bg='white', command=lambda: press("**"), height=1, width=7).grid(row=4, column=3)

 # Operation buttons
 Button(gui, text=' + ', fg='black', bg='white', command=lambda: press("+"), height=1, width=7).grid(row=2, column=0)
 Button(gui, text=' - ', fg='black', bg='white', command=lambda: press("-"), height=1, width=7).grid(row=2, column=1)
 Button(gui, text=' * ', fg='black', bg='white', command=lambda: press("*"), height=1, width=7).grid(row=2, column=2)
 Button(gui, text=' / ', fg='black', bg='white', command=lambda: press("/"), height=1, width=7).grid(row=2, column=3)
 Button(gui, text=' % ', fg='black', bg='white', command=lambda: press("%"), height=1, width=7).grid(row=3, column=3)

 # Equal button
 Button(gui, text=' = ', fg='black', bg='white', command=lambda: press("="), height=1, width=7).grid(row=6, column=3)

 # Clear button
 Button(gui, text='Clear', fg='black', bg='white', command=lambda: press("c"), height=1, width=7).grid(row=6, column=0)

 # Start the GUI
 gui.mainloop()
