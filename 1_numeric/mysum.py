def mysum(*numbers):#전개연산자(splat operator)는 함수의 매개변수를 원하는 만큼 받아서 활용할 수 있게 해주는 연산자
    output = 0
    for i in numbers:
        output = output + i
    return output

print(mysum(10,20,30))