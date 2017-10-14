import random
import names

class IA():
    def __init__(self, id, name, money, hand):
        self.n = name
        self.m = money
        self.id = id
        self.h = hand


class card():
    def __init__(self, simbolo, naipe, valor, image):
        self.s = simbolo
        self.n = naipe
        self.v = valor
        self.img = image


class player():
    def __init__(self, name, money, hand):
        self.n = name
        self.m = money
        self.h = hand


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

                deck[item] = card("Q", naipe(deck[item]), int(str(deck[item][1] + deck[item][2])), 'images/{}'.format(deck[item]))

            elif int(str(deck[item][1])) == 9:

                deck[item] = card("J", naipe(deck[item]), int(str(deck[item][1] + deck[item][2])), 'images/{}'.format(deck[item]))

            else:

                deck[item] = card(str(deck[item][1]), naipe(deck[item]), int(str(deck[item][1] + deck[item][2])),
                                  'images/{}'.format(deck[item]))

            #print("Objeto", deck[item], "(", deck[item].s, deck[item].n, deck[item].v, deck[item].img, ") foi criado.")

        else:

            if int(str(deck[item][1] + deck[item][2])) == 10:

                deck[item] = card("K", naipe(deck[item]), int(str(deck[item][1] + deck[item][2] + deck[item][3])),
                                  'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 11:

                deck[item] = card("A", naipe(deck[item]), int(str(deck[item][1] + deck[item][2] + deck[item][3])),
                                  'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 12:

                deck[item] = card("2", naipe(deck[item]), int(str(deck[item][1] + deck[item][2] + deck[item][3])),
                                  'images/{}'.format(deck[item]))

            elif int(str(deck[item][1] + deck[item][2])) == 13:

                deck[item] = card("3", naipe(deck[item]), int(str(deck[item][1] + deck[item][2] + deck[item][3])),
                                  'images/{}'.format(deck[item]))

            #print("Objeto", deck[item], "(", deck[item].s, deck[item].n, deck[item].v, ") foi criado.")

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

        objeto = IA(i, name, money, [])
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
    p = player(name, 500, [])
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
        id_player = ""
    else:
        quantidade_players = len(IA) + 1
        id_player = player.n

    if quantidade_players % 2 != 0:
        new_player = create_IA(1)
        IA.append(new_player)

    # Passando Jogadores para uma nova lista para formar times

    players_to_composition = IA[:]

    # Caso exista jogador ele irá junta-lo para definir os times.

    if player != None:
        players_to_composition.append(player)

    teams = make_teams(players_to_composition)

    ''' Truco é o pedido de "aumento de aposta". A rodada que normalmente vale 1 ponto passa a valer 3.
        Quando um jogador Truca outro jogador, este pode aceitar o Truco e rodada passa a valer 3 pontos,
        pode fugir, interrompendo a rodada e perdendo 1 ponto, ou pode pedir Seis, elevando o valor da
        aposta para 6 pontos.

        Da mesma maneira quando é pedido o Seis, as respostas podem ser aceitar, fugir or pedir Nove.
        Isso pode continuar até alguém pedir Doze onde as respostas somente podem ser aceitar ou fugir (não existe um
        Quinze já que a partida vai até 12 pontos).
        O jogador, dupla ou trio que pediu Truco não pode pedir Seis, essa regra igualmente vale para o Seis e Nove. '''

    team_points = [[0],[0]]

    while team_points[0][0] <= 11 or team_points[1][0] <= 11:

        # Criando Deck do Truco

        deck = create_deck_truco()
        shuffle_deck(deck)

        # Definindo carta Vira

        deck_size = len(deck)
        vira = deck[0]
        del deck[0]
        print("A carta vira é:", vira.s, vira.n, ")(Valor:", vira.v, ")")

        # Modificando os valores das cartas do deck conforme a Manilha

        deck = manilha(deck, vira)

        # Distribuindo cartas para a mãos dos jogadores

        for team in teams:
            for player in team:
                player.h = []

        for team in teams:
            for player in team:
                for i in range(3):
                    deck_size = len(deck)
                    pegar = random.randint(0, deck_size - 1)
                    player.h.append(deck[pegar])
                    del deck[pegar]

                    print(player.n,"sacou a carta", player.h[-1].s, player.h[-1].n, ")(Valor:",player.h[-1].v,")")

        match_points = [[0],[0]]

        while match_points[0][0] < 2 and match_points[1][0] < 2:

            card_to_beat = []

            for player_team in range(int(quantidade_players/2)):
                for team in range(2):

                    this_player = teams[team][player_team]

                    if this_player.n != id_player:

                        if card_to_beat == []:

                            pick = random.randint(0,len(this_player.h) - 1)
                            card_to_beat = [this_player.h[pick], team, this_player]
                            print(this_player.n, "jogou a carta (", this_player.h[pick].s, this_player.h[pick].n, ") e começou a rodada.")
                            del this_player.h[pick]

                        elif card_to_beat[1] != team:

                            right_card = -10

                            for card in range(len(this_player.h)):

                                if this_player.h[card].v > card_to_beat[0].v and right_card == -10:
                                    right_card = card
                                elif this_player.h[card].v < card_to_beat[0].v and right_card == -10:
                                    right_card = card
                                elif this_player.h[card].v > card_to_beat[0].v and this_player.h[card].v < this_player.h[right_card].v:
                                    right_card = card
                                elif this_player.h[card].v < this_player.h[right_card].v and this_player.h[right_card].v < card_to_beat[0].v:
                                    right_card = card

                            if this_player.h[right_card].v > card_to_beat[0].v:

                                print(this_player.n, "jogou a carta (", this_player.h[right_card].s,
                                    this_player.h[right_card].n, ") e venceu a atual.")
                                card_to_beat = [this_player.h[right_card], team, this_player]
                                del this_player.h[right_card]

                            else:

                                print(this_player.n, "jogou a carta (", this_player.h[right_card].s,
                                    this_player.h[right_card].n, ") e não venceu a atual.")
                                del this_player.h[right_card]

                        elif card_to_beat[1] == team:

                            right_card = -10

                            for card in range(len(this_player.h)):

                                if right_card == -10:

                                    right_card = card

                                elif this_player.h[card].v < this_player.h[right_card].v:

                                    right_card = card

                            if this_player.h[right_card].v > card_to_beat[0].v:

                                print(this_player.n, "jogou a carta (", this_player.h[right_card].s,
                                    this_player.h[right_card].n, ") e venceu a atual.")
                                card_to_beat = [this_player.h[right_card], team, this_player]
                                del this_player.h[right_card]

                            else:

                                print(this_player.n, "jogou a carta (", this_player.h[right_card].s,
                                    this_player.h[right_card].n, ") e não venceu a atual.")
                                del this_player.h[right_card]

            if card_to_beat[1] == 0:
                match_points[0][0] += 1
            else:
                match_points[1][0] += 1

        if match_points[0][0] >= 2:
            team_points[0][0] += 1
        else:
            team_points[1][0] += 1

    if team_points[0][0] >= 12:
        print("Time 1 venceu!")
    else:
        print("Time 2 venceu!")


def manilha(deck, vira):

    if vira.v >= 131:
        valor = 4
    elif vira.v >= 101:
        valor = int(str(vira.v)[0] + str(vira.v)[1]) + 1
    elif vira.v >= 41:
        valor = int(str(vira.v)[0]) + 1

    for carta in deck:

        if carta.v < 101:
            if int(str(carta.v)[0]) == valor:
                print("A carta",carta.s,carta.n,"é manilha")
                carta.v += 100
        else:
            if int(str(carta.v)[0] + str(carta.v)[1]) == valor:
                print("A carta", carta.s, carta.n, "é manilha")
                carta.v += 100

    return deck


def make_teams(players):

    quantidade_players = len(players)

    if quantidade_players == 2:
        times = [["P1"], ["P2"]]
    elif quantidade_players == 4:
        times = [["P1", "P3"], ["P2", "P4"]]
    elif quantidade_players == 6:
        times = [["P1", "P3", "P5"], ["P2", "P4", "P6"]]

    ready_team = False

    while ready_team == False:

        dados = []

        for item in players:
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
                    if len(players) == 6 and escolhido >= 0:
                        escolhido2 = x + 1
                    else:
                        escolhido = x + 1

            if contador == 1 and len(players) == 4:
                print(players[i].n, "fara dupla com", players[escolhido].n)
                times[0][0] = players[i]
                times[0][1] = players[escolhido]
                del players[escolhido]
                del players[i]
                times[1][0] = players[0]
                times[1][1] = players[1]
                ready_team = True
                break

            elif contador == 2 and len(players) == 6:
                print("Time 1:",players[i].n, "-", players[escolhido].n, "-"
                ,players[escolhido2].n)
                times[0][0] = players[i]
                times[0][1] = players[escolhido]
                times[0][2] = players[escolhido2]
                del players[escolhido2]
                del players[escolhido]
                del players[i]
                print("Time 2:", players[0].n, "-", players[1].n, "-", players[2].n)
                times[1][0] = players[0]
                times[1][1] = players[1]
                times[1][2] = players[2]
                ready_team = True
                break

    return times


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


main_title()

