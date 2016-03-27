import os
import random
import string

class HockeyIpsum:
    MAX_PARAGRAPHS = 10

    def __init__(self, directory = "/wordbank"):
        self.files = []
        self.words = []
        self.wordbank_dir = "." + directory + "/"
        self._loadfiles()
        self._readfiles()

    def _loadfiles(self):
        for f in os.listdir(self.wordbank_dir):
            if f.endswith(".txt"):
                self.files.append(self.wordbank_dir + f)

    def _readfiles(self):
        i = 0;
        for filename in self.files:
            f = open(filename, 'r')
            for line in f:
                self.words.append(line.rstrip())
                i = i+1
            f.close()

    def printwordbank(self):
        for w in self.words:
            print w

    #getwords returns a string size number of entries from the wordbank
    def getwords(self, size):
        tmp_words = []
        max_index = len(self.words) - 1

        for i in range(size):
            tmp_words.append(self.words[random.randrange(0, max_index, 1)])
        return ' '.join(tmp_words)

    #gettitle returns a 1-5 words string.
    def gettitle(self):
        num_words = random.randrange(1,5,1)
        return string.capwords(self.getwords(num_words))

    #sentence has capitalized first word and ends with a period.
    def getsentence(self, size):
        sentence = self.getwords(size)
        sentence = sentence + '.'
        return sentence[0].upper() + sentence[1:]

    #returns a 5-10 sentence paragraph
    def getparagraph(self):
        tmp_sentences = []
        num_sentences = random.randrange(5, 10, 1)
        for i in range(num_sentences):
            tmp_sentences.append(self.getsentence(random.randrange(5, 20, 1)))
        return ' '.join(tmp_sentences)

    #return num_paragraphs seperated by by a line of space
    def getarticle(self, num_paragraphs):
        paragraphs = []
        if num_paragraphs > self.MAX_PARAGRAPHS:
            num_paragraphs = self.MAX_PARAGRAPHS

        for i in range(num_paragraphs):
            paragraphs.append(self.getparagraph())

        return '\n\n'.join(paragraphs)



hockey = HockeyIpsum()
print hockey.gettitle()
#print hockey.getsentence(8)
print hockey.getarticle(4)
#print hockey.getparagraph()
