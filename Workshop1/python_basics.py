"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64


def part1():
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    guess = input('Please enter a number:')
    if guess % 2 == 0:
        print("even")
    else:
        print("odd")
    return guess
    

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    randomNum = random.randint(1,9)
    guess = input('Please guess a number:')
    while (guess != randomNum) and (guess != "exist"):
        if randomNum > guess:
            print('too low')
        elif randomNum < guess:
            print('too high')
        guess = input('Please guess another number!:')


def part3():
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    Input = raw_input('please enter a string:')
    for i in range(len(Input)):
        if Input[i] != Input[len(Input)-i-1]:
            print('It is not a palidrome')
            break
        else:
            i = i + 1
    

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f= open(filename,"w+")
    encodedUsername = base64.b64encode(username)
    encodePassword = base64.b64encode(password)
    f.write(encodedUsername+'\n')
    f.write(encodePassword)
    f.close()

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f= open(filename,"r")
    contents = f.readlines()
    for i in contents:
        decodedVersion = base64.b64decode(i)
        print(decodedVersion)


if __name__ == "__main__":
    
    part3()  # False
    part3()  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
    part1()  # odd!
    part1()  # even!
    part2()
