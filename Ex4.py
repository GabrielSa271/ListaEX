numeros = input("Digite uma lista de números separados: ")
lista = numeros.split(" ") # Converte a string de entrada em uma lista de strings

# Converte cada string na lista em um número inteiro
for i in range(len(lista)):
    lista[i] = int(lista[i])

# Calcula a média dos números na lista
media = int(sum(lista)) / int(len(lista))


# Imprime o resultado
print("A média dos números é:", media)
