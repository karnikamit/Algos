# coding=utf-8
__author__ = 'karnikamit'


class Fleshkincaid(object):
    """
    Flesch Reading Ease Formula

    RE = 206.835 – (1.015 x ASL) – (84.6 x ASW)

    RE = Readability Ease

    ASL = Average Sentence Length (i.e., the number of words divided by the number of sentences)

    ASW = Average number of syllables per word (i.e., the number of syllables divided by the number of words)
    """
    def __init__(self, passage):
        """

        :param (str) passage: text to process
        """
        self.passage = passage
        self.delimeters = ".!:;"
        self.vowels = "aeiou"
        self.sentences = []
        self.words = []
        self.syllables = []
        self.ignored_syllable_endings = ['es', 'ed', 'e']

    def _sanitize(self):
        temp_sentences = [i for i in self.passage if i not in self.delimeters]
        self.passage = "".join(temp_sentences)

    def average_sentence_length(self):
        """
        periods, exclamation points, colons and semicolons serve as sentence delimiters
        :return:
        """
        start = 0
        for i, char in enumerate(self.passage):
            if char in self.delimeters:
                end = i + 1
                self.sentences.append(self.passage[start: end])
                start = end+1
        self._sanitize()
        self.words = self.passage.split(" ")
        return len(self.words) / len(self.sentences)

    def average_syllabels(self):
        """
        each vowel in a word is considered one syllable subject to:
        (a) -es, -ed and -e (except -le) endings are ignored
        (b) words of three letters or shorter count as single syllables
        (c) consecutive vowels count as one syllable.
        :return:
        """
        no_syllables = 0
        for word in self.words:
            no_syllables += self.count_syllables(word)
        return no_syllables / len(self.words)

    def count_syllables(self, word):
        if len(word)+1 < 4:
            return 1
        no_syllables = 0
        start = 0
        end = 4
        _words = []
        while end < len(word):
            _words.append(word[start: end])
            start = end
            end += 4
        else:
            _words.append(word[start:])
        for _word in _words:
            if all([not _word.endswith(ending) for ending in self.ignored_syllable_endings]) or len(_word)+1 < 4:
                no_syllables += 1
        return no_syllables


    def readability(self):
        asl = self.average_sentence_length()
        asw = self.average_syllabels()
        return 206.835 - (1.015 * asl) - (84.6 * asw)


if __name__ == "__main__":
    with open("/Users/amkarnik/PycharmProjects/Algos/try_push.txt", 'r') as f:

        fckd = Fleshkincaid(f.read())
        print fckd.readability()
