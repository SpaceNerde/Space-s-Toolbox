import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic




# Main Calculator Window
    
class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
       
        # implementing ui sheet
        
        uic.loadUi("ui/calculator.ui", self)
        
        # connecting buttons to function
        
        self.button_0.clicked.connect(self.action0)
        self.button_1.clicked.connect(self.action1)
        self.button_2.clicked.connect(self.action2)
        self.button_3.clicked.connect(self.action3)
        self.button_4.clicked.connect(self.action4)
        self.button_5.clicked.connect(self.action5)
        self.button_6.clicked.connect(self.action6)
        self.button_7.clicked.connect(self.action7)
        self.button_8.clicked.connect(self.action8)
        self.button_9.clicked.connect(self.action9)
        self.button_ce.clicked.connect(self.action_ce)
        self.button_div.clicked.connect(self.action_div)
        self.button_mul.clicked.connect(self.action_mul)
        self.button_dot.clicked.connect(self.action_dot)
        self.button_plus.clicked.connect(self.action_plus)
        self.button_minus.clicked.connect(self.action_minus)
        self.button_equals.clicked.connect(self.action_equals)       
        
    # action functions
        
    def action_equals(self):     
        try:
            ans = eval(self.screen.text())
            
            self.screen.setText(str(ans))
        except:
            self.screen.setText("Error")
        
    def action0(self):
        text = self.screen.text() 
        self.screen.setText(text + str(0))
        
    def action1(self):
        text = self.screen.text() 
        self.screen.setText(text + str(1))
        
    def action2(self):
        text = self.screen.text() 
        self.screen.setText(text + str(2))
        
    def action3(self):
        text = self.screen.text() 
        self.screen.setText(text + str(3))
        
    def action4(self):
        text = self.screen.text() 
        self.screen.setText(text + str(4))
        
    def action5(self):
        text = self.screen.text() 
        self.screen.setText(text + str(5))
        
    def action6(self):
        text = self.screen.text() 
        self.screen.setText(text + str(6))
        
    def action7(self):
        text = self.screen.text() 
        self.screen.setText(text + str(7))
        
    def action8(self):
        text = self.screen.text() 
        self.screen.setText(text + str(8))
        
    def action9(self):
        text = self.screen.text() 
        self.screen.setText(text + str(9))
    
    def action_minus(self):
        text = self.screen.text() 
        self.screen.setText(text + "-")
        
    def action_plus(self):
        text = self.screen.text() 
        self.screen.setText(text + "+")
        
    def action_mul(self):
        text = self.screen.text() 
        self.screen.setText(text + "*")
        
    def action_div(self):
        text = self.screen.text() 
        self.screen.setText(text + "/")
        
    def action_dot(self):
        text = self.screen.text() 
        self.screen.setText(text + ".")
    
    def action_ce(self):
        self.screen.clear()   

# creating main loop

if __name__ == "__main__":
    
    app = QApplication([])
        
    window = CalculatorWindow()
    window.show()      
        
    # exiting loop
        
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window")