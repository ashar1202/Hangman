""" Hangman Game"""

#from words import get_random_word
from random_word import RandomWords
r = RandomWords()


def user_input():
    val = input("How many incorrect attempts you want? ")
    try:
        val = int(val)
    except ValueError:
        print('The value passed is not integer, Please pass the integer only')
        user_input()
    print(val)
    return val

def len_of_word():
    val = imput('what minimum word length you want?')
    try:
        val = int(val)
    except ValueError:
        print('The value entered is not integer, Please pass the integer value')
        len_of_word()
    print(val)
    return val


def wordenc(str):
    a = '*'
    len_of_str = len(str)
    while len_of_str > 1:
        a = a + '*'
        len_of_str = len_of_str-1
    return a

def evaluate(val,str,enc_str):
    previous_letter = None
    str_len = len(str)-1
    while val > 0 and str_len >= 0:
        print('Attempts Remainig', val)
        print('Previous Word', previous_letter)
        word_in = input('Choose the next letter')

        if word_in in str:
            pos = str.find(word_in)
            temp = list(enc_str)
            temp[pos] = word_in
            str_new = "".join(temp)
            str_len = str_len - 1
            print('Your word is', str_new)
            enc_str = str_new
            previous_letter = word_in

        else:
            val = val-1
            print(word_in,' is not in the word')


def main():
    print('Starting the Hangman game')
    val_in = user_input()
    word_len = len_of_word()
    print('Selecting a word...')
    sel_word = r.get_random_word(word_len)
    print(sel_word)
    enc_val = wordenc('Mark')
    print('Word:', enc_val)
    evaluate(val_in ,'Mark', enc_val)



if __name__ == '__main__' :
    main()




