import random

def guessing_game():
    number = random.randint(10,30) #10~30(30포함) 범위의 정수 생성

    while True:
        i = int(input()) #input 함수는 항상 문자열을 리턴, int형으로 받아야 비교 가능
        if number > i:
            print("Too low")
        elif number < i:
            print("Too high")
        elif i == number:
            print("just right")
            break

guessing_game()