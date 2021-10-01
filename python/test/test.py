def sockMerchant(ar):

    hashmap = {}
    for i in ar:
        if i in hashmap:
            hashmap[i] += 1
        else: hashmap[i] = 1
    
    counter = 0
    for v in hashmap.values():
        while v >= 2:
            v -= 2
            counter += 1
    return counter
socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
socks2 = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
print(sockMerchant(socks))
# print(sockMerchant(socks2))