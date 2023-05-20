import pytest

from estate_project.domain.use_cases.property_valuation import (
    Property,
    Estimator,
    VALUE_PER_SQFT,
    MAX_AGE,
    GOOD_CONDITION_MODIFIER,
    BAD_CONDITION_MODIFIER,
)


def test_estimation():
    property = Property(location="Paris", size=50.0, age=10, condition="good")
    estimator = Estimator()

    estimated_value = estimator.estimate_value(property)

    expected_value = (
        property.size
        * VALUE_PER_SQFT
        * ((MAX_AGE - property.age) / MAX_AGE)
        * GOOD_CONDITION_MODIFIER
    )
    assert estimated_value == expected_value


def test_bad_condition_estimation():
    property = Property(location="Paris", size=50.0, age=10, condition="bad")
    estimator = Estimator()

    estimated_value = estimator.estimate_value(property)

    expected_value = (
        property.size
        * VALUE_PER_SQFT
        * ((MAX_AGE - property.age) / MAX_AGE)
        * BAD_CONDITION_MODIFIER
    )
    assert estimated_value == expected_value
