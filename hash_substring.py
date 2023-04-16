# python3

import sys

def read_input():
    if sys.argv[1] == 'F':
        with open('input.txt', 'r') as f:
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
    p_hash = sum([ord(pattern[i])*pow(10, p_len-i-1) for i in range(p_len)]) % 101
    t_hash = sum([ord(text[i])*pow(10, p_len-i-1) for i in range(p_len)]) % 101
    if t_hash == p_hash and text[:p_len] == pattern:
        occurrences.append(0)
    for i in range(1, t_len-p_len+1):
        t_hash = (t_hash-ord(text[i-1])*pow(10, p_len-1))*10 + ord(text[i+p_len-1])
        if t_hash == p_hash and text[i:i+p_len] == pattern:
            occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

