class StateStore:
    def __init__(self):
        self.state = {}

    def set(self, key, value):
        self.state[key] = value
