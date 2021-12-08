class MapSum:

    def __init__(self):
        self.dct = {}

    def insert(self, key: str, val: int) -> None:
        self.dct.setdefault(key, val)
        self.dct[key] = val

    def sum(self, prefix: str) -> int:
        sum = 0
        for key, val in self.dct.items():
            temp = key[:len(prefix)]
            if prefix == temp:
                sum += val
        return val
