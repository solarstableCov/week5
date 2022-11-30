#!/usr/bin/env python3

def fibo(num):
    fib1=1
    fib2=1
    for i in range(2,num):
        #fib3=fib1+fib2
        newVal=fib2
        fib1=fib2
        fib2=newVal+fib2
    return fib2 
num=int(input("Enter a number: "))
print(fibo(num))
