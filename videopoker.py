import random
from collections import Counter
import time
import os

class VideoPoker:
    def __init__(self):
        self.deck = []
        self.hand = []
        self.credits = 100  # Set initial credit purse to 100
        self.bet = 5
        self.reset_deck()

    def reset_deck(self):
        suits = ['♥', '♦', '♣', '♠']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
        random.shuffle(self.deck)

    def deal_hand(self):
        if len(self.deck) < 5:
            self.reset_deck()

        self.hand = [self.deck.pop() for _ in range(5)]
        return self.hand

    def draw_cards(self, hold_indices):
        new_cards = []
        for i in range(5):
            if i in hold_indices:
                new_cards.append(self.hand[i])
            else:
                new_cards.append(self.deck.pop())
        self.hand = new_cards
        return self.hand

    def display_hand(self, hold_indices=[]):
        print("\n▓▒░ YOUR HAND ░▒▓")
        print(" ".join(f"[{card}]" for card in self.hand))
        print(" ".join("[X]" if i in hold_indices else "[ ]" for i in range(5)))

    def evaluate_hand(self):
        ranks = [card[:-1] for card in self.hand]
        suits = [card[-1] for card in self.hand]

        rank_counts = Counter(ranks)
        suit_counts = Counter(suits)

        is_flush = len(suit_counts) == 1
        is_straight = self._is_straight(ranks)

        if is_flush and set(ranks) == {'10', 'J', 'Q', 'K', 'A'}:
            return "Royal Flush", 250
        if is_flush and is_straight:
            return "Straight Flush", 50
        if 4 in rank_counts.values():
            return "Four of a Kind", 25
        if sorted(rank_counts.values()) == [2, 3]:
            return "Full House", 9
        if is_flush:
            return "Flush", 6
        if is_straight:
            return "Straight", 4
        if 3 in rank_counts.values():
            return "Three of a Kind", 3
        if list(rank_counts.values()).count(2) == 2:
            return "Two Pair", 2
        if any(rank_counts.get(rank, 0) == 2 for rank in ['J', 'Q', 'K', 'A']):
            return "Jacks or Better", 1

        return "No Win", 0

    def _is_straight(self, ranks):
        rank_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        sorted_ranks = sorted(ranks, key=lambda x: rank_order.index(x))

        if set(sorted_ranks) == {'A', '2', '3', '4', '5'}:
            return True

        for i in range(1, 5):
            if rank_order.index(sorted_ranks[i]) != rank_order.index(sorted_ranks[i-1]) + 1:
                return False
        return True

    def play_round(self, input_func):
        if self.credits < self.bet:
            print("Not enough credits to play.")
            return

        self.credits -= self.bet
        self.deal_hand()
        hold_indices = []
        self.display_hand(hold_indices)

        hold_input = input_func("Hold cards (e.g., '1 3 5' to keep K♠, A♦, Q♠ or 'H' to hold all): ")
        if hold_input.strip():
            try:
                hold_indices = [int(i) - 1 for i in hold_input.split() if i.strip().isdigit()]
            except ValueError:
                print("Invalid input, drawing all new cards.")

        self.draw_cards(hold_indices)
        self.display_hand(hold_indices)

        hand_rank, payout = self.evaluate_hand()
        winnings = self.bet * payout
        self.credits += winnings
        print(f"\n{hand_rank}! You won {winnings} credits. Current balance: {self.credits}")

    def start_game(self, input_func):
        print("▓▒░▒▓▒░▒▓▒░▒▓▒░▒▓▒▓")
        print("▓▒░ WELCOME TO  ░▒▓")
        print("▓▒░ VIDEO POKER ░▒▓")
        print("▓▒░▒▓▒░▒▓▒░▒▓▒░▒▓▒▓")
        time.sleep(2)

        while True:
            print("\n▓▒░ MENU ░▒▓")
            print("1: Play hand")
            print("2: Change bet (current: {})".format(self.bet))
            print("3: See paytable")
            print("4: Quit")

            choice = input_func("Select an option: ")

            if choice == "1":
                self.play_round(input_func)
            elif choice == "2":
                try:
                    new_bet = int(input_func("Enter new bet amount: "))
                    if new_bet > 0:
                        self.bet = new_bet
                        print(f"Bet adjusted to {self.bet} credits per hand.")
                    else:
                        print("Bet must be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "3":
                print("""
╔════════════════════════════╗
║      ▓▒░ PAYTABLE ░▒▓      ║
╠════════════════════════════╣
║ Royal Flush       - 250    ║
║ Straight Flush    - 50     ║
║ Four of a Kind    - 25     ║
║ Full House        - 9      ║
║ Flush             - 6      ║
║ Straight          - 4      ║
║ Three of a Kind   - 3      ║
║ Two Pair          - 2      ║
║ Jacks or Better   - 1      ║
╚════════════════════════════╝
                """)
            elif choice == "4":
                print("\nThanks for playing!")
                self.display_outro()
                break
            else:
                print("Invalid choice. Please try again.")

    def display_outro(self):
        print("""
█       █   ██████
█▒      █▒  █▒    █▒
█▒      █▒  █▒    █▒
 █▒    █▒   █▒    █▒
 █▒    █▒   ██▒███▒
  █▒  █▒    █▒▒▒▒▒
   █▒█▒     █▒
    █▒      █▒
     ▒ IDEO ▒ OKER
        """)
        time.sleep(2)
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sound_path = os.path.join(script_dir, "bye.wav")
            os.system(f"aplay '{sound_path}'")
        except Exception as e:
            print(f"Could not play sound: {e}")

if __name__ == "__main__":
    game = VideoPoker()
    game.start_game(input)
