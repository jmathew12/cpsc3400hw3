# James Mathew
# hw3.py
# cpsc3400

import sys

def create(nodes):
    for x in range(1, len(nodes)):
        if x % 2 == 1:
            if not nodes[x][0].isdigit():
                if nodes[x+1].isalpha():
                    yield [nodes[x], nodes[x+1]]
                else:
                    yield [nodes[x], int(nodes[x+1])]
            else:
                if nodes[x+1][0].isalpha():
                    yield [int(nodes[x]), nodes[x+1]]
                else:
                    yield [int(nodes[x]), int(nodes[x+1])]

def createList(connect, attached, value):
    for x in connect:
        if x[0] == value:
            attached.append(x[1])
            connect.pop(connect.index(x))
            createList(connect, attached, x[1])

inputs = sys.argv


with open(inputs[1], 'r') as input:
    nodes = []
    s = ''
    for line in input:
        for x in line:
            if ',' == x or '\n' == x:
                if  s != '':
                    nodes.append(s)
                    s = ''
            else:
                s = s+x
    if s != '':
        nodes.append(s)      
length = int(nodes[0])   
connect = []
for x in create(nodes):
    connect.append(x)
names = []
for x in connect:
    if type(x[0]) == str:
        names.append(x[0])
attached = []
marked = set()
unmarked = set()
for x in names:
    attached.append(x)
    createList(connect, attached, x)
    for y in attached:
        if str(y).isdigit():
            marked.add(y)
    attached = []
for x in connect:
    unmarked.add(x[0])
for x in range(0, length):
    if not x in marked:
        unmarked.add(x)
marked = sorted(list(marked))
unmarked = sorted(list(unmarked))
s = 'Marked nodes: '
for x in marked:
    s = s + str(x) + ' '
print(s)
s = 'Swept nodes: '
for x in unmarked:
    s = s + str(x) + ' '
print(s)