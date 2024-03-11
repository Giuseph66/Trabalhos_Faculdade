while True:
    try:
        numero=int(input("Digite um numero ...\n"))
        if numero % 2 ==0:
            print("par")
        else:
            print("impar")
        if not (input("Deseja ir Dnv? (0==sim , 0!=nao)\n"))=="0":
            break
    except:
        print("Digite apenas numeros inteiros...\n")