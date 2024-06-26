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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from .v1_ip_block import V1IPBlock
from .v1_label_selector import V1LabelSelector
from typing import Optional, Set
from typing_extensions import Self

class V1NetworkPolicyPeer(BaseModel):
    """
    NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed
    """ # noqa: E501
    ip_block: Optional[V1IPBlock] = Field(default=None, alias="ipBlock")
    namespace_selector: Optional[V1LabelSelector] = Field(default=None, alias="namespaceSelector")
    pod_selector: Optional[V1LabelSelector] = Field(default=None, alias="podSelector")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["ipBlock", "namespaceSelector", "podSelector"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V1NetworkPolicyPeer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ip_block
        if self.ip_block:
            _dict['ipBlock'] = self.ip_block.to_dict()
        # override the default output from pydantic by calling `to_dict()` of namespace_selector
        if self.namespace_selector:
            _dict['namespaceSelector'] = self.namespace_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pod_selector
        if self.pod_selector:
            _dict['podSelector'] = self.pod_selector.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1NetworkPolicyPeer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipBlock": V1IPBlock.from_dict(obj["ipBlock"]) if obj.get("ipBlock") is not None else None,
            "namespaceSelector": V1LabelSelector.from_dict(obj["namespaceSelector"]) if obj.get("namespaceSelector") is not None else None,
            "podSelector": V1LabelSelector.from_dict(obj["podSelector"]) if obj.get("podSelector") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


