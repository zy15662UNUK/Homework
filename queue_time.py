# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:05:14 2017

@author: James
"""

def queue_time(customers, n):
    """
    There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

The function has two input variables:

customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
The function should return an integer, the total time required.

EDIT: A lot of people have been confused in the comments. To try to prevent any more confusion:

There is only ONE queue, and
The order of the queue NEVER changes, and
Assume that the front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
The diagram on the wiki page I linked to at the bottom of the description may be useful.
So, for example:

queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
N.B. You should assume that all the test input will be valid, as specified above.
    """
    if customers==[]:
        return 0
    if len(customers)==1:
        return customers[0]
    if n==1:
        return sum(customers)
    if n>= len(customers):
        return max(customers)
    batch=[]
    for i in range(n):
        batch.append(customers[i])
        customers[i]=0
    time=0
    index=n   
    while sum(customers)>0 or sum(batch)>0:
        for i in range(len(batch)):
            if batch[i]>0:
                batch[i] -= 1
                
            
            else:
                if index<len(customers):
                    batch[i]=customers[index]
                    customers[index]=0
                    index += 1
                    batch[i] -= 1
        time=time+1
    return time
                
            
                
        
    