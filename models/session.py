class Session:
    def __init__(self, title, date, description, capacity, id = None):
        self.title = title
        self.date = date
        self.description = description
        self.capacity = capacity
        self.counter = 0
        self.id = id

    def get_capacity(self):
        return self.capacity

    