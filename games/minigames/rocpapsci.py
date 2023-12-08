import random

user_wins = 0
computer_wins = 0

options = ["kámen", "papír", "nůžky"]

history = []

while True:
    user_input = input("Napiš kámen/nůžky/papír nebo Q pro odchod: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # kámen: 0, papír: 1, nůžky: 2
    computer_pick = options[random_number]
    print("počítač vybral", computer_pick + ".")

    history.append((user_input, computer_pick))  

   
    if len(history) >= 3:
        last_user_move = history[-2][0]
        last_computer_move = history[-2][1]
        current_computer_move = history[-1][1]


        if last_user_move == last_computer_move:
            predicted_move = current_computer_move
        else:
            predicted_move = random.choice(options)

        print("Počítač předpověděl:", predicted_move)


        if user_input == current_computer_move:
            print("Remíza, hraješ znovu!")
            
        elif user_input == "kámen" and computer_pick == "nůžky":
            print("Vyhrrál jsi!")
            user_wins += 1

        elif user_input == "papír" and computer_pick == "kámen":
            print("Vyhrál jsi!")
            user_wins += 1

        elif user_input == "nůžky" and computer_pick == "papír":
            print("Vyhrál jsi!")
            user_wins += 1

        else:
            print("Prohrál jsi!")
            computer_wins += 1

print("Vyhrál jsi", user_wins, "krát.")
print("Počítač  vyhrál", computer_wins, "krát.")
print("Uvidíme se příště!")