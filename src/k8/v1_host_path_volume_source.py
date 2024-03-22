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

class V1HostPathVolumeSource(BaseModel):
    """
    Represents a host path mapped into a pod. Host path volumes do not support ownership management or SELinux relabeling.  # noqa: E501
    """
    path: StrictStr = Field(..., description="path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath")
    type: Optional[StrictStr] = Field(default=None, description="type for HostPath Volume Defaults to \"\" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath")
    __properties = ["path", "type"]

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
    def from_json(cls, json_str: str) -> V1HostPathVolumeSource:
        """Create an instance of V1HostPathVolumeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1HostPathVolumeSource:
        """Create an instance of V1HostPathVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1HostPathVolumeSource.parse_obj(obj)

        _obj = V1HostPathVolumeSource.parse_obj({
            "path": obj.get("path"),
            "type": obj.get("type")
        })
        return _obj

