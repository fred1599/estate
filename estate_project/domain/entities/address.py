from pydantic import BaseModel


class Address(BaseModel):
    name: str
    city: str
    postal_code: str
    country: str
