import random

def jogar():

    boas_vindas_ao_jogo()

    numero_secreto = random.randrange(1,101)
    pontos = 1000

    total_de_tentativas = dificuldade_escolhida()

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = chute_do_jogador()

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
    print("Fim do jogo")

def boas_vindas_ao_jogo():

    print("Bem Vindo(a) ao Jogo de Adivinhação!!\n")

def dificuldade_escolhida():

    print("Temos 3 graus de dificuldade para este jogo: Facíl, Médio e Díficl, a única diferença entre elas é o número de tentativas.")
    infos_da_dificuldade = input("Se deseja saber o número de tentativas de cada dificuldade digite: sim\n")

    if infos_da_dificuldade == "sim":
        print("Fácil = 20 tentativas\nMédio = 10 tentativas\nDíficil = 5 tentativas\n")

    print("Qual o nível de dificuldade deseja?")
    print("(1) Fácil (2) Médio (3) Difícil\n")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    return total_de_tentativas

def chute_do_jogador():

    chute = int(input("Digite um número entre 1 e 100: "))
    print("Você digitou:", chute)
    return chute

if (__name__ == "__main__"):
    jogar()

#mensagens de parabens e perdeu
#numero secreto no final caso perca