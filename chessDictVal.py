def isValidChessBoard(chessBoard):
    whitePawns = 0
    blackPawns = 0
    whiteKing = 0
    blackKing = 0
    whiteRemaining = 0
    blackRemaining = 0
    for valPos, valPiec in chessBoard.items():
        if valPos not in chessPosition:
            return False
        if valPiec not in chessPieces:
            return False
    for i in range(len(chessMoves)):
        if list(chessMoves.values())[i] == 'wpawn':
            whitePawns += 1       
        if list(chessMoves.values())[i] == 'bpawn':
            blackPawns += 1       
        if list(chessMoves.values())[i] == 'wking':
            whiteKing += 1        
        if list(chessMoves.values())[i] == 'bpawn':
            blackPawns += 1
        if list(chessMoves.values())[i] == 'wbishop' or list(chessMoves.values())[i] == 'wrook' or  list(chessMoves.values())[i] == 'wqueen' or list(chessMoves.values())[i] == 'wknight':
            whiteRemaining += 1
        if list(chessMoves.values())[i] == 'bbishop' or list(chessMoves.values())[i] == 'brook' or  list(chessMoves.values())[i] == 'bqueen' or list(chessMoves.values())[i] == 'bknight':
            blackRemaining += 1    
    if whitePawns > 8:
            return False
    if blackPawns > 8:
        return False
    if whiteKing != 1:
            return False
    if blackPawns > 8:
            return False
    if whiteRemaining > 7:
        return False
    if blackRemaining > 7:
            return False
    
    return True        

chessPosition = []
for x in range(1, 9):
    for y in ['a','b','c','d','e','f','g','h']:
        chessPosition.append(str(x)+y)
chessPieces = []
whiteChessPieces = []
blackChessPieces = []
for x in ['king','queen','bishop','rook','knight','pawn']:
    whiteChessPieces.append('w'+x)
    blackChessPieces.append('b'+x)
    chessPieces = whiteChessPieces + blackChessPieces

chessMoves = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
              '2h': 'wking', '4e':'wpawn', '8e':'wpawn','7e':'wpawn'}

print(isValidChessBoard(chessMoves))
