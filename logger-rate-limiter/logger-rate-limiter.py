from collections import defaultdict


class Logger:
    """
    Time: O(1) because we use hash table lookup to check if the message is already in the log.
    Space: O(M) where M is the size of all unique incoming messages.
    """

    def __init__(self):
        self.log = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.log and timestamp < self.log[message]:
            return False
        self.log[message] = timestamp + 10
        return True
