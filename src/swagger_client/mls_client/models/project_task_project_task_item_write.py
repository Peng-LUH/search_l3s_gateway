# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProjectTaskProjectTaskItemWrite(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'task': 'str',
        'project': 'str',
        'position': 'int',
        'lock_after_step': 'list[str]',
        'lock_after': 'bool'
    }

    attribute_map = {
        'task': 'task',
        'project': 'project',
        'position': 'position',
        'lock_after_step': 'lockAfterStep',
        'lock_after': 'lockAfter'
    }

    def __init__(self, task=None, project=None, position=None, lock_after_step=None, lock_after=None):  # noqa: E501
        """ProjectTaskProjectTaskItemWrite - a model defined in Swagger"""  # noqa: E501
        self._task = None
        self._project = None
        self._position = None
        self._lock_after_step = None
        self._lock_after = None
        self.discriminator = None
        if task is not None:
            self.task = task
        if project is not None:
            self.project = project
        if position is not None:
            self.position = position
        if lock_after_step is not None:
            self.lock_after_step = lock_after_step
        if lock_after is not None:
            self.lock_after = lock_after

    @property
    def task(self):
        """Gets the task of this ProjectTaskProjectTaskItemWrite.  # noqa: E501


        :return: The task of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ProjectTaskProjectTaskItemWrite.


        :param task: The task of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def project(self):
        """Gets the project of this ProjectTaskProjectTaskItemWrite.  # noqa: E501


        :return: The project of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectTaskProjectTaskItemWrite.


        :param project: The project of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def position(self):
        """Gets the position of this ProjectTaskProjectTaskItemWrite.  # noqa: E501


        :return: The position of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ProjectTaskProjectTaskItemWrite.


        :param position: The position of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def lock_after_step(self):
        """Gets the lock_after_step of this ProjectTaskProjectTaskItemWrite.  # noqa: E501


        :return: The lock_after_step of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._lock_after_step

    @lock_after_step.setter
    def lock_after_step(self, lock_after_step):
        """Sets the lock_after_step of this ProjectTaskProjectTaskItemWrite.


        :param lock_after_step: The lock_after_step of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._lock_after_step = lock_after_step

    @property
    def lock_after(self):
        """Gets the lock_after of this ProjectTaskProjectTaskItemWrite.  # noqa: E501


        :return: The lock_after of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._lock_after

    @lock_after.setter
    def lock_after(self, lock_after):
        """Sets the lock_after of this ProjectTaskProjectTaskItemWrite.


        :param lock_after: The lock_after of this ProjectTaskProjectTaskItemWrite.  # noqa: E501
        :type: bool
        """

        self._lock_after = lock_after

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ProjectTaskProjectTaskItemWrite, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectTaskProjectTaskItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
