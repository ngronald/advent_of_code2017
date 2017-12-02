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
            divisible = None
            for i in numlist:
                if i % firstNum == 0:
                    divisible = i
            if divisible is not None:
                quotient = divisible / firstNum
                divList.append(quotient)
                break
printAnswer('Day2','Q2',sum(divList))





