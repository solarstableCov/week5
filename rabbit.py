#!/usr/bin/env python3
start=5
days=200
litter=3
mature=20
population=[0]*(days+mature)
for day in range(1,days):
    population[0]+=start
    population[day]+=population[day-1]
    newRabbits = (population[day] // 2) * litter
    population[day+mature]+=newRabbits
print(population[0:days])
print(population[days])




