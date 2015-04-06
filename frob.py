# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
    def __str__(self):
        b = 'None'
        a = 'None'
        if self.before != None:
            b = self.before.myName()
        if self.after != None:
            a = self.after.myName()
        return self.name + ': ' + b + ', ' + a        

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    
    currentNode = atMe
    while True:
        if currentNode.myName() > newFrob.myName():
            beforeNode = currentNode.getBefore()
            if beforeNode == None:
                currentNode.setBefore(newFrob)
                newFrob.setAfter(currentNode)
                return
            elif beforeNode.myName() <= newFrob.myName():
                currentNode.setBefore(newFrob)
                newFrob.setAfter(currentNode)
                newFrob.setBefore(beforeNode)
                beforeNode.setAfter(newFrob)
                return
            else:
                currentNode = currentNode.getBefore()
        else:
            afterNode = currentNode.getAfter()
            if afterNode == None:
                currentNode.setAfter(newFrob)
                newFrob.setBefore(currentNode)
                return
            elif afterNode.myName() >= newFrob.myName():
                currentNode.setAfter(newFrob)
                newFrob.setBefore(currentNode)
                newFrob.setAfter(afterNode)
                afterNode.setBefore(newFrob)
                return
            else:
                currentNode = currentNode.getAfter()        

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() == None:
        return start
    return findFront(start.getBefore())

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

print str(eric)
print str(andrew)
print str(ruth)
print str(fred)
print str(martha)

s = findFront(martha)
print str(s)