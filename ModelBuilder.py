# authorized libraries: NumPy, math, re, sys, Matplotlib.
# read all text files and build  vocabulary
import copy
import os, re, math, operator
# todo: uncomment ploting in spyder 3

import matplotlib.pyplot as plt



class ModelBuilder:

    # ctor
    def __init__(self, directory_str):
        self.directory_str = directory_str

        self.ham_file_count = 0
        self.ham_word_count = 0
        self.ham_dictionary = dict()
        self.ham_prior = 0

        self.spam_file_count = 0
        self.spam_word_count = 0
        self.spam_dictionary = dict()
        self.spam_prior = 0

        self.vocabulary = dict()
        self.vocabulary_size = 0
        self.file_count = 0
        self.word_count = 0

        self.char_encoding = 'iso-8859-1'

        self.test_results = []
        self.stop_words_set = set()

        self.classes = ['ham', 'spam']
        # self.stop_vocabulary = {}

    # getters

    def get_ham_dictionary(self):
        return self.ham_dictionary

    def get_ham_file_count(self):
        return self.ham_file_count

    def get_spam_file_count(self):
        return self.spam_file_count

    def get_spam_dictionary(self):
        return self.spam_dictionary

    def get_vocabulary_size(self):
        return self.vocabulary_size

    # methods
    def extractWords(self):

        directory = os.fsencode(self.directory_str)

        for file in os.listdir(directory):
             filename = os.fsdecode(file)
             if filename.endswith('.txt'): # just .txt for all files, isolated the 1st one for testing
                 if 'ham' in filename:
                    self.ham_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r', encoding=self.char_encoding)
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


                 elif 'spam' in filename:
                    self.spam_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r', encoding=self.char_encoding)
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

    def extract_non_stop_words(self):

        directory = os.fsencode(self.directory_str)

        for file in os.listdir(directory):
             filename = os.fsdecode(file)
             if filename.endswith('.txt'): # just .txt for all files, isolated the 1st one for testing
                 if 'ham' in filename:
                    self.ham_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r', encoding=self.char_encoding)
                    line_index = 0
                    for line in input_file:
                        line_index += 1
                        line = line.lower()
                        # aString = 1
                        line_arr = re.split('[^a-zA-Z]', line)
                        line_arr = list(filter(None, line_arr))

                        #IGNORE WORDs IF IN STOP WORD SET
                        if len(self.stop_words_set)>0:
                            # print('length of stop word set = ', len(self.stop_words_set))
                            for word in line_arr:
                                if word in self.stop_words_set:
                                    continue
                                else:
                                    if word in self.ham_dictionary:
                                        self.ham_dictionary[word] += 1
                                    else:
                                        self.ham_dictionary[word] = 1



                 elif 'spam' in filename:
                    self.spam_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r', encoding=self.char_encoding)
                    line_index = 0
                    for line in input_file:
                        line_index += 1
                        line = line.lower()
                        # aString = 1
                        line_arr = re.split('[^a-zA-Z]', line)
                        line_arr = list(filter(None, line_arr))

                        if len(self.stop_words_set)>0:
                            # print('length of stop word set = ', len(self.stop_words_set))
                            for word in line_arr:
                                if word in self.stop_words_set:
                                    continue
                                else:
                                    if word in self.spam_dictionary:
                                        self.spam_dictionary[word] += 1
                                    else:
                                        self.spam_dictionary[word] = 1

        self.ham_word_count = sum(self.ham_dictionary.values())
        self.spam_word_count = sum(self.spam_dictionary.values())


    def extract_words_of_length(self, min_length, max_length):

        directory = os.fsencode(self.directory_str)

        for file in os.listdir(directory):
             filename = os.fsdecode(file)
             if filename.endswith('.txt'): # just .txt for all files, isolated the 1st one for testing
                 if 'ham' in filename:
                    self.ham_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r', encoding=self.char_encoding)
                    line_index = 0
                    for line in input_file:
                        line_index += 1
                        line = line.lower()
                        # aString = 1
                        line_arr = re.split('[^a-zA-Z]', line)
                        line_arr = list(filter(None, line_arr))

                        for word in line_arr:
                            if len(word) > min_length and len(word) < max_length:
                                if word in self.ham_dictionary:
                                    self.ham_dictionary[word] += 1
                                else:
                                    self.ham_dictionary[word] = 1


                 elif 'spam' in filename:
                    self.spam_file_count +=1
                    file_path = os.path.join(self.directory_str, filename)
                    # print(file_path)
                    input_file = open(file_path, 'r', encoding=self.char_encoding)
                    line_index = 0
                    for line in input_file:
                        line_index += 1
                        line = line.lower()
                        # aString = 1
                        line_arr = re.split('[^a-zA-Z]', line)
                        line_arr = list(filter(None, line_arr))

                        for word in line_arr:
                            if len(word) > min_length and len(word) < max_length:
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
        # calculating priors
        self.ham_prior = self.ham_file_count/self.file_count
        self.spam_prior = self.spam_file_count/self.file_count


    def printVocabulary(self, limit):
        if limit == 0:
            max = 100000
        else:
            max = limit
        i = 0
        for key, value in sorted(self.vocabulary.items()): #check the first 10 words
            i+=1
            if i <= max:
                print(key, ':', value)


    def printVocabularyInfo(self):
        print('vocabulary_size:', self.vocabulary_size)
        print('file_count:', self.file_count)
        print('word_count:', self.word_count)


    def smoothProbability(self, delta):

        smoothed_ham_word_count = self.ham_word_count + delta*self.vocabulary_size
        smoothed_spam_word_count = self.spam_word_count + delta*self.vocabulary_size

        for word in self.vocabulary:
            self.vocabulary.get(word)[1] = (self.vocabulary.get(word)[0]+delta)/ smoothed_ham_word_count
            self.vocabulary.get(word)[3] = (self.vocabulary.get(word)[2]+delta) / smoothed_spam_word_count


    def outputModelFile(self, folder, fileName):

        new_doc_path = os.path.join(folder, fileName)
        file = open(new_doc_path, 'w+', encoding=self.char_encoding)
        line_counter=0
        for key, value in sorted(self.vocabulary.items()):  # check the first 10 words
            line_counter += 1
            line_str = str(line_counter) + '  ' + key + '  ' + str(value[0]) + '  ' \
                       + str(value[1]) + '  ' + str(value[2]) + '  ' + str(value[3]) + '\r'
            file.write(line_str)
            # print(key, ':', value)

        file.close()


    def testModel(self, test_directory_str):
        print('Testing the built model on the testing set.')
        directory = os.fsencode(test_directory_str)
        # calculate both score
        file_count = 0
        for file in os.listdir(directory):
            file_count += 1
            score_ham = math.log10(self.ham_prior)
            score_spam = math.log10(self.spam_prior)

            new_document = os.fsdecode(file)
            if new_document.endswith('.txt'):  # just .txt for all files, isolated the 1st one for testing
                new_doc_path = os.path.join(test_directory_str, new_document)

                # apple.decode('iso-8859-1').encode('utf8')

                new_doc = open(new_doc_path, 'r', encoding=self.char_encoding)
                line_index = 0
                for line in new_doc:
                    line_index += 1
                    line = line.lower()
                    line_wrd_list = re.split('[^a-zA-Z]', line)
                    line_wrd_list = list(filter(None, line_wrd_list))

                    for word in line_wrd_list:
                        if word in self.vocabulary:
                            score_ham += math.log10(self.vocabulary.get(word)[1])
                            score_spam += math.log10(self.vocabulary.get(word)[3])
                # print('score_ham: ', score_ham,'score_spam:', score_spam)

            if (score_ham > score_spam):
                predicted_category = 'ham'
            else:
                predicted_category = 'spam'

            if 'ham' in new_document:
                real_category = 'ham'
            else:
                real_category = 'spam'

            if (predicted_category == real_category):
                decision = 'right'
            else:
                decision = 'wrong'

            # print(file_count, ' ', new_document, ' ', predicted_category, ' ', score_ham,
            #       ' ', score_spam, ' ', real_category, ' ', decision)

            file_result_str = str(file_count) + '  ' + new_document + '  ' + predicted_category + '  '\
                              + str(score_ham) + '  ' + str(score_spam) + '  ' + real_category + '  ' + decision

            self.test_results.append(str(file_result_str))


    def outputTestFile(self, folder, fileName):
        print('Outputting the test results to a .txt file.')
        new_doc_path = os.path.join(folder, fileName)
        file = open(new_doc_path, 'w+', encoding=self.char_encoding)
        for result_str in self.test_results:  # check the first 10 words
            line_str = result_str + '\r'
            file.write(line_str)
            # print(key, ':', value)
        file.close()


    def read_stop_word(self, stopwords_str):
        filename = os.fsdecode(stopwords_str)
        if filename.endswith('.txt'):
            input_file = open(filename, 'r', encoding=self.char_encoding)
            # read every stop word.
            for line in input_file:
                # line_index += 1
                stop_word = line.lower().rstrip()
                self.stop_words_set.add(stop_word)
        self.stop_words_set.remove('')
        # print('set of stop word: ',self.stop_words_set)


    def remove_less_freq_wrd(self, freq_int):

        # copy to a new temp dictionary only if matches criteria
        temp_vocabulary = dict()

        # remove words of freq = 1 from the vocabulary
        for word, value in self.vocabulary.items():
            ham_freq = self.vocabulary.get(word)[0]
            spam_freq = self.vocabulary.get(word)[2]
            word_freq = ham_freq + spam_freq
            if (word_freq > freq_int):
                temp_vocabulary[word] = value

        self.vocabulary = temp_vocabulary
        # re adjust the vocabulary
        self.vocabulary_size = len(self.vocabulary)

        self.ham_word_count = 0
        self.spam_word_count = 0
        for word in self.vocabulary:
            self.ham_word_count += self.vocabulary.get(word)[0]
            self.spam_word_count += self.vocabulary.get(word)[2]

        # update total
        self.word_count = self.ham_word_count + self.spam_word_count


    def remove_most_freq_wrd(self, percentage):
        word_freq_vocab = []

        for word, value in self.vocabulary.items():

            ham_freq = self.vocabulary.get(word)[0]
            spam_freq = self.vocabulary.get(word)[2]
            word_freq = ham_freq + spam_freq
            # add each word and his frequency as tuple
            word_freq_vocab.append((word, word_freq))

        # sort the list of words base on their frequence
        word_freq_vocab.sort(key=operator.itemgetter(1), reverse = True)
        # print('word_freq_vocab = ',word_freq_vocab)
        # identify the top most frequent words
        top_n_words = round(percentage/100*len(word_freq_vocab))
        # print('the top', percentage, '% to int = ', top_n_words)
        words_to_remove = word_freq_vocab[0:top_n_words]
        # print('words_to_remove =',words_to_remove)

        # remove the words

        for word_to_remove in words_to_remove:
            key = word_to_remove[0]
            # print('key =', key)
            if key in self.vocabulary:
                del self.vocabulary[key]

        # re adjust the vocabulary info
        self.vocabulary_size = len(self.vocabulary)
        self.ham_word_count = 0
        self.spam_word_count = 0
        for word in self.vocabulary:
            self.ham_word_count += self.vocabulary.get(word)[0]
            self.spam_word_count += self.vocabulary.get(word)[2]
        # update total
        self.word_count = self.ham_word_count + self.spam_word_count


    def calculateAccuracy(self, folder, result_txt_str):
        # print(result_txt_str)
        file_path = os.path.join(folder, result_txt_str)
        filename = os.fsdecode(file_path)

        test_file = open(filename, 'r', encoding=self.char_encoding)
        count_row = 0
        count_A = 0 #right classification
        for line in test_file:
            count_row += 1
            line = line.lower().rstrip()
            line_arr = line.split('  ')
            # print(line_arr)
            result = line_arr[6]#end of the line where the result is stored
            if result == 'right':
                count_A+=1

        accuracy = (count_A/count_row)*100

        return accuracy


    def precision_recall(self, folder, result_txt_str, class_eval, opp_class):
        # print(result_txt_str)
        file_path = os.path.join(folder, result_txt_str)
        filename = os.fsdecode(file_path)

        test_file = open(filename, 'r', encoding=self.char_encoding)
        count_row = 0
        count_A = 0  # right classification
        count_B = 0  # classified as spam but ham
        count_C = 0
        count_D = 0

        for line in test_file:
            count_row += 1
            line = line.lower().rstrip()
            line_arr = line.split('  ')
            # print(line_arr)
            classified_as = line_arr[2]
            actual_class = line_arr[5]
            result = line_arr[6]

             # end of the line where the result is stored
            if classified_as == class_eval and actual_class == class_eval and result == 'right':
                count_A += 1

            if classified_as == class_eval and actual_class == opp_class and result == 'wrong':
                count_B += 1

            if classified_as == opp_class and actual_class == class_eval and result == 'wrong':
                count_C += 1

            if classified_as == opp_class and actual_class == opp_class and result == 'right':
                count_D += 1

        print(class_eval, 'count A =', count_A, 'count B = ',count_B, 'count C =',count_C, 'count D =',count_D)

        precision = (count_A / (count_A+count_B)) * 100
        recall = (count_A / (count_A + count_C)) * 100


        return precision, recall

    # beta represents the relative importance of precision and recall when 1 both are equal
    def f_measure(self, precision, recall, beta):
        f_measure = ((pow(beta,2)+1)*precision*recall)/((pow(beta,2)*precision)+recall)
        return  f_measure

    


