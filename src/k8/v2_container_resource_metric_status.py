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



from pydantic import BaseModel, Field, StrictStr
from .v2_metric_value_status import V2MetricValueStatus

class V2ContainerResourceMetricStatus(BaseModel):
    """
    ContainerResourceMetricStatus indicates the current value of a resource metric known to Kubernetes, as specified in requests and limits, describing a single container in each pod in the current scale target (e.g. CPU or memory).  Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the \"pods\" source.  # noqa: E501
    """
    container: StrictStr = Field(..., description="container is the name of the container in the pods of the scaling target")
    current: V2MetricValueStatus = Field(...)
    name: StrictStr = Field(..., description="name is the name of the resource in question.")
    __properties = ["container", "current", "name"]

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
    def from_json(cls, json_str: str) -> V2ContainerResourceMetricStatus:
        """Create an instance of V2ContainerResourceMetricStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V2ContainerResourceMetricStatus:
        """Create an instance of V2ContainerResourceMetricStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V2ContainerResourceMetricStatus.parse_obj(obj)

        _obj = V2ContainerResourceMetricStatus.parse_obj({
            "container": obj.get("container"),
            "current": V2MetricValueStatus.from_dict(obj.get("current")) if obj.get("current") is not None else None,
            "name": obj.get("name")
        })
        return _obj

