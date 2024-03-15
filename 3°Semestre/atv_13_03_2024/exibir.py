cnt_linhas,acho,Lista_nome=0,False,[]
with open("Aprovados.txt", "r") as f:
    linhas = f.readlines()
    desejado=linhas[1].replace("Nomes dos alunos: ","").replace("\n","").replace(",","\n").replace(" ","")
    conver=desejado.split("\n")
    print("\nAprovados...")
    for nome in conver:
        for linha in linhas:
            cnt_linhas+=1
            if f"{nome}\n" == linha:
                Nota=float(linhas[cnt_linhas+3].replace("Media passa :","").replace("\n","").replace(" ",""))
                print(f"{nome} passou com a nota {Nota}")
                acho,cnt_linhas=True,0
                break
with open("Reprovados.txt", "r") as f:
    linhas = f.readlines()
    desejado=linhas[1].replace("Nomes dos alunos: ","").replace("\n","").replace(",","\n").replace(" ","")
    conver=desejado.split("\n")
    print("\nReprovados...")
    for nome in conver:
        for linha in linhas:
            cnt_linhas+=1
            if f"{nome}\n" == linha:
                print(f"{nome} infelizmente reprovou...")
                acho,cnt_linhas=True,0
                break