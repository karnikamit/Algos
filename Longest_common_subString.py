__author__ = 'karnikamit'


class LCS(object):

    def __init__(self, line1, line2):
        self.line1 = line1.lower()
        self.line2 = line2.lower()
        self.len1 = len(self.line1)
        self.len2 = len(self.line2)
        self.longest = 0
        self.lcs_set = set()

    def lcs(self):
        self.line1 = self.sanitize(self.line1)
        self.line2 = self.sanitize(self.line2)
        counter = [[0]*(self.len2+1) for x in range(self.len1+1)]
        for i in range(self.len1):
            for j in range(self.len2):
                if self.line1[i] == self.line2[j]:
                    c = counter[i][j] + 1
                    counter[i+1][j+1] = c
                    if c > self.longest:
                        self.lcs_set = set()
                        self.longest = c
                        self.lcs_set.add(self.line1[i-c+1:i+1])
                    elif c == self.longest:
                        self.lcs_set.add(self.line1[i-c+1:i+1])

        return self.lcs_set

    def sanitize(self, line):
        l = line.split(" ")
        for word in l:
            if '.' in word:
                word = word.replace('.', '')
            elif ',' in word:
                word = word.replace(',', '')
            elif '-' in word:
                word = word.replace('-', ' ')
        a_line = " ".join(l)
        return a_line
