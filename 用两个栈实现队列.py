# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def push(self, node):
        # write code here
        self.instack.append(node)
    def pop(self):
        # return xx
        if self.outstack==[]:
            while self.instack:
                self.outstack.append(self.instack.pop())
        if self.outstack:     
            return self.outstack.pop()
        else:
            return None