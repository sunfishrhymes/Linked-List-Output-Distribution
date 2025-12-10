import pandas as pd

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

list1 = ['apple', 2, 14, 'apple', 323, 13, 13, 13, 323234, 13, 412, 'bananana']
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

assign(directory[dirkeys[0]])   

def pickconnect(node): #first attempt
    freqtable = []
    CurrentNode = node
    NextNode = CurrentNode.next
    while CurrentNode and NextNode:
        freqtable.append([CurrentNode.data, NextNode.data])
        CurrentNode = CurrentNode.next
        NextNode = NextNode.next
    print(pd.Series(freqtable).value_counts())

pickconnect(directory[dirkeys[0]])   

def outcomedist(node): #second attempt
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
    print(inout.groupby('Input_Node')['Output_Node'].value_counts('Output_Node'))
    
outcomedist(directory[dirkeys[0]])