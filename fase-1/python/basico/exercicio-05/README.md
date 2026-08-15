# Python 05 - Time Converter

## Goal

Convert a total number of seconds into days, hours, minutes, and remaining seconds.

## Input

The program asks the user for a total number of seconds.

The input:

- must be an integer
- cannot be negative
- can be zero

## Conversion

The program uses integer division and the remainder operator to calculate each time unit.

    1 day = 86400 seconds
    1 hour = 3600 seconds
    1 minute = 60 seconds

Example:

    Enter total seconds: 90061
    1 days, 1 hours, 1 minutes, 1 seconds

## How to run

    python main.py

## What I learned

I practiced integer division with //, calculating remainders with %, validating integer input with try/except, and breaking a total value into smaller time units.
