import random
import time
import pandas

player_1_id = 1
player_2_id = 2
game_plans = {#ROW PLANS
              "0":
                  {"1": ("r1","1"), "2": ("r1","2"), "3": ("r1","3")},
              "1":
                  {"1": ("r2","1"), "2": ("r2","2"), "3": ("r2","3")},
              "2":
                  {"1": ("r3","1"), "2": ("r3","2"), "3": ("r3","3")},
              #COLUMN PLANS
              "3":
                  {"1": ("r1","1"), "2": ("r2","1"), "3": ("r3","1")},
              "4":
                  {"1": ("r1","2"), "2": ("r2","2"), "3": ("r3","2")},
              "5":
                  {"1": ("r1","3"), "2": ("r2","3"), "3": ("r3","3")},
              #DIAGONAL PLANS
              "6":
                  {"1": ("r1","1"), "2": ("r2","2"), "3": ("r3","3")},
              "7":
                  {"1": ("r3","1"), "2": ("r2","2"), "3": ("r1","3")},
              }
chosen_plan = ""
active_plan = ""

def set_game():
    game_dict = {'r1': {'1':'⌗','2':'⌗','3':'⌗'},
            'r2': {'1':'⌗','2':'⌗','3':'⌗'},
            'r3': {'1':'⌗','2':'⌗','3':'⌗'}
            }
    return game_dict
def select_plan(plans):
    new_plan = random.choice(plans)
    return new_plan
def print_game(dictionary):
    print(f"1 - \033[4m{dictionary["r1"]["1"]}\033[0m|\033[4m{dictionary["r1"]["2"]}\033[0m|\033[4m{dictionary["r1"]["3"]}\033[0m")
    print(f"2 - \033[4m{dictionary["r2"]["1"]}\033[0m|\033[4m{dictionary["r2"]["2"]}\033[0m|\033[4m{dictionary["r2"]["3"]}\033[0m")
    print(f"3 - {dictionary["r3"]["1"]}|{dictionary["r3"]["2"]}|{dictionary["r3"]["3"]}")
    print("    1 2 3")
def import_hs(ai_opponent):
    if ai_opponent == 'N':
        file = "2p_scores.txt"
    else:
        file = "scores.txt"
    try:
        pandas.read_csv(file)
    except FileNotFoundError:
        with open(file, "w") as scores_output:
            scores_output.write("Condition" + "," + "Scores" + "\n")
            if opponent == 'N':
                scores_output.write("Player 1 Wins" + "," + "0" + "\n")
                scores_output.write(f"Ties" + "," + "0" + "\n")
                scores_output.write(f"Player 2 Wins" + "," + "0" + "\n")
            else:
                scores_output.write("Player Wins" + "," + "0" + "\n")
                scores_output.write(f"Ties" + "," + "0" + "\n")
                scores_output.write(f"Computer Wins" + "," + "0" + "\n")
    finally:
        data = pandas.read_csv(file)
        high_scores = {data_row["Condition"]: data_row["Scores"] for (index, data_row) in data.iterrows()}
        return high_scores
def print_hs(player_1_no, ties_no, player_2_no, ai_opponent):
    if ai_opponent == 'N':
        print("HIGH SCORES:\n"
              f"Player 1 Wins: {player_1_no}\n"
              f"Ties: {ties_no}\n"
              f"Player 2 Wins: {player_2_no}\n")
    else:
        print("HIGH SCORES:\n"
              f"Player Wins: {player_1_no}\n"
              f"Ties: {ties_no}\n"
              f"Computer Wins: {player_2_no}\n")
def reset_hs(ai_opponent):
    if ai_opponent == 'N':
        file = "2p_scores.txt"
    else:
        file = "scores.txt"
    with open(file, "w") as scores_output:
        scores_output.write("Condition" + "," + "Scores" + "\n")
        if opponent == 'N':
            scores_output.write("Player 1 Wins" + "," + "0" + "\n")
            scores_output.write("Ties" + "," + "0" + "\n")
            scores_output.write("Player 2 Wins" + "," + "0" + "\n")
        else:
            scores_output.write("Player Wins" + "," + "0" + "\n")
            scores_output.write("Ties" + "," + "0" + "\n")
            scores_output.write("Computer Wins" + "," + "0" + "\n")
    print("High Scores Reset")
