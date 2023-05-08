class BrowserHistory:

    def __init__(self, homepage: str):
        self.b = []
        self.f = []
        self.cur = homepage

    def visit(self, url: str) -> None:
        self.b.append(self.cur)
        self.f = []
        self.cur = url

    def back(self, steps: int) -> str:       
        for i in range(steps):
            if self.b:
                self.f.append(self.cur)
                self.cur = self.b.pop()
        return self.cur

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.f:
                self.b.append(self.cur)
                self.cur = self.f.pop()
        return self.cur

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)