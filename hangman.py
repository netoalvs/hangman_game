import random  # Importa o módulo random para gerar números aleatórios

def escolher_palavra():
    # Função para escolher uma palavra aleatória da lista
    palavras = ["python", "programacao", "computador", "desenvolvimento", "algoritmo", "tecnologia", "java", "notebook", "suporte", "wifi", "internet"]
    return random.choice(palavras)

def jogar_forca(palavra):
    # Função principal do jogo da Forca
    letras_certas = []
    tentativas = 10
    
    while True:
        # Mostra o estado atual da palavra com letras adivinhadas
        palavra_atual = ""
        for letra in palavra:
            if letra in letras_certas:
                palavra_atual += letra
            else:
                palavra_atual += "_"
        print(palavra_atual)
        
        # Solicita uma letra ao jogador
        letra = input("Digite uma letra: ")
        
        # Verifica se a letra já foi adivinhada
        if letra in letras_certas:
            print("Você já adivinhou essa letra.")
            continue
        
        # Verifica se a letra está na palavra
        if letra in palavra:
            letras_certas.append(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.")
        
        # Verifica se o jogador ganhou ou perdeu
        if "_" not in palavra_atual:
            print(f"Parabéns, você ganhou! A palavra era '{palavra}'.")
            break
        elif tentativas == 0:
            print(f"Você perdeu! A palavra era '{palavra}'.")
            break

def main():
    print("Bem-vindo ao Jogo da Forca!")
    
    palavra = escolher_palavra()  # Escolhe uma palavra aleatória
    jogar_forca(palavra)  # Inicia o jogo da Forca

if __name__ == "__main__":
    main()  # Chama a função principal do jogo
