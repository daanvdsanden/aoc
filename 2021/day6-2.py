if __name__ == "__main__":
    with(open("day6-input.txt")) as f:
        line = f.readlines()
    temp_fishes = list(map(int,line[0].split(',')))

    fishes={i: 0 for i in range(9) }

    for fish in temp_fishes:
        fishes[fish] += 1
    for _ in range(256):
        new_fish = fishes[0]
        for i in range(8):
            fishes[i]=fishes[i+1]
            if i == 6:
                fishes[i]+=new_fish
        fishes[8]=new_fish
    print(sum(fishes.values()))
