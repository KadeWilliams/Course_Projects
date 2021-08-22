import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet_dict = {row.letter: row.code for index, row in df.iterrows()}

def generate_phonetic():
    word = input('Enter a word: ').upper()
    try:
        letter = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the English alphabet please.")
        generate_phonetic()
    else:
        print(letter)

generate_phonetic()
