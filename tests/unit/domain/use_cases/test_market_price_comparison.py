from decimal import Decimal

import pytest

from estate_project.domain.entities.market_price_comparison import \
    PropertyPriceComparisonResult
from estate_project.domain.entities.real_estate import BaseRealEstate
from estate_project.domain.use_cases.market_price_comparison import \
    MarketPriceComparison


@pytest.fixture
def properties() -> list[BaseRealEstate]:
    """
    Fixture that creates a list of BaseRealEstate objects for test purposes.
    """
    return [
        BaseRealEstate(
            id="1",
            title="Maison 1",
            address=None,
            description="Maison avec jardin",
            price="350000",
            currency="€",
            area="120",
            available=True,
        ),
        BaseRealEstate(
            id="2",
            title="Maison 2",
            address=None,
            description="Maison sans jardin",
            price="300000",
            currency="€",
            area="100",
            available=True,
        ),
    ]


@pytest.fixture
def target_property() -> BaseRealEstate:
    """
    Fixture that creates a target BaseRealEstate object for test purposes.
    """
    return BaseRealEstate(
        id="3",
        title="Maison 3",
        address=None,
        description="Maison avec piscine",
        price="400000",
        currency="€",
        area="150",
        available=True,
    )


def test_market_price_comparison(properties, target_property) -> None:
    """
    Test the MarketPriceComparison.compare method with valid inputs.
    """
    market_price_comparison = MarketPriceComparison(properties)
    result: list[PropertyPriceComparisonResult] = market_price_comparison.compare(
        target_property
    )

    assert len(result) == 2
    assert all(isinstance(res, PropertyPriceComparisonResult) for res in result)
    assert result[0].price_difference == "50000"
    assert result[1].price_difference == "100000"


def test_market_price_comparison_invalid_input() -> None:
    """
    Test the MarketPriceComparison constructor with an empty list, expecting a ValueError.
    """
    empty_properties: list = []

    with pytest.raises(ValueError):
        MarketPriceComparison(empty_properties)


def test_market_price_comparison_no_price(properties, target_property) -> None:
    """
    Test the MarketPriceComparison.compare method when the properties have no price.
    """
    for prop in properties:
        prop.price = None

    market_price_comparison = MarketPriceComparison(properties)
    result: list[PropertyPriceComparisonResult] = market_price_comparison.compare(
        target_property
    )

    assert len(result) == 0
