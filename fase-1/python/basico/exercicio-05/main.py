

while True:
    try:
        sec = int(input("Enter total seconds: "))
        if sec < 0:
            print("Please enter a non-negative integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#1 day = 86400 seconds
#1 hour = 3600 seconds
#1 minute = 60 seconds


days = sec // 86400
remaining_seconds = sec % 86400
hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60


print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
