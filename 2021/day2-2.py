def read_input(filename):
    with open(filename) as f:
        instructions = f.readlines()
    return list(instructions)

if __name__ == "__main__":
    instructions = read_input("day2-input.txt")
    depth = 0
    horizontal = 0
    aim = 0
    for command in instructions:
        match command.split():
            case ["forward", unit]:
                horizontal += int(unit)
                depth += aim*int(unit)
            case ["down", unit]:
                aim += int(unit)
            case ["up", unit]:
                aim -= int(unit)

    print(depth*horizontal)
