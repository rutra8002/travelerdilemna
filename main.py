import inspect
def get_first_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):
    functionname = inspect.currentframe().f_code.co_name
    if functionname == "get_first_player_choice":
        source_code = inspect.getsource(get_second_player_choice)
        exec(source_code)
        return min(max(get_second_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices) -10, 20), 100)
    elif functionname == "get_second_player_choice":
        source_code = inspect.getsource(get_first_player_choice)
        exec(source_code)
        return min(max(get_first_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices) -10, 20), 100)
    else:
        return 20
def get_second_player_choice(current_round, your_score, enemy_score, your_choices, enemy_choices):
        if current_round == 0:
            return 20
        else:
            counter = 0
            sum = 0
            for item in enemy_choices:
                if item > 0:
                    counter += 1
                    sum += item
            if len(enemy_choices) > 0 and enemy_choices[-1] == your_choices[-1]:
                result = round(sum / counter) - 10
            if your_score == enemy_score:
                result = round(sum / counter)
            elif your_score < enemy_score:
                result = round(sum / counter) + 10
            elif your_score > enemy_score:
                result = round(sum / counter) - 10
            return round(min(max(result, 20), 100))
def game():
    min_price = 20
    max_price = 100
    bonus = 10
    rounds = 100

    first_player_choices = [0 for i in range(0, rounds)]
    second_player_choices = [0 for i in range(0, rounds)]
    first_player_total_score = 0
    second_player_total_score = 0

    for currentRound in range(0, rounds):
        first_player_choices_temp = []
        second_player_choices_temp = []
        for i in range(0, rounds):
            first_player_choices_temp.append(first_player_choices[i])
            second_player_choices_temp.append(second_player_choices[i])
        first_player_choice = get_first_player_choice(currentRound, first_player_total_score, second_player_total_score,
                                                      first_player_choices_temp, second_player_choices_temp)

        first_player_choices_temp = []
        second_player_choices_temp = []
        for i in range(0, rounds):
            first_player_choices_temp.append(first_player_choices[i])
            second_player_choices_temp.append(second_player_choices[i])
        second_player_choice = get_second_player_choice(currentRound, second_player_total_score,
                                                        first_player_total_score, second_player_choices_temp,
                                                        first_player_choices_temp)

        first_player_choices[currentRound] = first_player_choice
        second_player_choices[currentRound] = second_player_choice

        first_player_score = -1
        second_player_score = -1

        if first_player_choice < min_price or first_player_choice > max_price:
            first_player_score = 0
            if min_price <= second_player_choice <= max_price:
                second_player_score = second_player_choice + bonus

        if second_player_choice < min_price or second_player_choice > max_price:
            second_player_choice = 0
            if min_price <= first_player_choice <= max_price:
                first_player_score = first_player_choice + bonus

        if first_player_score == -1 and second_player_score == -1:
            if first_player_choice == second_player_choice:
                first_player_score = second_player_score = first_player_choice
            elif first_player_choice < second_player_choice:
                first_player_score = first_player_choice + bonus
                second_player_score = first_player_choice - bonus
            else:
                first_player_score = second_player_choice - bonus
                second_player_score = second_player_choice + bonus

        first_player_total_score += first_player_score
        second_player_total_score += second_player_score

        print("First player choice: {0} and score: + {1} (= {2}), second player choice {3} and score: + {4} (= {5}).\n"
              .format(first_player_choice, first_player_score, first_player_total_score, second_player_choice,
                      second_player_score, second_player_total_score))

    print("First player score: {0}, second player score: {1}.".format(first_player_total_score,
                                                                      second_player_total_score))
    print("First player choices: ", first_player_choices)
    print("Second player choices: ", second_player_choices)


if __name__ == '__main__':
    game()
