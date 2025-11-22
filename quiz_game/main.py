# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/22 21:16:52 by fomanca           #+#    #+#              #
#    Updated: 2025/11/22 22:38:00 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

questions = ("How many days are in a normal year?: \n",
          "What's the best language to learn in cybersecurity?: \n",
          "What's the language with most offers?: \n",
          "What is RAM used for?: \n",
          "What is a SIGEV error?: \n")

options = (("A. 341", "B. 127", "C. 365", "D. 357"),
        ("A. C++", "B. Python", "C. Java", "D. Rust"),
        ("A. JavaScript", "B. C#", "C. Rust", "D. PHP"),
        ("A. To store data temporarily for quick access", "B. To store files permanently like a hard drive", "C. To connect a computer to the internet", "D. To display images on the monitor"),
        ("A. A memory access error", "B. A network issue", "C. A battery problem", "D. A graphics glitch"))

answers = ("C", "B", "A", "A", "A")
guesses = []
score = 0
question_num = 0
name = input("\nWhat's your name: ")

print(f"\n\nHi!, {name}, thanks for playing my game!!!")
print("Welcome to my Guessing Game.")

for question in questions:
    print("\n------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("\nEnter a (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("\nCORRECT!")
    else:
        print("\nINCORRECT!")
        print(f"\n({answers[question_num]}) is the correct answer")

    question_num += 1
