import re
def email_validate(mail):
    testmail = re.compile(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')
    if testmail.search(mail):
        return True
    else:
        return False
def name_validate(name):
    testname = re.compile(r'^[A-Za-z]+(?:[A-Za-z0-9-_]+){5,15}$')
    if testname.search(name):
        return True
    else:
        return False

def number_validate(name):
    testname = re.compile(r'^[0-9]{1,6}$')
    if testname.search(name):
        return True
    else:
        return False

def age_validate(age):
    testname = re.compile(r'^[0-9]{2}$')
    if testname.search(age):
        return True
    else:
        return False

def password_validate(password):
    testname = re.compile(r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,20})\S$')
    if testname.search(password):
        return True
    else:
        return False

