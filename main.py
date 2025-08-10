# display art
from threading import active_count

from art import logo,vs
from game_data import data
import random

def format_name(account):
    """"#format  the account data into printable format"""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_descr},from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
   if a_followers > b_followers:
    return user_guess =="a"
   else:
    return user_guess =="b"

print(logo)
score=0
game_should_continue=True
account_b=random.choice(data)
while game_should_continue:
    # generate a random account from game data
    # account_a = random.choice(data)
    # account_b = random.choice(data)
    account_a=account_b
    account_b=random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"COMPARE A :{format_name(account_a)}.")
    print(vs)
    print(f"AGAINST B :{format_name(account_b)}")
    
    # ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B' :  ").lower()
    # clear the screen
    print("\n " * 20)
    print(logo)
    account_followers_a = account_a["follower_count"]
    account_followers_b = account_b["follower_count"]
    is_correct = check_answer(guess, account_followers_a, account_followers_b)
    # check if user is correct
    ##get followers count of each account
    ##use if statement to check if user is correct.
    
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! ,Current score{score}")
    else:
        print(f"Sorry that is wrong,Final score {score}")
        game_should_continue =False
    # score keeping


    # make game repeatable


    # making account at position B become the next account at position A.
