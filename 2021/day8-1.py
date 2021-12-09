if __name__ == "__main__":
    with(open("day8-input.txt")) as f:
        lines = f.readlines()

    codes = [ list(map(len,x.split(" | ")[1].split())) for x in lines]

    codes = [ 1 for code in codes for x in code if x in (2,3,4,7)  ]
    print(sum(codes))
