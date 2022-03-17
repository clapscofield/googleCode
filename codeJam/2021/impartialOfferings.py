# the problem here https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777098#problem

def divide(pets, pets_size):
    pets_size.sort()
    anterior = -1
    valor = 1
    total_gasto = 0
    for pet in pets_size:
        if(anterior < pet and anterior != -1):
            valor += 1
            total_gasto += valor
        else:
            total_gasto += valor
        anterior = pet
        
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
