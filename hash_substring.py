# python3

def read_input():
    t_in=input().strip().upper()
    if t_in=="I":
        pattern=input().strip()
        text=input().strip()
    elif t_in=="F":
        filename='tests/06'
        with open(filename) as file:
            pattern=file.readline().strip()
            text=file.readline().strip()
            
    else:
        exit()
    return t_in, pattern,text          
    

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences( t_in,pattern, text):
    text_l=len(text)
    pattern_l=len(pattern)
    occurances=[]
    if t_in=="I":
        for i in range(text_l-pattern_l+1):
            if text[i: i+pattern_l]==pattern:
                occurances.append(i)
    elif t_in=="F":
        pattern1=sum(ord(pattern[i])*pow(10,pattern_l-i-1) for i in range(pattern_l))
        text1=sum(ord(text[i])*pow(10,pattern_l-i-1) for i in range(pattern_l))
        for i in range(text_l-pattern_l+1):
            if text1==pattern1 and text[i:i +pattern_l]==pattern:
                occurances.append(i)
            if i<text_l-pattern_l:
                text1=(text1-ord(text[i])*pow(10,pattern_l-1))*10+ord(text[i+pattern_l]) 
                                        
    return occurances
    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
