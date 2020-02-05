rows = ['1','2','3','4','5','6','7','8']
columns = ['a','b','c','d','e','f','g','h']
color = ['w','b']
pieces= ['king','queen','bishop','rook','knight','pawn']
cells= []
coloredPieces = []
chessValids = {}
for single1 in rows:
    for each1 in columns:
        cell = single1 + each1
        cells.append(cell)
print(cells)
print()
for single2 in color:
    for each2 in pieces:
        coloredPiece = single2 + each2
        coloredPieces.append(coloredPiece)
print(coloredPieces)
print()
for single3 in cells:
#    for each3 in coloredPieces:
#        chessValid = {}
#        chessValid[single3] = each3
        chessValids.setdefault(single3,coloredPieces)
print(chessValids)
