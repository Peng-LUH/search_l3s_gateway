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

class GroupTaskTodoLinkGroupTaskTodoLinkItemWrite(object):
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
        'steps_processed': 'int',
        'group_task_todo': 'str',
        'lock_after_step': 'list[str]'
    }

    attribute_map = {
        'steps_processed': 'stepsProcessed',
        'group_task_todo': 'groupTaskTodo',
        'lock_after_step': 'lockAfterStep'
    }

    def __init__(self, steps_processed=None, group_task_todo=None, lock_after_step=None):  # noqa: E501
        """GroupTaskTodoLinkGroupTaskTodoLinkItemWrite - a model defined in Swagger"""  # noqa: E501
        self._steps_processed = None
        self._group_task_todo = None
        self._lock_after_step = None
        self.discriminator = None
        if steps_processed is not None:
            self.steps_processed = steps_processed
        if group_task_todo is not None:
            self.group_task_todo = group_task_todo
        if lock_after_step is not None:
            self.lock_after_step = lock_after_step

    @property
    def steps_processed(self):
        """Gets the steps_processed of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501


        :return: The steps_processed of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._steps_processed

    @steps_processed.setter
    def steps_processed(self, steps_processed):
        """Sets the steps_processed of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.


        :param steps_processed: The steps_processed of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501
        :type: int
        """

        self._steps_processed = steps_processed

    @property
    def group_task_todo(self):
        """Gets the group_task_todo of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501


        :return: The group_task_todo of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._group_task_todo

    @group_task_todo.setter
    def group_task_todo(self, group_task_todo):
        """Sets the group_task_todo of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.


        :param group_task_todo: The group_task_todo of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501
        :type: str
        """

        self._group_task_todo = group_task_todo

    @property
    def lock_after_step(self):
        """Gets the lock_after_step of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501


        :return: The lock_after_step of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._lock_after_step

    @lock_after_step.setter
    def lock_after_step(self, lock_after_step):
        """Sets the lock_after_step of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.


        :param lock_after_step: The lock_after_step of this GroupTaskTodoLinkGroupTaskTodoLinkItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._lock_after_step = lock_after_step

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
        if issubclass(GroupTaskTodoLinkGroupTaskTodoLinkItemWrite, dict):
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
        if not isinstance(other, GroupTaskTodoLinkGroupTaskTodoLinkItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
