import random

def play_game():
    lucky_num = random.randint(1, 50)
    
    while True:
        user_num = int(input("Guess the lucky num : "))
        
        if user_num == lucky_num:
            print("You won. Game over!!")
            print("Thank you for playing")
            break
        elif user_num <lucky_num:
            print("Too Low")

        else:
            print("Too High")


play_game()