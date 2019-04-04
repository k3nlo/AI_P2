# authorized libraries: NumPy, math, re, sys, Matplotlib.

# read all text files and build  vocabulary



# print('building vocabulary...')

import os, re

directory_str = 'train'
directory = os.fsencode(directory_str)

ham_file_count = 0
ham_dictionary = dict()
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith('00001.txt'): # just .txt for all files, isolated the 1st one for testing
         if 'ham' in filename:
            ham_file_count +=1
            file_path = os.path.join(directory_str, filename)
            print(file_path)
            input_file = open(file_path, 'r')
            line_index = 0
            for line in input_file:
                line_index += 1
                line = line.lower()
                # aString = 1
                line_arr = re.split('[^a-zA-Z]', line)
                line_arr = list(filter(None, line_arr))
                for word in line_arr:
                    if word in ham_dictionary:
                        ham_dictionary[word] += 1
                    else:
                        ham_dictionary[word] = 1
                # if line_index == 1:
                    # print('line_arr', line_arr)

         # print(directory, filename)
         continue
     else:
         continue
print('ham_dictionary:')
for key, value in sorted(ham_dictionary.items()):
    print(key,':', value)

# each word frequencies

# each word probability per class

# for ham / spam

# loop: for each file in the train folder
    # open file

    # lower case

    # tokenize it (split) each word re.split(’\[\^a-zA-Z\]’,aString)


# vocabulary = set of all words

# for each word: save frequency, conditional class/probability

# smooth with delta = 0.5

# output to model.txt in alphabetical order
# lineCount  word  frequencyInHam  smoothedProbHam  frequencyInSpam  smoothedProbSpam returnChar


