# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fomanca <fomanca@student.42porto.com>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/21 16:14:22 by fomanca           #+#    #+#              #
#    Updated: 2025/11/22 14:10:20 by fomanca          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to exit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print()
print("----- YOUR CART -----")

for food, price in zip(foods, prices):
    print(f"{food}: ${price}")

for price in prices:
    total += price
print()
print(f"Your Total is: ${total:.2f}")
