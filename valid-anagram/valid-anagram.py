from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    d1, d2 = Counter(s), Counter(t)
    d1.subtract(d2)
    for val in d1.values():
        if val != 0:
            return False
    return True
