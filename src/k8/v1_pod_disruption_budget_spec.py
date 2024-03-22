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
from .v1_label_selector import V1LabelSelector

class V1PodDisruptionBudgetSpec(BaseModel):
    """
    PodDisruptionBudgetSpec is a description of a PodDisruptionBudget.  # noqa: E501
    """
    max_unavailable: Optional[StrictStr] = Field(default=None, alias="maxUnavailable", description="An eviction is allowed if at most \"maxUnavailable\" pods selected by \"selector\" are unavailable after the eviction, i.e. even in absence of the evicted pod. For example, one can prevent all voluntary evictions by specifying 0. This is a mutually exclusive setting with \"minAvailable\".")
    min_available: Optional[StrictStr] = Field(default=None, alias="minAvailable", description="An eviction is allowed if at least \"minAvailable\" pods selected by \"selector\" will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying \"100%\".")
    selector: Optional[V1LabelSelector] = None
    unhealthy_pod_eviction_policy: Optional[StrictStr] = Field(default=None, alias="unhealthyPodEvictionPolicy", description="UnhealthyPodEvictionPolicy defines the criteria for when unhealthy pods should be considered for eviction. Current implementation considers healthy pods, as pods that have status.conditions item with type=\"Ready\",status=\"True\".  Valid policies are IfHealthyBudget and AlwaysAllow. If no policy is specified, the default behavior will be used, which corresponds to the IfHealthyBudget policy.  IfHealthyBudget policy means that running pods (status.phase=\"Running\"), but not yet healthy can be evicted only if the guarded application is not disrupted (status.currentHealthy is at least equal to status.desiredHealthy). Healthy pods will be subject to the PDB for eviction.  AlwaysAllow policy means that all running pods (status.phase=\"Running\"), but not yet healthy are considered disrupted and can be evicted regardless of whether the criteria in a PDB is met. This means perspective running pods of a disrupted application might not get a chance to become healthy. Healthy pods will be subject to the PDB for eviction.  Additional policies may be added in the future. Clients making eviction decisions should disallow eviction of unhealthy pods if they encounter an unrecognized policy in this field.  This field is beta-level. The eviction API uses this field when the feature gate PDBUnhealthyPodEvictionPolicy is enabled (enabled by default).")
    __properties = ["maxUnavailable", "minAvailable", "selector", "unhealthyPodEvictionPolicy"]

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
    def from_json(cls, json_str: str) -> V1PodDisruptionBudgetSpec:
        """Create an instance of V1PodDisruptionBudgetSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of selector
        if self.selector:
            _dict['selector'] = self.selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1PodDisruptionBudgetSpec:
        """Create an instance of V1PodDisruptionBudgetSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1PodDisruptionBudgetSpec.parse_obj(obj)

        _obj = V1PodDisruptionBudgetSpec.parse_obj({
            "max_unavailable": obj.get("maxUnavailable"),
            "min_available": obj.get("minAvailable"),
            "selector": V1LabelSelector.from_dict(obj.get("selector")) if obj.get("selector") is not None else None,
            "unhealthy_pod_eviction_policy": obj.get("unhealthyPodEvictionPolicy")
        })
        return _obj


