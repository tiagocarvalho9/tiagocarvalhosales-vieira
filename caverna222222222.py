import random

persons = {
    'heroi':{
        'vida': 100,
        'ouro':100,
        'nome':"",
        'nivel':0,
        'inv' : {
            'espada':False,
            'escudo':False,
            'pocao': 2
        }
    }
}
print("-----------Bem vindo a caverna-----------\n")
print("qual e o seu nome\n")
persons['heroi']['nome'] = input()
print(f"bem vindo{persons['heroi']['nome']}\n")

def caminho():
    print (' \n')
    c = random.randint(1,2)
    if c == 1:
        o = random.randint(5,15)
        persons ['heroi']['ouro'] += o


def escolha():
    print ('escolha placeholder')
    print('𝟏: 𝐜𝐨𝐧𝐭𝐢𝐧𝐮𝐚𝐫 𝟐: 𝐟𝐮𝐠𝐢𝐫 𝟑: 𝐮𝐬𝐚𝐫 𝐩𝐨ca𝐨')
    esc = int(input("sua escolha"))

    if esc == 1:
        caminho()
        return 1
    elif esc == 2:
        return 2
    elif esc == 3:
        return 3
    else:
        print("𝐍𝐚𝐨 𝐩𝐨𝐝𝐞𝐫𝐚𝐬 𝐟𝐚𝐳𝐞𝐫 𝐞𝐬𝐭𝐚 𝐚𝐜𝐚𝐨")

def loja():
    print(f"voce tem"{persons['heroi']["ouro"]}"de ouro")
    return 'recurso'

def main():
    s =escolha()
    if s == 2:
        return 1
    else:
        return 0

while persons['heroi']['vida'] > 0:
    r = main()
    if r == 1:
        print(f"voce fugiu com{persons['heroi']['ouro']}")
        break

