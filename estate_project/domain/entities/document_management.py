"""
Module for managing real estate documents and contracts.
"""

from enum import Enum
from pydantic import BaseModel


class TypeDocument(str, Enum):
    """
    Enumeration class for document types.
    """

    DOCX = "docx"
    PDF = "pdf"
    TXT = "txt"


class Document(BaseModel):
    """
    Class representing a real estate document.

    Attributes:
    - name (str): The name of the document.
    - type (TypeDocument): The type of the document.

    """

    name: str
    type: TypeDocument
