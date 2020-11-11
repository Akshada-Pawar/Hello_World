# -*- coding: utf-8 -*-
"""
@author: Akshata

Python program to demonstrate inheritance

"""

class Team:
    def show_Team(self):
        print("This is our team:")
        
# Testing class inherited from Team
class Testing(Team):
    TestingName = ""
    
    def show_Testing(self):
        print(self.TestingName)
        
# Dev class inherited from Team
class Dev(Team):
    DevName = ""
    
    def show_Dev(self):
        print(self.DevName)
        
# Sprint class inherited from Testing and Dev classes
class Sprint(Testing,Dev):
    def show_parent(self):
        print("Testing :", self.TestingName)
        print("Dev :", self.DevName)
        
s = Sprint()                                  # Object of Sprint class
s.TestingName = "Platinum"
s.DevName = "Diamond"
s.show_Team()
s.show_parent()







