import math
import cmath
import random

# 1. Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 2. Kilometers to Miles
def kilometers_to_miles(km):
    return km * 0.621371

# 3. Solve Quadratic Equation
def solve_quadratic(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = (-b - cmath.sqrt(d)) / (2*a)
    root2 = (-b + cmath.sqrt(d)) / (2*a)
    return root1, root2

# 4. Generate Random Number
def generate_random(start=1, end=100):
    return random.randint(start, end)

# 5. Square Root
def square_root(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return cmath.sqrt(num)  # handles negatives

# 6. Swap Two Variables
def swap(x, y):
    return y, x


# ---------------------------
# Example usage of functions:
# ---------------------------

print("1. Celsius to Fahrenheit:", celsius_to_fahrenheit(37))
print("2. Kilometers to Miles:", kilometers_to_miles(10))
print("3. Solve Quadratic (a=1, b=5, c=6):", solve_quadratic(1, 5, 6))
print("4. Random Number:", generate_random())
print("5. Square Root of 25:", square_root(25))
print("5. Square Root of -9:", square_root(-9))
x, y = swap(5, 10)
print("6. Swap (5,10):", x, y)
