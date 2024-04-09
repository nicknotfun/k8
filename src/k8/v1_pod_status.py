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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .v1_container_status import V1ContainerStatus
from .v1_host_ip import V1HostIP
from .v1_pod_condition import V1PodCondition
from .v1_pod_ip import V1PodIP
from .v1_pod_resource_claim_status import V1PodResourceClaimStatus
from typing import Optional, Set
from typing_extensions import Self

class V1PodStatus(BaseModel):
    """
    PodStatus represents information about the status of a pod. Status may trail the actual state of a system, especially if the node that hosts the pod cannot contact the control plane.
    """ # noqa: E501
    conditions: Optional[List[V1PodCondition]] = Field(default=None, description="Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions")
    container_statuses: Optional[List[V1ContainerStatus]] = Field(default=None, description="The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status", alias="containerStatuses")
    ephemeral_container_statuses: Optional[List[V1ContainerStatus]] = Field(default=None, description="Status for any ephemeral containers that have run in this pod.", alias="ephemeralContainerStatuses")
    host_ip: Optional[StrictStr] = Field(default=None, description="hostIP holds the IP address of the host to which the pod is assigned. Empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns mean that HostIP will not be updated even if there is a node is assigned to pod", alias="hostIP")
    host_ips: Optional[List[V1HostIP]] = Field(default=None, description="hostIPs holds the IP addresses allocated to the host. If this field is specified, the first entry must match the hostIP field. This list is empty if the pod has not started yet. A pod can be assigned to a node that has a problem in kubelet which in turns means that HostIPs will not be updated even if there is a node is assigned to this pod.", alias="hostIPs")
    init_container_statuses: Optional[List[V1ContainerStatus]] = Field(default=None, description="The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status", alias="initContainerStatuses")
    message: Optional[StrictStr] = Field(default=None, description="A human readable message indicating details about why the pod is in this condition.")
    nominated_node_name: Optional[StrictStr] = Field(default=None, description="nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.", alias="nominatedNodeName")
    phase: Optional[StrictStr] = Field(default=None, description="The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase")
    pod_ip: Optional[StrictStr] = Field(default=None, description="podIP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.", alias="podIP")
    pod_ips: Optional[List[V1PodIP]] = Field(default=None, description="podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.", alias="podIPs")
    qos_class: Optional[StrictStr] = Field(default=None, description="The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes", alias="qosClass")
    reason: Optional[StrictStr] = Field(default=None, description="A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'")
    resize: Optional[StrictStr] = Field(default=None, description="Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\"")
    resource_claim_statuses: Optional[List[V1PodResourceClaimStatus]] = Field(default=None, description="Status of resource claims.", alias="resourceClaimStatuses")
    start_time: Optional[datetime] = Field(default=None, description="RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.", alias="startTime")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["conditions", "containerStatuses", "ephemeralContainerStatuses", "hostIP", "hostIPs", "initContainerStatuses", "message", "nominatedNodeName", "phase", "podIP", "podIPs", "qosClass", "reason", "resize", "resourceClaimStatuses", "startTime"]

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
        """Create an instance of V1PodStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in container_statuses (list)
        _items = []
        if self.container_statuses:
            for _item in self.container_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['containerStatuses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ephemeral_container_statuses (list)
        _items = []
        if self.ephemeral_container_statuses:
            for _item in self.ephemeral_container_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ephemeralContainerStatuses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in host_ips (list)
        _items = []
        if self.host_ips:
            for _item in self.host_ips:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hostIPs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in init_container_statuses (list)
        _items = []
        if self.init_container_statuses:
            for _item in self.init_container_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['initContainerStatuses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pod_ips (list)
        _items = []
        if self.pod_ips:
            for _item in self.pod_ips:
                if _item:
                    _items.append(_item.to_dict())
            _dict['podIPs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resource_claim_statuses (list)
        _items = []
        if self.resource_claim_statuses:
            for _item in self.resource_claim_statuses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceClaimStatuses'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1PodStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conditions": [V1PodCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "containerStatuses": [V1ContainerStatus.from_dict(_item) for _item in obj["containerStatuses"]] if obj.get("containerStatuses") is not None else None,
            "ephemeralContainerStatuses": [V1ContainerStatus.from_dict(_item) for _item in obj["ephemeralContainerStatuses"]] if obj.get("ephemeralContainerStatuses") is not None else None,
            "hostIP": obj.get("hostIP"),
            "hostIPs": [V1HostIP.from_dict(_item) for _item in obj["hostIPs"]] if obj.get("hostIPs") is not None else None,
            "initContainerStatuses": [V1ContainerStatus.from_dict(_item) for _item in obj["initContainerStatuses"]] if obj.get("initContainerStatuses") is not None else None,
            "message": obj.get("message"),
            "nominatedNodeName": obj.get("nominatedNodeName"),
            "phase": obj.get("phase"),
            "podIP": obj.get("podIP"),
            "podIPs": [V1PodIP.from_dict(_item) for _item in obj["podIPs"]] if obj.get("podIPs") is not None else None,
            "qosClass": obj.get("qosClass"),
            "reason": obj.get("reason"),
            "resize": obj.get("resize"),
            "resourceClaimStatuses": [V1PodResourceClaimStatus.from_dict(_item) for _item in obj["resourceClaimStatuses"]] if obj.get("resourceClaimStatuses") is not None else None,
            "startTime": obj.get("startTime")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


