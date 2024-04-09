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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .v1_job_template_spec import V1JobTemplateSpec
from typing import Optional, Set
from typing_extensions import Self

class V1CronJobSpec(BaseModel):
    """
    CronJobSpec describes how the job execution will look like and when it will actually run.
    """ # noqa: E501
    concurrency_policy: Optional[StrictStr] = Field(default=None, description="Specifies how to treat concurrent executions of a Job. Valid values are:  - \"Allow\" (default): allows CronJobs to run concurrently; - \"Forbid\": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - \"Replace\": cancels currently running job and replaces it with a new one", alias="concurrencyPolicy")
    failed_jobs_history_limit: Optional[StrictInt] = Field(default=None, description="The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1.", alias="failedJobsHistoryLimit")
    job_template: V1JobTemplateSpec = Field(alias="jobTemplate")
    schedule: StrictStr = Field(description="The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron.")
    starting_deadline_seconds: Optional[StrictInt] = Field(default=None, description="Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.", alias="startingDeadlineSeconds")
    successful_jobs_history_limit: Optional[StrictInt] = Field(default=None, description="The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3.", alias="successfulJobsHistoryLimit")
    suspend: Optional[StrictBool] = Field(default=None, description="This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones", alias="timeZone")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["concurrencyPolicy", "failedJobsHistoryLimit", "jobTemplate", "schedule", "startingDeadlineSeconds", "successfulJobsHistoryLimit", "suspend", "timeZone"]

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
        """Create an instance of V1CronJobSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of job_template
        if self.job_template:
            _dict['jobTemplate'] = self.job_template.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V1CronJobSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "concurrencyPolicy": obj.get("concurrencyPolicy"),
            "failedJobsHistoryLimit": obj.get("failedJobsHistoryLimit"),
            "jobTemplate": V1JobTemplateSpec.from_dict(obj["jobTemplate"]) if obj.get("jobTemplate") is not None else None,
            "schedule": obj.get("schedule"),
            "startingDeadlineSeconds": obj.get("startingDeadlineSeconds"),
            "successfulJobsHistoryLimit": obj.get("successfulJobsHistoryLimit"),
            "suspend": obj.get("suspend"),
            "timeZone": obj.get("timeZone")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