def update_hs(player_1_no, ties_no, player_2_no, ai_opponent):
    if ai_opponent == 'N':
        file = "2p_scores.txt"
    else:
        file = "scores.txt"
    with open(file, "w") as scores_output:
        scores_output.write("Condition" + "," + "Scores" + "\n")
        if opponent == 'N':
            scores_output.write("Player 1 Wins" + "," + str(player_1_no) + "\n")
            scores_output.write("Ties" + "," + str(ties_no) + "\n")
            scores_output.write("Player 2 Wins" + "," + str(player_2_no) + "\n")
        else:
            scores_output.write("Player Wins" + "," + str(player_1_no) + "\n")
            scores_output.write(f"Ties" + "," + str(ties_no) + "\n")
            scores_output.write(f"Computer Wins" + "," + str(player_2_no) + "\n")
def player_turn(dictionary, value, ai_opponent, player_id):
    if ai_opponent == 'N':
        print(f"Player {player_id}, it is your turn.")
    else:
        print("It is your turn.")
    choice = True
    while choice:
        row_check = True
        while row_check:
            row = input("Please choose a row between 1 and 3\n")
            if row == "1" or row == "2" or row == "3":
                row_check = False
            else:
                print("Invalid choice.\n")

        col_check = True
        while col_check:
            column = input("Please choose a column between 1 and 3\n")
            if column == "1" or column == "2" or column == "3":
                col_check = False
            else:
                print("Invalid choice.\n")

        row_choice = f"r{row}"
        if dictionary[row_choice][column] == "⌗":
            dictionary[row_choice][column] = value
            choice = False
        else:
            print("That spot has already been chosen. Please choose again")
    print("\n")
