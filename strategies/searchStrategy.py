from abc import ABC, abstractmethod


class SearchStrategy(ABC):
    @abstractmethod
    def search(self, events, search_param):
        pass
