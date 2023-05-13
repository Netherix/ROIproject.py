class ROI_calc():

    def __init__(self, income, expenses, investment):
        self.income = income
        self.expenses = expenses
        self.investment = int(investment)

    def my_cash_flow(self):
        cash_flow = int(self.income) - int(self.expenses)
        return cash_flow
    
    def my_roi(self):
        annual_cash_flow = self.my_cash_flow() * 12
        return_on_investment = annual_cash_flow / self.investment 
        return return_on_investment 
        

def calculate():
    income = ""
    expenses = ""
    roi = None

    print("What would you like to do?")
    print("1. Enter my income and expenses.")
    print("2. Calculate my cash flow.")
    print("3. Calculate my ROI.")
    print("4. Exit the program.")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            income = input("Enter your monthly income: ")
            expenses = input("Now enter your expenses: ")
            investment = input("Enter the amount of your total investment: ")
            roi = ROI_calc(income, expenses, investment)

        if choice == "2":
            if income == "" or expenses == "":
                print("Please enter your income and expenses first.")
            else:
                cash_flow = roi.my_cash_flow()
                print(f"Your cash flow is: {cash_flow}")

        if choice == "3":
            if roi is None:
                print("Please enter your income and expenses first.")
            else:
                roi_percent = roi.my_roi()
                print(f"Your ROI is: {roi_percent}") 

        if choice == "4":
            print("Thank you for choosing our services.")
            break


calculate()
