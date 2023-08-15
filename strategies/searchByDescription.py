from strategies.searchStrategy import SearchStrategy


class SearchByDescription(SearchStrategy):
    def search(self, events, search_param):
        return [event for event in events if search_param.lower() in event.description.lower()]