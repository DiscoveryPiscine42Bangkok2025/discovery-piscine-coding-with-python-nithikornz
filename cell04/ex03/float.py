user_input = input("Give me a number: ").strip()
num = float(user_input)

if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
