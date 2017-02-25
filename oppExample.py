# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 10:50:32 2017

@author: James
"""
import datetime
class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday =None
        self.lastName = name.split(' ')[-1]
        """name is a string, so spilt into a list of strings based on spaces, then extract ;astr element"""
    
    def getLastName(self):
        return self.lastName
        
    def __str__(self):
        return self.name
        
    def setBirthday(self,month,day,year):
        self.birthday=datetime.date(year,month,day)
        
    def getAge(self):
        if self.birthday== None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days

    def __lt__(self,other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName <other.lastName
   
class MITPerson(Person):
    nextIdNum = 0
    
    def __init__(self,name):
        Person.__init__(self,name)
        self.IdNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    
    def getIdNum(self):
        return self.IdNum
    
    def __lt__(self,other):
        return self.IdNum < other.IdNum
    def speak(self,utterance):
        return (self.getLastName()+'says: '+ utterance)

class UG(MITPerson):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year=classYear
    
    def getClass(self):
        return self.year
    
    def speak(self,utterence):
        return MITPerson.speak(self,'Dude '+utterance)
class Grad(MITPerson):
    pass
def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)
        
