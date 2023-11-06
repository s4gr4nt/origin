#!/usr/bin/env python

wordbank = ["indentation", "spaces"]

tlgstudents = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append('4')

import random

#Try if wordbank works
#print(wordbank)

#num= input("Pick a student number!")

#num= int(input("Pick a student number!"))

##choice = int(input("Pick a student number!"))
##student_name = tlgstudents[choice]

random_students = random.choice(tlgstudents)

#print(student_name)
##print((student_name) + " always uses " + wordbank[2], wordbank[1], "to indent.")

print((random_students) + " always uses " + wordbank[2], wordbank[1], "to indent.")

