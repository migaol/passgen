# passgen
A quick password generator for when you don't want to go to lastpass.

Features:
- Cryptographically secure random sequence using the `secrets` module
- Specify the length with an argument (default 16)
- Include numbers 0-9 (`-n`), letters a-zA-Z (`-l`), and symbols (`-s`); all are included by default
- Automatically copies to clipboard

How to use: download & run `python3 passgen.py <length>`
