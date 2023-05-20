"""
Estimation of a property's value.
"""

import pydantic

# Business constants
VALUE_PER_SQFT = 1000  # Represents the base value of a property per square foot.
MAX_AGE = 100  # Represents the maximum considered age of a property.
# Represents the condition modifier when the property is in 'good' condition.
GOOD_CONDITION_MODIFIER = 1.0
# Represents the condition modifier when the property is in 'bad' condition.
BAD_CONDITION_MODIFIER = 0.8


class Property(pydantic.BaseModel):
    """
    A class used to represent a Property.

    Attributes
    ----------
    location : str
        The location of the property.
    size : float
        The size of the property in square feet.
    age : int
        The age of the property in years.
    condition : str
        The condition of the property, can be either 'good' or 'bad'.
    """

    location: str
    size: float
    age: int
    condition: str


class Estimator:
    """
    A class used to estimate the value of a Property.

    Methods
    -------
    estimate_value(property)
        Estimates the value of a property based on its size, age,
        and condition. It uses business constants for the calculation.
    """

    def estimate_value(self, property: Property) -> float:
        """
        Estimate the value of a property based on its size, age, and condition.

        The base value is calculated as the size of the property multiplied by
        a per square foot value (VALUE_PER_SQFT).
        An age modifier is calculated based on the age of the property relative
        to a maximum age (MAX_AGE).
        A condition modifier is determined based on the condition of the property,
        with different modifiers for 'good' and 'bad' conditions
        (GOOD_CONDITION_MODIFIER, BAD_CONDITION_MODIFIER).

        Parameters
        ----------
        property : Property
            The property to estimate the value of.

        Returns
        -------
        float
            The estimated value of the property.
        """

        base_value: float = property.size * VALUE_PER_SQFT
        age_modifier: float = (MAX_AGE - property.age) / MAX_AGE
        condition_modifier: float = (
            GOOD_CONDITION_MODIFIER
            if property.condition == "good"
            else BAD_CONDITION_MODIFIER
        )

        estimated_value: float = base_value * age_modifier * condition_modifier

        return estimated_value
