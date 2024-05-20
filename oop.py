import math

# Constants
MIN_TAXABLE_INCOME = 300_000
NPPF_DEDUCTIBLE_RATE = 12  # percent
GIS_DEDUCTIBLE_RATE = 3  # percent
CHILDREN_DEDUCTIBLE_RATE = 50_000  # per child
SURCHARGE_THRESHOLD = 1_000_000
SURCHARGE_RATE = 10  # percent

# Classes
class Employee:
    def __init__(self, salary, is_contract, organization_type):
        self.salary = salary
        self.is_contract = is_contract
        self.organization_type = organization_type

class TaxCalculator:
    def __init__(self, employee):
        self.employee = employee
        self.gross_salary = employee.salary
        self.nppf_deductible = self.gross_salary * (NPPF_DEDUCTIBLE_RATE / 100) if not employee.is_contract else 0
        self.gis_deductible = self.gross_salary * (GIS_DEDUCTIBLE_RATE / 100)
        self.children_deductible = CHILDREN_DEDUCTIBLE_RATE * len(employee.children) if hasattr(employee, 'children') else 0

    def calculate_tax(self, children=None):
        if children:
            self.children_deductible = CHILDREN_DEDUCTIBLE_RATE * len(children)
        taxable_income = self.gross_salary - self.nppf_deductible - self.gis_deductible - self.children_deductible
        tax = 0
        surcharge = 0

        if taxable_income > 0:
            tax_slabs = [(0, 300_000, 0), (300_001, 400_000, 0.1), (400_001, 650_000, 0.15),
                         (650_001, 1_000_000, 0.2), (1_000_001, 1_500_000, 0.25), (1_500_001, math.inf, 0.3)]

            for lower_limit, upper_limit, rate in tax_slabs:
                if taxable_income > lower_limit:
                    tax += max(0, taxable_income - lower_limit) * rate

            if taxable_income >= SURCHARGE_THRESHOLD:
                surcharge = tax * (SURCHARGE_RATE / 100)

        return tax + surcharge


# Example usage
employee = Employee(salary=500_000, is_contract=False, organization_type="Government")
tax_calculator = TaxCalculator(employee)
tax = tax_calculator.calculate_tax()
print(f"The calculated tax for the employee is: {tax}")