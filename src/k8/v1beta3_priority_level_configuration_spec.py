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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .v1beta3_exempt_priority_level_configuration import V1beta3ExemptPriorityLevelConfiguration
from .v1beta3_limited_priority_level_configuration import V1beta3LimitedPriorityLevelConfiguration
from typing import Optional, Set
from typing_extensions import Self

class V1beta3PriorityLevelConfigurationSpec(BaseModel):
    """
    PriorityLevelConfigurationSpec specifies the configuration of a priority level.
    """ # noqa: E501
    exempt: Optional[V1beta3ExemptPriorityLevelConfiguration] = None
    limited: Optional[V1beta3LimitedPriorityLevelConfiguration] = None
    type: StrictStr = Field(description="`type` indicates whether this priority level is subject to limitation on request execution.  A value of `\"Exempt\"` means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of `\"Limited\"` means that (a) requests of this priority level _are_ subject to limits and (b) some of the server's limited capacity is made available exclusively to this priority level. Required.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["exempt", "limited", "type"]

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
        """Create an instance of V1beta3PriorityLevelConfigurationSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of exempt
        if self.exempt:
            _dict['exempt'] = self.exempt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limited
        if self.limited:
            _dict['limited'] = self.limited.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1beta3PriorityLevelConfigurationSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exempt": V1beta3ExemptPriorityLevelConfiguration.from_dict(obj["exempt"]) if obj.get("exempt") is not None else None,
            "limited": V1beta3LimitedPriorityLevelConfiguration.from_dict(obj["limited"]) if obj.get("limited") is not None else None,
            "type": obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


