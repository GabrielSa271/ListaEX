numeros = input("Digite uma lista de números separados por espaço (pode ser negativo ou não): ")

numeros = [int(num) for num in numeros.split()]

impares = []

for num in numeros:
    if num % 2 == 1:
        impares.append(num)

print(impares)
        
soma = sum(impares)
print("A soma dos numeros impares é:", soma)
