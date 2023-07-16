import random
import os

os.system("cls")
print("-" * 30)
print("BEM-VINDO AO JOGO DO VIRCS")
print("-" * 30)

def perguntar():
    pergunta = input("Você deseja começar o jogo? (sim/nao): ")
    while pergunta != "sim" and pergunta != "nao":
        print("Opção inválida. Por favor, escolha 'sim' ou 'nao'.")
        pergunta = input("Você deseja começar o jogo? (sim/nao): ")
    return pergunta

def jogar_jogo():
    escolha2 = input("Escolha uma dificuldade (easy, medium, hard): ")
    if escolha2 == "easy":
        print("Escolheu a dificuldade mais fácil? Kakaka tu é uma piada.")
    elif escolha2 == "medium":
        print("Você escolheu o nível padrão do jogo. Boa sorte.")
    elif escolha2 == "hard":
        print("Temos um corajoso então.")

    if escolha2 == "easy":
        escolha = int(input("Escolha um número (0-3): "))
        computador = random.randint(0, 3)
        if escolha == computador:
            print(f"Eu escolhi {computador} e você {escolha}. Você acertou o número.")
        else:
            print(f"Eu escolhi {computador} e você {escolha}. Meu conselho é você não tentar outra vez.")
    elif escolha2 == "medium":
        escolha = int(input("Escolha um número (0-6): "))
        computador = random.randint(0, 6)
        if escolha == computador:
            print(f"Eu escolhi {computador} e você {escolha}. Você acertou o número.")
        else:
            print(f"Eu escolhi {computador} e você {escolha}. Meu conselho é abaixar a dificuldade.")
    elif escolha2 == "hard":
        escolha = int(input("Escolha um número (0-10): "))
        computador = random.randint(0, 10)
        if escolha == computador:
            print(f"Eu escolhi {computador} e você {escolha}. Você acertou o número.")
        else:
            print(f"Eu escolhi {computador} e você {escolha}. Volte para uma dificuldade ao seu alcance.")

pergunta = perguntar()

if pergunta == "sim":
    jogar_jogo()
elif pergunta == "nao":
    print("CAGAOOOOO...")