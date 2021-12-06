import pprint

if __name__ == "__main__":
    with(open("day5-test-input.txt")) as f:
        raw_lines = f.readlines()
    
    max_column = 0
    max_row = 0
    lines = []
    for line in raw_lines:
        begin,end = line.split(' -> ')
        x1,y1 = list(map(int,begin.split(',')))
        x2,y2 = list(map(int,end.split(',')))
        max_column=max(max_column,x1,x2)
        max_row=max(max_row,y1,y2)
        if x1 > x2 or y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        lines.append([x1,y1,x2,y2])
    board = [[ 0 for _ in range(max_column+1) ] for _ in range(max_row+1) ]
    for line in lines:
        if line[0] == line[2]:
            for row in range(line[1],line[3]+1):
                board[row][line[0]]+=1
        if line[1] == line[3]:
            for column in range(line[0],line[2]+1):
                board[line[1]][column]+=1
    totaal = 0
    for row in board:
        for column in row:
            if column > 1:
                totaal+=1
    pprint.pprint(board)
