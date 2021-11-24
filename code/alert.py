class Alert:
    def __init__(self, attributes, data, color="#1f78b4"):
        self.vector = []
        self.dict = {}
        for attr in attributes:
            value = data.get(attr, '')
            self.vector.append(value)
            self.dict[attr] = value
        self.color = color