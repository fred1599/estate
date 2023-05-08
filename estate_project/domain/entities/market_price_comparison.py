from pydantic import BaseModel

from estate_project.domain.entities.real_estate import BaseRealEstate


class PropertyPriceComparisonResult(BaseModel):
    compared_property: BaseRealEstate
    target_property: BaseRealEstate
    price_difference: str
