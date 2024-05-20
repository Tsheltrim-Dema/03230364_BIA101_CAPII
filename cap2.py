class Employee:
    def __init__(self, name, income, position, organization, dividend_income, num_children, rental_income, self_education):
        # this suit of code initlized 
        self._name = name  
        self._income = income 
        self._position = position  
        self._organization = organization
        self._dividend_income = dividend_income
        self._num_children = num_children
        self._rental_income = rental_income
        self._self_education = self_education

class TaxCalculator:
    def __init__(self, employee):
        # this code help to initialize the tax calculation as per employee information
        self._employee = employee  
        self._taxable_income = self._calculate_taxable_income()  # it about taxable income
        self._tax_amount = self._calculate_tax_amount()  # calculation of tax

    def _calculate_taxable_income(self):
        # it shows taxable income based on there postion
        taxable_income = self._employee._income

        # deduction based on position
        if self._employee._position == "Regular":
            taxable_income -= 0.10 * self._employee._income  #deduction of 10%  provident fund
            taxable_income -= 0.05 * self._employee._income  # deduction of 5% group insurence scheme
        # Deduction for children
        child_deduction = min(350000 * self._employee._num_children, taxable_income)
        taxable_income -= child_deduction

        # Deduction for rental income
        rental_deduction = 0.20 * self._employee._rental_income
        taxable_income -= rental_deduction

        # Deduction for self-education
        if self._employee._self_education:
            education_deduction = min(350000, taxable_income)
            taxable_income -= education_deduction

        # General deduction of income as per the Income Tax Act of Bhutan
        general_deductions = min(0.05 * taxable_income, 350000)  # As per income tax of bhutan 5% or 350,000 of income, whichever is lower is deductable
        taxable_income -= general_deductions

        return taxable_income

    def _calculate_tax_amount(self):
        # this defines general tax rates of income per yaar of individuals
        tax_rates = [
            (300000, 0.0),
            (400000, 0.10),
            (650000, 0.15),
            (1000000, 0.20),
            (1500000, 0.25),
            (float('inf'), 0.30)
        ]

        # This code helps to calculate the amount of tax based on the above-provided tax rate of Bhutan per annum
        tax_amount = 0
        taxable_income = self._taxable_income

        for limit, rate in tax_rates:
            if taxable_income <= 0:
                break
            if taxable_income > limit:
                tax_amount += limit * rate  # Calculate tax amount for current slab
                taxable_income -= limit  # Deduct current slab from taxable income
            else:
                tax_amount += taxable_income * rate  # Calculate tax amount for remaining income
                break

        # Apply surcharge if applicable (10% surcharge if tax amount >= 1,000,000)
        if tax_amount >= 1000000:
            tax_amount += 0.10 * tax_amount  # Apply 10% surcharge

        return tax_amount

    def calculate_total_tax(self):
        # Calculate the total tax including TDS on dividend income
        total_tax = self._tax_amount
        dividend_income = self._employee._dividend_income
        if dividend_income > 30000:
            tds = 0.10 * dividend_income  # 10% TDS on the whole dividend income
            total_tax += tds
        return total_tax

try:
    # Ask the employee details on the terminal
    name = input("Enter employee's name: ")
    income = float(input("Enter employee's income: "))
    position = input("Enter employee's position (Regular/Non-Regular): ").capitalize()
    organization = input("Enter employee's organization: ")
    dividend_income = float(input("Enter employee's dividend income: "))
    num_children = int(input("Enter the number of children: "))
    rental_income = float(input("Enter employee's rental income: "))
    self_education = input("Is the employee engaged in self-education (yes/no): ").strip().lower() == 'yes'

    emp_1 = Employee(name, income, position, organization, dividend_income, num_children, rental_income, self_education)
    
    if emp_1._income < 300000:
        # Inform employee if they're not liable for taxes (income below taxable income as per the rules of tax Act)
        print(f"{emp_1._name}, you are not liable for taxes as your income is below the taxable threshold.")
    else:
        # This code helps to calculate the tax amount for eligible employees (income ≥ 300,000)
        calculator = TaxCalculator(emp_1)
        total_tax = calculator.calculate_total_tax()
        print(f"Total tax amount for {emp_1._name} including TDS on dividend income: Nu. {total_tax:.2f}")
except ValueError:
    # Handle invalid input for income
    print("Please enter a valid numerical value for income.")
except Exception as e:
    # Handle any other exceptions
    print("An error occurred:", str(e))




