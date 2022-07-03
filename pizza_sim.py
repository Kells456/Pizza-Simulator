prompt = "\nHello and Welcome to Pizza Simulator!"
prompt += "\nPlease, enter toppings for the Pizza."
prompt += "\nOnce you are done, please enter 'pizza' to see your pizza with toppings!"
prompt += "\nEnter 'quit' to end the program. "

prompt_2 = "\nIf you want to see your drinks just type 'drinks'"
prompt_2 += "\nDo you want drinks? Yes or no answer. "
prompt_3 = "\nWhat do you want to drink? "
prompt_3_5 = "\nWhat else do you want to drink? "
prompt_3_6 = "\nDo you still want to drink? "

prompt_4 = "\nSending you back to making pizzas! "

toppings = []
drinks = []

flag = True
while True:
    pizza = input(prompt)
    toppings.append(pizza)
    if pizza == '':
        print("\nYou didn't put anything!")
    elif pizza == 'quit':
        break
    elif pizza == 'pizza':
        toppings.pop()
        if toppings:
            print(f"Here is your pizza with toppings:")
            for pizza in toppings:
                print(f"\t{pizza.title()}")
        else:
            print("You didn't input any toppings!!")
            continue

        while flag:
            # do you want drinks question
            question = input(prompt_2)

            if question == 'no':
                # summary of user's order
                print("\nHere is your order:")
                print(f"\tThis is your toppings: ")
                for pizza in toppings:
                    print(f"\t{pizza.title()}.")

                print(f"\tThis is your drinks: ")
                for drink in drinks:
                    print(f"\t{drink.title()}.")
                sec_question = prompt_4
                print(sec_question)
                break
            elif question == 'yes':
                drink = input(prompt_3)
                drinks.append(drink)
                print(f'\n{drink}s are being added to your order...')
                # if the user still wants a drink.
                still_drink_question = input(prompt_3_6)
                if still_drink_question == 'yes':
                    drink = input(prompt_3)
                    drinks.append(drink)
                    print(f'\n{drink}s are being added to your order...')
                elif still_drink_question == 'no':
                    print("\nHere is your order: ")
                    # summary of the user's order
                    print(f"\tThis is your toppings: ")
                    for pizza in toppings:
                        print(f"\t{pizza.title()}.")
                    print(f"\tThis is your drinks: ")
                    for drink in drinks:
                        print(f"\t{drink.title()}.")
                    sec_question = prompt_4
                    print(sec_question)
                    break

                # if the user writes drinks it shows what they got.
            elif question == 'drinks':
                if drinks:
                    print(f"\nHere are your drinks:")
                    for drink in drinks:
                        print(f"\t{drink.title()}")
                else:
                    print("You didn't input any drinks!!!")
    else:
        print(f"\n{pizza} adding to pizza...")
