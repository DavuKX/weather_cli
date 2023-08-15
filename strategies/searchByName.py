from strategies.searchStrategy import SearchStrategy


class SearchByName(SearchStrategy):
    def search(self, events, search_param):
        return [event for event in events if search_param.lower() in event.title.lower()]
