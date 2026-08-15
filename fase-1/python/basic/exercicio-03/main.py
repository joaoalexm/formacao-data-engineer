while True:
    try:
        gross_salary = float(input("Enter your gross salary: "))

        if gross_salary <= 0:
            print("Invalid salary. Salary must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")


if gross_salary <= 2000:
    tax_rate = 0.0
elif gross_salary <= 3000:
    tax_rate = 0.08
elif gross_salary <= 4500:
    tax_rate = 0.18
else:
    tax_rate = 0.28


tax_amount = gross_salary * tax_rate
salary_net = gross_salary - tax_amount

print(f"Gross Salary: ${gross_salary:.2f}")
print(f"Tax Rate: {tax_rate * 100:.0f}%")
print(f"Tax Amount: ${tax_amount:.2f}")
print(f"Net Salary: ${salary_net:.2f}")
