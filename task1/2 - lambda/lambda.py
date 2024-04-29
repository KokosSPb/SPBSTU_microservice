def filter(func, arStr):
    arAns = []
    for iL in arStr:
        if(func(iL)):
            arAns.append(iL)

    return arAns

data = [
    "Do geese see God?",
    "rotator",
    "text", # длина меньше 5 и не Палиндром :-)
    "a Toyota's a Toyota",
    "refer", # Длина 5 и Палиндром
    "Madam, I'm Adam"
]

print(filter(lambda str : ' ' not in str, data))
print(filter(lambda str : str[0] != 'a', data))
print(filter(lambda str : len(str) >= 5, data))