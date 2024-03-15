cnt_linhas,acho,situacao,Lista_nome=0,False,None,[]

print("Qual o nome do estudante ?")
with open("Notas.txt", "r") as a:
    linhas = a.readlines()
    desejado=linhas[1].replace("Nomes dos alunos: ","").replace("\n","").replace(",","\n").replace(" ","")
    print(f"{desejado}\nTodos")
nome_busca=input("Escreva exatamente o nome do estudante para descobrir suas notas ...\n").upper()
if nome_busca == "TODOS":
    conver=desejado.split("\n")
    with open("Aprovados.txt", "w") as a:
         a.write("---------------------------------------------------------------------------------------------\nNomes dos alunos: \n---------------------------------------------------------------------------------------------")
    with open("Exame.txt", "w") as a:
         a.write("---------------------------------------------------------------------------------------------\nNomes dos alunos: \n---------------------------------------------------------------------------------------------")
    for nome in conver:
        for linha in linhas:
            cnt_linhas+=1
            if f"Nome: {nome}\n" == linha:
                pri=float(linhas[cnt_linhas].replace("Primeira nota :","").replace("\n","").replace(" ",""))
                seg=float(linhas[cnt_linhas+1].replace("Segunda nota :","").replace("\n","").replace(" ",""))
                ter=float(linhas[cnt_linhas+2].replace("Terceira nota :","").replace("\n","").replace(" ",""))
                media=(pri+seg+ter)/3

                if media>=7:
                    situacao="Aprovado"
                    with open("Aprovados.txt", "r") as a:
                        linhas_e = a.readlines()
                        desejado=linhas_e[1].replace("Nomes dos alunos: ","").replace("\n","")
                    if desejado!="":
                        Lista_nome.append(desejado)
                    Lista_nome.append(f" {nome}")
                    conjunto = ','.join(map(str, Lista_nome))
                    linhas_e[1] = f"Nomes dos alunos: {conjunto}\n" 
                    Lista_nome=[]
                    with open("Aprovados.txt", "w") as a:
                        a.writelines(linhas_e)
                    with open("Aprovados.txt", "a") as a:
                        a.write(f"\n---------------------------------------------------------------------------------------------\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media passa :{media:.2f}")
                else:
                    situacao="Exame"
                    with open("Exame.txt", "r") as a:
                        linhas_e = a.readlines()
                        desejado=linhas_e[1].replace("Nomes dos alunos: ","").replace("\n","")
                    if desejado!="":
                        Lista_nome.append(desejado)
                    Lista_nome.append(f" {nome}")
                    conjunto = ','.join(map(str, Lista_nome))
                    linhas_e[1] = f"Nomes dos alunos: {conjunto}\n" 
                    Lista_nome=[]
                    with open("Exame.txt", "w") as a:
                        a.writelines(linhas_e)
                    with open("Exame.txt", "a") as a:
                        a.write(f"\n---------------------------------------------------------------------------------------------\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media :{media:.2f}")
                print(f"\nAchei...\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media :{media:.2f}\nSituação :{situacao}")
                acho,cnt_linhas=True,0
                break
else:
    for linha in linhas:
        cnt_linhas+=1
        if f"Nome: {nome_busca}\n" == linha:
            pri=float(linhas[cnt_linhas].replace("Primeira nota :","").replace("\n","").replace(" ",""))
            seg=float(linhas[cnt_linhas+1].replace("Segunda nota :","").replace("\n","").replace(" ",""))
            ter=float(linhas[cnt_linhas+2].replace("Terceira nota :","").replace("\n","").replace(" ",""))
            media=(pri+seg+ter)/3
            if media>7:
                situacao="Aprovado"
            elif media<7:
                situacao="Exame"
            print(f"\nAchei...\n{nome_busca}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media :{media:.2f}\nSituação :{situacao}")
            acho,cnt_linhas=True,0
            break
if not acho:
    print("Estudante nao encontrado...")
    cnt_linhas=0