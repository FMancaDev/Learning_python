# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/23 14:31:43 by fomanca           #+#    #+#              #
#    Updated: 2025/11/23 14:51:30 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import choice

name = str(input("\nwhat's your name: "))
print()

print(f"HI, {name} thanks for playing my game")
print("Welcome to my sorting item game")

i1 = str(input("\nFirst item: "))
i2 = str(input("Second item: "))
i3 = str(input("Third item: "))
i4 = str(input("fourth item: "))
i5 = str(input("Fith item: "))

list = [i1, i2, i3, i4, i5]
escolha = choice(list)

print(f"\nO item escolhido foi: {escolha}. ")
