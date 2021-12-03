def read_input(filename):
    with open(filename) as f:
        depths = f.readlines()
    return list(map(int,depths))

if __name__ == "__main__":
    depths = read_input("day1-input.txt")
    higher = 0

    for i in range(len(depths) - 1):
        if depths[i+1] > depths[i]:
            higher+=1

    print(higher)


