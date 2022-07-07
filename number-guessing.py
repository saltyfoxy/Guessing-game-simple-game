import random

score = 0

totalScore = 0

numberOfGames = 0

again = None

play = True

gameOver = False

playerNumber = None

#  Functions

def wrongGuess():
    
    global score
    global again
    global gameOver
    
    if score == 100:
        score -= 20
        print(f"Nope. Wrong guess, there is now {score} points to win ")
   
    elif score == 80:
        score -= 40
        print(f"Nope. Wrong guess, there is now {score} points to win ")
   
    elif score == 40:
        score = 0
        gameOver = True
        
    
def rightGuess():
    
    global score
    global again
    global gameOver
    
    if score == 100:
        print(f"Easy, you got it first try. You just won {score} points")
        gameOver = True
        
    else:
        print(f"You won! You just won {score} points")
        gameOver = True
            

# Game

while play : 
    
    print("--------------------------------   GAME START   -------------------------------- \n ")
    
    print(f"Your current total score is : {totalScore}")
    score = 100
    gameOver = False
    print(f"You are playing to win {score} points " )    
       
    while True:
            try:
                difficulty = int(input("Choose the level of difficulty you'd like to play the game. 1 : EASY | 2 : MEDIUM | 3 : HARD : "))
            except ValueError:
                print("Sorry, that is not the expected answer.")
                continue
            if difficulty < 1 or difficulty > 3 :
                print("Answer must be either 1, 2 or 3.")
            else:
                break
    
    number = 0
    easy = random.choice(range(1, 10, 1))
    medium = random.choice(range(1, 100, 1))
    hard = random.choice(range(1, 1000, 1))
    
    if difficulty == 1:
        number = easy
    elif difficulty == 2:
        number = medium
    elif difficulty == 3:
        number = hard
        
    print(f"answser is : {number}")
    
    while gameOver == False:
                  
        while True:
            try:
                if difficulty == 1:
                    playerNumber = int(input("Find the number between 1 and 10 : ")) 
                elif difficulty == 2:
                    playerNumber = int(input("Find the number between 1 and 100 : "))
                elif difficulty == 3:
                    playerNumber = int(input("Find the number between 1 and 1000 : "))
                    
            except ValueError:
                print("Error, try again")
                continue
            
            if difficulty == 1 and (playerNumber < 1 or playerNumber > 10) :
                print("Only numbers between 1 and 10 are accepted. Try that again.")
                continue
            if difficulty == 2 and (playerNumber < 1 or playerNumber > 100):
                print("Only numbers between 1 and 100 are accepted. Try that again.")
                continue
            if difficulty == 3 and (playerNumber < 1 or playerNumber > 1000):
                print("Only numbers between 1 and 1000 are accepted. Try that again.")
                continue
            
            else:
                ("breaking the try except \n")
                break
        
        if playerNumber == number:
            rightGuess()
            totalScore += score
        else:
            wrongGuess()
            
    else:
        numberOfGames += 1
        print(f"Number of finished games : {numberOfGames}. Your total score is {totalScore} .")
        while True:
            try:
                again = str(input("You just won. Want to play again? Write Y or N : "))
            except:
                print("That is not the answer we are waiting for.")
                continue
            else:
                break
        if again == "N":
            play = False    
    
        
    
        
        
    
    
    
        

        