def ai(dictionary, player_1_value, player_2_value, active_plan, chosen_plan):
    if chosen_plan == "":
        chosen_plan = select_plan(available_plans)
        active_plan = game_plans[chosen_plan]
    can_win = True
    plan_check = True
    defensive = True
    while can_win:
        #CHECK ROWS
        for row in range(1,4):
            player_1_count = 0
            player_2_count = 0
            for column in range(1,4):
                row_choice = f"r{row}"
                if dictionary[row_choice][str(column)] == player_1_value:
                    player_1_count += 1
                if dictionary[row_choice][str(column)] == player_2_value:
                    player_2_count += 1
            if player_2_count == 2 and player_1_count == 0:
                choice = True
                while choice:
                    column = str(random.randint(1, 3))
                    row_choice = f"r{row}"
                    if dictionary[row_choice][column] == "⌗":
                        dictionary[row_choice][column] = player_2_value
                        return
                    else:
                        choice = True
            else:
                pass
        #CHECK COLUMNS
        for column in range(1, 4):
            player_1_count = 0
            player_2_count = 0
            for row in range(1, 4):
                row_choice = f"r{row}"
                if dictionary[row_choice][str(column)] == player_1_value:
                    player_1_count += 1
                if dictionary[row_choice][str(column)] == player_2_value:
                    player_2_count += 1
            if player_2_count == 2 and player_1_count == 0:
                choice = True
                while choice:
                    row = str(random.randint(1, 3))
                    row_choice = f"r{row}"
                    if dictionary[row_choice][str(column)] == "⌗":
                        dictionary[row_choice][str(column)] = player_2_value
                        return
                    else:
                        choice = True
        #CHECK DIAGONALS (LR)
        player_1_count = 0
        player_2_count = 0
        for lr in range(1,4):
            row_choice = f"r{lr}"
            if dictionary[row_choice][str(lr)] == player_1_value:
                player_1_count += 1
            if dictionary[row_choice][str(lr)] == player_2_value:
                player_2_count += 1
        if player_2_count == 2 and player_1_count == 0:
            choice = True
            while choice:
                lr = str(random.randint(1, 3))
                row_choice = f"r{lr}"
                if dictionary[row_choice][lr] == "⌗":
                    dictionary[row_choice][lr] = player_2_value
                    return
                else:
                    choice = True
        #CHECK DIAGONALS (RL)
        player_1_count = 0
        player_2_count = 0
        if dictionary["r1"]["3"] == player_1_value:
            player_1_count += 1
        if dictionary["r1"]["3"] == player_2_value:
            player_2_count += 1
        if dictionary["r2"]["2"] == player_1_value:
            player_1_count += 1
        if dictionary["r2"]["2"] == player_2_value:
            player_2_count += 1
        if dictionary["r3"]["1"] == player_1_value:
            player_1_count += 1
        if dictionary["r3"]["1"] == player_2_value:
            player_2_count += 1
        if player_2_count == 2 and player_1_count == 0:
            if dictionary["r1"]["3"] == "⌗":
                dictionary["r1"]["3"] = player_2_value
                return
            elif dictionary["r2"]["2"] == "⌗":
                dictionary["r2"]["2"] = player_2_value
                return
            else:
                dictionary["r3"]["1"] = player_2_value
                return
        else:
            can_win = False
    while defensive:
        #CHECK ROWS
        for row in range(1,4):
            player_1_count = 0
            player_2_count = 0
            for column in range(1,4):
                row_choice = f"r{row}"
                if dictionary[row_choice][str(column)] == player_1_value:
                    player_1_count += 1
                if dictionary[row_choice][str(column)] == player_2_value:
                    player_2_count += 1
            if player_1_count == 2 and player_2_count == 0:
                choice = True
                while choice:
                    column = str(random.randint(1, 3))
                    row_choice = f"r{row}"
                    if dictionary[row_choice][column] == "⌗":
                        dictionary[row_choice][column] = player_2_value
                        return
                    else:
                        choice = True
            else:
                pass
        #CHECK COLUMNS
        for column in range(1,4):
            player_1_count = 0
            player_2_count = 0
            for row in range(1,4):
                row_choice = f"r{row}"
                if dictionary[row_choice][str(column)] == player_1_value:
                    player_1_count += 1
                if dictionary[row_choice][str(column)] == player_2_value:
                    player_2_count += 1
            if player_1_count == 2 and player_2_count == 0:
                choice = True
                while choice:
                    row = str(random.randint(1, 3))
                    row_choice = f"r{row}"
                    if dictionary[row_choice][str(column)] == "⌗":
                        dictionary[row_choice][str(column)] = player_2_value
                        return
                    else:
                        choice = True
            else:
                pass
        #CHECK DIAGONALS (LR)
        player_1_count = 0
        player_2_count = 0
        for lr in range(1,4):
            row_choice = f"r{lr}"
            if dictionary[row_choice][str(lr)] == player_1_value:
                player_1_count += 1
            if dictionary[row_choice][str(lr)] == player_2_value:
                player_2_count += 1
        if player_1_count == 2 and player_2_count == 0:
            choice = True
            while choice:
                lr = str(random.randint(1, 3))
                row_choice = f"r{lr}"
                if dictionary[row_choice][lr] == "⌗":
                    dictionary[row_choice][lr] = player_2_value
                    return
                else:
                    choice = True
        # CHECK DIAGONALS (RL)
        player_1_count = 0
        player_2_count = 0
        if dictionary["r1"]["3"] == player_1_value:
            player_1_count += 1
        if dictionary["r1"]["3"] == player_2_value:
            player_2_count += 1
        if dictionary["r2"]["2"] == player_1_value:
            player_1_count += 1
        if dictionary["r2"]["2"] == player_2_value:
            player_2_count += 1
        if dictionary["r3"]["1"] == player_1_value:
            player_1_count += 1
        if dictionary["r3"]["1"] == player_2_value:
            player_2_count += 1
        if player_1_count == 2 and player_2_count == 0:
            if dictionary["r1"]["3"] == "⌗":
                dictionary["r1"]["3"] = player_2_value
                return
            elif dictionary["r2"]["2"] == "⌗":
                dictionary["r2"]["2"] = player_2_value
                return
            else:
                dictionary["r3"]["1"] = player_2_value
                return
        else:
            defensive = False
    # OFFENSIVE MOVES
    while plan_check:
        player_1_count = 0
        player_2_count = 0
        for position in range(1, 4):
            row_choice = str(active_plan[str(position)][0])
            column = str(active_plan[str(position)][1])
            if dictionary[row_choice][column] == player_1_value:
                player_1_count += 1
            if dictionary[row_choice][column] == player_2_value:
                player_2_count += 1
        if player_1_count == 0 and player_2_count <= 3:
            #print("Go for plan")
            plan_check = False
            choice = True
            while choice:
                for position in range(1, 4):
                    row_choice = str(active_plan[str(position)][0])
                    column = str(active_plan[str(position)][1])
                    if dictionary[row_choice][str(column)] == "⌗":
                        dictionary[row_choice][str(column)] = player_2_value
                        #print(dictionary)
                        return
                else:
                    choice = False
        else:
            # print("New plan needed")
            available_plans.remove(chosen_plan)
            try:
                chosen_plan = select_plan(available_plans)
                active_plan = game_plans[chosen_plan]
                #print(f"New plan is {chosen_plan}")
            except (ValueError, IndexError):
                # print("Out of plans")
                plan_check = False
                choice = True
                while choice:
                    row = random.randint(1, 3)
                    column = str(random.randint(1, 3))
                    row_choice = f"r{row}"
                    if dictionary[row_choice][column] == "⌗":
                        dictionary[row_choice][column] = player_2_value
                        return
                    else:
                        choice = True
