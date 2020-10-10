def most_common_letter(s):
    return best_key(count_freq(s))

def count_freq(st):
    d={}
    for i in st:
        if i not in d:
            d[i]=0
        d[i] = d[i] + 1
    return d    

def best_key(d):
    key=list(d.keys())[0]
    for i in d:
        if d[i] > d[key]:
            key=i
    return key

print(most_common_letter("aaabddddddd"))      