# output to model.txt in alphabetical order
# lineCount  word  frequencyInHam  smoothedProbHam  frequencyInSpam  smoothedProbSpam returnChar
# @staticmethod

def base_experiment():
    separator = ('=' * 50) + '\r'
    delta = 0.5
    train_folder_str = 'train'
    test_folder_str = 'test'
    #
    # TASK 1 AND 2: BASE EXPERIMENT
    #
    dirName = 'base'

    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    print(separator)
    print('BASE MODEL:')
    print(separator)
    model = ModelBuilder(train_folder_str)
    model.extractWords()
    model.printCategoryInfo('ham')
    model.printCategoryInfo('spam')
    model.buildVocabulary()
    model.printVocabularyInfo()
    model.smoothProbability(delta)
    # print('BASE MODEL SAMPLE = ')
    # model.printVocabulary(10)
    model.outputModelFile(dirName, 'baseline-model.txt')
    # switch output for demo
    # model.outputModelFile(dirName, 'demo-model-base.txt')
    # Task2 test the model
    model.testModel(test_folder_str)
    result_str = 'baseline-result.txt'
    model.outputTestFile(dirName, result_str)
    # model.outputTestFile(dirName, 'demo-result-base.txt')
    # evaluate accuracy
    accuracy = model.calculateAccuracy(dirName, result_str)
    print('accuracy =', accuracy)
    for eval_class in model.classes:
        if eval_class == 'ham':
            opp_class = 'spam'
        else:
            opp_class = 'ham'
        precision, recall = model.precision_recall(dirName, result_str, eval_class, opp_class)
        print(eval_class,'precision =', precision, 'recall = ', recall)
        beta = 1
        f1_measure = model.f_measure(precision, recall, beta)
        print(eval_class, 'f1_measure =', f1_measure)


