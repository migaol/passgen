# Random password generator

import argparse, string, secrets, pyperclip

def generate_password(length: int = 16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main(args: argparse.Namespace) -> None:
    pw = generate_password(args.nbytes)
    pyperclip.copy(pw)
    print(f"{pw}\nCopied to clipboard!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate password")
    parser.add_argument('nbytes', nargs='?', type=int, default=16, help='Password length (default: 16)')
    args = parser.parse_args()
    main(args)
