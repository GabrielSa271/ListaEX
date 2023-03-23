numeros = input("Digite uma lista de numeros: ")
numeros = [int(num) for num in numeros.split()]

numeros.sort(key=int, reverse=True)

print("A ordem dos numeros em forma decrescente é:", numeros)