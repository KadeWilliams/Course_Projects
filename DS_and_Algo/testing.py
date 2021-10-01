def lengthOfLongestSubstring(s):
    longest = []
    cur_longest = 0
    for letter in s:
        if letter not in longest:
            longest.append(letter)
        else:
            if len(longest) > cur_longest:
                cur_longest = len(longest)
            longest = []
            

    return cur_longest 

print(lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10