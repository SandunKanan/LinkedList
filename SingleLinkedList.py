# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:25:47 2022

@author: kanangas
"""



class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
    
class SLinkedList:
    def __init__(self):
        self.headval = None
        
    # Method iterates through each node in list and prints value
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
        
    # return length (num of nodes) in linked list
    def length(self):
        curr = self.headval
        if curr is None:
            return 0
        total = 1
        while curr.nextval is not None:
            total += 1
            curr = curr.nextval
        return total
        
    # add a node to the start of the list
    def add_to_start(self, newValue):
        NewNode = Node(newValue)
        NewNode.nextval = self.headval
        self.headval = NewNode
        
    # add a node to the end of the list
    def add_to_end(self, newValue):
        NewNode = Node(newValue)
        #If list is empty
        if self.headval is None:
            self.headval = NewNode
            return
        # Non-Empty list
        curr_val = self.headval
        while curr_val.nextval is not None:
            curr_val = curr_val.nextval
        curr_val.nextval = NewNode
        
    # Create a linked list from an input classic array
    def create_from_array(self, array):
        if len(array)==0:
            return None
        self.headval = Node(array[0])
        if len(array)==1:
            return
        for val in array[1:]:
            self.add_to_end(val)
    
    # return the node contain entered value if it exists, else return None
    def search_for(self, value):
        req_node = self.headval
        while req_node is not None:
            if req_node.dataval == value:
                return req_node
            req_node = req_node.nextval
        return None
    
    # return the node before the entered value, returns None is first value is entered
    def give_prev_node(self, value, searchOnly=True):
        req_node = self.headval
        if value == req_node.dataval:
            if searchOnly:
                print("First value is given, no previous node")
            return None
        prev_node = req_node
        req_node = req_node.nextval
        while req_node is not None:
            if req_node.dataval == value:
                return prev_node
            prev_node = req_node
            req_node = req_node.nextval
        return None
    
    # add a node after a specified value already contained in the list
    def add_after(self, newVal, prevVal):
        newNode = Node(newVal)
        prevNode = self.search_for(prevVal)
        if prevNode is None:
            print(f"{prevVal} does not exist in list")
            return
        newNode.nextval = prevNode.nextval
        prevNode.nextval = newNode
        
    #add a node before a specified value already contained in the list
    def add_before(self, newVal, afterVal):
        newNode = Node(newVal)
        afterNode = self.search_for(afterVal)
        if afterNode is None:
            print(f"{afterVal} does not exist in list")
            return
        newNode.nextval = afterNode
        # If afterNode is first value
        if afterNode == self.headval:
            self.headval = newNode
            return
        #afterVal is not first
        prevNode = self.give_prev_node(afterVal, searchOnly=False)
        prevNode.nextval = newNode
    
    
        
list1 = SLinkedList()
arr_list = ["Mon", "Tue", "Wed", "Thu", "Fri"]
list1.create_from_array(arr_list)

list1.add_to_start("Sun")
list1.add_to_end("Sat")

list1.add_after("WednHalf", "Wed")
list1.add_before("Start", "Sun")
list1.listprint()
print(list1.length())
