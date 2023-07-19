class Labels:
    def __init__(self):
        self.labels = {}
    
    def get(self, label):
        return self.labels[label]
    
    def add(self, label):
        self.labels[label] = IP.IP
    
class IPCounter:
    def __init__(self):
        self.IP = 0
    
    def inc(self, n):
        self.IP += n

labels = Labels()
IP = IPCounter()