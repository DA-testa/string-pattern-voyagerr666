# python3

def read_input():
    choice = input().rstrip()
    if choice == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif choice == 'F':
        with open('input.txt', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31
    m = 10**9 + 9
    p_pow = [1]
    for i in range(1, len(text)):
        p_pow.append((p_pow[-1] * p) % m)
    
    pattern_hash = 0
    for c in pattern:
        pattern_hash = (pattern_hash * p + ord(c)) % m
    
    text_hash = [0] * (len(text) - len(pattern) + 1)
    text_hash[0] = 0
    for i in range(len(pattern)):
        text_hash[0] = (text_hash[0] * p + ord(text[i])) % m
    for i in range(1, len(text) - len(pattern) + 1):
        text_hash[i] = (text_hash[i-1] - ord(text[i-1]) * p_pow[len(pattern)-1] + ord(text[i+len(pattern)-1])) % m
    
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text_hash[i] == pattern_hash:
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
