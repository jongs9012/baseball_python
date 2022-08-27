import random

number = []
count = 0
strike = 0
ball = 0
foul = 0
is_foul = True

while len(number) < 3:
    temp = random.randint(0, 9)
    if temp not in number:
        number.append(temp)

while True:
    if strike >= 3:
        print("YOU WON!")
        break

    print(number)
    strike = 0
    paul = True
    if count >= 10:
        print("GAME OVER")
        break

    try:
        while True:
            choice_number = list(map(int, input().split()))
            if len(choice_number) != len(set(choice_number)):
                print("----------------------")
                print("NUMBERS SHOULD BE DIFFERENT WITH EACH OTHER")
                print("----------------------")
                continue
            else:
                break
    except ValueError:
        print("----------------------")
        print("PLEASE ENTER VALID VALUE.")
        print("EX : 1 3 9")
        print("----------------------")
        continue
        
    print("----------------------")
    for index, value in enumerate(choice_number):
        if value in number:
            if number[index] == choice_number[index]:
                print("RESULT : STRIKE")
                strike += 1
                if ball >= 1:
                    ball -= 1
            else:
                print("RESULT : BALL")
                ball += 1
            paul = False
    if paul:
        print("RESULT : FOUL")
        foul += 1
    count += 1
    print(f"REMAIN COINS : {10 - count}")
    print(f"STRIKE : {strike} / BALL : {ball} / FOUL : {foul}")
    print("----------------------")

