import random


def guess_random_number(tries, start, stop):
    number = random.randint(start, stop)
    past_guess = []
    while tries != 0:
        print("π₯ Number of tries left: π₯", tries)
        while True:
            guess = input(f"Guess a number between {start} and {stop}: ")

            if guess.isnumeric() == False or (int(guess) < start or int(guess) > stop):
                print(
                    f"Please enter ONLY numbers between --> {start} and {stop} <--")
            elif guess in past_guess:
                print(
                    f"You already guessedπ number {guess} <-- Please try again -->")
            else:
                past_guess.append(guess)
                # print(past_guess)
                break
        if int(guess) == number:
            print("πΉπΉπΉ YES! It's the correct answer! πΉπΉπΉ")
            return
        if int(guess) < number:
            print("Guess higher!πΊ")
        else:
            print("π»Guess lower!")
        tries -= 1
        if tries == 0:
            print("You've used all your tries.βββ You failed. βββ")
            print(f"The guess number is {number}πΌ!")
            return


def guess_random_num_linear(tries, start, stop):
    number = random.randint(start, stop)
    print("The number for the program to guess isπ:", number)

    for i in range(start, stop + 1):
        print("Number of tries left:π‘", tries)
        print("------------------------------")
        print("The program is guessing...", i)
        if i == number:
            print("π πΌπΌπΌ The program has guessed the correct number! πΌπΌπΌ π")
            return True
        else:
            tries -= 1
            if tries == 0:
                print("βββ The program has failed to guess the correct number. βββ")
                return False


def guess_random_num_binary(tries, start, stop):
    number = random.randint(start, stop)
    print("Random number to find:π", number)

    while start <= stop:
        pivot = (start + stop) // 2
        if pivot == number:
            print("π©π©π© Found it! π©π©π©", number)
            return
        if pivot > number:
            stop = pivot - 1
            print("π»Guessing lower!")
        else:
            start = pivot + 1
            print("Guessing higher!πΊ")
        tries -= 1
        if tries == 0:
            print("βββ Your program failed to find the number. βββ")
            return


def guess_menu():
    tries = int(input("\nπ° Enter number of tries π°: "))
    start = int(input("Enter start valueβ: "))
    stop = int(input("Enter end valueβ: "))

    while True:
        method = input(
            "\nPress 1 to guess manually: \n"
            "Press 2 to search linearly: \n"
            "Press 3 to perform binary search: \n"
            "Press 'Q' to quit: ").lower()
        if method.isnumeric():
            if method == '1':
                guess_random_number(tries, start, stop)
                continue
            if method == '2':
                guess_random_num_linear(tries, start, stop)
                continue
            if method == '3':
                guess_random_num_binary(tries, start, stop)
                continue
        elif method == 'q':
            break
        else:
            print()
            print(
                "Wrong Input βββ!!! Try AgainπΎ! ONLY NUMBERS! --> 1 - 2 - 3 or 'Quit' : \n")
            continue


def gambling_mode():
    player_money = 10
    while True:
        print("\n")
        print("Your balance is: π²", player_money)
        print("β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄β΄")
        print("βMake a bet. Will computer guess correctly or notβ")
        call = input(
            "Enter 'Y' --> to guess computer WILLβ guess the correct numberπ°\n"
            "Enter 'N' --> to guess computer WILL NOTπ guess the correct number\n"
            "------------------------------------------------------------------\n"
            "Enter your prediction: βΆ 'Y' [yes] π΅ or [no] βΆ  'N': ").lower()
        print("\n")
        bet = input("How many dollars will you bet? Enter 1 to 10: ")

        if bet.isnumeric():
            result = guess_random_num_linear(5, 0, 10)
            if result == True and call == 'y':
                player_money += int(bet)
                print("πΈπΈπΈπΈ You won! You now have π°π°π°π²", player_money)
            elif result == False and call == 'y':
                player_money -= int(bet)
                print("---> You lost. You now have π°π°π°π²", player_money)
            elif result == True and call == 'n':
                player_money -= int(bet)
                print("---> You lost. You now have π°π°π°π²", player_money)
            elif result == False and call == 'n':
                player_money += int(bet)
                print("πΈπΈπΈπΈ You won! You now have π°π°π°π²", player_money)

            if player_money <= 0:
                print("π­π­π­ Game Over π’π’π’")
                return
            if player_money >= 50:
                print("π€π€π€ You have over π°π°π°π²50. You win! πππ")
                return
        else:
            print()
            print("Wrong Input βββ!!! Try AgainπΎ\n")
            continue


# Test Driver Code 1ssss
# guess_random_number(6, 0, 100)

# Test Task 2
# guess_random_num_linear(5, 0, 10)

# Test Task 3
# guess_random_num_binary(5, 0, 100)

# Bonus Task 2
# guess_menu()

# Bonus Task 4
# gambling_mode()
