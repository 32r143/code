import random
#numOfStreaks = 0
longStreak = 0

for numOfSteaks in range(1,10001):
    flipList = []
    streak = 1
    for experiments in range(100):
        res = random.choice(['H', 'T'])
        flipList.append(res)

#    print(flipList)
    streak = 1
    for i in range(len(flipList)):
        if flipList[i] == flipList[i-1]:
            streak += 1
            if streak >= 6:
                longStreak += 1
        else:
            streak = 1
#    print(streak)
print(longStreak)
print('Chance of Streak: ',((longStreak / 10000)*100))
