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
from .v1_endpoint_conditions import V1EndpointConditions
from .v1_endpoint_hints import V1EndpointHints
from .v1_object_reference import V1ObjectReference
from typing import Optional, Set
from typing_extensions import Self

class V1Endpoint(BaseModel):
    """
    Endpoint represents a single logical \"backend\" implementing a service.
    """ # noqa: E501
    addresses: List[StrictStr] = Field(description="addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267")
    conditions: Optional[V1EndpointConditions] = None
    deprecated_topology: Optional[Dict[str, StrictStr]] = Field(default=None, description="deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.", alias="deprecatedTopology")
    hints: Optional[V1EndpointHints] = None
    hostname: Optional[StrictStr] = Field(default=None, description="hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.")
    node_name: Optional[StrictStr] = Field(default=None, description="nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node.", alias="nodeName")
    target_ref: Optional[V1ObjectReference] = Field(default=None, alias="targetRef")
    zone: Optional[StrictStr] = Field(default=None, description="zone is the name of the Zone this endpoint exists in.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["addresses", "conditions", "deprecatedTopology", "hints", "hostname", "nodeName", "targetRef", "zone"]

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
        """Create an instance of V1Endpoint from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hints
        if self.hints:
            _dict['hints'] = self.hints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_ref
        if self.target_ref:
            _dict['targetRef'] = self.target_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1Endpoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addresses": obj.get("addresses"),
            "conditions": V1EndpointConditions.from_dict(obj["conditions"]) if obj.get("conditions") is not None else None,
            "deprecatedTopology": obj.get("deprecatedTopology"),
            "hints": V1EndpointHints.from_dict(obj["hints"]) if obj.get("hints") is not None else None,
            "hostname": obj.get("hostname"),
            "nodeName": obj.get("nodeName"),
            "targetRef": V1ObjectReference.from_dict(obj["targetRef"]) if obj.get("targetRef") is not None else None,
            "zone": obj.get("zone")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


