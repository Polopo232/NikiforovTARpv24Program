from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os
import json
import ttkbootstrap as ttk

suits = ['hearts', 'diamonds', 'clubs', 'spades']
rank_files = {
    '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7',
    '08': '8', '09': '9', '10': '10', 'jack': 'J', 'queen': 'Q', 'king': 'K', 'ace': 'A'
}
ranks = list(rank_files.keys())

player_name = ""
game_history = []
current_game = {"name": "", "result": "", "score": 0}

def load_player_data():
    global game_history
    try:
        with open('blackjack_scores.json', 'r') as f:
            game_history = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        game_history = []

def save_player_data():
    with open('blackjack_scores.json', 'w') as f:
        json.dump(game_history, f)

def get_name():
    global player_name
    player_name = simpledialog.askstring("Blackjack", "Sisestage nimi:", parent=window)
    if player_name:
        current_game["name"] = player_name
        start_game()
    else:
        window.destroy()

def start_game():
    start_button.pack()
    history_button.pack()
    GameWindow()

def show_history():
    history_window = Toplevel(window)
    history_window.title("Mängu ajalugu")
    history_window.geometry("600x400")
    
    if not game_history:
        Label(history_window, text="Mängu ajalugu on tühi", font=("Arial", 16)).pack(pady=50)
    else:
        for game in game_history[-10:]:
            Label(history_window, 
                  text=f"{game['name']}: {game['result']} (Punktid: {game['score']})", 
                  font=("Arial", 14)).pack(pady=5)

def calculate_score(hand):
    score = 0
    aces = 0
    
    for card in hand:
        rank = card.split()[0]
        if rank in ['jack', 'queen', 'king']:
            score += 10
        elif rank == 'ace':
            score += 11
            aces += 1
        else:
            score += int(rank)

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
        
    return score

def load_card_image(card_name):
    if card_name == "back":
        image_path = "card_back.png"
    else:
        suit = card_name.split()[-1].lower()
        rank = card_name.split()[0].lower()
        
        if rank == 'jack': file_rank = 'J'
        elif rank == 'queen': file_rank = 'Q'
        elif rank == 'king': file_rank = 'K'
        elif rank == 'ace': file_rank = 'A'
        elif rank == '10': file_rank = '10'
        else: file_rank = rank
        
        image_path = f"card_{suit}_{file_rank}.png"
    
    if os.path.exists(image_path):
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)
    else:
        print(f"Image not found: {image_path}")
        return None

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            display_rank = rank
            if rank == 'ace': display_rank = 'ace'
            elif rank == 'jack': display_rank = 'jack'
            elif rank == 'queen': display_rank = 'queen'
            elif rank == 'king': display_rank = 'king'
            deck.append(f"{display_rank} of {suit}")
    random.shuffle(deck)
    return deck

def deal_and_show_card():
    if len(deck) > 0 and not game_over:
        card = deck.pop()
        player_hand.append(card)
        image = load_card_image(card)
        if image:
            label = Label(cards_frame, image=image)
            label.image = image
            label.grid(row=0, column=len(player_card_labels), padx=5)
            player_card_labels.append(label)
        
        player_score = calculate_score(player_hand)
        player_hand_label.config(text=f"{player_name}: {player_score} punktid")

        if player_score > 21:
            end_game("Liiga palju! Sa oled kaotanud.")
        elif player_score == 21:
            end_game("Blackjack! Sa võidad!")

def dealer_turn():
    global game_over
    
    if game_over:
        return

    dealer_card_labels[0].grid_forget()
    image = load_card_image(dealer_hand[0])
    if image:
        label = Label(cards_frame, image=image)
        label.image = image
        label.grid(row=1, column=0, padx=5)
        dealer_card_labels[0] = label
    
    dealer_score = calculate_score(dealer_hand)

    while dealer_score < 17 and len(deck) > 0:
        card = deck.pop()
        dealer_hand.append(card)
        image = load_card_image(card)
        if image:
            label = Label(cards_frame, image=image)
            label.image = image
            label.grid(row=1, column=len(dealer_card_labels), padx=5)
            dealer_card_labels.append(label)
        
        dealer_score = calculate_score(dealer_hand)
    
    dealer_hand_label.config(text=f"Edasimüüja: {dealer_score} punktid")
    
    player_score = calculate_score(player_hand)
    current_game["score"] = player_score
    
    if dealer_score > 21:
        end_game("Edasimüüja ületas seda! Sa võidad!")
        current_game["result"] = "Win"
    elif dealer_score > player_score:
        end_game("Diiler võitis!")
        current_game["result"] = "Lose"
    elif dealer_score < player_score:
        end_game("Sa võidad!")
        current_game["result"] = "WIN"
    else:
        end_game("Tie!")
        current_game["result"] = "Draw"

    game_history.append(current_game.copy())
    save_player_data()

