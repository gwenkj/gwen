# File: homework1.py

# -----Variables and Data Types-----
a = 10
print(a)
print(type(a))
# a is an integer (whole number)
b = 1.5
print(b)
print(type(b))
# b is a float (decimal number)
c = 3j
print(c)
print(type(c))
# c is a complex number (both real and imaginary parts)
d = "hello"
print(d)
print(type(d))
# d is a string (text)
e = [1, 2, 3]
print(e)
print(type(e))
# e is a list (multiple values in one variable)
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))
# f is a dictionary (holds data in pairs of keys and values)
g = (1, 2)
print(g)
print(type(g))
# g is a tuple (multiple values in a variable and cannot be changed)
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# h is a list (multiple values in a variable and can be changed)
i = True
print(i)
print(type(i))
# i is a boolean (True or False)
j = None
print(j)
print(type(j))
# j is a null value (no value for the variable)
k = [True, "blue", 12]
print(k)
print(type(k))
# k is a list of multiple data types (boolean, string, integer)
l = str(14)
print(l)
print(type(l))
# l is a string (text) made from an integer (whole number)
m = 1e4
print(m)
print(type(m))
# m is a float (decimal number) because it is written in scientific notation
'''
1) 9 types of data 
2) Float, int, complex, str, list, tuple, dict, bool, null
3) b and m (floats); e, h, k (lists); d and l (strings)
4) l is a string because str converts the integer 14 into a string
'''
n = range(4)
print(n)
print(type(n))
# n is a range (a sequence of numbers without writing them all out)



# -----Booleans-----
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True, non-empty string is True
print(bool(123)) # True, non-zero number is True
print(bool(["apple", "cherry", "banana"])) # True, non-empty list is True
print(bool(True)) # True
print(bool(False)) # False
print(bool(0)) # False, zero is False
print(bool("")) # False, empty string is False
print(bool(" ")) # True, non-empty string is True
print(bool(())) # False, empty tuple is False
print(bool([])) # False, empty list is False
print(bool({})) # False, empty dictionary is False
print(bool(True and False)) # False, True AND False is False
print(bool(True and True)) # True, True AND True is True
print(bool(False and False)) # False, False AND False is False
print(bool(True or False)) # True, one is True and that's enough for "or"
print(bool(True or True)) # True, both can be True for "or"
print(bool(False or False)) # False, both can be False for "or"
print(bool(not(False))) # True, opposite of False is True
print(bool(not(True))) # False, opposite of True is False
'''
1) Any non-empty string, non-zero number, or non-empty list is True, whereas empty string, zero, or empty list is False
2) Spaces being considered a non-empty string and thus being True suprised me 
3) print(bool(not(True and False))) True and False is False, and not(False) is True
4) print(bool(False or True and False)) True and False is False, and False or False is always False
'''



# -----Operators-----
# Arithmetic Operators
print(10 + 5) # 15 addition
print(10 - 5) # 5 subtraction
print(2 * 4) # 8 multiplication
print(6 / 3) # 2.0 division
print(5 % 2) # 1 finds remainder
print(3 ** 2) # 9 exponential expressions
print(15 // 2) # 7 division that rounds down to the nearest integer
# Comparison Operators
print(5 == 2) # False, checks equivalency
print(10 != 10) # False, checks if not equal
print(2 < 5) # True, checks if less than
print(12 > 5) # True, checks if greater than
print(5 <= 6) # True, checks if less than or equal to
print(1 >= 10) # False, checks if greater than or equal to
# Assignment Operators
x = 5
x += 5
print(x) # 10, adds to the variable
x -= 4
print(x) # subtracts from the variable
x *= 3
print(x) # multiplies the variable
# Logical Operators
'''
1) and combines conditions, both must be true; True and not(False); False and True
2) or also combines conditions, but at least one must be true; True or False; False or not(True)
3) not reverses the value of the condition; not(True and False); not(False or True)

1) / divides regularly (returns a float), // divides and rounds down to return an integer
2) % finds the remainder of a division, // ignores the remainder and rounds down
3) you would use %; print(14 % 4) = 2
4) assignment operators can change the value of a variable through the operations
'''



# -----Strings-----
my_string = "hello"
print(my_string) # prints: hello
print(my_string[0]) # prints: h
print(my_string[1]) # prints: e
print(my_string[2]) # prints: l
print(my_string[3]) # prints: l
print(my_string[4]) # prints: o
print(my_string[-1]) # prints: o
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo
print(len(my_string)) # prints: 5
print(my_string + "goodbye") # prints: hellogoodbye
print(my_string * 7) # prints: hellohellohellohellohellohellohello
'''
1) Slicing is pulling out a portion of a string; all of the operations with brackets
2) Returned "Hello, my name is Oski" 
3) Returned the same "Hello, my name is Oski" as in #2
4) F strings make it easier to join variables and strings together 
'''
name = "Oski"
print("Hello, my name is", name)
name = "Oski"
print(f"Hello, my name is {name}")



# -----Terminal Commands-----
'''
1) cd - changes directories; move between folders - ex. cd homework1
2) ls - lists all files in the current directory
3) ls -a - lists all files in current directory including hidden files
4) mkdir - makes a new directory
5) cat - prints the contents of a file into the terminal
6) pwd - prints the location of the current directory
7) cd .. - moves up one directory level
8) cd . - stays in the current directory
9) cd ∼ - moves to the home directory
10) cp - copies a file or folder 
11) mv - moves a file or folder to a new location
12) rm - removes a file or folder
13) clear - clears the terminal screen
14) grep - searches for certain text in files

1) head - prints the first 10 lines of a file
echo - prints text to the terminal
history - shows a list of previously entered commands
2) ls does not show hidden files, ls -a does show hidden files
3) hidden files are files that do not show up by default when browsing directories (often system files)
4) -l shows extra details about files, -f forces the command to run without confirmation, -r runs the command on folders and all their contents
'''