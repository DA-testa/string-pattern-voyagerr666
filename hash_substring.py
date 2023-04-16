# python3

import sys


def read_input():
    if len(sys.argv) > 1 and sys.argv[1] == 'F':
        with open('input.txt') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    occurrences = []
    p_len = len(pattern)
    t_len = len(text)

    p_hash = sum(ord(pattern[i]) * pow(10, p_len - i - 1) for i in range(p_len))

    t_hash = sum(ord(text[i]) * pow(10, p_len - i - 1) for i in range(p_len))

    for i in range(t_len - p_len + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            t_hash = (t_hash - ord(text[i]) * pow(10, p_len - 1)) * 10 + ord(text[i+p_len])

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
