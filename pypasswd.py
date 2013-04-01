import random
import argparse
from string import digits, ascii_uppercase, ascii_lowercase


def main():
    args = get_args()
    passwd_length = 100
    if args.length:
        passwd_length = args.length

    random.seed()
    alphanumerics = digits + ascii_uppercase + ascii_lowercase

    if args.alphanumeric:
        print generate_passwd(alphanumerics, passwd_length)


def generate_passwd(character_list, passwd_length):
    passwd = ""
    for x in range(0, int(passwd_length)):
        passwd += random.choice(character_list)
    return passwd


def get_args():
    parser = argparse.ArgumentParser(description='Generate passwords')
    parser.add_argument('-a', '--alphanumeric', help='Alphanumeric characters only', action='store_true', )
    parser.add_argument('-l', '--length', help='Specify length')
    return parser.parse_args()


if __name__ == '__main__':
    main()
