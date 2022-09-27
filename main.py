#import the art
from art import logo, vs


#Import random and the game_data 
from game_data import data
import random 
from replit import clear

def format_data(account):
  """format the account data into printable format"""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f" {account_name}, a {account_description}, from {account_country} "

def check_guess(guess, follower_count_A, follow_count_B):
  """Takes the user count and follower count to see if the user is correct"""
  if follower_count_A > follower_count_B:
    return guess == "a"
  else:
    return guess == "b"
      
print(logo)
score = 0 
game_should_continue = True
account_A = random.choice(data)
account_B = random.choice(data)

#make the game repeatable
while game_should_continue:
  #genreate a random account from data 

  #making the account at postion B move to position A
  account_A =  account_B
  account_B =  random.choice(data)
  
  while account_A == account_B:
    account_B = random.choice(data)
  
  print(f"Compare A:{format_data(account_A)}")
  print(vs)
  print(f"Compare B:{format_data(account_B)}")
  
  #ask the user for a guess
  guess = input("Who has more followers? Type 'A' or Type 'B': ").lower()
  
  #check to see if the user is correct
  ## get the follower data 
  follower_count_A = account_A["follower_count"]
  follower_count_B = account_B["follower_count"]
  is_correct =  check_guess(guess, follower_count_A, follower_count_B)

  #clear the screen  between rounds 
  clear()
  
  # give the user feedback
  #keep scoring 
  if is_correct:
    score += 1 
    print(f"You're Right! Current Score: {score}. ")
  else:
    game_should_continue = False 
    print(f"Sorry that Wrong! Final Score: {score}. ")






