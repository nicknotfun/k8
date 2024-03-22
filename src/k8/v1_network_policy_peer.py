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
from pydantic import BaseModel, Field
from .v1_ip_block import V1IPBlock
from .v1_label_selector import V1LabelSelector

class V1NetworkPolicyPeer(BaseModel):
    """
    NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed  # noqa: E501
    """
    ip_block: Optional[V1IPBlock] = Field(default=None, alias="ipBlock")
    namespace_selector: Optional[V1LabelSelector] = Field(default=None, alias="namespaceSelector")
    pod_selector: Optional[V1LabelSelector] = Field(default=None, alias="podSelector")
    __properties = ["ipBlock", "namespaceSelector", "podSelector"]

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
    def from_json(cls, json_str: str) -> V1NetworkPolicyPeer:
        """Create an instance of V1NetworkPolicyPeer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ip_block
        if self.ip_block:
            _dict['ipBlock'] = self.ip_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of namespace_selector
        if self.namespace_selector:
            _dict['namespaceSelector'] = self.namespace_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pod_selector
        if self.pod_selector:
            _dict['podSelector'] = self.pod_selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1NetworkPolicyPeer:
        """Create an instance of V1NetworkPolicyPeer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1NetworkPolicyPeer.parse_obj(obj)

        _obj = V1NetworkPolicyPeer.parse_obj({
            "ip_block": V1IPBlock.from_dict(obj.get("ipBlock")) if obj.get("ipBlock") is not None else None,
            "namespace_selector": V1LabelSelector.from_dict(obj.get("namespaceSelector")) if obj.get("namespaceSelector") is not None else None,
            "pod_selector": V1LabelSelector.from_dict(obj.get("podSelector")) if obj.get("podSelector") is not None else None
        })
        return _obj

