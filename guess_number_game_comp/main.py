# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/21 16:11:06 by fomanca           #+#    #+#              #
#    Updated: 2025/11/22 15:46:28 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0;
    while guess != random_number:
        guess = int(input(f"Enter a number beetween 1 and {x}: \n"))
        if guess < random_number:
            print("\nsorry, guess again. Too Low")
        elif guess > random_number:
            print("\nsorry, guess again. Too Hight")
    print(f"\nyay congrats, you guessed the number {random_number} correctly;")



guess(800)
