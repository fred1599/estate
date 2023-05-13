"""
Module for managing real estate documents.
"""

from estate_project.domain.entities.document_management import Document


class DocumentManagement:
    """
    Class for managing real estate documents.

    Attributes:
    - _documents (list[Document]): List of documents in the document management system.
    - _is_empty (bool): Indicates if the document management system is empty.

    """

    def __init__(self) -> None:
        """
        Initializes a DocumentManagement instance.

        Parameters:
        None

        Returns:
        None
        """
        self._documents: list[Document] = []
        self._is_empty: bool = True

    def add_document(self, document: Document) -> None:
        """
        Adds a document to the document management system.

        Parameters:
        - document (Document): The document to be added.

        Returns:
        None
        """
        self._documents.append(document)
        if self._is_empty is True:
            self._is_empty = False

    def remove_document_from_name(self, name: str) -> None:
        """
        Removes a document from the document management system based on its name.

        Parameters:
        - name (str): The name of the document to be removed.

        Returns:
        None
        """
        for doc in self._documents:
            if doc.name == name:
                self._documents.remove(doc)
                break
        if not self._documents and self._is_empty is False:
            self._is_empty = True

    def search_document_by_name(self, name: str) -> None | Document:
        """
        Searches for a document in the document management system based on its name.

        Parameters:
        - name (str): The name of the document to search for.

        Returns:
        - Document | None: The found document if it exists, None otherwise.
        """
        if self._is_empty:
            return None

        for doc in self._documents:
            if doc.name == name:
                return doc

        return None
