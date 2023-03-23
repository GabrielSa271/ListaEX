numeros = input("Digite uma lista de numeros: ")
numeros = [int(num) for num in numeros.split()]
newnum = []

for num in numeros:
    if num < 5:
        newnum.append(num)
print("Os numeros menores que 5 são: ", newnum)