from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    """
    Time: O(n + m) where n is len(s) and m is len(t)
    Space: O(n + m) where n is len(s) and m is len(t)
    """
    string_one_freq, string_two_freq = Counter(s), Counter(t)
    string_one_freq.subtract(string_two_freq)
    for val in string_one_freq.values():
        if val != 0:
            return False
    return True
