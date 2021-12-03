def read_input(filename):
    with open(filename) as f:
        readings = f.readlines()
    return list(map(str.strip,readings))

if __name__ == "__main__":
    readings = read_input("day3-input.txt")
    
    temp_reading = [0]*len(readings[0])

    for reading in readings:
        temp_reading = [ x + int(reading[y]) for y, x in enumerate(temp_reading) ]

    gamma = [ '1' if x > len(readings)/2 else '0' for x in temp_reading ]
    epsilon = [ '1' if x < len(readings)/2 else '0' for x in temp_reading ]
    print(int(''.join(gamma),2)*int(''.join(epsilon),2))



