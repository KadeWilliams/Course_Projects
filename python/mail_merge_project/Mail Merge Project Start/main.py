with open('Input/Names/invited_names.txt', 'r') as f_names:
    for name in f_names.readlines():
        name = name.strip()
        with open('Input/Letters/starting_letter.txt', 'r') as f_letter:
            letter = f_letter.read()
            complete_letter = letter.replace('[name]', name)
            with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as f_completed:
                f_completed.write(complete_letter)

