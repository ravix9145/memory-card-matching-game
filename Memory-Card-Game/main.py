import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Memory Card Matching Game")
root.geometry("600x450")

# Card values (4 pairs)
card_values = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']
random.shuffle(card_values)

buttons = []
first_card = None
second_card = None
first_index = None
second_index = None
matched_pairs = 0
lock = False


def check_match():
    global first_card, second_card
    global first_index, second_index
    global matched_pairs, lock

    if first_card == second_card:
        matched_pairs += 1

        if matched_pairs == len(card_values) // 2:
            status_label.config(text="You Won!")

        reset_selection()
        lock = False

    else:
        root.after(1000, hide_cards)


def hide_cards():
    global lock

    buttons[first_index].config(text="")
    buttons[second_index].config(text="")

    reset_selection()
    lock = False


def reset_selection():
    global first_card, second_card
    global first_index, second_index

    first_card = None
    second_card = None
    first_index = None
    second_index = None


def card_click(index):
    global first_card, second_card
    global first_index, second_index
    global lock

    if lock:
        return

    if buttons[index]["text"] != "":
        return

    buttons[index].config(text=card_values[index])

    if first_card is None:
        first_card = card_values[index]
        first_index = index

    elif second_card is None:
        second_card = card_values[index]
        second_index = index

        lock = True
        check_match()


# Create card buttons
for i in range(8):
    btn = tk.Button(
        root,
        text="",
        width=10,
        height=4,
        font=("Arial", 14),
        command=lambda i=i: card_click(i)
    )

    btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
    buttons.append(btn)

status_label = tk.Label(
    root,
    text="Find all matching pairs!",
    font=("Arial", 14)
)
status_label.grid(row=3, column=0, columnspan=4, pady=20)

root.mainloop()