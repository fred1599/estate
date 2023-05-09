"""
This module contains the PropertyPriceComparisonResult
class which represents the result of a property
price comparison between two real estate properties.

Classes:
    - PropertyPriceComparisonResult: A model that holds the result of a property price comparison.
"""

from pydantic import BaseModel

from estate_project.domain.entities.real_estate import BaseRealEstate


class PropertyPriceComparisonResult(BaseModel):
    """
    A model that represents the result of a property price comparison.

    Attributes:
        compared_property (BaseRealEstate):
        The property being compared to the target property.
        target_property (BaseRealEstate):
        The property that serves as a reference for the comparison.

        price_difference (str): The difference in price between
        the compared property and the target property.
    """

    compared_property: BaseRealEstate
    target_property: BaseRealEstate
    price_difference: str
