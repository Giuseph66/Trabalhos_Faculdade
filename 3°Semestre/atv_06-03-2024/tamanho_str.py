while True:
    pri=(input("Digite uma palavra que sera comparada o tamanho...\n"))
    seg=(input("Digite a segunda palavra\n"))
    try:
        test=int(pri)
        test=int(seg)
        print("Digite apenas letras...\n")
        continue
    except:
        pass
    pri_tam,seg_tam=len(str(pri)),len(str(seg))
    if pri_tam==seg_tam:
        print("Palavras com o mesmo tamanho !")
    else:
        print("Palavras de tamanho diferentes !")

    if not (input("Deseja ir Dnv? (0==sim , 0!=nao)\n"))=="0":
        break




