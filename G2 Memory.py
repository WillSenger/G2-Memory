import random
import time
from emojis import emojis
import os


def board_generation():
    list_01 = random.sample(range(0, 8), 8)
    list_02 = random.sample(range(0, 8), 8)
    result = []

    for i in range(0, 8):
        result.append(list_01[i])
        result.append(list_02[i])
    return result


def display_board(board, hidden_cards):
    for item, i in enumerate(board):
        if item in hidden_cards:
            print("?", end='\n' if (item + 1) % 4 == 0 else '\t')
        else:
            print(emojis[i], end='\n' if (item + 1) % 4 == 0 else '\t')
    time.sleep(8)

    os.system('cls')
    print('Numeração:')
    for i in range(16):
        print(i, end='\n' if (i + 1) % 4 == 0 else '\t')


def start_game():
    hits = []
    name = input("Digite seu nome: ")
    score = 1000
    board = board_generation()

    while len(hits) < 16:
        display_board(board, hits)
        print("Escolha uma carta:")
        try:
            card_1 = int(input("Digite o número da primeira carta: "))
            card_2 = int(input("Digite o número da segunda carta: "))

            if (
                    card_1 == card_2
                    or card_1 >= len(board)
                    or card_2 >= len(board)
                    or card_1 < 0
                    or card_2 < 0
                    or card_1 in hits
                    or card_2 in hits
            ):
                print("Cartas inválidas, tente novamente.")
                continue

            if board[card_1] == board[card_2]:
                print("Você acertou!")
                hits.extend([card_1, card_2])
            else:
                print("Você errou!")
                score -= 50

        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

        except IndexError:
            print("Carta inválida. Por favor, digite um número válido.")

    print("Você venceu, parabéns!")
    save_score(name, score)


def get_ranking_data():
    if not os.path.isfile("ranking.txt"):
        return
    with open("ranking.txt", "r") as file:
        content = file.read()
    lines = content.strip().splitlines()
    dictionary = {}
    for line in lines:
        key, value = line.split(': ')
        dictionary[key] = int(value)
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def save_score(name, score):
    ranking = get_ranking_data() or {}
    file = open("ranking.txt", "w")
    text = f"{name}: {score}\n"
    if len(ranking):
        for key in ranking:
            text = text + f"{key}: {ranking[key]}\n"
    file.write(text)


def ranking():
    ranking = get_ranking_data()
    if not len(ranking):
        print("O arquivo de ranking não existe.")
        return
    for key in ranking:
        print(f"{key}: {ranking[key]}")


def main():
    while True:
        print("Menu do Jogo da Memória :D")
        print("0. Sair")
        print("1. Iniciar")
        print("2. Ranking de jogadores")

        option = int(input("\nDigite a opção desejada: "))

        if option == 0:
            print("Saindo do programa...")
            break
        elif option == 1:
            start_game()
        elif option == 2:
            ranking()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


main()