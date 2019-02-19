from .bip39gen import *


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("length", type=int, default=6, help="Number of words", nargs='?')
    parser.add_argument("--lang", "-l", type=str, default="en", help="Language for wordlist; defaults to 'en'")
    parser.add_argument("--separator", "-s", type=str, default=" ", help="String to separate words")
    parser.add_argument("--count", "-c", type=int, default=1, help="Number of wordsets to print")
    args = parser.parse_args()
    for x in range(args.count):
        print(random_as_string(args.length, args.separator, args.lang))

if __name__ == '__main__':
    main()