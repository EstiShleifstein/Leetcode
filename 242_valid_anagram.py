def isAnagram(s, t):

    if len(s) != len(t):
        return False

    # Method 1: using built-in sorted method to sort them and then compare the strings
    # return sorted(s) == sorted(t)

    # Method 2: Counter -- using the count of each letter in each string and seeing if there is the same count of each
    from collections import Counter

    return Counter(s) == Counter(t)

    # Just realized that the below method is incorrect because it will not work for all cases. For example, if the string is "aa" and "abb", it will return false, but they are anagrams. The reason is that the count of each letter is not even. So, we need to check if the count of each letter is even.
    # Method 2: Goal -- to use a hashmap. Will loop over both strings and increment the value of the letter key by 1 for every appearance. Then, if a value % 2 != 0, it means that it is not an anagram, since the sign of an anagram is an even amount of each value. Actually, incorrect because it could just mean that
    # Instead: use 2 hashmaps for each string and compare the values of each in one for loop = )(N)
    # countS, countT = {}, {}

    # for i in range(len(s)):
    #     countS[s[i]] = 1 + countS.get(
    #         s[i], 0
    #     )  # we have a default value in case there is no value for it yet
    #     countT[t[i]] = 1 + countT.get(t[i], 0)
    #     print("dict", countT, countS)
    # for key in countS:
    #     if countS[key] != countT.get(key, 0):
    #         return False
    # return True


print(isAnagram("anagram", "managra"))
