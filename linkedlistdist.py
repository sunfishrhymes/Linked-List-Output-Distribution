import pandas as pd

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

list1 = ['apple',  13, 13, 13, 412, 'bananana']
directory = {}

for i, n in enumerate(list1):
    directory[i] = Node(n)

dirkeys = list(directory.keys())

def assign(first):
    CurrentNode = first
    while CurrentNode:
        print (CurrentNode.data)
        CurrentNode = CurrentNode.next
        
for t in dirkeys[:-1]:
    directory[t].next = directory[t + 1]
 

def pickconnect(node): #first attempt
    freqtable = []
    CurrentNode = node
    NextNode = CurrentNode.next
    while CurrentNode and NextNode:
        freqtable.append([CurrentNode.data, NextNode.data])
        CurrentNode = CurrentNode.next
        NextNode = NextNode.next
    print(pd.Series(freqtable).value_counts())

def outcomedist(node): #second attempt
    global inout
    inrange = []
    outrange = []
    CurrentNode = node
    NextNode = CurrentNode.next
    while CurrentNode and NextNode:
        inrange.append(CurrentNode.data)
        outrange.append(NextNode.data)
        CurrentNode = CurrentNode.next
        NextNode = NextNode.next
    inouttotal = zip(inrange, outrange)
    inout = pd.DataFrame(inouttotal, columns= ['Input_Node', 'Output_Node'])

outcomedist(directory[dirkeys[0]])

def maxprob(node):
    CurrentNode = node
    while CurrentNode.next is not None:
        print(inout[inout['Input_Node'] == CurrentNode.data]['Output_Node'].value_counts('Output_Node').idxmax())
        CurrentNode = CurrentNode.next

maxprob(directory[dirkeys[0]])