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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .v1_custom_resource_column_definition import V1CustomResourceColumnDefinition
from .v1_custom_resource_subresources import V1CustomResourceSubresources
from .v1_custom_resource_validation import V1CustomResourceValidation
from typing import Optional, Set
from typing_extensions import Self

class V1CustomResourceDefinitionVersion(BaseModel):
    """
    CustomResourceDefinitionVersion describes a version for CRD.
    """ # noqa: E501
    additional_printer_columns: Optional[List[V1CustomResourceColumnDefinition]] = Field(default=None, description="additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used.", alias="additionalPrinterColumns")
    deprecated: Optional[StrictBool] = Field(default=None, description="deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false.")
    deprecation_warning: Optional[StrictStr] = Field(default=None, description="deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists.", alias="deprecationWarning")
    name: StrictStr = Field(description="name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/...` if `served` is true.")
    var_schema: Optional[V1CustomResourceValidation] = Field(default=None, alias="schema")
    served: StrictBool = Field(description="served is a flag enabling/disabling this version from being served via REST APIs")
    storage: StrictBool = Field(description="storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true.")
    subresources: Optional[V1CustomResourceSubresources] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["additionalPrinterColumns", "deprecated", "deprecationWarning", "name", "schema", "served", "storage", "subresources"]

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
        """Create an instance of V1CustomResourceDefinitionVersion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in additional_printer_columns (list)
        _items = []
        if self.additional_printer_columns:
            for _item in self.additional_printer_columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalPrinterColumns'] = _items
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subresources
        if self.subresources:
            _dict['subresources'] = self.subresources.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CustomResourceDefinitionVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "additionalPrinterColumns": [V1CustomResourceColumnDefinition.from_dict(_item) for _item in obj["additionalPrinterColumns"]] if obj.get("additionalPrinterColumns") is not None else None,
            "deprecated": obj.get("deprecated"),
            "deprecationWarning": obj.get("deprecationWarning"),
            "name": obj.get("name"),
            "schema": V1CustomResourceValidation.from_dict(obj["schema"]) if obj.get("schema") is not None else None,
            "served": obj.get("served"),
            "storage": obj.get("storage"),
            "subresources": V1CustomResourceSubresources.from_dict(obj["subresources"]) if obj.get("subresources") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


