from tkinter import Tk, Entry, StringVar, Button

expression = ""

class Calculator:
    
    def btnClik(self, num):
        
        global expression
        expression += str(num)
        self.inputText.set(expression)

    def clear(self):

        global expression
        expression = ""
        self.inputText.set(expression)

    def equals(self):

        global expression
        try:
            result=str(eval(expression))
        except:
            self.clear()
            result=("ERROR")
        self.inputText.set(result)

    def __init__(self, master):
        master.title("GUI Calculator v.1")
        
        self.inputText = StringVar()
        self.inputText.set("Test")
        self.display = Entry(master,font=('arial',16), textvariable=self.inputText, width=30)
        self.display.grid(row=0,columnspan=4,pady=3)

        buttonLayout = [
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["C", "0", "=", "/"]
            ]
        
        seven = Button(master, text=buttonLayout[0][0], command=lambda:self.btnClik(7))
        seven.grid(row=1, column=0, sticky="we")
        eight = Button(master, text=buttonLayout[0][1], command=lambda:self.btnClik(8))
        eight.grid(row=1, column=1, sticky="we")
        nine = Button(master, text=buttonLayout[0][2],  command=lambda:self.btnClik(9))
        nine.grid(row=1, column=2, sticky="we") 
        multi = Button(master, text=buttonLayout[0][3], command=lambda:self.btnClik("*"))
        multi.grid(row=1, column=3, sticky="we")

        four = Button(master, text=buttonLayout[1][0], command=lambda:self.btnClik(4))
        four.grid(row=2, column=0, sticky="we")
        five = Button(master, text=buttonLayout[1][1], command=lambda:self.btnClik(5))
        five.grid(row=2, column=1, sticky="we")
        six = Button(master, text=buttonLayout[1][2], command=lambda:self.btnClik(6))
        six.grid(row=2, column=2, sticky="we") 
        subtract = Button(master, text=buttonLayout[1][3], command=lambda:self.btnClik("-"))
        subtract.grid(row=2, column=3, sticky="we")

        one = Button(master, text=buttonLayout[2][0], command=lambda:self.btnClik(1))
        one.grid(row=3, column=0, sticky="we")
        two = Button(master, text=buttonLayout[2][1], command=lambda:self.btnClik(2))
        two.grid(row=3, column=1, sticky="we")
        three = Button(master, text=buttonLayout[2][2], command=lambda:self.btnClik(3))
        three.grid(row=3, column=2, sticky="we") 
        add = Button(master, text=buttonLayout[2][3], command=lambda:self.btnClik("+"))
        add.grid(row=3, column=3, sticky="we")


        clear = Button(master, text=buttonLayout[3][0], command=lambda:self.clear())
        clear.grid(row=4, column=0, sticky="we")
        zero = Button(master, text=buttonLayout[3][1], command=lambda:self.btnClik(0))
        zero.grid(row=4, column=1, sticky="we")
        equal = Button(master, text=buttonLayout[3][2], command=lambda:self.equals())
        equal.grid(row=4, column=2, sticky="we")
        division = Button(master, text=buttonLayout[3][3], command=lambda:self.btnClik("/"))
        division.grid(row=4, column=3, sticky="we") 
       

        

def main():
    gui = Tk()
    object = Calculator(gui)
    gui.mainloop()

if __name__ == "__main__":
    main()


