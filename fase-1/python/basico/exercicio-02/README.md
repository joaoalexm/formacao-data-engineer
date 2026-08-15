# Python 02 — Temperature Converter

## Goal

Convert temperatures between Celsius, Fahrenheit, and Kelvin while validating user input and physical temperature limits.

## Input

The program asks the user for:

- a temperature value
- the source scale: Celsius (`C`), Fahrenheit (`F`), or Kelvin (`K`)

Temperature values can contain decimals.

## Validation

The program:

- rejects non-numeric temperature values
- accepts only `C`, `F`, or `K` as scales
- ignores extra spaces and letter case in scale input
- rejects temperatures below absolute zero
- validates whether the user wants to perform another conversion

Physical limits:

```text
Celsius:    >= -273.15
Fahrenheit: >= -459.67
Kelvin:     >= 0
```

## Conversions

The program converts the entered temperature to the other two scales.

Example:

```text
Enter the temperature: 25
Enter scale (C/F/K): C
25.0°C is equal to 77.00°F and 298.15K.
```

## How to run

```bash
python main.py
```

## What I learned

I practiced numeric input with `float()`, conditional logic, loops, input validation with `try`/`except`, string normalization, temperature conversion formulas, and controlling program flow with `break` and `continue`.
