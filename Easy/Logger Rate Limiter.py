# Logger Rate Limiter
class Logger:

    def __init__(self):
        self.memo = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.memo:
            self.memo[message] = timestamp
            return True
        else:
            curr = self.memo[message]
            if curr <= timestamp - 10:
                self.memo[message] = timestamp
                return True
            else:
                return False