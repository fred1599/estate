from pydantic import BaseModel


class Address(BaseModel):
    """
    A base real class for Address entities
    """

    name: str
    city: str
    postal_code: str
    country: str
