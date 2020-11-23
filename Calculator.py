#importing library
import re
program_run = True
previous = 0
print("Enter the equation or type quit to Exit")
while program_run != False:

    if previous == 0:
        data = input("Enter the Equation : ")
        data = re.sub('[a-zA-Z,:()" "]', '', data)

    else:
        data = input(previous)
        data = re.sub('[a-zA-Z,:()" "]', '', data)
        data = str(previous)+str(data)
    if data == "quit":
        program_run = False

    #Eval function
    previous = eval(data)


