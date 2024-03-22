# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.29
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from .v1_claim_source import V1ClaimSource

class V1PodResourceClaim(BaseModel):
    """
    PodResourceClaim references exactly one ResourceClaim through a ClaimSource. It adds a name to it that uniquely identifies the ResourceClaim inside the Pod. Containers that need access to the ResourceClaim reference it with this name.  # noqa: E501
    """
    name: StrictStr = Field(..., description="Name uniquely identifies this resource claim inside the pod. This must be a DNS_LABEL.")
    source: Optional[V1ClaimSource] = None
    __properties = ["name", "source"]

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
    def from_json(cls, json_str: str) -> V1PodResourceClaim:
        """Create an instance of V1PodResourceClaim from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodResourceClaim:
        """Create an instance of V1PodResourceClaim from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodResourceClaim.parse_obj(obj)

        _obj = V1PodResourceClaim.parse_obj({
            "name": obj.get("name"),
            "source": V1ClaimSource.from_dict(obj.get("source")) if obj.get("source") is not None else None
        })
        return _obj

