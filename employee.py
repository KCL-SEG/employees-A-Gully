"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, salary=0, commission=0, desc=""):
        self.name = name
        self.salary = salary
        self.commission = commission
        self.desc = desc

    def create_contract_salary(self, monthlyRate):
        self.salary = monthlyRate
        return

    def create_hourly_salary(self, rate, hours):
        self.salary = rate * hours
        return

    def create_bonus_commission(self, bonus):
        self.commission = bonus
        return

    def create_contract_commission(self, contracts, perContract):
        self.commission = contracts * perContract
        return

    def create_desc(self, desc):
        self.desc = desc
        return

    def get_pay(self):
        return self.salary + self.commission

    def __str__(self):
        return self.desc


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.create_contract_salary(4000)
billie.create_desc(
    "Billie works on a monthly salary of 4000.  Their total pay is 4000.")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.create_hourly_salary(100, 25)
charlie.create_desc(
    "Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.")

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.create_contract_salary(3000)
renee.create_contract_commission(4, 200)
renee.create_desc(
    "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.")

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.create_hourly_salary(150, 25)
jan.create_contract_commission(3, 220)
jan.create_desc(
    "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.create_contract_salary(2000)
robbie.create_bonus_commission(1500)
robbie.create_desc(
    "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.create_hourly_salary(120, 30)
ariel.create_bonus_commission(600)
ariel.create_desc(
    "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.")
