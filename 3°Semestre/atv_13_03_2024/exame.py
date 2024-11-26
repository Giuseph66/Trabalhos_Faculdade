import os
cnt_linhas,acho,Lista_nome=0,False,[]
Exame=(os.path.join(os.path.dirname(__file__), "Exame.txt"))
Reprovados=(os.path.join(os.path.dirname(__file__), "Reprovados.txt"))
Aprovados=(os.path.join(os.path.dirname(__file__), "Aprovados.txt"))
        
print("Qual o nome do estudante ?")
with open(Exame, "r") as f:
    linhas = f.readlines()
    desejado=linhas[1].replace("Nomes dos alunos: ","").replace("\n","").replace(",","\n").replace(" ","")
    print(f"{desejado}\nTodos")
nome_busca=input("Escreva exatamente o nome do estudante ...\n").upper()
if nome_busca == "TODOS":
    conver=desejado.split("\n")
    with open(Reprovados, "w") as a:
        a.write("---------------------------------------------------------------------------------------------\nNomes dos alunos: \n---------------------------------------------------------------------------------------------")
    for nome in conver:
        for linha in linhas:
            cnt_linhas+=1
            if f"{nome}\n" == linha:
                pri=float(linhas[cnt_linhas].replace("Primeira nota :","").replace("\n","").replace(" ",""))
                seg=float(linhas[cnt_linhas+1].replace("Segunda nota :","").replace("\n","").replace(" ",""))
                ter=float(linhas[cnt_linhas+2].replace("Terceira nota :","").replace("\n","").replace(" ",""))
                media=(pri+seg+ter)/3
                min_nota=(5*2)-media
                seg_nota=float(input(f"Qual a nota  do exame ?(...{nome}...)(Nota minima: {min_nota:.2f})\n"))
                media_media=(media+seg_nota)/2
                if media_media>=5:
                    situacao="Aprovado"
                    with open(Aprovados, "r") as a:
                        linhas_e = a.readlines()
                        desejado=linhas_e[1].replace("Nomes dos alunos: ","").replace("\n","")
                    if desejado!="":
                        Lista_nome.append(desejado)
                    Lista_nome.append(f" {nome}")
                    conjunto = ','.join(map(str, Lista_nome))
                    linhas_e[1] = f"Nomes dos alunos: {conjunto}\n" 
                    Lista_nome=[]
                    with open(Aprovados, "w") as a:
                        a.writelines(linhas_e)
                    print(f"\nAchei...\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media anterior :{media:.2f}\nMedia da media :{media_media:.2f}\nParabens, voce passou!!!")
                    with open(Aprovados, "a") as a:
                        a.write(f"\n---------------------------------------------------------------------------------------------\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media passa :{media_media:.2f}\nMedia anterior :{media:.2f}\nObs: Passou com exame!")
                else:
                    situacao="Reprovado"
                    with open(Reprovados, "r") as a:
                        linhas_e = a.readlines()
                        desejado=linhas_e[1].replace("Nomes dos alunos: ","").replace("\n","")
                    if desejado!="":
                        Lista_nome.append(desejado)
                    Lista_nome.append(f" {nome}")
                    conjunto = ','.join(map(str, Lista_nome))
                    linhas_e[1] = f"Nomes dos alunos: {conjunto}\n" 
                    Lista_nome=[]
                    with open(Reprovados, "w") as a:
                        a.writelines(linhas_e)
                    print(f"\nAchei...\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media anterior :{media:.2f}\nMedia da media :{media_media:.2f}\nLamento mas voce esta reprovado")
                    with open(Reprovados, "a") as a:
                        a.write(f"\n---------------------------------------------------------------------------------------------\n{nome}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media :{media:.2f}\nMedia da media :{media_media:.2f}")
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
            seg_nota=input("Qual a nota  do exame ?")
            media_media=(media+float(seg_nota)/2)
            if media_media>5:
                situacao="Aprovado"
                print(f"\nAchei...\n{nome_busca}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media da media :{media_media:.2f}\nParabens, voce passou!!!")
            else:
                situacao="Reprovado"
                print(f"\nAchei...\n{nome_busca}\n{linhas[cnt_linhas]}{linhas[cnt_linhas+1]}{linhas[cnt_linhas+2]}Media da media :{media_media:.2f}\nLamento mas voce esta reprovado")
            acho,cnt_linhas=True,0
            break
if not acho:
    print("Estudante nao encontrado...")
    cnt_linhas=0