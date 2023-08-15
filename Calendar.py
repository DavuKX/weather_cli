import json
from Event import Event
from strategies.searchByDate import SearchByDate
from strategies.searchByDescription import SearchByDescription
from strategies.searchByName import SearchByName


class Calendar:
    def __init__(self):
        self.events = []
        self.load_calendar()

    def load_calendar(self):
        with open("calendar.json", "r") as file:
            for event in json.load(file):
                self.events.append(
                    Event(
                        event['date'],
                        event['time'],
                        event['title'],
                        event['description']
                    )
                )

    def add_event(self, date, time, title, description):
        new_event = Event(date, time, title, description)
        self.events.append(new_event)

        with open("calendar.json", "r+") as file:
            file_data = json.load(file)
            file_data.append(new_event.__dict__)
            file.seek(0)
            json.dump(file_data, file, indent=4)

        print("Event added successfully")

    def delete_event(self, event_to_delete):
        events_to_keep = [event for event in self.events if event != event_to_delete]

        with open("calendar.json", "w") as file:
            json.dump([event.__dict__ for event in events_to_keep], file, indent=4)

        self.events = events_to_keep
        print("Event deleted successfully")

    def search_events(self, search_type, search_param):
        strategies = {
            "date": SearchByDate(),
            "name": SearchByName(),
            "description": SearchByDescription()
        }

        strategy = strategies.get(search_type.lower())

        results = strategy.search(self.events, search_param)

        return results

    def view_all_events(self):
        for event in self.events:
            event.display()
            print("\n")
