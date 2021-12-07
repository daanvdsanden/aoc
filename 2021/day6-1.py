if __name__ == "__main__":
    with(open("day6-input.txt")) as f:
        line = f.readlines()
    fishes = list(map(int,line[0].split(',')))



    for _ in range(80):
        for i in range(len(fishes)):
            fishes[i]-=1
            if fishes[i]<0:
                fishes.append(8)
                fishes[i]+=7
    print(len(fishes))
