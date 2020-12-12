class Session:
    def __init__(self, title, date, description, attendees, id = None):
        self.title = title
        self.date = date
        self.description = description
        self.attendees = []
        self.id = id