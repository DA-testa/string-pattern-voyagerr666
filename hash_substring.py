# python3

def read_input():

    choice = input().strip()

    if choice == 'I':
        pattern = input().strip()
        text = input().strip()
    elif choice == 'F':
        with open('test.txt', 'r') as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
    else:
        raise ValueError('Invalid input choice')

    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 10**9 + 7
    x = 263
    n = len(text)
    m = len(pattern)
    p_hash = [0] * (n - m + 1)
    t_hash = [0] * (n - m + 1)
    x_pow = [1] * (n - m + 1)

    # Precompute hashes
    p_hash[0] = hash(pattern, p, x)
    t_hash[0] = hash(text[:m], p, x)

    for i in range(1, n - m + 1):
        p_hash[i] = (x * p_hash[i-1] + ord(pattern[i+m-1])) % p
        t_hash[i] = (x * t_hash[i-1] + ord(text[i+m-1])) % p
        x_pow[i] = (x * x_pow[i-1]) % p

    occurrences = []
    for i in range(n - m + 1):
        if p_hash[i] != t_hash[i]:
            continue
        if text[i:i+m] == pattern:
            occurrences.append(i)

    return occurrences

def hash(s, p, x):
    h = 0
    for c in reversed(s):
        h = (h * x + ord(c)) % p
    return h

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
