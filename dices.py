'''
dev : felipe g. 
description :
get player name
generate two random number into 2 dices
dice 1: 1-6
dice 2: 1-6
print dices values 
'''
import os 
from random import randint, uniform 

os .system('clear')
print ("::: WELCOME TO MY PARCHIS;;;")

#print("player name: ")
player_name= input("player name: ")
dice1 = randint(1,6)
dice2 = randint(1,6)

print(f"Dice 1: {dice1}")
print(f"Dice 2: {dice2}")

