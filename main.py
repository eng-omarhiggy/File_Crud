import os
import sys
from authentication import *
from modification import *
from account import *
from validation import *

print("welcom to our system  press 1 to continuo and any key to exit ")
enter_to_system = input()

try:
    if enter_to_system == '1':
        print("please enter your password and email\n")
        # check if user in db or not
        while True:
            email = input("enter your email\n")
            password = input("enter your password\n")
            respons = check_user(email, password)

            # if is exists will exite from while
            if respons:
                break
            else:
                print("wrong data please enter correct data ")

        # welcome message
        print("welcome ===> " + str(respons[1]) + " <======")

        # check if it is admin or not
        if (respons[6] == "admin"):
            record=[]
            admin_choice=input("Enter:\n 1 to add employee or admin \n 2 to delete employee\n 3 to edit employee\n any key to exite\n")

            if admin_choice == '1':
                print("enter the data of employee " )
                id = input("enter id  : ")
                while not number_validate(id):
                    id = input('please enter your id  ')
                name = input("enter name : ")
                while not name_validate(name):
                    name = input('please enter valid name :')
                salary = input("enter salary: ")
                while not number_validate(salary):
                    salary = input('please enter your salary  ')
                role = input("enter type of empolyee admin or user").lower()

                email = input('please enter your email : ')
                while  check_mail(email) == -1:
                    print("this email already exists")
                    email = input("enter a new email : ")
                while not email_validate(email):
                    email = input("enter a valid email : ")
                password = input("enter your password : ")
                while not password_validate(password):
                    password = input('password contain (a-z)(A-Z)(1-9)(@#$%^) :')
                age = input("enter age : ")
                while not age_validate(age):
                    age = input('please enter valid age :')

                while True:
                    role = input("enter new type of empolyee admin or user").lower()
                    if role == 'admin' or role == 'user':
                        break
                    else:
                        role = input("* enter valid type of empolyee")

                print('Employee added Successfully ')
                emp_rec=[id, name, password,email, salary, age, role]
                addNewEmp(emp_rec)

            elif admin_choice =='2':
                del_mail=input("enter employee email to delete it XXXX ")
                while True:
                    if email_validate(del_mail):
                        if check_mail(del_mail) == -1 :
                            print("this employee is not exists in database")
                            break
                        else:
                            index_of_employee=search_line(del_mail)

                            remove_employee(index_of_employee)
                            break
                    else:
                        print("not valid email")

            elif admin_choice == '3':
                while True:
                    n_mail = input("enter email of the user to edit : ")

                    if email_validate(n_mail):
                        if check_mail(n_mail) == -1:
                            print("**this email not in database * please enter write mail\n")

                        else:
                            number_line = search_line(n_mail)
                            emp_data = search_index(number_line)
                            break
                    else:
                        print("***please enter valid email\n  ")

                print(
                    'please enter the number for the edit value \n [1:id, 2: name, 3:passwd, 4:email , 5:salary, 6:age, 7:role]')
                while True:
                    ind = input('please enter the number of the value')
                    if ind.isnumeric():
                        ind = int(ind)
                        if ind > 0 and ind < 8:
                            break
                    else:
                        ind = input('please enter correct value')
                new_value = 0
                # caching the line
                if ind == 1:
                    new_value = input('please enter your id  ')
                    while not number_validate(new_value):
                        new_value = input('***please valid id  ')

                elif ind == 2:
                    new_value = input("enter new  name : ")
                    while not name_validate(new_value):
                        new_value = input('***please enter valid name :')
                elif ind == 3:
                    new_value = input("enter new password : ")
                    while not password_validate(new_value):
                        new_value = input('***password contain (a-z)(A-Z)(1-9)(@#$%^) :')
                elif ind == 4:
                    new_value = input("enter a new email : ")
                    while not email_validate(new_value):
                        new_value = input("enter a valid email : ")
                elif ind == 5:
                    new_value = input("enter new salary: ")
                    while not number_validate(new_value):
                        new_value = input('***enter valid salary  ')
                elif ind == 6:
                    new_value = input("enter new age : ")
                    while not age_validate(new_value):
                        new_value = input('***please enter valid age :')
                elif ind == 7:
                    while True:
                        new_value = input("enter new type of empolyee admin or user").lower()
                        if new_value == 'admin' or new_value == 'user':
                            break
                        else:
                            new_value = input("* enter valid type of empolyee")

                emp_data[ind - 1] = new_value
                remove_employee(number_line)
                addNewEmp(emp_data)


        else:
            print("""press 1 to Calculate your salary data.\npress 2 to Calculate all employees salaries.\npress 3 to Get the age of an employee\npress -1 to restart program\npress any key to exite""")
            employee_choice = input()

            if employee_choice == '1':
                print("your sallary is : " + str(respons[4]))
            elif employee_choice == '2':
                print("all sallaries of employees  is  : " + str(all_sallaries("db.txt")))
            elif employee_choice == '3':
                # such do -- while loop
                while True:

                    mail_ = input("please enter the Email of employee to get age ")
                    # validte the email
                    if email_validate(mail_):
                        # search of which line email existe
                        mail_index = search_line(mail_)
                        # return -1 means not exist
                        if mail_index == '-1':
                            print("this employee not in database")
                            # to end while loop
                            break
                        else:
                            # here we call search indx and pass the number of line to respose with information
                            age_response = search_index(mail_index)
                            print("the age of  " + age_response[1] + " " + age_response[5])
                            break
                    else:
                        # not validate
                        print("enter correct formatt  email ")
            elif employee_choice == '-1':
                # to restart the program
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                exit()


    else:
        print("Good By")
except Exception as ex:
    print(ex)
    print("Oooops !! unexpected error ocured")
finally:
    final = input("press 1 to restart program\npress any key to end program\n")
    if final == '1':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        exit()
