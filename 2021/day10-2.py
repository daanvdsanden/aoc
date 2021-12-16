if __name__ == "__main__":
    with(open("day10-input.txt")) as f:
        lines = f.readlines()
    openings = "({[<"
    closings = ")}]>"
    scores = { ')':1, ']':2,'}':3,'>':4 }

    points=[]
    for line in lines:
        stack = []
        for symbol in line.strip():
            if symbol in "([{<":
                stack.append(symbol)
                continue
            if symbol in closings:
                i = closings.index(symbol)
                if stack[-1] == openings[i]:
                    stack.pop()
                    continue
                else:
                    break
        else:
            score = 0
            for i in stack[::-1]:
                score *= 5
                score += scores[closings[openings.index(i)]]
            points.append(score)
    print(points)
    print(sorted(points)[(len(points)+1)//2 -1 ]) 
