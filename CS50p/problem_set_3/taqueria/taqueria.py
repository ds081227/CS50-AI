food_list = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        while True:
            user_input = input("Item: ").title()
            if user_input in food_list:
                x = food_list.get(user_input)
                total = total + x
                print(f"Total: ${total:.2f}")
    except EOFError:
        print("")
        break




