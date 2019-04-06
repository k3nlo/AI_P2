# authorized libraries: NumPy, math, re, sys, Matplotlib.

# read all text files and build  vocabulary




import os, re

class Builder:

# ctor

    def __init__(self, directory_str):
        self.directory_str = directory_str

        self.ham_file_count = 0
        self.ham_word_count = 0
        self.ham_dictionary = dict()

        self.spam_file_count = 0
        self.spam_word_count = 0
        self.spam_dictionary = dict()

        self.vocabulary = dict()
        self.vocabulary_size = 0
        self.file_count = 0
        self.word_count = 0

# getters

    def get_ham_dictionary(self):
        return self.ham_dictionary

    def get_spam_dictionary(self):
        return self.spam_dictionary


    def extractWords(self):
        directory = os.fsencode(self.directory_str)
        for file in os.listdir(directory):
             filename = os.fsdecode(file)
             if filename.endswith('.txt'): # just .txt for all files, isolated the 1st one for testing
                 if 'ham' in filename:
                    self.ham_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r')
                    line_index = 0
                    for line in input_file:
                        line_index += 1
                        line = line.lower()
                        # aString = 1
                        line_arr = re.split('[^a-zA-Z]', line)
                        line_arr = list(filter(None, line_arr))
                        for word in line_arr:
                            if word in self.ham_dictionary:
                                self.ham_dictionary[word] += 1
                            else:
                                self.ham_dictionary[word] = 1
                        # if line_index == 1:
                            # print('line_arr', line_arr)
                 elif 'spam' in filename:
                    self.spam_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r')
                    line_index = 0
                    for line in input_file:
                        line_index += 1
                        line = line.lower()
                        # aString = 1
                        line_arr = re.split('[^a-zA-Z]', line)
                        line_arr = list(filter(None, line_arr))
                        for word in line_arr:
                            if word in self.spam_dictionary:
                                self.spam_dictionary[word] += 1
                            else:
                                self.spam_dictionary[word] = 1

        self.ham_word_count = sum(self.ham_dictionary.values())
        self.spam_word_count = sum(self.spam_dictionary.values())


    def printDictionary(self, dictionary):
        # print('ham_dictionary:')
        for key, value in sorted(dictionary.items()):
            print(key,':', value)


    def printCategoryInfo(self, category_str):
        if category_str == 'ham':
            print('ham_file_count:', self.ham_file_count)
            print('ham_word_count:', self.ham_word_count)
        elif category_str == 'spam':
            print('spam_file_count:', self.spam_file_count)
            print('spam_word_count:', self.spam_word_count)

    def buildVocabulary(self):
        for word in self.ham_dictionary:
            # add every new word form ham
            self.vocabulary[word] = [self.ham_dictionary.get(word), 0, 0, 0]

        for word in self.spam_dictionary:
            if word in self.vocabulary:
                self.vocabulary.get(word)[2] = self.spam_dictionary.get(word)
            else:
                # spam new words:
                self.vocabulary[word] = [0, 0, self.spam_dictionary.get(word), 0]

        self.file_count = self.ham_file_count + self.spam_file_count
        self.word_count = self.ham_word_count + self.spam_word_count
        self.vocabulary_size = len(self.vocabulary)

    def printVocabulary(self):
        i = 0
        for key, value in sorted(self.vocabulary.items()): #check the first 10 words
            i+=1
            if i <=10:
                print(key, ':', value)


    def printVocabularyInfo(self):
        print('vocabulary_size:', self.vocabulary_size)
        print('file_count:', self.file_count)
        print('word_count:', self.word_count)


    def calculateSmoothedProbability(self, delta):
        smoothed_ham_word_count = self.ham_word_count + delta*self.vocabulary_size
        smoothed_spam_word_count = self.spam_word_count + delta*self.vocabulary_size

        for word in self.vocabulary:
            self.vocabulary.get(word)[1] = (self.vocabulary.get(word)[0]+delta)/ smoothed_ham_word_count
            self.vocabulary.get(word)[3] = (self.vocabulary.get(word)[2]+delta) / smoothed_spam_word_count

    def outputFile(self, fileName):
        file = open(fileName, 'w+')
        line_counter=0
        for key, value in sorted(self.vocabulary.items()):  # check the first 10 words
            line_counter += 1
            line_str = str(line_counter) + '  ' + key + '  ' + str(value[0]) + '  ' \
                       + str(value[1]) + '  ' + str(value[2]) + '  ' + str(value[3]) + '\r'
            file.write(line_str)
            # print(key, ':', value)

        file.close()


# output to model.txt in alphabetical order
# lineCount  word  frequencyInHam  smoothedProbHam  frequencyInSpam  smoothedProbSpam returnChar
# @staticmethod
def main():
    folder_str = 'train'
    model_builder = Builder(folder_str)
    model_builder.extractWords()
    # ham_dict = word_reader.get_ham_dictionary()
    # spam_dict = word_reader.get_spam_dictionary()
    model_builder.printCategoryInfo('ham')
    # word_reader.printDictionary(ham_dict)
    model_builder.printCategoryInfo('spam')
    # word_reader.printDictionary(spam_dict)
    model_builder.buildVocabulary()
    model_builder.printVocabularyInfo()
    # word_reader.printVocabulary()
    # 0.5 smoothing for conditional probability
    delta = 0.5
    model_builder.calculateSmoothedProbability(delta)
    print('VOCABULARY = ')
    model_builder.printVocabulary()
    model_builder.outputFile('model.txt')

#run the main method
main()
