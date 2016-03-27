import os
import random

class HockeyIpsum:
    def __init__(self, directory = "/wordbank"):
        self.files = []
        self.words = []
        self.wordbank_dir = "." + directory + "/"
        self._loadfiles()
        self._readfiles()

    def _loadfiles(self):
        for f in os.listdir(self.wordbank_dir):
            if f.endswith(".txt"):
                print "loading " + f
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

    #getwords returns a string of length from the wordbank
    def getwords(self, size):
        tmp_words = []
        max_index = len(self.words) - 1
        #create list of random integers between 0 and self.words.length
        for i in range(size):
            tmp_words.append(self.words[random.randrange(0, max_index, 1)])
        return ' '.join(tmp_words)

    #gettitle returns a 1-5 words string.
    def gettitle(self):
        num_words = random.randrange(1,5,1)
        return self.getwords(num_words)

    #returns a 100-200 word string
    def getparagraph(self):
        num_words = random.randrange(100,200,1)
        return self.getwords(num_words)


hockey = HockeyIpsum()
print hockey.gettitle()
#print hockey.getparagraph()