def experiment_2():
    separator = ('=' * 50) + '\r'
    delta = 0.5
    train_folder_str = 'train'
    test_folder_str = 'test'
    #
    # TASK 3 EXPERIMENT 2: STOP WORDS
    #
    dirName = 'exp_2'

    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")

    print(separator)
    print('STOP WORDS MODEL:')
    print(separator)
    stop_model = ModelBuilder(train_folder_str)
    stop_words_str = 'English-Stop-Words.txt'
    stop_model.read_stop_word(stop_words_str)
    stop_model.extract_non_stop_words()
    stop_model.printCategoryInfo('ham')
    stop_model.printCategoryInfo('spam')
    stop_model.buildVocabulary()
    stop_model.printVocabularyInfo()
    stop_model.smoothProbability(delta)
    # print('STOP MODEL SAMPLE= ')
    # stop_model.printVocabulary(10)
    stop_model.outputModelFile(dirName, 'stopword-model.txt')
    # stop_model.outputModelFile(dirName, 'demo-model-exp2.txt')
    stop_model.testModel(test_folder_str)
    result_str = 'stopword-result.txt'
    stop_model.outputTestFile(dirName, result_str)
    # stop_model.outputTestFile(dirName, 'demo-result-exp2.txt')
    accuracy = stop_model.calculateAccuracy(dirName, result_str)
    print('accuracy =', accuracy)
    for eval_class in stop_model.classes:
        if eval_class == 'ham':
            opp_class = 'spam'
        else:
            opp_class = 'ham'
        precision, recall = stop_model.precision_recall(dirName, result_str, eval_class, opp_class)
        print(eval_class, 'precision =', precision, 'recall = ', recall)
        beta = 1
        f1_measure = stop_model.f_measure(precision, recall, beta)
        print(eval_class, 'f1_measure =', f1_measure)


