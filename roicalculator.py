class roi_rental():
    """calculate the return on investment of a rental property"""
    def __init__(self, income, expenses, cashflow, investment):
        self.income = income
        self.cashflow = cashflow
        self.expenses = expenses
        self.investment = investment
    def calc_income(self, r_i, laundry, storage, misc):
        self.income = r_i + laundry + storage + misc 
        print(self.income) 
    def calc_expenses(self, tax, insurance, util, HOA, lawnsnow, vacancy, repairs, capex, propmanage, mort):
        self.expenses = tax + insurance + util + HOA + lawnsnow + vacancy + repairs + capex + propmanage + mort
        print(self.expenses)
    def calc_cashflow(self):
        self.cashflow = self.income - self.expenses
        print(self.cashflow)
    def calc_investment(self, downpay, closing, rehab, misc):
        self.investment = downpay + closing + rehab + misc
        print(self.investment)

    def calc_roi(self):
        roi = (self.cashflow*12) / self.investment
        print(f"{roi*100} %")


better_pockets = roi_rental(0, 0, 0, 0)

better_pockets.calc_income(2000, 0, 0, 0)

better_pockets.calc_expenses(150,100, 0, 0, 0, 100, 100, 100, 200, 860)

better_pockets.calc_investment(40000, 3000, 7000, 0)

better_pockets.calc_cashflow()

better_pockets.calc_roi()

        
    
    
    

        

