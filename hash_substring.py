# python3

import sys

def hash_func(s, p):
    p_len = len(p)
    h = 0
    for i in range(p_len):
        h += ord(s[i]) * pow(len(s), p_len - i - 1)
    return h % p_len

def get_occurrences(pattern, text):
    p_len = len(pattern)
    t_len = len(text)
    p_hash = hash_func(text[:p_len], pattern)
    result = []
    for i in range(t_len - p_len + 1):
        if p_hash == hash_func(text[i:i+p_len], pattern):
            flag = True
            for j in range(p_len):
                if text[i+j] != pattern[j]:
                    flag = False
                    break
            if flag:
                result.append(i)
    return result

def print_occurrences(output):
    for i in output:
        print(i, end=' ')
    print()

def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