def experiment_3():
    separator = ('=' * 50) + '\r'
    delta = 0.5
    train_folder_str = 'train'
    test_folder_str = 'test'
    #
    # TASK 3 EXPERIMENT 3: WORD LENGTH
    #
    dirName = 'exp_3'

    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


    print(separator)
    print('WORD LENGTH MODEL:')
    print(separator)
    word_length_model = ModelBuilder(train_folder_str)

    word_length_model.extract_words_of_length(2, 9)

    word_length_model.printCategoryInfo('ham')
    word_length_model.printCategoryInfo('spam')
    word_length_model.buildVocabulary()
    word_length_model.printVocabularyInfo()
    word_length_model.smoothProbability(delta)
    # print('WORD LENGTH MODEL SAMPLE= ')
    # word_length_model.printVocabulary(10)
    word_length_model.outputModelFile(dirName, 'wordlength-model.txt')
    # word_length_model.outputModelFile(dirName, 'demo-model-exp3.txt')
    word_length_model.testModel(test_folder_str)
    result_str = 'wordlength-result.txt'
    word_length_model.outputTestFile(dirName,result_str)
    # word_length_model.outputTestFile(dirName, 'demo-result-exp3.txt')
    accuracy = word_length_model.calculateAccuracy(dirName, result_str)
    print('accuracy =', accuracy)
    for eval_class in word_length_model.classes:
        if eval_class == 'ham':
            opp_class = 'spam'
        else:
            opp_class = 'ham'
        precision, recall = word_length_model.precision_recall(dirName, result_str, eval_class, opp_class)
        print(eval_class, 'precision =', precision, 'recall = ', recall)
        beta = 1
        f1_measure = word_length_model.f_measure(precision, recall, beta)
        print(eval_class, 'f1_measure =', f1_measure)


