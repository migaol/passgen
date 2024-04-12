# Random password generator

import argparse, string, secrets, pyperclip

def generate_password(length: int = 16, use_numbers: bool = True, use_letters: bool = True, use_symbols: bool = True):
    alphabet = ''
    if use_numbers: alphabet += string.digits
    if use_letters: alphabet += string.ascii_letters
    if use_symbols: alphabet += string.punctuation

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main(args: argparse.Namespace) -> None:
    pw = generate_password(args.nbytes, args.numbers, args.letters, args.symbols)
    pyperclip.copy(pw)
    print(f"{pw}\nCopied to clipboard!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate password")
    parser.add_argument('nbytes', nargs='?', type=int, default=16, help='Password length (default: 16)')
    parser.add_argument('-n', '--numbers', action='store_true', help='Include numbers')
    parser.add_argument('-l', '--letters', action='store_true', help='Include letters')
    parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols')
    args = parser.parse_args()
    if not any([args.numbers, args.letters, args.symbols]):
        args.numbers = args.letters = args.symbols = True
    main(args)
