from csv import writer


# function take word and return number of the line that word exists
def search_line(word):
    file = open('db.txt', 'r')
    line_number = 0
    for line in file:
        line = (line.replace('\n', '')).split(',')
        line_number += 1
        if word in line:
            file.close()
            return line_number

    return -1


# function take number of line and print the data in this line
def search_index(number_of_line):
    file = open('db.txt', 'r')
    information = []
    counter = 1
    for line in file:
        line = (line.replace('\n', '')).split(',')
        if number_of_line == counter:
            information = line
            file.close()
            return information

        counter = counter + 1
    file.close()
    return information


def addNewEmp(lst):
    emp = open('db.txt', 'a')
    csv_writer = writer(emp)
    csv_writer.writerow(lst)
    emp.close()


# record=[]
# record.extend(['78','kkk', 'rfrf', 'dddd','ddff', 'frfr'])


def remove_employee(lineToSkip):
    with open('db.txt', 'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open('db.txt', 'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)

            currentLine += 1
#
# rem_emp("data.txt", 4)
#
