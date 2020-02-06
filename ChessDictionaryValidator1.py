rows = ['1','2','3','4','5','6','7','8']
columns = ['a','b','c','d','e','f','g','h']
color = ['w','b']
pieces= ['king','queen','bishop','rook','knight','pawn']
cells= []
coloredPieces = []
chessValids = []
chessPieces = {}
for single1 in rows:
    for each1 in columns:
        cell = single1 + each1
        cells.append(cell)
#print(cells)
print()
for single2 in color:
    for each2 in pieces:
        coloredPiece = single2 + each2
        coloredPieces.append(coloredPiece)
#print(coloredPieces)
print()
for single3 in cells:
    for each3 in coloredPieces:
        chessValid = {}
        chessValid[single3] = each3
        chessValids.append(chessValid)
#print(chessValids)
#print(type(chessValids))
#print(type(chessValids[1]))
#print(chessValids[1])

print('Enter a cell in which the piece is to be moved')
moveofcell = input()
print('Enter the piece to be moved')
moveofpiece = input()
def isValidChessBoard():
    for i in range(len(chessValids)):
        for k,v in chessValids[i].items():
    #        print(k,v,end = ',')
            while k == moveofcell and v == moveofpiece:
                print(k,v,end = ',')
                return True
    return False
print(isValidChessBoard())
#print(len(chessValids))

print('Enter the white king cell')
chessPieces[input()] = 'wking'
print('Enter the white queen cell')
chessPieces[input()] = 'wqueen'
for i in range(2):
    print('Enter the white bishop cell')
    chessPieces[input()] = 'wbishop'
for i in range(2):
    print('Enter the white knight cell')
    chessPieces[input()] = 'wknight'    
for i in range(2):
    print('Enter the white rook cell')
    chessPieces[input()] = 'wrook'
for i in range(8):
    print('Enter the white pawn cell')
    chessPieces[input()] = 'wpawn'

print('Enter the black king cell')
chessPieces[input()] = 'bking'
print('Enter the black queen cell')
chessPieces[input()] = 'bqueen'
for i in range(2):
    print('Enter the black bishop cell')
    chessPieces[input()] = 'bbishop'
for i in range(2):
    print('Enter the black knight cell')
    chessPieces[input()] = 'bknight'    
for i in range(2):
    print('Enter the black rook cell')
    chessPieces[input()] = 'brook'
for i in range(8):
    print('Enter the black pawn cell')
    chessPieces[input()] = 'bpawn'


print(chessPieces)
