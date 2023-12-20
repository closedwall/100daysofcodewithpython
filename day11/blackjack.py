import random
import os

def deal_card():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def compare(user_score, computer_score):
    "Return message after comparing score of both the player"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent have BlackJack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You web over, You lose"
    elif computer_score > 21:
        return "opponent went over You won"
    elif user_score > computer_score:
        return "you Won"
    else:
        return "You lose"

def play_game():
    os.system('cls')
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards {user_cards} current score {user_score}")
        print(f"computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card and 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" your hand is {user_cards} and total score is: {user_score}")
    print(f" computer's hand: {computer_cards} and total score is: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    play_game()
    if input("Do you want to Play again? Y/N: ").lower()!='y':
        break