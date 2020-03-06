theBoard = {'top-L':' ', 'top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}
            
def checkWinnerRow ():
    if theBoard['top-L'] == 'X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
        print('X is the winner')
        printBoard(theBoard)
        quit()
    elif theBoard['mid-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
        print('X is the winner!')
        printBoard(theBoard)
        quit()
    elif theBoard['low-L'] == 'X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
        print('X is the winner!')
        printBoard(theBoard)
        quit()
    if theBoard['top-L'] == 'O' and theBoard['top-M'] == 'O' and theBoard['top-R'] == 'O':
        print('O is the winner')
        printBoard(theBoard)
        quit()
    elif theBoard['mid-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O':
        print('O is the winner!')
        printBoard(theBoard)
        quit()
    elif theBoard['low-L'] == 'O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O':
        print('O is the winner!')
        printBoard(theBoard)
        quit()

def checkWinnerColumn ():
    if theBoard['top-L'] == 'X' and theBoard['mid-L'] == 'X' and theBoard['low-L'] == 'X':
        print('X is the winner')
        quit()
    elif theBoard['top-M'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-M'] == 'X':
        print('X is the winner!')
        quit()
    elif theBoard['top-R'] == 'X' and theBoard['mid-R'] == 'X' and theBoard['low-R'] == 'X':
        print('X is the winner!')
        quit()
    if theBoard['top-L'] == 'O' and theBoard['mid-L'] == 'O' and theBoard['low-L'] == 'O':
        print('O is the winner')
        quit()
    elif theBoard['top-M'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-M'] == 'O':
        print('O is the winner!')
        quit()
    elif theBoard['top-R'] == 'O' and theBoard['mid-R'] == 'O' and theBoard['low-R'] == 'O':
        print('O is the winner!')
        quit()

def checkWinnerDiag ():
    if theBoard['top-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['low-R'] == 'X':
        print('X is the winner!')
        quit()
    elif theBoard['low-L'] == 'X' and theBoard['mid-M'] == 'X' and theBoard['top-R'] == 'X':
        print('X is the winner!')
        quit()
    if theBoard['top-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['low-R'] == 'O':
        print('O is the winner!')
        quit()
    elif theBoard['low-L'] == 'O' and theBoard['mid-M'] == 'O' and theBoard['top-R'] == 'O':
        print('O is the winner!')
        quit()

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-' + '-' + '-' + '-' + '-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-' + '-' + '-' + '-' + '-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-' + '-' + '-' + '-' + '-')

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    while True:
        move = input()
        if move not in ('top-L','top-M','top-L','mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R'):
            print("Invalid: Must Select a Row: top\mid\low and a column L\M\R (Left, Middle, Right) Ex. top-L ")
            continue
        else:
            break
    theBoard[move] = turn
    checkWinnerRow()
    checkWinnerColumn()
    checkWinnerDiag()
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    

printBoard(theBoard)