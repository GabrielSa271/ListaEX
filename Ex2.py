plrs = input("Digite uma lista de palavras separadas por espaço: ")
plrs = plrs.split()

for plr in plrs:
    if plr.startswith('a') or plr.startswith('A'):
        print(plr)
