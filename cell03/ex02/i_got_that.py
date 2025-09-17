while True:
    user_input = input("What you gotta say? : ").strip()
    if user_input == "STOP":
        break
    else:
        while True:
            user_input = input("I got that! Anything else? : ").strip()
            if user_input == "STOP":
                exit(0)
