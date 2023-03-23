numeros = input("Insira uma lista de números aleatórios:")
numeros = [int(num) for num in numeros.split()]

maximo = max(numeros)
minimo = min(numeros)
print("O numero maximo é:", maximo)
print("o numero minimo é:", minimo)