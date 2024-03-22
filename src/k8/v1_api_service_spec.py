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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conbytes, constr, validator
from .apiregistration_v1_service_reference import ApiregistrationV1ServiceReference

class V1APIServiceSpec(BaseModel):
    """
    APIServiceSpec contains information for locating and communicating with a server. Only https is supported, though you are able to disable certificate verification.  # noqa: E501
    """
    ca_bundle: Optional[Union[conbytes(strict=True), constr(strict=True)]] = Field(default=None, alias="caBundle", description="CABundle is a PEM encoded CA bundle which will be used to validate an API server's serving certificate. If unspecified, system trust roots on the apiserver are used.")
    group: Optional[StrictStr] = Field(default=None, description="Group is the API group name this server hosts")
    group_priority_minimum: StrictInt = Field(..., alias="groupPriorityMinimum", description="GroupPriorityMinimum is the priority this group should have at least. Higher priority means that the group is preferred by clients over lower priority ones. Note that other versions of this group might specify even higher GroupPriorityMinimum values such that the whole group gets a higher priority. The primary sort is based on GroupPriorityMinimum, ordered highest number to lowest (20 before 10). The secondary sort is based on the alphabetical comparison of the name of the object.  (v1.bar before v1.foo) We'd recommend something like: *.k8s.io (except extensions) at 18000 and PaaSes (OpenShift, Deis) are recommended to be in the 2000s")
    insecure_skip_tls_verify: Optional[StrictBool] = Field(default=None, alias="insecureSkipTLSVerify", description="InsecureSkipTLSVerify disables TLS certificate verification when communicating with this server. This is strongly discouraged.  You should use the CABundle instead.")
    service: Optional[ApiregistrationV1ServiceReference] = None
    version: Optional[StrictStr] = Field(default=None, description="Version is the API version this server hosts.  For example, \"v1\"")
    version_priority: StrictInt = Field(..., alias="versionPriority", description="VersionPriority controls the ordering of this API version inside of its group.  Must be greater than zero. The primary sort is based on VersionPriority, ordered highest to lowest (20 before 10). Since it's inside of a group, the number can be small, probably in the 10s. In case of equal version priorities, the version string will be used to compute the order inside a group. If the version string is \"kube-like\", it will sort above non \"kube-like\" version strings, which are ordered lexicographically. \"Kube-like\" versions start with a \"v\", then are followed by a number (the major version), then optionally the string \"alpha\" or \"beta\" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.")
    __properties = ["caBundle", "group", "groupPriorityMinimum", "insecureSkipTLSVerify", "service", "version", "versionPriority"]

    @validator('ca_bundle')
    def ca_bundle_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$", value):
            raise ValueError(r"must validate the regular expression /^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/")
        return value

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
    def from_json(cls, json_str: str) -> V1APIServiceSpec:
        """Create an instance of V1APIServiceSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict['service'] = self.service.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1APIServiceSpec:
        """Create an instance of V1APIServiceSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1APIServiceSpec.parse_obj(obj)

        _obj = V1APIServiceSpec.parse_obj({
            "ca_bundle": obj.get("caBundle"),
            "group": obj.get("group"),
            "group_priority_minimum": obj.get("groupPriorityMinimum"),
            "insecure_skip_tls_verify": obj.get("insecureSkipTLSVerify"),
            "service": ApiregistrationV1ServiceReference.from_dict(obj.get("service")) if obj.get("service") is not None else None,
            "version": obj.get("version"),
            "version_priority": obj.get("versionPriority")
        })
        return _obj

