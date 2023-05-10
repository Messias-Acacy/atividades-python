from random import choice
def palito (numero):
    match numero:
        case 6:
            print('')
        case 5:
            print("""
             ____
            |   |
            |   0
            |      
            |     """)
        case 4:
            print("""
             ____
            |   |
            |   0
            |   |   
            |     """)
        case 3:
            print("""
             ____
            |   |
            |   0
            |  /|   
            |     """)
        case 2:
             print("""
             ____
            |   |
            |   0
            |  /|\  
            |     """)
        case 1:
              print("""
             ____
            |   |
            |   0
            |  /|\  
            |    \  """)
        case 0:
            print("""
             ____
            |   |
            |   0
            |  /|\  
            |  / \  """)
def vitoria(numero2):
    print("""
 _______
(|     |)
  \   /
   \ /
   === 
    """)


palavras = ['sapato','cronologia','paralelepipedo','Fahrenheit','ministro']
texto = choice(palavras)
resultado = []
chances = 6
confirm = ''
palavra = ''

print('Bem-vindo ao jogo da forca!')
print()
for y in range(len(texto)):
    resultado.append('_')
    print(resultado[y], end = ' ')
print()
print("""
             ____
            |   |
            |   
            |      
            |     """)

print()
while True:
    print(f'Você tem {chances} Chances!')
    letra = input('digite a letra aqui: ').lower()
    for x in range(len(texto)):
        if letra == texto[x]:
            del resultado[x]
            resultado.insert(x,letra)
            print(resultado[x], end = ' ')
        else:
            print(resultado[x], end = ' ')
    if letra not in texto:
        chances = chances - 1
        palito(chances)
    else:
        palito(chances)

    if chances == 0:
        print('Você perdeu!')
        break
    if chances > 0:
        confirm= input('Quer responder? Digite SIM/NÃO: ')
        if confirm in "SIMsim":
            palavra = input('digite a palavra: ')
            if palavra == texto:
                print()
                print('parabéns! você venceu!')
                vitoria(0)
                break
            else:
                print('você perdeu!')
                break

