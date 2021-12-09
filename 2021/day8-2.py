if __name__ == "__main__":
    with(open("day8-input.txt")) as f:
        lines = f.readlines()
    
    total = 0
    for line in lines:
        learn = list(map(frozenset,line.split(' | ')[0].split()))
        digits={}
        digits[filter(lambda x: len(x) == 2, learn)[0]] = 1
        digits[filter(lambda x: len(x) == 3, learn)[0]] = 7
        digits[filter(lambda x: len(x) == 4, learn)[0]] = 4
        digits[filter(lambda x: len(x) == 7, learn)[0]] = 8
        r_digits={x:y for y,x in digits.items()}
        digits[filter(lambda x: len(x) == 6 and r_digits[4].issubset(x), learn)[0]] = 9
        digits[filter(lambda x: len(x) == 5 and r_digits[1].issubset(x), learn)[0]] = 3
        digits[filter(lambda x: len(x) == 6 and not r_digits[1].issubset(x), learn)[0]] = 6
        r_digits={x:y for y,x in digits.items()}
        digits[filter(lambda x: len(x) == 6 and r_digits[7].issubset(x) and not r_digits[4].issubset(x), learn)[0]] = 0
        digits[filter(lambda x: len(x) == 5 and x.issubset(r_digits[6]), learn)[0]] = 5
        digits[filter(lambda x: len(x) == 5 and x not in set(digits.keys()), learn)[0]] = 2

        numbers = list(map(frozenset,line.split(' | ')[1].split())) 
        
        total+=int(''.join([str(digits[number]) for number in numbers]))
    print(total)
