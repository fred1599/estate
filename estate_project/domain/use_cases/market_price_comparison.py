"""
Comparison of local real estate market prices
"""

from decimal import Decimal

from estate_project.domain.entities.market_price_comparison import \
    PropertyPriceComparisonResult
from estate_project.domain.entities.real_estate import BaseRealEstate


class MarketPriceComparison:
    """
    A class to represent the comparison of real estate market prices.

    Attributes:
        properties (list[BaseRealEstate]): A list of properties to be compared.

    Methods:
        compare(target_property: BaseRealEstate) -> list[PropertyPriceComparisonResult]:
            Compares the target property price with the prices of the properties in the list.
    """

    def __init__(self, properties: list[BaseRealEstate]) -> None:
        if not properties:
            raise ValueError("At least one property is required for comparison")
        self.properties: list[BaseRealEstate] = properties

    def compare(
        self, target_property: BaseRealEstate
    ) -> list[PropertyPriceComparisonResult]:
        """
        Compares the target property price with the prices of the properties in the list.

        Args:
            target_property (BaseRealEstate): The target property for price comparison.

        Returns:
            list[PropertyPriceComparisonResult]: A list of price comparison results for each property in the list.
        """

        results: list[PropertyPriceComparisonResult] = []
        if target_property.price is None:
            return results
        target_price = Decimal(target_property.price)
        for prop in self.properties:
            if prop.price is not None:
                price_difference: Decimal = target_price - Decimal(prop.price)
                result = PropertyPriceComparisonResult(
                    compared_property=prop,
                    target_property=target_property,
                    price_difference=str(price_difference),
                )
                results.append(result)
        return results
