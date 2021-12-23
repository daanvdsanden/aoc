from collections import namedtuple

F=namedtuple("F","d v")

def process_number(sf):
    for i,f in enumerate(sf):
        if f.d == 5:
            if i == 0:
                return False, [F(4,0), F(sf[i+1].d, sf[i+1].v + sf[i+2].v) ] + sf[i+3:]
            if i == len(sf)-2:
                return False, sf[:i-1] + [ F(4, sf[i-1].v+f.v), F(4,0)]
            return False, sf[:i-1] + [F(sf[i-1].d,sf[i-1].v+f.v),F(4,0),F(sf[i+2].d,sf[i+1].v+sf[i+2].v)] + sf[i+3:]
    for i,f in enumerate(sf):
        if f.v > 9:
            if i == 0:
                return False, [F(f.d+1,f.v // 2), F(f.d+1,f.v - f.v // 2)] + sf[i+1:]
            if i == len(sf)-1:
                return False, sf[:i] + [F(f.d+1,f.v // 2), F(f.d+1,f.v - f.v // 2)]
            return False, sf[:i] + [F(f.d+1,f.v // 2), F(f.d+1,f.v - f.v // 2)] + sf[i+1:]
    return True, sf

with(open("day18-test-input.txt")) as f:
    lines = f.readlines()

numbers = []
for line in lines:
    d = 0
    sfs = []
    for c in line.strip():
        if c == "[":
            d+=1
        elif c == "]":
            d-=1
        elif c.isnumeric():
            sfs.append(F(d,int(c)))
    numbers.append(sfs)

total = [ i for i in numbers[0]] 

for x in numbers[1:]:
    print("===========================")
    print(total)
    print(x)
    total=[F(i.d+1,i.v) for i in total] + [F(i.d+1,i.v) for i in x]
    print("TOTAL and x")
    print(total,x)
    done=False
    while not done:
        done, total = process_number(total)
        print(total)
    print("===========================")

