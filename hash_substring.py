# python3

import os
import sys


def read_input():
    t_in = input().strip().upper()
    if t_in == "I":
        pattern = input().strip()
        text = input().strip()
    elif t_in == "F":
        filename = 'tests/06'
        try:
            with open(filename) as file:
                pattern = file.readline().strip()
                text = file.readline().strip()
        except FileNotFoundError:
            print("Error: file not found")
            sys.exit(1)
    else:
        print("Error: invalid input choice")
        sys.exit(1)
    return t_in, pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(t_in, pattern, text):
    n = len(text)
    m = len(pattern)
    p = 31
    p_pow = [pow(p, i) for i in range(m)]
    pattern_hash = sum([ord(pattern[i]) * p_pow[m - 1 - i] for i in range(m)])
    text_hash = sum([ord(text[i]) * p_pow[m - 1 - i] for i in range(m)])
    matches = []
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + m]:
                matches.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i]) * p_pow[m - 1]) * p + ord(text[i + m])
    return matches


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
