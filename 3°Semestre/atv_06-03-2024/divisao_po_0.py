while True:
    pri=(input("Digite um numero que sera dividido...\n"))
    seg=(input("Digite o segundo numero\n"))
    try:
        test=int(pri)
        test=int(seg)
        pass
    except:
        print("Digite apenas numeros inteiros...\n")
        continue
    try:
        print(f"Resultado da divisao: {int(pri)/int(seg)}")
    except ZeroDivisionError:
        print("Não é possivel se dividir por zero...\n ")

    if not (input("Deseja ir Dnv? (0==sim , 0!=nao)\n"))=="0":
        break


