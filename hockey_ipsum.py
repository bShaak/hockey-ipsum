import os

class HockeyIpsum:
    def __init__(self, directory = "/wordbank"):
        self.files = []
        self.words = []
        self.wordbank_dir = "." + directory + "/"
        self._load_files()
        self._read_files()

    def _load_files(self):
        for f in os.listdir(self.wordbank_dir):
            if f.endswith(".txt"):
                print "loading " + f
                self.files.append(self.wordbank_dir + f)

    def _read_files(self):
        i = 0;
        for filename in self.files:
            f = open(filename, 'r')
            for line in f:
                self.words.append(line.rstrip())
                i = i+1
            f.close()

    def print_wordbank(self):
        for w in self.words:
            print w

hockey = HockeyIpsum()
hockey.print_wordbank()
