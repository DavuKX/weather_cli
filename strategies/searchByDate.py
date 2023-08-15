from strategies.searchStrategy import SearchStrategy


class SearchByDate(SearchStrategy):
    def search(self, events, search_param):
        return [event for event in events if event.date == search_param]
