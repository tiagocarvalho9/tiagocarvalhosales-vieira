alunos=["Eduardo", "Paulo", "Rafael", "Tiago", "Pedro"]
for A in alunos:
    aluno=alunos[A]
    print(f"o aluno{aluno}esta presente?\n")
    presencas.append(int(input("1 - Sim| 2-nao\n")))
    presencas.append(presenca)

print("====================================\n")
print("lista de presenca\n")

A=0
for B in presencas:
    if B == 1:
        print(f"aluno{alunos[A]}esta presente")
    else:
        print(f"aluno{alunos[A]}faltou")