def ai_turn(dictionary):
    print("It is the computer's turn")
    print("The computer is thinking...")
    time.sleep(2)
    ai(dictionary, player_1, computer, active_plan, chosen_plan)
    print("\n")
def win_cond(winner):
    #ROW VICTORIES
    if game['r1']['1'] == game['r1']['2'] and game['r1']['1'] == game['r1']['3'] and game['r1']['1'] != "⌗":
        if winner == game['r1']['1']:
            outcome = 'win'
        else:
            outcome = 'lose'
    elif game['r2']['1'] == game['r2']['2'] and game['r2']['1'] == game['r2']['3'] and game['r2']['1'] != "⌗":
        if winner == game['r2']['1']:
            outcome = 'win'
        else:
            outcome = 'lose'
    elif game['r3']['1'] == game['r3']['2'] and game['r3']['1'] == game['r3']['3'] and game['r3']['1'] != "⌗":
        if winner == game['r3']['1']:
            outcome = 'win'
        else:
            outcome = 'lose'
    #COLUMN VICTORIES
    elif game['r1']['1'] == game['r2']['1'] and game['r1']['1'] == game['r3']['1'] and game['r1']['1'] != "⌗":
        if winner == game['r1']['1']:
            outcome = 'win'
        else:
            outcome = 'lose'
    elif game['r1']['2'] == game['r2']['2'] and game['r1']['2'] == game['r3']['2'] and game['r1']['2'] != "⌗":
        if winner == game['r1']['2']:
            outcome = 'win'
        else:
            outcome = 'lose'
    elif game['r1']['3'] == game['r2']['3'] and game['r1']['3'] == game['r3']['3'] and game['r1']['3'] != "⌗":
        if winner == game['r1']['3']:
            outcome = 'win'
        else:
            outcome = 'lose'
    #DIAGONAL VICTORIES
    elif game['r1']['1'] == game['r2']['2'] and game['r1']['1'] == game['r3']['3'] and game['r1']['1'] != "⌗":
        if winner == game['r1']['1']:
            outcome = 'win'
        else:
            outcome = 'lose'
    elif game['r1']['3'] == game['r2']['2'] and game['r1']['3'] == game['r3']['1'] and game['r1']['3'] != "⌗":
        if winner == game['r1']['3']:
            outcome = 'win'
        else:
            outcome = 'lose'
    else:
        outcome = ""
    return outcome
def end_game_msg(player_1_no, ties_no, player_2_no,game_state, ai_opponent):
    if game_state == "win":
        if ai_opponent == "N":
            print("Player 1 wins!")
        else:
            print("You win!")
        player_1_no += 1
        print_hs(player_1_no, ties_no, player_2_no, opponent)
        return player_1_no
    elif game_state == "tie":
        print("It's a tie!")
        ties_no += 1
        print_hs(player_1_no, ties_no, player_2_no, opponent)
        return ties_no
    else:
        if ai_opponent == "N":
            print("Player 2 wins!")
        else:
            print("You lose!")
        player_2_no += 1
        print_hs(player_1_no, ties_no, player_2_no, opponent)
        return player_2_no

#SET_UP
game_running = True

#CHOOSE OPPONENT
opponent = input("Lets play Tic Tac Toe!\nDo you want an ai opponent? 'Y' or 'N'?\n").upper()
while opponent != 'Y' and opponent !='N':
    opponent = input("Choice not recognised. Do you want to play against the computer? 'Y' or 'N'?\n").upper()

if opponent == 'N':
    player_1 = input("Player 1, do you want to be O's or X's?\n").upper()
else:
    player_1 = input("Do you want to be O's or X's?\n").upper()

