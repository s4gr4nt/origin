import html

trivia = {
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

# Function to format and display the question and answers
def display_trivia_question(trivia):
    question = html.unescape(trivia["question"])  # Decode HTML entities
    correct_answer = html.unescape(trivia["correct_answer"])  # Decode HTML entities
    incorrect_answers = [html.unescape(ans) for ans in trivia["incorrect_answers"]]  # Decode HTML entities

    print(f"Category: {trivia['category']}")
    print(f"Question: {question}\n")
    answers = incorrect_answers + [correct_answer]
    answers.sort()  # Shuffle the answers to display them in a random order
    for i, answer in enumerate(answers):
        print(f"{chr(65 + i)}. {answer}")
    return answers.index(correct_answer)

# Function to validate the user's answer
def validate_user_answer(correct_index, user_answer):
    correct_letter = chr(65 + correct_index)
    if user_answer.upper() == correct_letter:
        return True
    return False

# Main script
correct_index = display_trivia_question(trivia)
user_answer = input("\nEnter your answer (A, B, C, or D): ")

if validate_user_answer(correct_index, user_answer):
    print("Correct! You guessed the right answer.")
else:
    print("Sorry, that's incorrect. The correct answer is option", chr(65 + correct_index))


