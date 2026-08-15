while True:
    while True:
        try:
            temp = float(input("Enter the temperature: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        scale = input("Enter scale (C/F/K):").upper().strip()

        if scale in ["C", "F", "K"]:
            break
        else:
            print("Invalid scale. Please enter C, F, or K.")

    if scale == "C":
        if temp < -273.15:
            print("Invalid temperature.")
            continue
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
    elif scale == "F":
        if temp < -459.67:
            print("Invalid temperature.")
            continue
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temp}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K.")
    elif scale == "K":
        if temp < 0:
            print("Invalid temperature.")
            continue
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temp}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F.")

    while True:
        keep_going = input("Do you want to convert another temperature? (yes/no): ").lower().strip()
        if keep_going in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if keep_going == "no":
        print("Exiting the program.")
        break
