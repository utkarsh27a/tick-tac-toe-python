board = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
}

def isWon():
    return (board["1"] == board["2"] ==  board["3"]) or (board["4"] == board["5"] ==  board["6"]) or (board["7"] == board["8"] ==  board["9"]) or (board["1"] == board["4"] ==  board["7"]) or (board["2"] == board["5"] ==  board["8"]) or (board["3"] == board["6"] ==  board["9"]) or (board["1"] == board["5"] ==  board["9"]) or (board["3"] == board["5"] ==  board["7"])

def isStepFinished():
    print(steps)
    return steps > 8
    return len(list(filter(lambda val: type(1) == int, board.values())))

steps = 0
turn = 0
def start():
    global turn, steps
    players = ["X", "O"]
    turn = 0 if turn else 1
    bordView = f' {board["1"]} | {board["2"]} | {board["3"]} \n---------- \n {board["4"]} | {board["5"]} | {board["6"]} \n---------- \n {board["7"]} | {board["8"]} | {board["9"]} '
    print(bordView);
    place = input('Select you place to fill: ')
    steps = steps + 1
    if board[place]:
        board[place] = players[turn]
    if isWon():
       print(f'{players[turn]} won.')
       return
    if isStepFinished():
        print(f'Mathc draw.')
        return
    start()

start()
