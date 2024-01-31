import cardUtils

def compare_cards(name1, card1, name2, card2, currentWar):
    if card1.value > card2.value:
        player_1.add_one(card2)
        print(f'  {name1}\'s {card1} beats {name2}\'s {card2}') if currentWar else print(f'{name1}\'s {card1} beats {name2}\'s {card2}')
    elif card2.value > card1.value:
        player_2.add_one(card1)
        print(f'  {name2}\'s {card2} beats {name1}\'s {card1}') if currentWar else print(f'{name2}\'s {card2} beats {name1}\'s {card1}') 
    elif card1.value == card2.value:
        print(f'  {name2}\'s {card2} equals {name1}\'s {card1}\n  **WAR**') if currentWar else print(f'{name2}\'s {card2} equals {name1}\'s {card1}\n  **WAR**')
        return True
    return False


if __name__ == '__main__':
    deck = cardUtils.Deck()
    deck.shuffle()
    player_1 = cardUtils.Player('Player 1')
    player_2 = cardUtils.Player('Player 2')

    player_1.add_one(deck.cards[0:26])
    player_2.add_one(deck.cards[26:])

    print(f'{player_1}\n{player_2}\nStart!')
    game_on = True

    while game_on:
        if len(player_1.hand) == 0:
            print(f'{player_1}\n{player_2}')
            print(f'{player_1.name} out of cards.\n{player_2.name} wins!!!')
            game_on = False
            break
        elif len(player_2.hand) == 0:
            print(f'{player_1}\n{player_2}')
            print(f'{player_2.name} out of cards.\n{player_1.name} wins!!!')
            game_on = False
            break

        player_1_card = player_1.remove_one()
        player_2_card = player_2.remove_one()

        war_on = compare_cards(player_1.name, player_1_card, player_2.name, player_2_card, False)

        while war_on:
            if (len(player_1.hand) < 4):
                print(f'{player_1}\n{player_2}')
                print(f'{player_1.name} does not have enough cards for war.\n{player_2.name} wins!!!')
                game_on = False
                break
            elif (len(player_2.hand) < 4):
                print(f'{player_1}\n{player_2}')
                print(f'{player_2.name} does not have enough cards for war.\n{player_1.name} wins!!!')
                game_on = False
                break

            player_1_cards = [player_1.remove_one() for _ in range(4)]
            player_2_cards = [player_2.remove_one() for _ in range(4)]

            war_on = compare_cards(player_1.name, player_1_cards[3], player_2.name, player_2_cards[3], True)