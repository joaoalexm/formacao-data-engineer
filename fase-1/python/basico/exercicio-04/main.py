while True:
    try:
        number = int(input("Digit a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        continue

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("The number is not prime.")
                break
        else:
            print("The number is prime.")
    else:
        print("The number is not prime.")
    while True:
        keep_going = input("Do you want to check another number? (yes/no): ").lower().strip()

        if keep_going in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if keep_going == "no":
        print("Exiting the program.")
        break
