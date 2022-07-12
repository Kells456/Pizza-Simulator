"""Representing a model of a pizza"""


class Pizza:
    def __init__(self):
        self.topping = []
        self.crust = []

    def add_toppings(self):
        """telling user if want to input any toppings"""
        while True:
            top = input(
                "Please enter toppings for Pizza! \
                \nOnce you are done, please enter 'pizza' \
                to see your pizza with toppings.\
                \nEnter 'quit' to end the program. ")
            self.topping.append(top)
            if top == '':
                print("\nYou didn't put anything!")
            elif top == 'quit':
                break
            elif top == 'pizza':
                self.topping.pop()
                if self.topping:
                    print(f"Here is your pizza with toppings:")
                    for top in self.topping:
                        print(f"\t{top.title()}")
                else:
                    print("You didn't input any toppings!!")
                    continue
            else:
                print(f"\n{top} adding to pizza...")

    def make_crust(self):
        """what kind of crust would the user like?"""
        pass


# pizza = Pizza()

# pizza.add_toppings()
pizza.make_crust()
