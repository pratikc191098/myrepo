import numpy as np
variable_1 = 10
variable_2 = 20
variable_3 = 30
mylist = [variable_1,variable_2,variable_3]
print(mylist)
variable_1 = 2
mylist[2]= variable_1
print(mylist)


f= np.genfromtext("reading_text_line.txt",delimitor= ",")
print(f)

f = open("reading_text_line.txt", "w")
f.write(mylist)
f.close()

#open and read the file after the writing
f = open("reading_text_line.txt", "r")
print(f.read())

f.close()

