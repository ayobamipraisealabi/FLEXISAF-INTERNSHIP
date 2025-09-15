#To establish the basic rule of the code i.e. "rock" beats "scissors" etc, by creating a function
import random
def weapon_hierarchy(weapon_computer, weapon_user):

    #Tie
    if weapon_computer == weapon_user:
        print("There is a tie.\nTry again.")
        weapon_user= input("Select your weapon: ").title()
    
    #"Rock" beats "Scissors"
    if weapon_user == "Rock" and weapon_computer == "Scissors":
        print("You win, The Computer's choice was too weak for you")
    elif weapon_computer == "Rock" and weapon_user == "Scissors":
        print("You lose, The Computer's choice was too strong for you")

    #"Paper" beats "Rock"
    if weapon_user == "Paper" and weapon_computer == "Rock":
        print("You win, The Computer's choice was wrapped up")
    elif weapon_computer == "Paper" and weapon_user == "Rock":
        print("You lose, The Computer's choice covered you up")

    #"Scissors" beats "Paper"
    if weapon_user == "Scissors" and weapon_computer == "Paper":
        print("You win, The Computer's choice was too soft for you")
    elif weapon_computer == "Scissors" and weapon_user == "Paper":
        print("You lose, The Computer's choice was too sharp for you")


#For user input of name and basic information about the game.
name= input("Enter your name: ")
print("Welcome to the RPS World Series,", name )
print("You will be battling against the Computer.\n")

#For user to select "weapon of choice" i.e. "rock", "paper" or "scissors".
#To prevent random choices and errors
print("Rock, Paper or Scissors")
weapon_user= input("Select your weapon: ").title()
while weapon_user not in (["Rock", "Paper", "Scissors"]):
    print("Invalid choice, Please select between Rock, Paper or Scissors")
    weapon_user= input("Select your weapon: ").title()


#For random selection of weapon by computer
weapon_computer= random.choice(["Rock", "Paper", "Scissors"])
print("The Computer has chosen:", weapon_computer)

#To determine who wins the battle and output result
winner = weapon_hierarchy(weapon_computer, weapon_user)
print(winner)


