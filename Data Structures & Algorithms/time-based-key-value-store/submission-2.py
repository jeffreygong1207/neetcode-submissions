class TimeMap:

    def __init__(self):
        self.mappings = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mappings:
            self.mappings[key] = []
            self.mappings[key].append([value,timestamp])
        else:
            self.mappings[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        
        values = self.mappings.get(key, [])
        result = ""
        left, right = 0, len(values) - 1
        while left <= right:
            middle = (left + right) // 2
            value, stimestamp = values[middle]
            if stimestamp <= timestamp:
                result = value
                left = middle + 1
            else:
                right = middle - 1
        return result

