while True:
    pala=str(input("Digite um palavra com somente letras maiúsculas...\n"))
    try:
        test=float(pala)
        print("Digite apenas letras...\n")
        continue
    except :
        pass
    if not pala.isupper():
        print("Contem letras minúsculas")
    else:
        print("Contem somnete letras maiúsculas")
    if not (input("Deseja ir Dnv? (0==sim , 0!=nao)\n"))=="0":
        break

