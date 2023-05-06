"""
Biens immobiliers
"""

from typing import Optional
from pydantic import BaseModel

from estate_project.domain.entities.address import Address


class BaseProperty(BaseModel):
    id: str
    title: Optional[str]
    address: Address
    description: Optional[str]
    price: Optional[str]
    currency: str
    area: str
    num_bedrooms: str
    num_bathrooms: str
    construction_year: str
    available: bool  # à vendre (True) ou à louer (False)
    images: list[str]  # liste des images de la maison

class House(BaseProperty):
    num_floors: str
    has_garden: bool
    has_garage: bool

class Apartment(BaseProperty):
    num_floors: str
    has_elevator: bool  # ascenseur
    has_balcony: bool

