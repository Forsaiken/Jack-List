import random
import names

class IA():
    def __init__(self, id, name, money):
        self.n = name
        self.m = money
        self.id = id


class card():
    def __init__(self, simbolo, naipe, valor, image):
        self.s = simbolo
        self.n = naipe
        self.v = valor
        self.img = image


class player():
    def __init__(self, name, money):
        self.n = name
        self.m = money


class data:
    def save(self, money):

        data = open("data.flr", 'w+')
        data.write(money)

    def load(self):

        try:
            data = open("data.flr", 'r+')
            money = data.readlines()
            return money
        except FileNotFoundError:
            arquivo = open("data.flr", 'w+')
            arquivo.writelines('5')
            return 5


def create_deck_blackjack():
    '''Return list with objects (Deck in BlackJack)'''

    deck = []
    contador = 11

    while contador >= 11 and contador <= 134:

        scan = len(str(contador))
        atual = "C" + str(contador)
        deck.append(atual)

        if scan == 3:

            if str(contador)[2] == "4":

                contador += 7

            else:

                contador += 1

        else:

            if str(contador)[1] == "4":

                contador += 7

            else:

                contador += 1

    for item in range(len(deck)):

        if len(str(deck[item])) == 3:

            if int(str(deck[item][1])) == 1:

                deck[item] = card("A", naipe(deck[item]), int(str(deck[item][1])), 'images/{}'.format(deck[item]))

            else:

                deck[item] = card(str(deck[item][1]), naipe(deck[item]), int(str(deck[item][1])),
                                  'images/{}'.format(deck[item]))

            print("Objeto", deck[item], "(", deck[item].s, deck[item].n, deck[item].v, deck[item].img, ") foi criado.")

        else:

            if int(str(deck[item][1] + deck[item][2])) == 10:

                deck[item] = card("10", naipe(deck[item]), 10, 'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 11:

                deck[item] = card("J", naipe(deck[item]), 10, 'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 12:

                deck[item] = card("Q", naipe(deck[item]), 10, 'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 13:

                deck[item] = card("K", naipe(deck[item]), 10, 'images/{}'.format(deck[item]))

            print("Objeto", deck[item], "(", deck[item].s, deck[item].n, deck[item].v, ") foi criado.")

    return deck


def create_deck_truco():
    '''Return list with objects (Deck in Truco)'''

    deck = []
    contador = 41

    while contador >= 41 and contador <= 134:

        scan = len(str(contador))
        atual = "C" + str(contador)
        deck.append(atual)

        if scan == 3:

            if str(contador)[2] == "4":

                contador += 7

            else:

                contador += 1

        else:

            if str(contador)[1] == "4":

                contador += 7

            else:

                contador += 1

    for item in range(len(deck)):

        if len(str(deck[item])) == 3:

            if int(str(deck[item][1])) == 8:

                deck[item] = card("Q", naipe(deck[item]), int(str(deck[item][1])), 'images/{}'.format(deck[item]))

            elif int(str(deck[item][1])) == 9:

                deck[item] = card("J", naipe(deck[item]), int(str(deck[item][1])), 'images/{}'.format(deck[item]))

            else:

                deck[item] = card(str(deck[item][1]), naipe(deck[item]), int(str(deck[item][1])),
                                  'images/{}'.format(deck[item]))

            print("Objeto", deck[item], "(", deck[item].s, deck[item].n, deck[item].v, deck[item].img, ") foi criado.")

        else:

            if int(str(deck[item][1] + deck[item][2])) == 10:

                deck[item] = card("K", naipe(deck[item]), int(str(deck[item][1] + deck[item][2])),
                                  'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 11:

                deck[item] = card("A", naipe(deck[item]), int(str(deck[item][1] + deck[item][2])),
                                  'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 12:

                deck[item] = card("2", naipe(deck[item]), int(str(deck[item][1] + deck[item][2])),
                                  'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 13:

                deck[item] = card("3", naipe(deck[item]), int(str(deck[item][1] + deck[item][2])),
                                  'images/{}'.format(deck[item]))

            print("Objeto", deck[item], "(", deck[item].s, deck[item].n, deck[item].v, ") foi criado.")

    return deck


def shuffle_deck(deck):
    random.shuffle(deck, random.random)
    print(deck[0].v)
    return deck


def naipe(objeto):
    objeto = int(str(objeto[-1]))

    if objeto == 1:
        return "♦"
    elif objeto == 2:
        return "♠"
    elif objeto == 3:
        return "♥"
    elif objeto == 4:
        return "♣"


def create_IA(players):
    '''create_IA(INT - Number of Players (MAX 10)'''

    if type(players) != int or players < 1 or players > 99: return False

    players_list = []

    for i in range(players):
        players = players + 1
        money = random.randint(30, 100) * 100
        # name = "P" + str(random.randint(30, 100) * 100)
        name = names.get_full_name()

        objeto = IA(i, name, money)
        print("Objeto", objeto, "(", i, objeto.n, objeto.m, ") criado com sucesso.")

        players_list.append(objeto)

    return players_list


def main_title():
    print("Bem Vindo ao Black Jack Grand Prix\n \n1 - Novo Jogo\n2 - Continuar\n3 - Sair\n")
    choice = input("Qual opção deseja?")

    if int(choice) == 1:
        new_game()
    elif int(choice) == 2:
        data = data()
        data.load()
    else:
        exit()


def new_game():
    print("\nEscolha uma das opções abaixo:\n")
    print("1 - Modo Carreira")
    print("2 - Modo Partida")
    print("3 - Voltar\n")
    choice = input("Qual opção deseja?")

    if int(choice) == 1:
        carrer_mode()
    elif int(choice) == 2:
        match_mode()
    elif int(choice) == 3:
        main_title()


def carrer_mode():
    name = input("\nQual o nome do seu jogador?")
    p = player(name, 500)
    IA = create_IA(99)


def match_mode():
    print("\nEscolha uma das opções abaixo:\n")

    print("1 - Black Jack")
    print("2 - Truco")
    print("3 - Voltar\n")

    choice = input("Qual opção deseja?")

    if int(choice) == 1:

        players = input("Quantos jogadores deseja nessa partida de Black Jack?")
        IA = create_IA(int(players) - 1)
        player = ("Player", 500)
        blackjack(player, IA)

    elif int(choice) == 2:

        players = input("Quantos jogadores deseja nessa partida de Truco?")
        IA = create_IA(int(players) - 1)
        player = ("Player", 500)
        truco(None, IA)

    elif int(choice) == 3:
        new_game()


def blackjack(player, IA):
    IA_winner = False
    Player_winner = False
    soma = 0
    ia_soma = 0

    # Quem começa?

    player_turn = False
    player_dado = 0
    ia_dado = 0

    dado1 = roll_dice()
    dado2 = roll_dice()

    print("Você jogou os dados e os valores foram", dado1, "e", dado2, "total de", dado1 + dado2)

    player_dado = dado1 + dado2

    dado1 = roll_dice()
    dado2 = roll_dice()

    print(IA.n, "jogou os dados e os valores foram", dado1, "e", dado2, "total de", dado1 + dado2)

    ia_dado = dado1 + dado2

    if player_dado > ia_dado:

        player_turn = True

    else:

        player_turn = False

    # Create Deck and Hand

    deck = create_deck_blackjack()
    shuffle_deck(deck)
    player_hand = []
    ia_hand = []
    player_finish = False
    ia_finish = False

    # Game Begins

    while IA_winner == False and Player_winner == False:

        if player_turn == True and player_finish == False:

            # Draw Phase

            deck_size = len(deck)
            index = random.randint(0, deck_size - 1)
            player_hand.append(deck[index])
            del deck[index]

            print("Você sacou a carta (", player_hand[-1].s, player_hand[-1].n, ")")

            # Show Hand

            soma = soma_hand(player_hand)
            print(show_hand(player_hand), "e o valor total dela é:", soma_hand(player_hand), "\n")

            # Decisions

            if soma >= 21:

                player_finish = True

            else:

                print("1 - Continuar\n2 - Finalizar\n")
                decision = input("Qual opção deseja?")

                if int(decision) == 2:
                    player_finish = True

        player_turn = False

        if player_turn == False and ia_finish == False:

            # Draw Phase

            deck_size = len(deck)
            index = random.randint(0, deck_size - 1)
            ia_hand.append(deck[index])
            del deck[index]

            # Decisions

            ia_soma = soma_hand(ia_hand)

            if ia_soma >= 18:
                ia_finish = True

        player_turn = True

        if player_finish == True and ia_finish == True:

            print("Você fez", soma, "e", IA.n, "fez", ia_soma)

            if soma == ia_soma:

                print("Empatou! Disputem novamente.")
                blackjack(player, IA)

            elif soma <= 21 and ia_soma <= 21:

                if soma > ia_soma:

                    print("Você ganhou!")
                    Player_winner = True

                else:

                    print("Você perdeu!")
                    IA_winner = True

            elif soma > 21 and ia_soma > 21:

                if soma < ia_soma:

                    print("Você ganhou!")
                    Player_winner = True

                else:

                    print("Você perdeu!")
                    IA_winner = True

            elif soma <= 21 and ia_soma > 21:

                print("Você ganhou!")
                Player_winner = True

            else:

                print("Você perdeu!")
                IA_winner = True

    if Player_winner == True:

        return 0

    else:

        return 1


def truco(player, IA):
    # Método para criar jogador IA caso o número de jogadores seja impar.

    if player == None:
        quantidade_players = len(IA)
    else:
        quantidade_players = len(IA) + 1

    if quantidade_players % 2 != 0:
        new_player = create_IA(1)
        IA.append(new_player)

    if quantidade_players == 2:
        times = [["P1"], ["P2"]]
    elif quantidade_players == 4:
        times = [["P1", "P3"], ["P2", "P4"]]
    elif quantidade_players == 6:
        times = [["P1", "P3", "P5"], ["P2", "P4", "P6"]]

    ready_team = False
    players_to_composition = IA[:]

    # Caso exista jogador ele irá junta-lo para definir os times.

    if player != None:
        players_to_composition.append(player)

    while ready_team == False:

        dados = []

        for item in players_to_composition:
            valor = roll_dice()
            print(item.n, "tirou", valor, "no dado")
            dados.append(valor)

        array_dados = len(dados)
        contador = 0
        escolhido = -1

        for i in range(array_dados):
            contador = 0
            for x in range(array_dados - 1):
                print("Comparando", dados[i], "com", dados[x + 1])
                if dados[i] == dados[x+1] and i != x+1:
                    contador += 1
                    if len(players_to_composition) == 6 and escolhido >= 0:
                        escolhido2 = x + 1
                    else:
                        escolhido = x + 1

            if contador == 1 and len(players_to_composition) == 4:
                print(players_to_composition[i].n, "fara dupla com", players_to_composition[escolhido].n)
                times[0][0] = players_to_composition[i]
                times[0][1] = players_to_composition[escolhido]
                del players_to_composition[escolhido]
                del players_to_composition[i]
                times[1][0] = players_to_composition[0]
                times[1][1] = players_to_composition[1]
                ready_team = True
                break

            elif contador == 2 and len(players_to_composition) == 6:
                print(players_to_composition[i].n, "fara trio com", players_to_composition[escolhido].n, "e"
                ,players_to_composition[escolhido2].n)
                times[0][0] = players_to_composition[i]
                times[0][1] = players_to_composition[escolhido]
                times[0][2] = players_to_composition[escolhido2]
                del players_to_composition[escolhido2]
                del players_to_composition[escolhido]
                del players_to_composition[i]
                times[1][0] = players_to_composition[0]
                times[1][1] = players_to_composition[1]
                times[1][2] = players_to_composition[2]
                ready_team = True
                for item in times:
                    for i in item:
                        print(i.n)
                break

def show_hand(hand):
    Mão = "Sua mão atual é ("

    for item in hand:
        carta = item.s + " " + item.n + ", "
        Mão = Mão + carta

    Mão = Mão + ")"

    return Mão


def soma_hand(hand):
    soma = 0

    for item in hand:
        soma = soma + item.v

    return soma


def roll_dice():
    dado = random.randint(1, 6)
    return dado


def vez_jogador():
    pass


def vez_IA():
    pass


main_title()

