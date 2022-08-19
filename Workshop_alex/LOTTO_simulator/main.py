from random import shuffle

if __name__ == '__main__':

    print('Guess the six numbers between 1 and 49')
    num_id = 1
    guess_numbers = []

    while num_id < 7:
        try:
            guess_number = int(input(f'Guess the number {num_id}: '))
        except ValueError:
            print('You need to enter a integer!')
        else:
            if guess_number in guess_numbers or guess_number < 1 or guess_number > 49:
                print('number must be between 1 and 49, and not the same as earlier numbers!')
                continue
            else:
                guess_numbers.append(guess_number)
                num_id += 1

    all_6_nums = list(range(1, 49))
    shuffle(all_6_nums)
    rand_6_nums = all_6_nums[:6]

    rand_6_nums.sort()
    guess_numbers.sort()
    print(f"\nYour numbers:  {guess_numbers}\n"
          f"Drawn numbers: {rand_6_nums}\n")

    score = []
    for guess_num in guess_numbers:
        if guess_num in rand_6_nums:
            score.append(guess_num)

    if len(score) >= 3:
        print(f"\nCongratulations, you guessed {len(score)} numbers!")
    else:
        print(f"\nGuessed {len(score)} numbers, keep trying!")
