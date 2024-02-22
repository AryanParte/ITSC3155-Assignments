class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        quarters = int(input("Enter number of quarters: "))
        dimes = int(input("Enter number of dimes: "))
        nickels = int(input("Enter number of nickels: "))
        pennies = int(input("Enter number of pennies: "))
        return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            return True
        return False