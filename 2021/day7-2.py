if __name__ == "__main__":
    with(open("day7-input.txt")) as f:
        crabs = list(map(int,f.readlines()[0].split(',')))

    crabs = sorted(crabs)
    consumption = 9999999999999999999999999999999999999999
    for i in range(crabs[0],crabs[-1]):
        temp = sum([ (abs(crab-i)*(abs(crab-i)+1))//2 for crab in crabs ])
        if temp < consumption:
            consumption = temp
    print(consumption)
