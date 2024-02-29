from abc import ABC, abstractmethod
from typing import List, Dict, Any


class SearchEngineModule(ABC):
    def __init__(self, search_engines: Dict[str, str]):
        """
        Initialize the search engine module with configurations.

        Parameters:
            search_engines (Dict[str, str]): A mapping of search engine names to their base URLs.
        """
        self.search_engines = search_engines

    @abstractmethod
    def execute_search(self, query: str) -> List[Dict]:
        """
        Execute a search query on configured search engines.

        Parameters:
            query (str): The search query to execute.

        Returns:
            List[Dict]: A list of search results, each result as a dictionary.
        """
        pass

    @abstractmethod
    def filter_results(self, results: List[Dict], criteria: Dict[str, Any]) -> List[Dict]:
        """
        Filter search results based on specified criteria.

        Parameters:
            results (List[Dict]): The list of search results to be filtered.
            criteria (Dict[str, Any]): A dictionary of filtering criteria.

        Returns:
            List[Dict]: The filtered list of search results.
        """
        pass

    @abstractmethod
    def rank_results(self, results: List[Dict]) -> List[Dict]:
        """
        Rank the search results based on a predefined set of metrics.

        Parameters:
            results (List[Dict]): The list of search results to be ranked.

        Returns:
            List[Dict]: The ranked list of search results.
        """
        pass

    @abstractmethod
    def update_search_algorithm(self, parameters: Dict[str, Any]) -> None:
        """
        Update the search algorithm parameters or logic.

        Parameters:
            parameters (Dict[str, Any]): A dictionary of parameters to update the search algorithm.
        """
        pass
