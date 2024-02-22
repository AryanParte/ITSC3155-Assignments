class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if it cannot be made due to lack of resources."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] < amount:
                return False
        return True

    def make_sandwich(self, size, ingredients):
        """Decreases the ingredients from machine resources after making sandwich."""
        for ingredient, amount in ingredients.items():
            self.machine_resources[ingredient] -= amount
