def check_winner(marks):
    bingo = []
    for i in range(len(marks)):
        if 5 in [sum(row) for row in marks[i]]:
             bingo.append(i) 
    return sorted(bingo, reverse=True)

if __name__ == "__main__":
    with(open("day4-input.txt")) as f:
        input_txt = f.readlines()
    boards = []
    no_boards = (len(input_txt)-1) // 6
    for i in range(no_boards):
        test = [ x.strip().split() for x in input_txt[2+i*6:7+i*6] ]
        for x in range(5):
            test.append([test[y][x] for y in range(5)])
        boards.append(test)

    marks = [[[0 for _ in range(5)] for _ in range(10)] for _ in range(no_boards)] 
    draws = list(map(int,input_txt[0].split(',')))
    wins = len(boards)
    for draw in draws:
        for i,board in enumerate(boards):
            for j,row in enumerate(board):
                for k,number in enumerate(row):
                    if int(number) == int(draw):
                        marks[i][j][k]=1
        winners = check_winner(marks)
        print(winners, len(boards))
        if len(winners) > 0:
            totaal = 0
            for winner in winners:
                for i in range(5):
                    for j in range(5):
                        if marks[winner][i][j] == 0:
                            totaal+=int(boards[winner][i][j])
                print(totaal*draw)
            wins -= len(winners)
            for winner in winners:
                del boards[winner]
                del marks[winner]
