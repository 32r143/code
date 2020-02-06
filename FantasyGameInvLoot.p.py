def addToInventory(inventory,addedItems):
#    for k,v in inventory.items():
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] = inventory[i]+1
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)

 
#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(v,k)
        item_total += v
    print('Total number of items: ' + str(item_total))
    
#displayInventory(stuff)
displayInventory(inv)
print(inv)