def end_game(message):
    global game_over
    game_over = True
    
    result_label.config(text=message, fg="yellow")
    take_card.config(state=DISABLED)
    stand_button.config(state=DISABLED)
    restart_button.config(state=NORMAL)

def restart_game():
    game_window.destroy()
    GameWindow()

def begin_game():
    global deck, player_hand, dealer_hand, player_card_labels, dealer_card_labels, game_over
    
    game_over = False
    result_label.config(text="", fg="black")

    for widget in cards_frame.winfo_children():
        widget.destroy()
    
    player_card_labels = []
    dealer_card_labels = []
    
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    for i, card in enumerate(player_hand):
        image = load_card_image(card)
        if image:
            label = Label(cards_frame, image=image)
            label.image = image
            label.grid(row=0, column=i, padx=5)
            player_card_labels.append(label)

    back_image = load_card_image("back")
    if back_image:
        label = Label(cards_frame, image=back_image)
        label.image = back_image
        label.grid(row=1, column=0, padx=5)
        dealer_card_labels.append(label)

    if len(dealer_hand) > 1:
        image = load_card_image(dealer_hand[1])
        if image:
            label = Label(cards_frame, image=image)
            label.image = image
            label.grid(row=1, column=1, padx=5)
            dealer_card_labels.append(label)

    player_score = calculate_score(player_hand)
    player_hand_label.config(text=f"{player_name}: {player_score} punktid")
    dealer_hand_label.config(text="Edasimüüja: ? punkti")
    
    take_card.config(state=NORMAL)
    stand_button.config(state=NORMAL)
    restart_button.config(state=DISABLED)

    if player_score == 21:
        end_game("Blackjack! Sa võidad!")
        current_game["result"] = "Win"
        current_game["score"] = 21
        game_history.append(current_game.copy())
        save_player_data()

def GameWindow():
    global game_window, player_hand_label, dealer_hand_label, cards_frame
    global take_card, stand_button, restart_button, result_label
    
    game_window = Toplevel(window)
    game_window.title("In game")
    game_window.geometry("800x600")

    cards_frame = Frame(game_window, bg="green")

    player_hand_label = Label(game_window, text="", font=("Arial", 16), bg="green", fg="white")
    
    dealer_hand_label = Label(game_window, text="", font=("Arial", 16), bg="green", fg="white")

    buttons_frame = Frame(game_window, bg="green")
    
    take_card = ttk.Checkbutton(buttons_frame, text="Võtke kaart", bootstyle="success-toolbutton", command=deal_and_show_card)
    
    stand_button = ttk.Checkbutton(buttons_frame, text="Stop", bootstyle="danger-toolbutton", command=dealer_turn)
    
    restart_button = ttk.Checkbutton(buttons_frame, text="Uuesti", bootstyle="toolbutton" , command=restart_game, state=DISABLED)
    
    result_label = Label(game_window, text="", font=("Arial", 18), bg="green")



    cards_frame.pack(pady=20)
    player_hand_label.pack()
    dealer_hand_label.pack()
    buttons_frame.pack(pady=20)
    take_card.grid(row=0, column=0, padx=10)
    stand_button.grid(row=0, column=1, padx=10)
    restart_button.grid(row=0, column=2, padx=10)
    result_label.pack(pady=20)
    
    begin_game()

window = ttk.Window(themename="darkly")
window.title("BlackJack")
window.geometry("400x300")


load_player_data()

black_text = ttk.Label(window, text="Blackjack", bootstyle="light")
black_text.config(font=("", 24))

black_text.pack(pady=20)


start_button = ttk.Button(window, text="Alusta mängu", bootstyle="success", command=get_name)
start_button.pack(pady=10)

history_button = ttk.Button(window, text="Mängu ajalugu", bootstyle="light", command=show_history)
history_button.pack(pady=10)

window.mainloop()
