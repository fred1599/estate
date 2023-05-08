"""
Entities for Address Models
"""

import pydantic


class Address(pydantic.BaseModel):
    """
    A base real class for Address entities
    """

    name: str
    city: str
    postal_code: str
    country: str