def experiment_4():
    separator = ('=' * 50) + '\r'
    delta = 0.5
    train_folder_str = 'train'
    test_folder_str = 'test'

    # for each key = model, store value (list) vocab size, accuracy
    frequency_chart_data = dict()

    #
    # TASK 3 EXPERIMENT 4: WORD FREQUENCY
    #
    dirName = 'exp_4'

    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")


    print(separator)
    print('WORD FREQUENCY INITIAL MODEL B:')
    print(separator)
    word_frequency_model = ModelBuilder(train_folder_str)

    word_frequency_model.extractWords()

    word_frequency_model.printCategoryInfo('ham')
    word_frequency_model.printCategoryInfo('spam')
    word_frequency_model.buildVocabulary()
    word_frequency_model.printVocabularyInfo()
    # word_frequency_model.printVocabulary(20)
    word_frequency_model.smoothProbability(delta)
    x=0
    model_str = 'word-frequency-model-B' + str(x) + '.txt'
    word_frequency_model.outputModelFile(dirName, model_str)
    # # model.outputModelFile('demo-model-exp3.txt')
    word_frequency_model.testModel(test_folder_str)
    result_str = 'word-frequency-result-B' + str(x) + '.txt'
    word_frequency_model.outputTestFile(dirName, result_str)

    model_name = 'b'+str(x)
    vocab_size = word_frequency_model.get_vocabulary_size()
    # evaluate accuracy
    accuracy = word_frequency_model.calculateAccuracy(dirName, result_str)
    data_point = [vocab_size, accuracy]
    print('accuracy = ', accuracy)
    frequency_chart_data[model_name] = data_point


    # push as chart data

    print(separator)

    for x in range(0, 25, 5):
        if x == 0:
            x += 1
        # print(x)
        word_frequency_model.remove_less_freq_wrd(x)
        word_frequency_model.smoothProbability(delta)

        print(separator)
        print('WORD FREQUENCY (LEAST) MODEL L', x)
        print(separator)
        word_frequency_model.printCategoryInfo('ham')
        word_frequency_model.printCategoryInfo('spam')
        word_frequency_model.printVocabularyInfo()
        model_str = 'word-frequency-model-L' + str(x) + '.txt'
        word_frequency_model.outputModelFile(dirName, model_str)
        # word_frequency_model.outputModelFile(dirName, 'demo-model-exp4.txt')
        word_frequency_model.testModel(test_folder_str)
        result_str = 'word-frequency-result-L' + str(x) + '.txt'
        word_frequency_model.outputTestFile(dirName, result_str)
        # word_frequency_model.outputTestFile(dirName, 'demo-result-exp4.txt')


        model_name = 'L' + str(x)
        vocab_size = word_frequency_model.get_vocabulary_size()
        # evaluate accuracy
        accuracy = word_frequency_model.calculateAccuracy(dirName, result_str)
        data_point = [vocab_size, accuracy]
        print('accuracy = ', accuracy)
        frequency_chart_data[model_name] = data_point
        print(separator)

    for x in range(5, 30, 5):
        # print(x)
        # remove top 5% used words
        word_frequency_model.remove_most_freq_wrd(x)
        word_frequency_model.smoothProbability(delta)

        print(separator)
        print('WORD FREQUENCY (MOST) MODEL M', x)
        print(separator)
        word_frequency_model.printCategoryInfo('ham')
        word_frequency_model.printCategoryInfo('spam')
        word_frequency_model.printVocabularyInfo()
        model_str = 'word-frequency-model-M' + str(x) + '.txt'
        word_frequency_model.outputModelFile(dirName, model_str)
        # word_frequency_model.outputModelFile(dirName, 'demo-model-exp4.txt')
        word_frequency_model.testModel(test_folder_str)
        result_str = 'word-frequency-result-M' + str(x) + '.txt'
        word_frequency_model.outputTestFile(dirName, result_str)
        # word_frequency_model.outputTestFile(dirName, 'demo-result-exp4.txt')


        model_name = 'M' + str(x)
        vocab_size = word_frequency_model.get_vocabulary_size()
        # evaluate accuracy
        accuracy = word_frequency_model.calculateAccuracy(dirName, result_str)
        data_point = [vocab_size, accuracy]
        print('accuracy = ', accuracy)
        frequency_chart_data[model_name] = data_point
        print(separator)

    x_data=[]
    y_data=[]
    #plot data on a chart
    for model, value in frequency_chart_data.items():
        x_data.append(value[0]) #vocab size
        y_data.append(value[1]) #accuracy

    # todo: uncomment ploting in spyder 3
    plt.plot(x_data, y_data)
    plt.ylabel('Classifier Accuracy')
    plt.xlabel('Vocabulary Size')
    plt.show()


