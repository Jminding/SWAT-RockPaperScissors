import random

options = ["rock", "paper", "scissors"]

while True:
  user_input = input("Rock, Paper, or Scissors: ")
  user_input = user_input.lower()
  
  if user_input not in options:
    print("Please pick a valid option.")
    continue
  
  cpu_choice = random.choice(options)
  
  print("Computer picked: " + cpu_choice + ".")
  
  if user_input == cpu_choice:
    continue
  elif user_input == "rock" and cpu_choice == "paper":
    print("Computer wins!")
    break
  elif user_input == "rock" and cpu_choice == "scissors":
    print("Player wins!")
    break
  elif user_input == "paper" and cpu_choice == "scissors":
    print("Computer wins!")
    break
  elif user_input == "paper" and cpu_choice == "rock":
    print("Player wins!")
    break
  elif user_input == "scissors" and cpu_choice == "rock":
    print("Computer wins!")
    break
  elif user_input == "scissors" and cpu_choice == "paper":
    print("Player wins!")
    break
  
  
