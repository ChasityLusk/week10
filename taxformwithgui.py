"""
File: taxformwithgui.py
Tac Calculator.
"""

from breezypythongui import EasyFrame
import math

class TaxCalculatorGUI(EasyFrame):
    def __init__(self):
        """Sets up window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")
        
        # Label and field for the Gross Income
        self.addLabel(text = "Gross Income", row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0,
                                            row = 0,
                                            column = 1)
        # Label and field for the Dependents
        self.addLabel(text = "Dependents", row = 1, column = 0)
        self.dependentsField = self.addIntegerField(value = 0,
                                            row = 1,
                                            column = 1)
        # Label and field for the Total Tax output
        self.addLabel(text = "Total tax", row = 2, column = 0)
        self.outputField = self.addFloatField(value = 0.0,
                                              row = 2,
                                              column = 1,
                                              precision = 2,
                                              state = "readonly")
        # Compute button
        self.addButton(text = "Compute", row = 3, column = 0,
                       columnspan = 2, command = self.compute)

    # Event handling method
    def compute(self):
         income = self.incomeField.getNumber()
         dependents = self.dependentsField.getNumber()

         # Tax Formula
         deduction = dependents * 3000
         taxableIncome = max(0, income - deduction)

         if taxableIncome <= 10000:
             tax = taxableIncome * 0.10
         elif taxableIncome <= 30000:
             tax = 10000 * 0.10 + (taxableIncome - 10000) * 0.20
         else:
             tax = 10000 * 0.10 + 20000 * 0.20 + (taxableIncome - 30000)

         self.outputField.setNumber(tax)
        
        
if __name__ == "__main__":
    TaxCalculatorGUI().mainloop()
        

        
    
