# Python 03 - Net Salary Calculator

## Goal

Calculate net salary using fictional tax brackets while validating user input.

## Input

The program asks the user for a gross salary.

The salary:

- can contain decimal values
- must be numeric
- must be greater than zero

## Tax brackets

    Up to 2000.00        0%
    Up to 3000.00        8%
    Up to 4500.00       18%
    Above 4500.00       28%

The selected tax rate is applied to the entire gross salary.

## Calculation

    tax amount = gross salary * tax rate
    net salary = gross salary - tax amount

Example:

    Enter your gross salary: 3000
    Gross Salary: $3000.00
    Tax Rate: 8%
    Tax Amount: $240.00
    Net Salary: $2760.00

## How to run

    python main.py

## What I learned

I practiced validating numeric input with try/except, controlling loops with break and continue, using conditional branches to select tax rates, and calculating values from percentages.
