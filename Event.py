class Event:
    def __init__(self, date, time, title, description):
        self.date = date
        self.time = time
        self.title = title
        self.description = description

    def display(self):
        print(f"Event for date {self.date} - {self.time}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
