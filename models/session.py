class Session:
    def __init__(self, title, date, description, capacity, id = None):
        self.title = title
        self.date = date
        self.description = description
        self.capacity = capacity
        self.id = id

    def get_capacity(self):
        return self.capacity

    
    # attending_list = session_repository.members(booking.session)
    # attending_count = len(attending_list)

    # capacity = booking.session.capacity
    # if attending_count >= capacity:
    #     return None
    # else:     