import cardUtil

if __name__ == '__main__':
    deck = cardUtil.Deck()
    deck.shuffle()
    player_1 = cardUtil.Player('Player 1')
    player_2 = cardUtil.Player('Player 2')

    player_1.add_one(deck.cards[0:26])
    player_2.add_one(deck.cards[26:])

    print(f'{player_1}\n{player_2}\nStart!')
    game_on = True

    while game_on:
        war_on = False

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

        if player_1_card.value > player_2_card.value:
            player_1.add_one(player_2_card)
            print(f'{player_1.name}\'s {player_1_card} beats {player_2.name}\'s {player_2_card}')
        elif player_2_card.value > player_1_card.value:
            player_2.add_one(player_1_card)
            print(f'{player_2.name}\'s {player_2_card} beats {player_1.name}\'s {player_1_card}')
        elif player_1_card.value == player_2_card.value:
            war_on = True
            print(f'{player_2.name}\'s {player_2_card} equals {player_1.name}\'s {player_1_card}\n  **WAR**')


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
            war_on = False

            if player_1_cards[3].value > player_2_cards[3].value:
                player_1.add_one(player_2_cards)
                print(f'  {player_1.name}\'s {player_1_cards[3]} beats {player_2.name}\'s {player_2_cards[3]}')
            elif player_2_cards[3].value > player_1_cards[3].value:
                player_2.add_one(player_1_cards)
                print(f'  {player_2.name}\'s {player_2_cards[3]} beats {player_1.name}\'s {player_1_cards[3]}')
            elif player_1_cards[3].value == player_2_cards[3].value:
                war_on = True
                print(f'  {player_2.name}\'s {player_2_cards[3]} equals {player_1.name}\'s {player_1_cards[3]}\n  **WAR**')