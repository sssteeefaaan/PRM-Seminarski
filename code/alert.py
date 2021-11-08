class Alert:
    def __init__(self, attributes, data):
        self.vector = []
        self.dict = {}
        for attr in attributes:
            value = data.get(attr, '')
            self.vector.append(value)
            self.dict[attr] = value