import random


SUIT_TUPLE=('Spades','Hearts','Clubs','Diamdonds')
RANK_TUPLE=('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
score=50
NCARDS=8

def getCard(deckListIn):
    thiscard=deckListIn.pop()
    return thiscard

def shuffel(deckListIn):
    deckListOut=deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


print(20*'#')
print("Welcome to the Higher or Lower.")
print("Getting it right adds 20 points; get it wrong and you will lose 15 points.")
print("You have 50 points score to start.")
print(20*'#')
print()

startingDecklist=[]

for suit in SUIT_TUPLE:
    for val,Rank in enumerate(RANK_TUPLE):
        card={'suit':suit,'Rank':Rank,'value':val+1}
        startingDecklist.append(card)

while True:
    cardsshuffeld=shuffel(startingDecklist)
    currentCard=getCard(cardsshuffeld)
    currrank=currentCard['Rank']
    currsuit=currentCard['suit']
    currval=currentCard['value']
    print(f'Starting CARD is:{currrank} of {currsuit}\n')

    for cardNumber in range(0,NCARDS):
        answer=input(f'Will the next card be higher or lower than the {currrank} of {currsuit}. (Enter h or l): ')
        
        nextcard=getCard(cardsshuffeld)
        nextrank=nextcard['Rank']
        nextsuit=nextcard['suit']
        nextval=nextcard['value']
        print(f'Next Card is: {nextrank} of {nextsuit}')


        answer=answer.casefold()
        
        if answer=='h':
            if currval>nextval:
                print("You got it right, it was higher.")
                score=score+20
            else:
                print("You got it wrong, it was lower.")
                score=score-15
        elif answer=='l':
            if currval<nextval:
                print("You got it right, it was lower.")
                score=score+20
            else:
                print('You got it wrong, it was higher.')
                score=score-15
        print(f"Your score is: {score}\n")

        currrank=nextrank
        currval=nextval
        
        goagain=input("want to continue playing? press 'ENTER', or press 'q' to Quit ")
        if goagain:
            break

