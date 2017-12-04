# Advent of code 2017

def printAnswer(day, question, answer):
    print('Answer for {} on {} is {}'.format(question,day,answer))

# Day 1
# Q1
from collections import deque

with open('input/day1.txt') as fp:
    str = fp.read()
numlist = [int(num) for num in str]
items = deque(numlist)
items.rotate(1)
sumlist = [numlist[i] for i in xrange(len(items)) if items[i] == numlist[i] ]
printAnswer('Day1','Q1',sum(sumlist))

# Q2
halflen = len(numlist) / 2
items = deque(numlist)
items.rotate(halflen)
sumlist = [numlist[i] for i in xrange(len(items)) if items[i] == numlist[i] ]
printAnswer('Day1','Q2',sum(sumlist))

# Day 2
# Q1

diff = []
with open('input/day2.txt') as fp:
    for line in fp:
        numbers = line.split()
        numlist=[]
        for number in numbers:
            number = int(number)
            numlist.append(number)
        difference = max(numlist) - min(numlist)
        diff.append(difference)
printAnswer('Day2','Q1',sum(diff))


# Q2
divList=[]
with open('input/day2.txt') as fp:
    for line in fp:
        numbers = line.split()
        numlist=[]
        for number in numbers:
            number = int(number)
            numlist.append(number)
        numlist.sort()
        numlist.reverse()
        while len(numlist) > 0:
            firstNum = numlist.pop()
            for quotient, remainder in [divmod(ind,firstNum) for ind in numlist]:
                if remainder == 0:
                    divList.append(quotient)
                    break
printAnswer('Day2','Q2',sum(divList))


# Day 3
input = 368078
recordQ1=[(0,0)]  #a list to store the path
recordQ2={(0,0):1}  #a dict to store value of each coordinate
def get_spiral_coord(n):
    '''
    if n = 1 --> (1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)
    '''
    # entry point
    yield n,1-n
    # Move up (n*2-1 steps)
    for up in range(1,n*2):
        yield n, 1-n+up
    # Move left (2n steps)
    for left in range(1,n*2+1):
        yield n-left,n
    # Move down (2n steps)
    for down in range (1,n*2+1):
        yield -n,n-down
    # Move right (2n steps)
    for right in range (1,n*2+1):
        yield -n+right,-n

NEIGHBOUR=list(get_spiral_coord(1))

def get_neighbour_sum(xcoor,ycoor):
    return sum ([recordQ2.get((xcoor+x,ycoor+y),0)for x,y in NEIGHBOUR])

def main():
    # Q1
    layerQ1 = 1
    while len(recordQ1) < input:
        for x,y in get_spiral_coord(layerQ1):
            recordQ1.append((x,y))
        layerQ1+=1    
    finalCoor = recordQ1[input-1]
    printAnswer('Day3','Q1',abs(finalCoor[0])+abs(finalCoor[1]))
    # Q2
    layerQ2=1
    answer=None
    while recordQ2.values()[-1] < input:
        for x,y in get_spiral_coord(layerQ2):
            total = get_neighbour_sum(x,y)
            recordQ2[(x,y)] = total
            if total > input:
                answer = total
                break
        layerQ2+=1
        if answer is not None:
            break
    printAnswer('Day3','Q2',answer)
if __name__ == '__main__':
    main()


# Day4 
def main():
    validQ1=0
    validQ2=0
    with open('input/day4.txt') as fp:
        for line in fp:
            line=line.split()
            if len(line) == len(set(line)):
                validQ1+=1
            sortedWord=[]
            for word in line:
                sortedWord.append(''.join(sorted(word)))
            if len(sortedWord) == len(set(sortedWord)):
                validQ2+=1
    printAnswer('Day4','Q1',validQ1)
    printAnswer('Day4','Q2',validQ2)
if __name__ == '__main__':
    main()
