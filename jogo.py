import random

def jogar_forca():
    palavras = ['luzia', 'brasil', 'programacao', 'desafio', 'computador']
    palavra = random.choice(palavras)
    letras_descobertas = ['_'] * len(palavra)
    tentativas = 6
    letras_usadas = []

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0 and '_' in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        
        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_usadas:
            print("Você já tentou essa letra!")
            continue
        
        letras_usadas.append(palpite)

        if palpite in palavra:
            for i in range(len(palavra)):
                if palavra[i] == palpite:
                    letras_descobertas[i] = palpite
        else:
            tentativas -= 1
            print("Ops, essa letra não está na palavra.")

    if '_' not in letras_descobertas:
        print(f"\nParabéns! Você venceu! A palavra era: {palavra}")
    else:
        print(f"\nGame Over! A palavra era: {palavra}")

jogar_forca()
