numeros = input("Digite uma lista de numeros: ")
numeros = [int(num) for num in numeros.split()]
sem_duplicados = []

while numeros:
    elemento = numeros.pop(0)
    if elemento not in sem_duplicados:
        sem_duplicados.append(elemento)

print("Os numeros sem duplicados são: ", sem_duplicados)