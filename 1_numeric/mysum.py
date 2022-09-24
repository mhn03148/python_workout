def mysum(*numbers):#전개연산자(splat operator)는 함수의 매개변수를 원하는 만큼 받아서 활용할 수 있게 해주는 연산자
    output = 0
    for i in numbers:
        output = output + i
    return output

print(mysum(10,20,30))
#mysum([10,20,30])이런식의 리스트 형태로 자료를 input하면 ([1,2,3],)형태의 튜플이 전달된다. 이때 넘겨주는 방법은
#mysum(*[10,20,30])형태로 호출하면 mysum(10,20,30)의 형태로 각각 매개변수로 들어간다.