secret = 30
i=1
while i<6:
    answer = int(input("enter your guess:"))
    i= i+1

    if answer == secret:
        print("Correct congrats") 
    else:
        print("sorry wrong answer")