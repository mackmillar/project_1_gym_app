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

    def add_to_counter(self, session):
        if self.counter < self.capacity:
            self.counter += 1
            return self.counter


    