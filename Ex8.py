numeros = input("Digite uma lista de numeros: ")
numeros = [int(num) for num in numeros.split()]
newnum = []

for num in numeros:
    if num > 10:
        newnum.append(num)
print("Os numeros maiores que 10 são: ", newnum)