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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from .v1_container_port import V1ContainerPort
from .v1_container_resize_policy import V1ContainerResizePolicy
from .v1_env_from_source import V1EnvFromSource
from .v1_env_var import V1EnvVar
from .v1_lifecycle import V1Lifecycle
from .v1_probe import V1Probe
from .v1_resource_requirements import V1ResourceRequirements
from .v1_security_context import V1SecurityContext
from .v1_volume_device import V1VolumeDevice
from .v1_volume_mount import V1VolumeMount

class V1Container(BaseModel):
    """
    A single application container that you want to run within a pod.  # noqa: E501
    """
    args: Optional[list[StrictStr]] = Field(default=None, description="Arguments to the entrypoint. The container image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    command: Optional[list[StrictStr]] = Field(default=None, description="Entrypoint array. Not executed within a shell. The container image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell")
    env: Optional[list[V1EnvVar]] = Field(default=None, description="List of environment variables to set in the container. Cannot be updated.")
    env_from: Optional[list[V1EnvFromSource]] = Field(default=None, alias="envFrom", description="List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.")
    image: Optional[StrictStr] = Field(default=None, description="Container image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.")
    image_pull_policy: Optional[StrictStr] = Field(default=None, alias="imagePullPolicy", description="Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images")
    lifecycle: Optional[V1Lifecycle] = None
    liveness_probe: Optional[V1Probe] = Field(default=None, alias="livenessProbe")
    name: StrictStr = Field(..., description="Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.")
    ports: Optional[list[V1ContainerPort]] = Field(default=None, description="List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default \"0.0.0.0\" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See https://github.com/kubernetes/kubernetes/issues/108255. Cannot be updated.")
    readiness_probe: Optional[V1Probe] = Field(default=None, alias="readinessProbe")
    resize_policy: Optional[list[V1ContainerResizePolicy]] = Field(default=None, alias="resizePolicy", description="Resources resize policy for the container.")
    resources: Optional[V1ResourceRequirements] = None
    restart_policy: Optional[StrictStr] = Field(default=None, alias="restartPolicy", description="RestartPolicy defines the restart behavior of individual containers in a pod. This field may only be set for init containers, and the only allowed value is \"Always\". For non-init containers or when this field is not specified, the restart behavior is defined by the Pod's restart policy and the container type. Setting the RestartPolicy as \"Always\" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy \"Always\" will be shut down. This lifecycle differs from normal init containers and is often referred to as a \"sidecar\" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.")
    security_context: Optional[V1SecurityContext] = Field(default=None, alias="securityContext")
    startup_probe: Optional[V1Probe] = Field(default=None, alias="startupProbe")
    stdin: Optional[StrictBool] = Field(default=None, description="Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.")
    stdin_once: Optional[StrictBool] = Field(default=None, alias="stdinOnce", description="Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false")
    termination_message_path: Optional[StrictStr] = Field(default=None, alias="terminationMessagePath", description="Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.")
    termination_message_policy: Optional[StrictStr] = Field(default=None, alias="terminationMessagePolicy", description="Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.")
    tty: Optional[StrictBool] = Field(default=None, description="Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.")
    volume_devices: Optional[list[V1VolumeDevice]] = Field(default=None, alias="volumeDevices", description="volumeDevices is the list of block devices to be used by the container.")
    volume_mounts: Optional[list[V1VolumeMount]] = Field(default=None, alias="volumeMounts", description="Pod volumes to mount into the container's filesystem. Cannot be updated.")
    working_dir: Optional[StrictStr] = Field(default=None, alias="workingDir", description="Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.")
    __properties = ["args", "command", "env", "envFrom", "image", "imagePullPolicy", "lifecycle", "livenessProbe", "name", "ports", "readinessProbe", "resizePolicy", "resources", "restartPolicy", "securityContext", "startupProbe", "stdin", "stdinOnce", "terminationMessagePath", "terminationMessagePolicy", "tty", "volumeDevices", "volumeMounts", "workingDir"]

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
    def from_json(cls, json_str: str) -> V1Container:
        """Create an instance of V1Container from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in env (list)
        _items = []
        if self.env:
            for _item in self.env:
                if _item:
                    _items.append(_item.to_dict())
            _dict['env'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in env_from (list)
        _items = []
        if self.env_from:
            for _item in self.env_from:
                if _item:
                    _items.append(_item.to_dict())
            _dict['envFrom'] = _items
        # override the default output from pydantic by calling `to_dict()` of lifecycle
        if self.lifecycle:
            _dict['lifecycle'] = self.lifecycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of liveness_probe
        if self.liveness_probe:
            _dict['livenessProbe'] = self.liveness_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of readiness_probe
        if self.readiness_probe:
            _dict['readinessProbe'] = self.readiness_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resize_policy (list)
        _items = []
        if self.resize_policy:
            for _item in self.resize_policy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resizePolicy'] = _items
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict['resources'] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_context
        if self.security_context:
            _dict['securityContext'] = self.security_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of startup_probe
        if self.startup_probe:
            _dict['startupProbe'] = self.startup_probe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in volume_devices (list)
        _items = []
        if self.volume_devices:
            for _item in self.volume_devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumeDevices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in volume_mounts (list)
        _items = []
        if self.volume_mounts:
            for _item in self.volume_mounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumeMounts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> V1Container:
        """Create an instance of V1Container from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return V1Container.parse_obj(obj)

        _obj = V1Container.parse_obj({
            "args": obj.get("args"),
            "command": obj.get("command"),
            "env": [V1EnvVar.from_dict(_item) for _item in obj.get("env")] if obj.get("env") is not None else None,
            "env_from": [V1EnvFromSource.from_dict(_item) for _item in obj.get("envFrom")] if obj.get("envFrom") is not None else None,
            "image": obj.get("image"),
            "image_pull_policy": obj.get("imagePullPolicy"),
            "lifecycle": V1Lifecycle.from_dict(obj.get("lifecycle")) if obj.get("lifecycle") is not None else None,
            "liveness_probe": V1Probe.from_dict(obj.get("livenessProbe")) if obj.get("livenessProbe") is not None else None,
            "name": obj.get("name"),
            "ports": [V1ContainerPort.from_dict(_item) for _item in obj.get("ports")] if obj.get("ports") is not None else None,
            "readiness_probe": V1Probe.from_dict(obj.get("readinessProbe")) if obj.get("readinessProbe") is not None else None,
            "resize_policy": [V1ContainerResizePolicy.from_dict(_item) for _item in obj.get("resizePolicy")] if obj.get("resizePolicy") is not None else None,
            "resources": V1ResourceRequirements.from_dict(obj.get("resources")) if obj.get("resources") is not None else None,
            "restart_policy": obj.get("restartPolicy"),
            "security_context": V1SecurityContext.from_dict(obj.get("securityContext")) if obj.get("securityContext") is not None else None,
            "startup_probe": V1Probe.from_dict(obj.get("startupProbe")) if obj.get("startupProbe") is not None else None,
            "stdin": obj.get("stdin"),
            "stdin_once": obj.get("stdinOnce"),
            "termination_message_path": obj.get("terminationMessagePath"),
            "termination_message_policy": obj.get("terminationMessagePolicy"),
            "tty": obj.get("tty"),
            "volume_devices": [V1VolumeDevice.from_dict(_item) for _item in obj.get("volumeDevices")] if obj.get("volumeDevices") is not None else None,
            "volume_mounts": [V1VolumeMount.from_dict(_item) for _item in obj.get("volumeMounts")] if obj.get("volumeMounts") is not None else None,
            "working_dir": obj.get("workingDir")
        })
        return _obj

