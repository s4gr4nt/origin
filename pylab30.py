#!/usr/bin/env python3

import html
import random

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

category = trivia.get("category")
question = trivia.get("question")
correct = trivia.get("correct_answer")
incorrect = trivia.get("incorrect_answers")
inc1 = incorrect[0]
inc2 = incorrect[1]
inc3 = incorrect[2]

c0 = html.unescape(correct)
inc1 = html.unescape(inc1)
inc2 = html.unescape(inc2)
inc3 = html.unescape(inc3)

#Define pool of answers as a variable
options = [c0, inc1, inc2, inc3]


#Actual question displayed
print(category)
print(question)
for i, option in enumerate(options):
    letterchoice = chr(65 + i) #converting index letter to A, B, C, D...)
    print(f"{letterchoice}. {option}")


ans = (input("Choose an answer (A, B, C, or D): ")).upper()


if ans in [chr(65 + i) for i in range(len(options))]:
    index = ord(ans) - 65 #convert letter to index (0, 1, 2, 3)
    selected = options[index]
    correctans = options[0]
    
    # Check if answer input is correct answer
    if selected == correctans:
        print("Congratulations! You selected the right answer!")
    else:
        print(f"Sorry. The correct answer is {correctans}.")
else:
    print("Invalid choice. Please select a valid option (A, B, C, D). ")

