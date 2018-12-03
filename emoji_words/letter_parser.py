import yaml
from functools import reduce

with open('emoji_words/letters.yaml', "r") as f:
    letters = yaml.load(f)


# change letter into 3x5 binary representation
def letter_to_binary(letter):
    binary_temp = [[unit for unit in '{0:b}'.format(int(row))] for row in str(letters[letter])]
    return [["0"]*(3-len(unit)) + unit for unit in binary_temp]


# change word into list of binary representations
def word_to_binary(word):
    return [letter_to_binary(letter) for letter in word]


# add letters together with spacer
def letter_plus_letter(a, b):
    return [x + ['0'] + y for x, y in zip(a, b)]


# join rows of words
def word_to_rows(word):
    return [''.join(['0'] + row + ['0']) for row in reduce(letter_plus_letter, word_to_binary(word))]


# change word into list of rows of emoji given foreground and background
def word_to_emoji(word, background, foreground):
    row_len = len(word)*3 + len(word) + 1
    inner_word = [x.replace('0', background).replace('1', foreground) for x in word_to_rows(word.lower())]
    return [''.join([background]*row_len)] + inner_word + [''.join([background]*row_len)]


def print_emoji_word(word, background, foreground):
    for x in word_to_emoji(word, background, foreground):
        print(x)
    return None
