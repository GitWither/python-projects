import random

simulations = 10000
peopleNum = 23

def checkSameDates(list):
    
    listCopy = list[:]
    for x in range(len(listCopy) - 1):
        if listCopy[x] == listCopy[x + 1]:
            return True
    return False


def generateRandomDates(date_num):
    date = []
    for x in range(date_num):
        date.append(random.randint(1, 31))
    return date

prob = 0
for x in range(simulations):
    date = generateRandomDates(peopleNum)
    if (checkSameDates(date)):
        prob += 1

print(str((prob / simulations) * 100) + "%")