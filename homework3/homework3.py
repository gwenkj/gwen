import math

# -----Print Functions-----

def say_goodbye (name):
    print(f"Goodbye, {name}!")
say_goodbye("Gwen")

def circle_area(radius):
    print(3.14 * radius ** 2)
circle_area(3)



# -----Return Functions-----

def subtract(a, b):
    return a - b
print(subtract(7, 3))

def multiply(a, b):
    return a * b
print(multiply(4, 5))

def divide(a, b):
    return a / b
print(divide(10, 2))



# -----Conditionals-----

temperatures = [67, 59, 81, 73, 56]
def what_should_I_wear(temperatures):
    return (min(temperatures), max(temperatures))
print(what_should_I_wear(temperatures))

def day_of_week(day_number):
    if day_number == 6 or day_number == 7:
        return "Weekend!!!"
    else:
        return "Weekday :("  
print(day_of_week(6))

def fuel_efficiency(miles, gallons):
    return miles / gallons
print(fuel_efficiency(300, 10))

def encrypt(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining = n // 10
        num_digits = int(math.log10(remaining)) + 1
        return last_digit * (10 ** num_digits) + remaining
print(encrypt(2731))



# -----Loops-----

def power(base, exponent):
    if exponent == 0:
        return 1
    result = base
    for i in range(1,exponent):
        result *= base
    return result
print(power(3, 4))

numbers = [5, 2, 8, 1, 9]
def minimum(numbers):
    minimum = numbers[0]
    for n in numbers:
        if n < minimum:
            minimum = n
    return minimum
print(minimum(numbers))

def maximum(numbers):
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum
print(maximum(numbers))

def minimum2(numbers):
    minimum = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] < minimum:
            minimum = numbers[i]
        i += 1
    return minimum
print(minimum2(numbers))

def maximum2(numbers):
    maximum = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > maximum:
            maximum = numbers[i]
        i += 1
    return maximum
print(maximum2(numbers))

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(sum_digits(15281))

n = 62937
result = sum_digits(n) # Calculate the sum of digits of n (6+2+9+3+7)
print(f"The result of calculating the sum of digits (6.3) of {n} is {result}")