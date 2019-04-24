import xlwt
import re

#new workplace/new sheet
new_workbook = xlwt.Workbook()
new_sheet = new_workbook.add_sheet('社区矫正')

filename ='./text'

result = []
questions = []

# open txt file and read
with open(filename,'r',) as f:


    for line in f.readline():

        questions.append(line)

    print(questions)
#direct print result is a list, each of the result is a str

    num = len(questions)
    print(num)

#stick str together
    i = 0
    add = ''.join(questions)
    print(add)

#split str depand on english','
    add = str(add)
    result = add.split(',')
    print('result:', result[0])


    num2 = len(result)
    print(num2)

#save data to sheet
    for i in range(num2):
        new_sheet.write(i, 0, result[i])


    new_workbook.save(r"question.xls")

f.close()
