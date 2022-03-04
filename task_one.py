# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:05:57 2022

@author: yael
"""
##### A #########
def my_func(x1,x2,x3):
    if type(x1)!= float or type(x2)!= float or type(x3)!= float :
        print("ERROR : parameters should be float")
    elif x1+x2+x3 == 0 :
        print("NOT A NUMBER--->denominator is zero")
        
    else :
        print(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
    
my_func(4.5, 6, 7.3)
my_func(-7.0, 6.0, 1.0)
my_func(4.0, 6.8, 7.3)

#####  B #######             
def convert(hours=0,minute=0):
    
    if hours < 0 :
        print("Input error!")
    elif minute < 0 :
        print("Input error!")
    else:
       print(hours*3600+minute*60)


convert(0,1)
convert(2,1)
convert(2.0,1.0)


           
    
    