def experiment_5():
    #CHANGE THE DELTA VALUE FROM 0 TO 1 IN 0.1 INCREMENTS
    separator = ('=' * 50) + '\r'
    delta = 0
    train_folder_str = 'train'
    test_folder_str = 'test'

    # for each key = model, store value (list) vocab size, accuracy
    delta_chart_data = dict()

    for j in range(0, 10, 1):
        # print(x)
        delta += 0.1
        delta = round(delta, 1)
        # print(delta)

        dirName = 'exp_5'

        try:
            # Create target Directory
            os.mkdir(dirName)
            print("Directory ", dirName, " Created ")
        except FileExistsError:
            print("Directory ", dirName, " already exists")

        print(separator)
        print('MODEL WITH DELTA = ', delta)
        print(separator)
        delta_variation_model = ModelBuilder(train_folder_str)

        delta_variation_model.extractWords()

        delta_variation_model.printCategoryInfo('ham')
        delta_variation_model.printCategoryInfo('spam')

        delta_variation_model.buildVocabulary()
        delta_variation_model.printVocabularyInfo()
        # word_frequency_model.printVocabulary(20)


        delta_variation_model.smoothProbability(delta)

        model_str = 'delta-variation-model-D' + str(delta) + '.txt'
        delta_variation_model.outputModelFile(dirName, model_str)
        # delta_variation_model.outputModelFile(dirName, 'demo-model-exp5.txt')
        delta_variation_model.testModel(test_folder_str)
        result_str = 'delta-variation-result-D' + str(delta) + '.txt'
        delta_variation_model.outputTestFile(dirName, result_str)
        # delta_variation_model.outputTestFile(dirName, 'demo-result-exp5.txt')


        model_name = 'D' + str(delta)
        # evaluate accuracy
        accuracy = delta_variation_model.calculateAccuracy(dirName, result_str)
        data_point = [delta, accuracy]
        print('accuracy = ', accuracy)
        delta_chart_data[model_name] = data_point



    x_data = []
    y_data = []
    # plot data on a chart
    for model, value in delta_chart_data.items():
        x_data.append(value[0])  # delta
        y_data.append(value[1])  # accuracy

    # todo: uncomment ploting in spyder 3
    plt.plot(x_data, y_data)
    plt.ylabel('Classifier Accuracy')
    plt.xlabel('Delta Value')
    plt.show()


def main():

    # base_experiment()
    
    experiment_2()
    #
    experiment_3()
    #
    # experiment_4()

    # experiment_5()




#run the main method
main()

