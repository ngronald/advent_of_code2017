# Advent of code 2017

def printAnswer(day, question, answer):
    print('Answer for {} on {} is {}'.format(question,day,answer))

# Day 1
# Q1
from collections import deque

with open('input/day1.txt') as fp:
    string = fp.read()
numlist = [int(num) for num in string]
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

def mainDay3():
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
    mainDay3()


# Day4 
def mainDay4():
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
    mainDay4()
'''
# Day5
import copy
def mainDay5():
    with open('input/day5.txt') as fp:
        num1 = [int(line) for line in fp]
        num2 = copy.deepcopy(num1)
        c1=c2=i1=i2=0
        while i1 >=0 and i1 < len(num1):
            oldi=i1
            i1+=num1[i1]
            num1[oldi]+=1
            c1+=1
        printAnswer('Day5','Q1',c1)
        while i2>= 0 and i2 < len(num2):
            oldi=i2
            i2+=num2[i2]
            if num2[oldi] < 3:
                num2[oldi]+=1
            else:
                num2[oldi]-=1
            c2+=1
        printAnswer('Day5','Q2',c2)
if __name__ == '__main__':
    mainDay5()
'''
# Day 6
import copy
from collections import deque
def mainDay6():
    with open('input/day6.txt') as fp:
        numList = [int(num) for num in fp.read().split('\t')]
    record = []
    count = len(numList)
    while numList not in record:
        record.append(numList)
        maxIndex = numList.index(max(numList))
        tmpList = copy.deepcopy(numList)
        tmpList[maxIndex] = 0
        remainder = numList[maxIndex] % count
        remainderList = deque(([1] * remainder + [0] * count)[:count])
        remainderList.rotate(1+maxIndex)
        quotient = [numList[maxIndex] // count ] * count
        numList = [sum(x) for x in zip(tmpList,quotient,remainderList)]
    printAnswer('Day6','Q1',len(record))
    printAnswer('Day6','Q2',len(record)-record.index(numList))
if __name__ == '__main__':
    mainDay6()

# Day 8
import operator
class RegisterRecord(object):
    
    def __init__(self,file):
        self.record = dict()
        self.file = file
        self.maxValue = None

    def read_file(self):
        with open(self.file) as fp:
            for line in fp:
                line = line.rstrip().split(' ')
                yield line

    def parse_each_line(self,line):
        condVal = str(self.record.get(line[4],0))
        condition = " ".join([condVal]+line[-2:])
        if self.eval_condition(condition):
            if line[1] == 'inc':
                operation = operator.add
            else:
                operation = operator.sub
            register = line[0]
            value = int(line[2])
            self.update_record(register,value,operation)
        # update the maxValue after parsing each line
        self.update_maxValue()

    def eval_condition(self,conditionStr):
        return eval(conditionStr)   
    
    def update_record(self,register,chgValue,op):
        registerValue = self.record.get(register,0)
        self.record[register] = op(registerValue,chgValue)

    def get_max_register(self):
        return max(self.record.iterkeys(), key= lambda element: self.record[element])

    def get_max_value(self):
        return max(self.record.values())

    def update_maxValue(self):
        currMax = self.get_max_value()
        if currMax > self.maxValue:
            self.maxValue = currMax

if __name__ == '__main__':
    record = RegisterRecord('input/day8.txt')
    for line in record.read_file():
        record.parse_each_line(line)
    maxValueQ1 = record.get_max_value()
    printAnswer('Day8','Q1',str(maxValueQ1))
    maxValueQ2 = record.maxValue
    printAnswer('Day8','Q2',str(maxValueQ2))

# Day 9
class ProcessStream(object):
    def __init__(self,file):
        with open(file) as fp:
            self.stream = fp.read().rstrip()
        self.trash_storage = list()
        self.group_storage = list()

    def start(self):
        self.remove_bang()
        self.extract_group()

    def remove_bang(self):
        index = self.find_bang()
        self.stream = ''.join([self.stream[i] for i in range(len(self.stream)) if not i in index])

    def find_bang(self):
        index = [pos for pos,val in enumerate(self.stream) if val == '!']
        diff = [j-i for i,j in zip(index[:-1],index[1:])] + [0]
        for i in range(len(index)):
            if diff[i]==1 and index[i] is not None:
                index[i+1] = None
        index = [i for i in index if i is not None]
        index = index + [i+1 for i in index]
        index.sort()
        return index

    def extract_group(self):
        isTrash = False
        for chr in self.stream:
            if chr == '<' and not isTrash:
                isTrash = True
            elif chr == '>':
                isTrash = False
            elif chr in '{}' and not isTrash:
                self.group_storage.append(chr)
            elif isTrash:
                self.trash_storage.append(chr)

    def compute_score(self):
        tmplist = []
        score = 0
        for bracket in self.group_storage:
            if bracket == '{':
                tmplist.append(bracket)
            else:
                depth = len(tmplist)
                score += depth
                tmp = tmplist.pop()
        return score

    def count_trash(self):
        return len(self.trash_storage)

if __name__=='__main__':
    day9 = ProcessStream('input/day9.txt')
    day9.start()
    printAnswer('Day9','Q1',str(day9.compute_score()))
    printAnswer('Day9','Q2',str(day9.count_trash()))

# Day 11
def genSteps():
    with open('input/day11.txt') as fp:
        route = fp.read().rstrip().split(',')
    for step in route:
        yield step

def calcDist(stepDict):
    newCoor = {'n':[1,0,0],'s':[-1,0,0],'ne':[0,0,1],'nw':[0,-1,0],'sw':[0,0,-1],'se':[0,1,0]}
    total = [0,0,0]
    for key in stepDict.iterkeys():
        for i in range(3):
            total[i]+=newCoor[key][i]*stepDict[key]
    # total[0] -> north south plus min(total[1],total[2]) -> 'nw' + 'ne' = 'n'  plus total[1]-min(total[1],total[2]) + total[2]-min(total[1],total[2]) -> remaining steps
    totalstep = sum(total) - min(total[1],total[2])
    return totalstep

def mainDay11():
    steps = {'nw':0,'n':0,'ne':0,'se':0,'s':0,'sw':0}
    generateSteps = genSteps()
    maxStep = 0
    for step in generateSteps:
        steps[step]+=1
        distance = calcDist(steps)
        if distance > maxStep:
            maxStep = distance
    shortestDist = calcDist(steps)
    printAnswer('Day11','Q1',shortestDist)
    printAnswer('Day11','Q2',maxStep)
if __name__ == '__main__':
    mainDay11()