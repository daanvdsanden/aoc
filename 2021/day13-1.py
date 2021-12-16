from pprint import pprint

if __name__=="__main__":
    with(open("day13-input.txt")) as f:
        lines = f.readlines()

    max_x = 0
    max_y = 0

    dots = []

    for line in lines:
        if len(line.strip())==0:
            break
        x,y = map(int,line.strip().split(","))

        max_x = max(max_x,x)
        max_y = max(max_y,y)

        dots.append((x,y))
    paper = [[False] * (max_x+1) for _ in range(max_y+1) ]  

    for dot in dots:
        paper[dot[1]][dot[0]]=True

    folds = []
    for line in lines[len(dots)+1:]:
        if len(line.strip())==0:
            continue
        axis,value=line.strip().split(" ")[2].split("=")
        value = int(value)
        folds.append((axis,value))
    for fold in folds:
        if fold[0] == "y":
            if fold[1] >= (len(paper)//2):
                small_side = paper[fold[1]+1:]
                paper = paper[:fold[1]]
            else:
                small_side = paper[:fold[1]]
                paper = paper[fold[1]+1:]
            offset=len(paper)-len(small_side)
            for y,line in enumerate(small_side[::-1]):
                paper[offset+y] = [ x or paper[offset+y][i] for i,x in enumerate(line)]
        if fold[0]=="x":
            print(len(paper[0]),len(paper[0])//2)
            if fold[1] >= (len(paper[0])//2):
                small_side = [ x[fold[1]+1:] for x in paper ]
                paper = [ x[:fold[1]] for x in paper ]    
            else:
                small_side = [ x[:fold[1]] for x in paper ]
                paper = [ x[fold[1]+1:] for x in paper ]
            offset=len(paper[0])-len(small_side[0])
            for y,line in enumerate(paper):
                temp = [False] * offset + small_side[y][::-1]
                paper[y] = [ x or temp[i] for i,x in enumerate(line) ]
    pprint(["".join(['#' if x else '.' for x in line ]) for line in paper])

