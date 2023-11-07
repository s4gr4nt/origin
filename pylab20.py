#!/usr/bin/env python3
"""Alta3 Research | Lists Challenge"""

import random

def main():
    wordbank= ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping', 'Jacob', 'Steph']


    wordbank.append(4) #appends integer '4' to wordbank list
    print(wordbank) #verify changes to wordbank list

    totalstudents = int(len(tlgstudents))
    num = int(input(f"Give me a number between 0 and {totalstudents}: "))

    #student_name = tlgstudents[num]
    student_name = random.choice(tlgstudents)
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()




