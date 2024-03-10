# coding: utf-8

"""
    Vault Management API

    This schema documents the endpoints available to the Vault Management API, accessible from the Bitwarden CLI using the `bw serve` command ([learn more](https://bitwarden.com/help/cli/)). If you're looking for the **Organization Management** API, refer instead to [this document](https://bitwarden.com/help/api/).

    The version of the OpenAPI document: latest
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, validator

class ItemCard(BaseModel):
    """
    ItemCard
    """
    brand: Optional[StrictStr] = None
    cardholder_name: Optional[StrictStr] = Field(None, alias="cardholderName")
    code: Optional[StrictStr] = None
    exp_month: Optional[StrictStr] = Field(None, alias="expMonth")
    exp_year: Optional[StrictStr] = Field(None, alias="expYear")
    number: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["brand", "cardholderName", "code", "expMonth", "expYear", "number"]

    @validator('brand')
    def brand_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('visa'):
            raise ValueError("must be one of enum values ('visa')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ItemCard:
        """Create an instance of ItemCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ItemCard:
        """Create an instance of ItemCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ItemCard.parse_obj(obj)

        _obj = ItemCard.parse_obj({
            "brand": obj.get("brand"),
            "cardholder_name": obj.get("cardholderName"),
            "code": obj.get("code"),
            "exp_month": obj.get("expMonth"),
            "exp_year": obj.get("expYear"),
            "number": obj.get("number")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


