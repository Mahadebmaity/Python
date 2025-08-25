import random
def Guess_Game():
    options = ["Rock", "Paper", "Scissors"]

    for i in range(3):
        """ Now You have play 3 times only """
        user_input = input("Choose any one: Rock, Paper, or Scissors: ").capitalize().strip()
        computer_choice = random.choice(options)   

        print(f"Computer choice: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        # elif (user_input == "Rock" and computer_choice == "Scissors") or (user_input =="Scissors" and computer_choice == "Paper") or (user_input  == "Paper" and computer_choice =="Rock"):  
        #      print("You Won The Game!")
            
        # elif (user_input == "Rock" and computer_choice == "Scissors") or \
        #      (user_input =="Scissors" and computer_choice == "Paper") or \
        #      (user_input  == "Paper" and computer_choice =="Rock"):  
        #     print("You Won The Game!")

        elif (
            (user_input == "Rock" and computer_choice == "Scissors") or 
            (user_input == "Scissors" and computer_choice == "Paper") or 
            (user_input == "Paper" and computer_choice == "Rock")):  
            print("You Won The Game!")
        else:
            print("You Lost The Game!")
        
def call_Game():
    """ Welcome to Our Plateform 
        Rock , Paper , Scissors 
        if you are new in this game you should know this:
        Rock beat Scissors beat Paper beat Rock 
    """
    agree_to_play = input("Are you interested??(If yes write 'y'):: ").capitalize().strip()
    if agree_to_play == "Y":
        Guess_Game()
    print("Thank you for visiting our game!")

print(call_Game.__doc__)
call_Game()
