from ilonimi.normalizer import Normalizer
from ilonimi.tokenizer import Tokenizer

def main():
    normalizer = Normalizer()
    tokenizer = Tokenizer()

    with open('tokipona1000.txt') as f:
        for i, x in enumerate(f):
            x = x.strip()
            x = normalizer(x)
            x = tokenizer(x)
            print('# {}: {}'.format(i + 1, x))
            for k, w in enumerate(x.split()):
                print('{}	{}	{}	{}	{}'.format(k + 1, w, 'X', '0', 'x'))
            print('')

if __name__ == '__main__':
    #main()
    pass


