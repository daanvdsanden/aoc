import pprint

if __name__ == "__main__":
    with(open("day5-input.txt")) as f:
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
        if x1 > x2 or (x1==x2 and y1> y2):
            x1, y1, x2, y2 = x2, y2, x1, y1
        lines.append([x1,y1,x2,y2])
    board = [[ 0 for _ in range(max_column+1) ] for _ in range(max_row+1) ]
    for line in lines:
        if line[0] == line[2]:
            for row in range(line[1],line[3]+1):
                board[row][line[0]]+=1
        elif line[1] == line[3]:
            for column in range(line[0],line[2]+1):
                board[line[1]][column]+=1
        elif line[2]-line[0] == line[3]-line[1]:
            for i in range(line[2]-line[0]+1):
                board[line[1]+i][line[0]+i]+=1
        elif line[2]-line[0] == line[1]-line[3]:
            print(line)
            for i in range(line[2]-line[0]+1):
                print(line[2]-i,line[3]+i)
                board[line[3]+i][line[2]-i]+=1
    totaal = 0
    for row in board:
        for column in row:
            if column > 1:
                totaal+=1
    pprint.pprint(totaal)
