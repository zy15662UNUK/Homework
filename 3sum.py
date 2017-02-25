# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 23:26:42 2017

@author: James
"""
def compare(lis1,lis2):
    for i in lis1:
        if lis2.sort()==i.sort():
            return False
        else:
            return True
        
                    
                    
def threeSum(self, nums):
     ans=[]
     for i in range(len(nums)-2):
         for j in range(i+1,len(nums)-1):
             for k in range(j+1,len(nums)):
                 if nums[i]+nums[j]+nums[k]==0 and compare(ans,[nums[i],nums[j],nums[k]])==True:
                   print(compare(ans,[nums[i],nums[j],nums[k]]))
                   ans.append([nums[i],nums[j],nums[k]])
     return ans