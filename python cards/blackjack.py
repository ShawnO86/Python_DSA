import cardUtils

if __name__ == '__main__':
    game_on = True
    deck = cardUtils.Deck()
    deck.shuffle()
    testPlayer1 = cardUtils.Player('Test 1')
    testPlayer2 = cardUtils.Player('Test 2')

    deal = [deck.deal_one() for _ in range(2)]
    testPlayer1.add_one(deal)
    deal = [deck.deal_one() for _ in range(2)]
    testPlayer2.add_one(deal)
