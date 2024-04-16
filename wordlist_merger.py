from rich import print
from rich.console import Console
from rich.traceback import install
import sys
import os

install()
cs = Console()


def merge_wordlists(wordlists):
    merged = set()
    for wordlist in wordlists:
        with open(wordlist) as f:
            for word in f:
                merged.add(word.lower())

    return list(merged)


if __name__ == '__main__':
    if cs.color_system == 'standard' or cs.color_system is None:
        print('[bold italic red]Your terminal may not support full rich features.')
        print('[italic]Please consider using a terminal that supports "True Color".')

    args = sys.argv[1:]
    if not args:
        print('Type the wordlists one by one and press Enter. Leave empty to finish.')
        wordlists = []
        while True:
            wordlist = cs.input('Wordlist: ')

            if not wordlist:
                break

            if not os.path.exists(wordlist):
                print(f'[bold italic red]File "{wordlist}" not found.')
                continue

            wordlists.append(wordlist)

        output = cs.input('Output file: ')

    elif len(args) == 1 and args[0] == '-h' or args[0] == '--help':
        print('Usage: python wordlist_merger.py [output_file] [underline][wordlist1] [wordlist2] ...')
        sys.exit(0)
    else:
        wordlists = args[1:]
        output = args[0]

        for wordlist in wordlists:
            if not os.path.exists(wordlist):
                print(f'[bold italic red]File "{wordlist}" not found.')
                sys.exit(1)

    for wordlist in wordlists:
        word_count = sum(1 for line in open(wordlist))
        print(f'[bold italic]Wordlist: {os.path.basename(wordlist)} [italic]({word_count} words)')

    merged = merge_wordlists(wordlists)

    if os.path.isdir(output):
        output = os.path.join(output, 'merged_wordlist.txt')

    with open(output, 'w') as f:
        f.write('\n'.join(sorted(set(merged))))

    max_word_count = max(sum(1 for line in open(wordlist)) for wordlist in wordlists)
    print(f'Merged {len(merged)} words. ({len(merged) - max_word_count} more than the largest wordlist)')
    print(f'[bold italic]Merged wordlists saved to [underline]{output}')
