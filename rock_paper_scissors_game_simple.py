import random

# List of items
items = ['rock', 'paper', 'scissors']

# Function for computer choice
def computer_choice():
    return random.choice(items)

# Function for user choice
def user_choice():
    user_input = input("Enter your choice (rock/paper/scissors): ")
    while user_input not in items:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock/paper/scissors): ")
    return user_input

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main game logic
user_name = input("Enter your name: ")
    
user = user_choice()
comp = computer_choice()
    
print(f"Computer chose: {comp}")
result = determine_winner(user, comp)
print(result)
