import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_length = len(cards)

drawn_cards = {
    "user" : {
        "cards" : [],
        "user_total" : 0
    } ,
    "cpu" : {
        "cards" : [],
        "cpu_total" : 0
    }
}


def initial_draw():
    while len(drawn_cards["cpu"]["cards"]) < 2 or drawn_cards["cpu"]["cpu_total"] < 17:
        random_card = random.randint(0, cards_length - 1)
        drawn_cards["cpu"]["cards"].append(cards[random_card])
        drawn_cards["cpu"]["cpu_total"] += cards[random_card]
        
    while len(drawn_cards["user"]["cards"]) < 2:
        random_card = random.randint(0, cards_length - 1)
        drawn_cards["user"]["cards"].append(cards[random_card])
        drawn_cards["user"]["user_total"] += cards[random_card]

    print(f"Your cards: {drawn_cards["user"]["cards"]}, current score: {drawn_cards["user"]["user_total"]}")
    print(f"Computer's first card: {drawn_cards["cpu"]["cards"][0]}")

    

def draw_more():
    random_card = random.randint(0, cards_length - 1)
    if cards[random_card] == 11 and (drawn_cards["user"]["user_total"] + cards[random_card]) > 21:
        drawn_cards["user"]["cards"].append(1)
        drawn_cards["user"]["user_total"] += 1
    else:
        drawn_cards["user"]["cards"].append(cards[random_card])
        drawn_cards["user"]["user_total"] += cards[random_card]    

def start():
    initial_draw()

    get_more_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if get_more_card == 'y':
        draw_more()
    
    print(f"Your cards: {drawn_cards["user"]["cards"]}, current score: {drawn_cards["user"]["user_total"]}")
    print(f"CPU final cards: {drawn_cards["cpu"]["cards"]}, current score: {drawn_cards["cpu"]["cpu_total"]}")

start()