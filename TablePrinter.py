def printTable(tableList):
    maxLenList = []
    for x in range(len(tableList)):
        maxLen= 0
        for y in range(len(tableList[x])):
            if len(tableList[x][y])> maxLen:
                maxLen = len(tableList[x][y])
                maxStr = tableList[x][y]
        maxLenList.append(maxLen)

    width = len(tableList)
    for i in tableList:
        height = len(i)

    for x in range(height):
        for y in range(width):
            print(tableList[y][x].rjust(maxLenList[y]),end = ' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
