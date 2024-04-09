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
from .v1_secret_reference import V1SecretReference
from typing import Optional, Set
from typing_extensions import Self

class V1CSIPersistentVolumeSource(BaseModel):
    """
    Represents storage that is managed by an external CSI volume driver (Beta feature)
    """ # noqa: E501
    controller_expand_secret_ref: Optional[V1SecretReference] = Field(default=None, alias="controllerExpandSecretRef")
    controller_publish_secret_ref: Optional[V1SecretReference] = Field(default=None, alias="controllerPublishSecretRef")
    driver: StrictStr = Field(description="driver is the name of the driver to use for this volume. Required.")
    fs_type: Optional[StrictStr] = Field(default=None, description="fsType to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\".", alias="fsType")
    node_expand_secret_ref: Optional[V1SecretReference] = Field(default=None, alias="nodeExpandSecretRef")
    node_publish_secret_ref: Optional[V1SecretReference] = Field(default=None, alias="nodePublishSecretRef")
    node_stage_secret_ref: Optional[V1SecretReference] = Field(default=None, alias="nodeStageSecretRef")
    read_only: Optional[StrictBool] = Field(default=None, description="readOnly value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write).", alias="readOnly")
    volume_attributes: Optional[Dict[str, StrictStr]] = Field(default=None, description="volumeAttributes of the volume to publish.", alias="volumeAttributes")
    volume_handle: StrictStr = Field(description="volumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required.", alias="volumeHandle")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["controllerExpandSecretRef", "controllerPublishSecretRef", "driver", "fsType", "nodeExpandSecretRef", "nodePublishSecretRef", "nodeStageSecretRef", "readOnly", "volumeAttributes", "volumeHandle"]

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
        """Create an instance of V1CSIPersistentVolumeSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of controller_expand_secret_ref
        if self.controller_expand_secret_ref:
            _dict['controllerExpandSecretRef'] = self.controller_expand_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of controller_publish_secret_ref
        if self.controller_publish_secret_ref:
            _dict['controllerPublishSecretRef'] = self.controller_publish_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_expand_secret_ref
        if self.node_expand_secret_ref:
            _dict['nodeExpandSecretRef'] = self.node_expand_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_publish_secret_ref
        if self.node_publish_secret_ref:
            _dict['nodePublishSecretRef'] = self.node_publish_secret_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_stage_secret_ref
        if self.node_stage_secret_ref:
            _dict['nodeStageSecretRef'] = self.node_stage_secret_ref.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CSIPersistentVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "controllerExpandSecretRef": V1SecretReference.from_dict(obj["controllerExpandSecretRef"]) if obj.get("controllerExpandSecretRef") is not None else None,
            "controllerPublishSecretRef": V1SecretReference.from_dict(obj["controllerPublishSecretRef"]) if obj.get("controllerPublishSecretRef") is not None else None,
            "driver": obj.get("driver"),
            "fsType": obj.get("fsType"),
            "nodeExpandSecretRef": V1SecretReference.from_dict(obj["nodeExpandSecretRef"]) if obj.get("nodeExpandSecretRef") is not None else None,
            "nodePublishSecretRef": V1SecretReference.from_dict(obj["nodePublishSecretRef"]) if obj.get("nodePublishSecretRef") is not None else None,
            "nodeStageSecretRef": V1SecretReference.from_dict(obj["nodeStageSecretRef"]) if obj.get("nodeStageSecretRef") is not None else None,
            "readOnly": obj.get("readOnly"),
            "volumeAttributes": obj.get("volumeAttributes"),
            "volumeHandle": obj.get("volumeHandle")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


