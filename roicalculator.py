class roi_rental():
    """calculate the return on investment of a rental property"""
    def __init__(self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = investment
    def calc_roi(self):
        mc = self.income - self.expenses
        roi = mc * 12 / self.investment
        print(f"{roi * 100}%") 
    
    
    
my_rental_property = roi_rental(2000, 1610, 50000)
my_rental_property.calc_roi()

        

