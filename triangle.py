#!/usr/bin/env python3
triangle_size= input("Enter the size of the triangle: ")#number of rows
size=int(triangle_size)
#nested loop for each column
for i in range (0, size):
    for j in range (0, i+1):
        #print asterisk
        print("*", end=' ')
    #new line after each row
    print("\r")
