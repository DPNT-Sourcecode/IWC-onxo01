
class SumSolution:
    
    def compute(self, x, y):
        if not (0<=x<=100 and 0<=y<=100):
            raise ValueError("Both integers must be between 0 and 100")
        return x+y

