"""
Author:
    * Jeremiah D 'JD' Smith

Description:
    * Takes in texts and breaks them down to tokens/words
    * Then counts the frequency of the tokens/words
"""
import os
import operator
# imported because I can't use java based Porter stemmer
from nltk.stem import PorterStemmer

# TODO: Reformat entire code into functions and modules
# create list of stopwords
stop_list = []
# convert stopwords text to list
# TODO: ask for file of stopwords
with open('stopwords.txt', 'r') as stop_words:
    for entry in stop_words:
        stop_list.append(entry[:-1])

# alphabet will help eliminate unnecessary characters
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# list used to build a token/word character by characterc
word = []
# dictionary to count frequency of tokens/words
word_list = {}
porter = PorterStemmer()

# TODO: ask for directory of text(s)
# opening files in directory citeseer/
with os.scandir('citeseer') as filenames:
    for file in filenames:
        if file.is_file():
            with open(file, 'r') as f:
                # then breaking each file down line by line
                for line in f:
                    # then breaking each line down character by character
                    for character in line.lower():
                        # filtering out unnecessary characters
                        if character in alphabet:
                            # building token/word character by character
                            word.append(character)
                        else:
                            # completed token/word
                            current_word = ''.join(word)
                            # clearing word list to create new word
                            word.clear()
                            # filters stopwords
                            if current_word not in stop_list:
                                # stems the token
                                current_word = porter.stem(current_word)
                                if current_word not in word_list:
                                    # initializes a dictionary entry
                                    word_list[current_word] = 1
                                else:
                                    # adds to the frequency of the dictionary \
                                    # entry
                                    word_list[current_word] += 1
            f.close()

# sorts word_list by value as a list of tuples and types as a dictionary
sorted_dictionary = dict(sorted(word_list.items(), key=operator.itemgetter(1)))
                                # , reverse=True))  # show in ascending order
sorted_dictionary.pop('')
for keys, values in sorted_dictionary.items():
    print(keys, values)
