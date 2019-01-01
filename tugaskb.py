from math import log


kata = open("kamus-kata.txt").read().split()
jumlahkata = dict((k, log((i+1)*log(len(kata)))) for i,k in enumerate(kata))
maxkata = max(len(x) for x in kata)

def split_kata(s):
    

  
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxkata):i]))
        return min((c + jumlahkata.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

s = input('masukan kata untuk di split!! ')
print(split_kata(s))