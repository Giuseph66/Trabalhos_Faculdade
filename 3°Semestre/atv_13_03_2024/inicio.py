import os 

Notas=(os.path.join(os.path.dirname(__file__), "Notas.txt"))
Lista_nome=[]
if not os.path.exists(Notas):
    with open(Notas, "w") as a:
        a.write("---------------------------------------------------------------------------------------------\nNomes dos alunos: \n---------------------------------------------------------------------------------------------")
while True:
    nome=input("Nome do aluno?\n").upper()
    P_nota=input("P_nota do aluno?\n")
    S_nota=input("S_nota do aluno?\n")
    T_nota=input("T_nota do aluno?\n")
    with open(Notas, "r") as a:
        linhas = a.readlines()
        desejado=linhas[1].replace("Nomes dos alunos: ","").replace("\n","")
    if desejado!="":
        Lista_nome.append(desejado)
    Lista_nome.append(f" {nome}")
    conjunto = ','.join(map(str, Lista_nome))
    linhas[1] = f"Nomes dos alunos: {conjunto}\n" 
    with open(Notas, "w") as a:
        a.writelines(linhas)
    with open(Notas, "a") as a:
        a.write(f"\nNome: {nome}\nPrimeira nota :{P_nota}\nSegunda nota :{S_nota}\nTerceira nota :{T_nota}\n---------------------------------------------------------------------------------------------")
    Lista_nome=[]   
    if input("Deseja lançar novamente?(0=sim||1=nao)\n")!="0":
        break