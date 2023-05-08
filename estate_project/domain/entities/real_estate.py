"""
All entities for RealEstate

This module contains the data models for different
types of real estate entities including base classes
for real estate and properties, and specific classes
for houses, apartments, and land.
"""

from typing import Optional

import pydantic

from estate_project.domain.entities.address import Address


class BaseRealEstate(pydantic.BaseModel):
    """A base class for real estate entities."""

    id: str
    title: Optional[str]
    address: Optional[Address]
    description: Optional[str]
    price: Optional[str]
    currency: Optional[str]
    area: Optional[str]
    available: Optional[bool]  # à vendre (True) ou à louer (False)
    images: Optional[list[str]]  # liste des images de la maison


class BaseProperty(BaseRealEstate):
    """A base class for property entities."""

    num_bedrooms: Optional[str]
    num_bathrooms: Optional[str]
    construction_year: Optional[str]


class House(BaseProperty):
    """A class representing a house entity."""

    num_floors: Optional[str]
    has_garden: Optional[bool]
    has_garage: Optional[bool]


class Apartment(BaseProperty):
    """A class representing an apartment entity."""

    num_floors: Optional[str]
    has_elevator: Optional[bool]  # ascenseur
    has_balcony: Optional[bool]


class Land(BaseRealEstate):
    """A class representing a land entity."""

    land_area: str
    zoning_type: Optional[str]
    has_utilities: bool  # eau, électricité, gaz... disponibles ou pas
    has_road_access: bool
    topography: str
    soil_type: str  # type de sol présent
    vegetation: str
    permits_available: bool
    flood_risk: bool
