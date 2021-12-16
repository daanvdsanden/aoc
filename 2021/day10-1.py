if __name__ == "__main__":
    with(open("day10-input.txt")) as f:
        lines = f.readlines()
    openings = "({[<"
    closings = ")}]>"
    scores = { ')':3, ']':57,'}':1197,'>':25137 }

    points=0
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
                    print(line)
                    print(stack)
                    points += scores[symbol]
                    break
    print(points)        
