class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []

        

    def next(self, price: int) -> int:
        count = 1
        if self.stack:
            while self.stack and self.stack[-1] <= price:
                count += self.prices.pop()
                self.stack.pop()
            self.prices.append(count)
            self.stack.append(price)
            return count
        else:
            self.stack.append(price)
            self.prices.append(count)
            return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)