import commune as c
from typing import List, Dict, Optional



class DataCollectingModule(c.Module):
    def __init__(self, source_urls: List[str]):
        """
        Initialize the data collecting module with common configurations.

        Parameters:
            source_urls (List[str]): A list of URLs to the data sources.
        """
        self.source_urls = source_urls


    def fetch_paper_metadata(self, search_query: str) -> List[Dict]:
        """
        Fetch metadata for scientific papers based on a given search query.

        Parameters:
            search_query (str): The search query to use for finding scientific papers.

        Returns:
            List[Dict]: A list of dictionaries, each containing metadata of a scientific paper.
        """
        pass


    def download_paper(self, paper_id: str) -> Optional[bytes]:
        """
        Download the full text of a scientific paper by its unique identifier.

        Parameters:
            paper_id (str): The unique identifier of the paper to download.

        Returns:
            Optional[bytes]: The full text of the paper as a byte stream, if available.
        """
        pass

    def fetch_references(self, paper_id: str) -> List[str]:
        """
        Fetch references or cited works of a given scientific paper.

        Parameters:
            paper_id (str): The unique identifier of the paper whose references are to be fetched.

        Returns:
            List[str]: A list of identifiers for the referenced papers.
        """
        pass

    def update_data_source(self, new_sources: List[str]) -> None:
        """
        Update the list of data sources or search engines to be queried.

        Parameters:
            new_sources (List[str]): A list of new data sources to be added.
        """
        pass
