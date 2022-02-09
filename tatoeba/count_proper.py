import sys
from collections import defaultdict
from ilonimi import (
        Normalizer,
        Tokenizer,
        Splitter)

normalizer = Normalizer()
tokenizer = Tokenizer(
        convert_unk = True,
        convert_number = False,
        convert_proper = False)

def count():
    counter = defaultdict(int)

    for line in sys.stdin:
        x = line.strip()
        x = normalizer(x)
        x = tokenizer(x)
        for word in x.split():
            if word.istitle():
                counter[word] += 1

    lst = list(counter.items())
    lst.sort()
    lst.sort(key = lambda x: -x[-1])

    for name, freq in lst:
        print('{}\t{}'.format(name, freq))


def main():
    try:
        count()
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

