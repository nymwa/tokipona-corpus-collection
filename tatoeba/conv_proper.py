import numpy as np
import sys
import re
from ilonimi import Vocabulary
from tqdm import tqdm

output0 = [(1, 'k'), (1, 'l'), (1, 'm'), (1, 'n'), (1, 'p'), (1, 's'), (2, 'j'), (2, 't'), (3, 'w'), (4, 'a'), (4, 'e'), (4, 'i'), (4, 'o'), (4, 'u')]
probs0 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.02, 0.02, 0.02, 0.02, 0.02]

output1 = [(4, 'a'), (4, 'e'), (4, 'i'), (4, 'o'), (4, 'u')]
output2 = [(4, 'a'), (4, 'e'), (4, 'o'), (4, 'u')]
output3 = [(4, 'a'), (4, 'e'), (4, 'i')]

output4 = [(1, 'k'), (1, 'l'), (1, 'm'), (1, 'p'), (1, 's'), (2, 'j'), (2, 't'), (3, 'w'), (5, 'n')]

output5 = [(1, 'k'), (1, 'l'), (1, 'p'), (1, 's'), (2, 'j'), (2, 't'), (3, 'w'), (4, 'a'), (4, 'e'), (4, 'i'), (4, 'o'), (4, 'u')]

class ProperGenerator:

    def __init__(self):
        self.vocab = set(Vocabulary().word_list)

    def change(self):
        if self.state == 0:
            output, probs = output0, probs0
        elif self.state == 1:
            output, probs = output1, None
        elif self.state == 2:
            output, probs = output2, None
        elif self.state == 3:
            output, probs = output3, None
        elif self.state == 4:
            output, probs = output4, None
        elif self.state == 5:
            output, probs = output5, None
        index = np.random.choice(range(len(output)), p = probs)
        self.state, char = output[index] 
        return char

    def cond(self, name, minlen):
        if name in self.vocab:
            return True

        if self.state not in {4, 5}:
            return True

        return len(name) < minlen

    def __call__(self):
        #minlen = np.random.poisson(5)
        minlen = np.random.choice(
                10,
                p = [0, 0.01, 0.01, 0.5, 0.25, 0.1, 0.07, 0.03, 0.02, 0.01])
        self.state = 0
        name = ''
        while self.cond(name, minlen):
            char = self.change()
            name += char
        return name.title()


def main():
    generator = ProperGenerator()

    for line in tqdm(sys.stdin, bar_format = '{l_bar}{r_bar}'):
        x = line.strip()
        x = re.sub('Ton', generator(), x)
        x = re.sub('Mewi', generator(), x)
        x = re.sub('Mali', generator(), x)
        x = re.sub('Mawi', generator(), x)
        x = re.sub('Sami', generator(), x)
        x = re.sub('San', generator(), x)
        print(x)


if __name__ == '__main__':
    main()

