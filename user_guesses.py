import random
answer=0
num=random.randint(1,100)
new=num+0.5
print(new)

def run_game():
    for i in range (0,10):
        guess=int(input("alright, what's your guess!"))
        if guess>num:
            print("Lower it!")
        elif num>guess:
            print("Higher it!")
        elif guess==num:
            print(f"Umm no {num} wasn't my number! It was.. erm.. {new}. You lose, hmph.")
            print(guesses)
            exit()
        else:
            print("Bruh add valid responses from next time on.")
            run_game()
    
print("enter with y for yes and n for no for all the following questions.")
play=input("I'll choose an integer between 1 and 100 and you try to guess it within 10 attempts or less! Kapische?")
if play=='y':
    run_game()
elif play=='n':
    print("pwetty pwease, play wiv me.")
else:
    print("Bruh add valid responses from next time on.")
    

    