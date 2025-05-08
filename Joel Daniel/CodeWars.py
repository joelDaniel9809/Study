#%%

def spin_words(sentence):
    return " ".join(word[::-1] if len(word)>=5 else word for word in sentence.split()) 

spin_words("Hey fellow warriors")
#%%

def descending_order(num):
    return int("".join(sorted(str(num),reverse=True)))
descending_order(42145)
#%%
def unique_in_order(sequence):
    return [x for i,x in enumerate(sequence) if i ==0 or (sequence[i-1] is not x)  ]

#%%

def digital_root(n):
    return n if n < 10 else digital_root(sum(int(x) for x in str(n)))

digital_root(493193)