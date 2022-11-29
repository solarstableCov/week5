#!/usr/bin/env python3

name=input("Enter your name: ")
print(f'Give me an {name[0].upper()}')#first letter of word to be capital
print(f'Give me an {name[1:-1].lower()}')#send to second last letter to be lower case
print(f'Give me an {name[-1].upper()}')#last letter of word to be capital
print(f'{name.upper()}!')