#CHECK WHO GOES FIRST
turn = 1
coin_flip = random.randint(1,2)
print("Flipping a coin to see who goes first...")
time.sleep(1)
if opponent == 'N':
    if coin_flip == 1:
        print("It's Heads! Player 1 goes first.")
        turn = 1
    else:
        print("It's Tails! Player 2 goes first.")
        turn = 2
else:
    if coin_flip == 1:
        print("It's Heads! You go first.")
        turn = 1
    else:
        print("It's Tails! The Computer goes first.")
        turn = 2

#RESET SCOREBOARD (SECRET OPTION) AND CHECK FOR VALID INPUT
while player_1 != "X" and player_1 != "O":
    while player_1 == "RESET":
        reset_hs(opponent)
        player_1 = input("Do you want to be O's or X's?\n").upper()
    while player_1 != "X" and player_1 != "O" and player_1 != "RESET":
            player_1 = input("Invalid option entered. PLease choose from O's or X's.").upper()

#IMPORT HIGH SCORES
time.sleep(2)
hs = import_hs(opponent)
if opponent == 'N':
    player_1_wins = int(hs['Player 1 Wins'])
    ties = int(hs['Ties'])
    player_2_wins = int(hs['Player 2 Wins'])
else:
    player_1_wins = int(hs['Player Wins'])
    ties = int(hs['Ties'])
    player_2_wins = int(hs['Computer Wins'])

#SET GAME BOARD
while game_running:
    available_plans = ["0", "1", "2", "3", "4", "5", "6", "7"]
#    chosen_plan = select_plan(available_plans)
#    print(f"Chosen plan is {chosen_plan}")
#    print(game_plans)
#    print(available_plans)
#    active_plan = game_plans[chosen_plan]
    print_hs(player_1_wins, ties, player_2_wins, opponent)
    game = set_game()
    print_game(game)
    win_check = 0
    game_on = True
#PLAY GAME
    while game_on:
        if opponent == 'Y':
            if player_1 == "O":
                computer = "X"
            else:
                computer = "O"
        else:
            if player_1 == "O":
                player_2 = "X"
            else:
                player_2 = "O"
        if turn == 1:
            player_turn(game, player_1, opponent, player_1_id)
            turn = 2
        else:
            if opponent == 'N':
                player_turn(game, player_2, opponent, player_2_id)
                turn = 1
            else:
                ai_turn(game)
                turn = 1

        print_game(game)
        win_check += 1
        cont = win_cond(player_1)
        if cont == "":
            if win_check == 9:
                game_on = False
                state = "tie"
                ties = end_game_msg(player_1_wins, ties, player_2_wins, state, opponent)
            else:
                game_on = True
                if turn == 1:
                    player_turn(game, player_1, opponent, player_1_id)
                    turn = 2
                else:
                    if opponent == 'N':
                        player_turn(game, player_2, opponent, player_2_id)
                        turn = 1
                    else:
                        ai_turn(game)
                        turn = 1
                print(chosen_plan)
                print(active_plan)
                print_game(game)
                win_check += 1
                cont = win_cond(player_1)
                if cont == "":
                    game_on = True
                    if win_check == 9:
                        game_on = False
                        state = "tie"
                        ties = end_game_msg(player_1_wins, ties, player_2_wins, state, opponent)
                else:
                    game_on = False
                    if cont == 'win':
                        state = "win"
                        player_1_wins = end_game_msg(player_1_wins, ties, player_2_wins, state, opponent)
                    else:
                        state = "lose"
                        player_2_wins = end_game_msg(player_1_wins, ties, player_2_wins, state, opponent)
        else:
            game_on = False
            if cont == 'win':
                state = "win"
                player_1_wins = end_game_msg(player_1_wins, ties, player_2_wins, state, opponent)
            else:
                state = "lose"
                player_2_wins = end_game_msg(player_1_wins, ties, player_2_wins, state, opponent)
    update_hs(player_1_wins, ties, player_2_wins, opponent)

#CHECKS TO SEE IF PLAYER WANTS ANOTHER GAME AND CHECK FOR VALID INPUTS
    another = True
    while another:
        again = input("Would you like to play again? 'Y' or 'N'\n").upper()
        if again == 'Y':
            another = False
        elif again != "Y" and again != "N":
            print("Choice not recognised, please try again.")
        else:
            print("Goodbye!")
            another = False
            game_running = False
