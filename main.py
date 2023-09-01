from art import logo
from art import vs
from game_data import data
from random import randint
import os

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

loop_keep_going = True
user_current_score = 0
previous_answer = False

while loop_keep_going:
  clear_console()
  print(logo)
  first_celebrity = randint(0, len(data) - 1)
  second_celebrity = randint(0, len(data) - 1)
  if first_celebrity == second_celebrity:
    while second_celebrity == first_celebrity:
      second_celebrity = randint(0, len(data) - 1)
  first_celebrity_name = (data[first_celebrity])['name']
  second_celebrity_name = (data[second_celebrity])['name']
  first_celebrity_description = (data[first_celebrity])['description']
  second_celebrity_description = (data[second_celebrity])['description']
  first_celebrity_country = (data[first_celebrity])['country']
  second_celebrity_country = (data[second_celebrity])['country']
  first_celebrity_followers = (data[first_celebrity])['follower_count']
  second_celebrity_followers = (data[second_celebrity])['follower_count']
  if previous_answer:
    print(f"You're right! Current score: {user_current_score}")
  print(f"Compare A: {first_celebrity_name}, a {first_celebrity_description}, from {first_celebrity_country}.")
  print(vs)
  print(f"Against B: {second_celebrity_name}, a {second_celebrity_description}, from {second_celebrity_country}.")
  if first_celebrity_followers > second_celebrity_followers:
    more_followers = 'A'
  elif first_celebrity_followers < second_celebrity_followers:
    more_followers = 'B'
  user_guess = (input("Who has more followers? Type 'A' or 'B': ")).upper()
  if user_guess == more_followers:
    loop_keep_going = True
    user_current_score += 1
    previous_answer = True
  else:
    break

clear_console()
print(logo)
print(f"Sorry, that's wrong. Final score: {user_current_score}")
    
  
  
  
  

#Loop that is going to keep on going until the user guesses wrong (while loop)
#Display the logo at the start of each loop, clear the console at the beginning of each iteration and re-display the logo
#Creating a variable that is going to end the loop once the guess of the user is wrong
#Variable initialized to 0 that is keep track of the number of right guess the user has
#Generating two random numbers that will select two celebrity in the data list
#Displaying the name of the celebrity, their description, and where they are from
#Fetching their respective number of followers and comparing them, and store the winner in a variable named more followers that is going to store either 'A' or 'B'
#Prompt the user to enter its guess (either 'A' or 'B') and change the value of the initial condition of the loop depending on if the user entered the right guess or not
#If the user guesses right you restart the loop, if the user guesses wrong the loop will not restart because the condition would have change, you will clear the console, display the final score and end the program

