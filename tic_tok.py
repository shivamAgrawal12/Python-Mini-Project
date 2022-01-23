board = [' ' for x in range(20)]


def insert(letter, pos):
    board[pos] = letter


def space(pos):
    return board(pos) == ' '


def printboard(board):
    print("     |   |   ")
    print(' '+board[1] + '   |  ' + board[1] + '| '+board[3])
    print("     |   |   ")
    print("_______________")
    print("     |   |   ")
    print(' '+board[4] + '   |  ' + board[5] + '| '+board[6])
    print("     |   |   ")
    print("_______________")
    print("     |   |   ")
    print(' '+board[7] + '   |  ' + board[8] + '| '+board[9])
    print("     |   |   ")


def boardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        True


def winner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


def playermove():
    run = True
    while run:
        move = input("Please enter the number for X betwween 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space(move):
                    run = False
                    insert('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number between 1 to 9")

        except:
            print("Please type the number only")


def compmove():
    possiblemove = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in ['0', 'X']:
        for i in possiblemove:
            boardcopy = board[:]
            boardcopy[i] = let
            if winner(boardcopy, let):
                move = 1
                return move
    corneropen = []
    for i in possiblemove:
        if i in [1, 3, 7, 9]:
            corneropen.append()

    if len(corneropen) > 0:
        move = selectRandom(corneropen)
        return move

    if 5 in possiblemove:
        move = 5
        return move

    edgeopen = []
    for i in possiblemove:
        if i in [2, 4, 6, 8]:
            edgeopen.append(i)

    if len(edgeopen) > 0:
        move = selectRandom(edgeopen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print("Welcome to the game")
    printboard(board)

    while not (boardfull(board)):
        if not winner(board, 'O'):
            playermove()
            printboard(board)
        else:
            print("sorry you loose!..")
            break

        if not winner(board, 'X'):
            move = compmove()
            if move == 0:
                print(" ")
            else:
                insert('O', move)
                print("Computer placed an o on position", move, ':')
                printboard(board)
        else:
            print("you win!..")
            break

    if boardfull(board):
        print("Game tie")


while True:
    x = input("Do you want to play again(y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(20)]
        print("-------------------------------------")
        main()
    else:
        break
