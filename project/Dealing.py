from card import card
import deck
def deal(dealerHand, playerHand):
    for i in range(1,5):
        if i%2=1:
            playerHand.append(deck[i-1])
        else:
            dealerHand.append(deck[i-1])
    for i in range(0,4):
        del deck(4-i)
def checkScore(dealerHand,playerHand)
    playerScore=0
    dealerScore=0
    for i in range(1,3):
        if i%2==1:
            for card in dealerHand:
                dealerScore+=card.val
        else:
            for card in playerHand:
                playerScore+=card.val
if __name__ == "__main__":
    playerHand= []
    dealerHand= []
    deal(playerHand,dealerHand)
    checkScore(playerHand,dealerHand)

