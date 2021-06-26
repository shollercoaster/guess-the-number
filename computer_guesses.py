import random
answer=0
print("enter with y for yes and n for no for all the following questions.")
play=input("Choose an integer between 1 and 100 and I'll try to guess it! y or n?")
if play=="y":
    while answer!='y':
        guess=random.randint(1,100) 
        answer=input(f"alright, is your number {guess}?")
        if answer=='y':
            print("told you, you couldn't beat me.")
elif play=='n':
    print("oh c'mon, are you scared to lose?")
else:
    print("invalid input, champ.")
    