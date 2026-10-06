fav_foods = ["sushi", "hummus", "acai bowls", "pomegranates", "salad"]

print(fav_foods[1])
print(fav_foods[-1])
fav_foods.append("pho")
fav_foods.insert(0, "apple")
fav_foods.remove("apple")
print(len(fav_foods))

for food in fav_foods:
    print(food.upper())

first_and_last = [fav_foods[0], fav_foods[-1]]

def list_potato(food):
    found = False
    for food in fav_foods:
        if food == "potato":
            found = True      
    if found == True:
        print("A potato!")
    if not found:
        print("No potato!")

list_potato("fav_foods")
'''
I printed if every single item in the list is a potato 
I instead defined a variable 'found' to be true or false and printed at the end
'''

numbers = list(range(0, 21))
'''
I accidentally made the range into the variable, not a list
I added list to the variable definition
'''

def get_first_15(numbers):
    return numbers[:15]
print(get_first_15(numbers))

def get_every_5(numbers):
    return numbers[::5]
print(get_every_5(numbers))

def reverse_and_stride(numbers):
    return get_every_5(numbers[::-3])
print(reverse_and_stride(numbers))

'''
NameError: name 'every_5_reversed' is not defined
I changed the function call to the input list (idk why I named an output list)
'''

print(reverse_and_stride(get_every_5(get_first_15(numbers))))

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2])
'''
SyntaxError: invalid syntax. Perhaps you forgot a comma?
I removed the brackets that signify which column to print
'''

print(numbers[2][1])
numbers.append([10, 11, 12])

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for n in row:
            total += n
    return total
print(sum_nested(numbers))


def make_nested_list():
    nested_25 = []
    num = 1
    for i in range(5) :
        row = []
        for j in range(5) :
            row.append(num)
            num += 1
        nested_25.append(row)
    return nested_25

def replace_multiples_3(nested_25):
    for i in range(len(nested_25)):
        for j in range(len(nested_25[i])):
            if nested_25[i][j] % 3 == 0:
                nested_25[i][j] = "?"
    return nested_25

def add_numbers(nested_25):
    total = 0
    for row in nested_25:
        for num in row:
            if num != "?":
                total += num
    return total

ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
print(ages)
ages.pop("Mariam")

for name, age in ages.items():
    print(f"{name}: {age}")

print(add_numbers(replace_multiples_3(make_nested_list()))) # total = 217