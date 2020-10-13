class Neuron:

    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        return self.f(sum(map(lambda w,x: w*x, self.w, self.x)))

    def backlog(self):
        return self.x