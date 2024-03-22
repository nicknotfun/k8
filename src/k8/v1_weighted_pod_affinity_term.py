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



from pydantic import BaseModel, Field, StrictInt
from .v1_pod_affinity_term import V1PodAffinityTerm

class V1WeightedPodAffinityTerm(BaseModel):
    """
    The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)  # noqa: E501
    """
    pod_affinity_term: V1PodAffinityTerm = Field(..., alias="podAffinityTerm")
    weight: StrictInt = Field(..., description="weight associated with matching the corresponding podAffinityTerm, in the range 1-100.")
    __properties = ["podAffinityTerm", "weight"]

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
    def from_json(cls, json_str: str) -> V1WeightedPodAffinityTerm:
        """Create an instance of V1WeightedPodAffinityTerm from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of pod_affinity_term
        if self.pod_affinity_term:
            _dict['podAffinityTerm'] = self.pod_affinity_term.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1WeightedPodAffinityTerm:
        """Create an instance of V1WeightedPodAffinityTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1WeightedPodAffinityTerm.parse_obj(obj)

        _obj = V1WeightedPodAffinityTerm.parse_obj({
            "pod_affinity_term": V1PodAffinityTerm.from_dict(obj.get("podAffinityTerm")) if obj.get("podAffinityTerm") is not None else None,
            "weight": obj.get("weight")
        })
        return _obj

