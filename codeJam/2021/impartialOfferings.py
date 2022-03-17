# the problem here https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777098#problem

from collections import Counter

def divide(pets, pets_size):
    res = {}
    for i in pets_size:
        res[i] = pets_size.count(i)
    print(res)
    valor = 1
    total_gasto = 0
    for key, value in res.items():
        total_gasto += value * valor
        valor += 1
        
    return total_gasto
    
def main():
    total = int(input())
    cases = []
    for x in range(0, total):
        pets = int(input())
        pets_size = list(map(int,input().split()))
        cases.append(divide(pets,pets_size))
        
    count = 0
    for case in range(0, total):
        print("Case #" + str(count+1) + ": " + str(cases[count]))
        count += 1

main()
