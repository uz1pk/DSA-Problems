def get_next_happy(n: int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        total += digit**2
    return total


def isHappy(n: int) -> bool:
    """
    Time: O(log n)
    Space: O(n)
    """
    visited = set()
    while n not in visited:
        visited.add(n)
        if n == 1:
            return True
        n = get_next_happy(n)
    return False
