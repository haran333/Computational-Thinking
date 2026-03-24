yut = {
    "1": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "0": "E"
}

result = [input("").split(), input("").split(), input("").split()]

for i in range(0,3):
    counter = result[i].count("0")
    print(yut[str(counter)])