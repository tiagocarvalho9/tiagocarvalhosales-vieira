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
        }
    }
}

print("-----------Bem vindo a caverna-----------")
persons ['heroi']['nome']("qual é o teu nome \n")
print(f'olá viajante' persons ['heroi']['nome'])

while vida > 0:

    escolha = input("1 entrar na caverna\n2 ir para o norte\n")
    if escolha == '1':
        print(f {persons ['heroi']['nome']} 'avança na caverna)
        caminho == 1
        caminho = random.randint(1,2)
        print(f'voce esta com {ouro}de ouro')

    elif escolha == '2':
        print(f"{persons ['heroi']['nome']} foge com segurança")
    else:
        print("açao invalida")
