from os.path import isfile
from re import findall

class Statistical_Processing:

    def __init__(self, file_name):
        if not isinstance(file_name, str) or not isfile(file_name):
            raise Exception
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def name(self, file_name):
        if not isinstance(file_name, str) or not isfile(file_name):
            raise Exception
        self.__name = file_name

    def fnumber_of_charecters(self):
        number_of_charecters = 0
        file = open(self.file_name, 'r')
        for i in file:
                number_of_charecters += len(i)
        file.close()
        return number_of_charecters

    def fnumber_of_words(self):
        number_of_words = 0
        file = open(self.file_name, 'r')
        for line in file:
            number_of_words += len(findall('[`\-\w]+', line))
        file.close

        return number_of_words

    def fnumber_of_sentences(self):
        number_of_sentences = 0
        file = open(self.file_name, 'r')
        ind = False
        ch = file.read(1)
        while ch != '':
            if ind and (ch in ('!', '.', '?')):
                ind = False
            elif not ind and ch not in ('!', '.', '?'):
                ind = True
                number_of_sentences += 1
            ch = file.read(1)

        file.close()
        return number_of_sentences


reader = Statistical_Processing("text.txt")
print(reader.fnumber_of_charecters())
print(reader.fnumber_of_words())
print(reader.fnumber_of_sentences())