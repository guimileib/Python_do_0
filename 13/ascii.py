# pip install pyfiglet

"""
EX1:
Transformar seu nome em caracteres ascii usando a lib pyfiglet
EX2:
O pyfiglet vem com várias fontes. 
Modifique o programa do exercício anterior para que ele peça ao usuário para digitar uma palavra qualquer e, 
em seguida, exiba essa palavra usando uma fonte diferente.
Dica: A função figlet_format aceita um parâmetro opcional chamado font. 
Tente usar font='slant' ou font='starwars'.
"""
import pyfiglet
try:
    palavra = str(input('Digite uma palavra: '))
    slant = pyfiglet.figlet_format(f"{palavra}", font='slant')
    print(slant)
    starwars = pyfiglet.figlet_format(f"{palavra}", font='starwars')
    print(starwars)
    
except:
    print("ocorreu um errinho ahahhaha")
