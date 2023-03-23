numeros = input("Digite uma lista de numeros: ")
numeros = [int(num) for num in numeros.split()]

numeros.sort(key=int, reverse=False)

print("A ordem dos numeros em forma crescente é:", numeros)