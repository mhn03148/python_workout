def hex_output():
    hex_num = int(input())
    decimal_num = 0

    i=0
    while True:
        decimal_num = decimal_num + (16**i)*(hex_num % 10)
        hex_num = (hex_num) // 10
        print(hex_num)
        i+=1

        if hex_num <= 0:
            break
        else:
            continue
        print(decimal_num)
def hex_output_book():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) +(16 ** power)
    print(decnum)

hex_output()
