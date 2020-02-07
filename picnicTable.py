def printPicnic(itemsDict, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth,'-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftwidth,'.') + str(v).rjust(rightwidth))
picnicitems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':3000}
printPicnic(picnicitems,12,5)
printPicnic(picnicitems,20,6)
