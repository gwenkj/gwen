'''
-----Vocab Review-----
1) Git - a system that keeps track of changes in code vs GitHub - an online platform that holds git repositories
2) Terminal - the application/interface used to interact with the computer vs Command Line - the place where text is entered
3) Local - repository that exists solely on your computer vs Remote - repository that can be accessed online
4) Version Control - system that tracks changes in code
5) Staging Area - the place where changes are sent before being committed
6) git add - the command used to add changes to the staging area
7) git commit - the command used to save changes to the local repository
8) git push - the command used to send changes to the remote repository
9) git status - the command used to check the status of a repository
10) git pull - the command used to fetch changes from the remote repository
11) pwd - the command used to display the working directory
12) ls - the command used to list files and directories in the current directory
13) cd - the command used to change the working directory
14) nano - the command used to open a text editor in terminal
15) touch - the command used to create an empty file
16) mv - the command used to move or rename files and directories
17) rm - the command used to remove files and directories
18) cat - the command used to display the contents of a file in terminal

-----Directory Trees-----
1) pwd
2) ls
3) cd .., cd brianna_repo, git pull
4) cp homework.py ../judy_decal/homework
5) cd ../judy_decal/homework
6) cat homework.py
7) git add homework.py, git commit -m "completed homework", git push origin main
8) It means that someone else has commited files, so you do not have the most up to date repository stored locally.
    To fix this, use git pull to get the most up-to-date files and then you can add, commit, and push.
9) ~/Recent
'''

# -----Data Types-----
def checkDataType(value):
    if type(value) == int:
        return "integer"
    elif type(value) == float:
        return "float"
    elif type(value) == str:
        return "string"
    elif type(value) == bool:
        return "boolean"
    else:
        return "other"
print(checkDataType(3.14))  # Output: float
print(checkDataType(True))   # Output: boolean

def evenOrOdd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(evenOrOdd(7))  # Output: odd
print(evenOrOdd(10)) # Output: even

numbers = [1,2,3,4,5]
def sumWithLoop(lst):
    total = 0
    for n in lst:
        total += n
    return total
print(sumWithLoop(numbers))  # Output: 15

def square(num):
    return num ** 2
# error is in the operation used, it should be ** not *
print(square(5))  # Output: 25
