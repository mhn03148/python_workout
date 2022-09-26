def pig_latin():
    word = str(input())
    if word[0] in 'aeiou':
        word = word + 'way'
    else:
        word = word + word[0] + 'ay'
        word = word[1:]
    print(word)

pig_latin()