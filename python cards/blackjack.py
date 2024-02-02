import cardUtils

def take_bet(player):
    '''Allows user to input a bet'''

    while True:
        try:
            bet = int(input('\nMake your bet: '))
        except ValueError:
            print("Bet must be a number.")
        #if no exception ->
        else:
            if bet > player.bank:
                print(f'Not enough in bank! {player.name}\'s balance is {player.bank}.')
            else:
                player.make_bet(bet)
                return bet


def ask_hit_or_stand(player, dealer, deck, bet):
    '''Asks user to hit or stand, calls display_cards() and check_bust() for each option, breaks out of current round and calls check_winner() on stand (s)'''

    global game_on
    while game_on:
        user_response = input('\nHit or Stand? (h/s): ')
        if user_response.lower() == 'h':
            player.add_one(deck.deal_one())
            player.adjust_aces()
            display_cards(player, dealer)
            check_bust(player, dealer, bet)
        elif user_response.lower() == 's':
            print(f'{player.name} stands. Dealer\'s turn.')
            while dealer.hand_value < 21 and dealer.hand_value <= player.hand_value:
                dealer.add_one(deck.deal_one())
                dealer.adjust_aces()
                display_cards(player, dealer, False)
                check_bust(player, dealer, bet)
            game_on = False
            break
        else:
            print('Please enter h for hit or s for stand.')


def display_cards(player, dealer, firstdeal=True):
    '''Displays player and dealer hands, hides dealers first card if players turn'''

    if firstdeal:
        print('\nDealer\'s hand:')
        print(f'    |  {"First card hidden"}  |  {dealer.hand[1]}  |')
        print('-' * 50)
        print('\nPlayer\'s hand:')
        print('    |  ', end='')
        for card in player.hand:
            print(card, end='  |  ')
        print(f'\nPlayer\'s hand value: {player.hand_value}')
        print('-' * 50)
    else:
        #asterisk used to iterate over hand list
        print('\nDealer\'s hand:')
        print('    |  ', end='')
        for card in dealer.hand:
            print(card, end='  |  ')
        print(f'\nDealer\'s hand value: {dealer.hand_value}')
        print('-' * 50)
        print('\nPlayer\'s hand:')
        print('    |  ', end='')
        for card in player.hand:
            print(card, end='  |  ')
        print(f'\nPlayer\'s hand value: {player.hand_value}')
        print('-' * 50)
        print('')


def check_bust(player, dealer, bet):
    '''Checks if a hand is over 21 then, breaks out of current round if either bust and adds bet to player bank if dealer bust'''

    global game_on
    if player.hand_value > 21:
        print('Player BUST!')
        game_on = False
    elif dealer.hand_value > 21:
        print('Dealer BUST!')
        player.win_bet(bet)
        game_on = False


def check_winner(player, dealer, bet):
    '''Finds highest hand value, prints winner, adds player bet to player bank if they win'''

    if player.hand_value > dealer.hand_value:
        print('Player WINS!')
        player.win_bet(bet)
    elif dealer.hand_value > player.hand_value:
        print('Dealer WINS!')


if __name__ == '__main__':
    #TODO win conditions, game loop
    
    deck = cardUtils.Deck()
    deck.shuffle()
    player = cardUtils.Player('Player')
    dealer = cardUtils.Player('Dealer')

    while True:
        game_on = True

        player_bet = take_bet(player)

        deal = [deck.deal_one() for _ in range(2)]
        player.add_one(deal)
        deal = [deck.deal_one() for _ in range(2)]
        dealer.add_one(deal)

        display_cards(player, dealer)

        while game_on:

            ask_hit_or_stand(player, dealer, deck, player_bet)
