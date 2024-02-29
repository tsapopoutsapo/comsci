from abc import ABC, abstractmethod
from typing import Dict, Optional


class StorageModule(ABC):
    def __init__(self, database_connection_string: str):
        """
        Initialize the storage module with database configurations.

        Parameters:
            database_connection_string (str): The connection string for the database.
        """
        self.database_connection_string = database_connection_string

    @abstractmethod
    def save_paper(self, paper_data: Dict) -> None:
        """
        Save the metadata and, optionally, the full text of a scientific paper.

        Parameters:
            paper_data (Dict): A dictionary containing the paper's metadata and possibly its full text.
        """
        pass

    @abstractmethod
    def retrieve_paper(self, paper_id: str) -> Optional[Dict]:
        """
        Retrieve a scientific paper by its identifier.

        Parameters:
            paper_id (str): The unique identifier of the paper.

        Returns:
            Optional[Dict]: The paper's metadata and possibly its full text, if available.
        """
        pass

    @abstractmethod
    def update_paper_metadata(self, paper_id: str, metadata: Dict) -> None:
        """
        Update the metadata for an existing scientific paper.

        Parameters:
            paper_id (str): The unique identifier of the paper to update.
            metadata (Dict): A dictionary containing the updated metadata.
        """
        pass

    @abstractmethod
    def delete_paper(self, paper_id: str) -> None:
        """
        Delete a scientific paper from storage.

        Parameters:
            paper_id (str): The unique identifier of the paper to be deleted.
        """
        pass
