"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. 
A strong password is defined as one that is at least eight characters long, \
    contains both uppercase and lowercase characters,\
    and has at least one digit.\
    You may need to test the string against multiple regex patterns to validate its strength.
"""
import re

def check_password(password: str):
    password.strip()
    if len(password) > 8:
        pattern = re.compile(r'''
                            (\w{8, })
                            [A-Z]+
                            [a-z]+
                            [1-9]+''',re.VERBOSE)
        result = pattern.findall(password)
        print(result)

check_password("mdsd36du6f")


def isStrong(password:str):
    length = re.compile(r'(\w{8,})')
    upper_letter = re.compile(r'[A-Z]+')
    lower_letter =re.compile(r'[a-z]+')
    digit_ = re.compile(r'[1-9]+')
    if length.findall(password) == []:
        print("Password must contain 8 character")
    elif upper_letter.findall(password) == []:
        print("Password must contain atleast one Uppercase(A-Z) letter")
    elif lower_letter.findall(password) == []:
        print("Password must contain atleast one lowercase(a-z) letter")
    elif digit_.findall(password) == []:
        print("Password must contain atleast one digit(1-9) letter")
    else:
        print('Your password was strong')
        return True


while False:
    password_rule = """
    Password must contain 8 character length
    Password must contain atleast one Uppercase(A-z) letter
    Password must contain atleast one digit(1-9) letter
    Password must contain atleast one lowercase(a-z) letter
    """
    print(password_rule)
    Password = input("Enter your password hear-->").strip()
    if isStrong(Password):
        break