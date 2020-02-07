# This program reads text from a file, then prints out the word count.

import re

def read_file():
    try:
        f = open('test.txt','r')
        word_split = []
        for line in f:
            # removes punctuation with regex
            line = re.sub(r'[^\w\s]','', line)

            # adds words to a list and is split based on space
            word_split += line.split(' ')
    except:
        print('Error: Could not find file or read data')
    else:
        f.close()
        
        #return length of the list, i.e. the words within the text file
        return len(word_split)

print(f"This file contains {read_file()} words")