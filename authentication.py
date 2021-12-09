def check_user(mail, password):
    file = open('db.txt', 'r')

    for line in file:
            line = (line.replace('\n', '')).split(',')

            if line[2] == password and line[3] == mail:
                information = line
                return information

print(check_user("ibrahim@gmail.com",'12345'))
#     return False
#
#
#
# def check_mail(mail):
#     file = open('db.txt', 'r')
#     content = file.read()
#     flag = content.find(mail)
#     file.close()
#     return flag


