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

class GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead(object):
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
        'context': 'OneOfGroupTaskTodoLinkJsonldGroupTaskTodoLinkItemReadContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'user': 'str',
        'steps_processed': 'int',
        'group_task_todo': 'str',
        'lock_after_step': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'user': 'user',
        'steps_processed': 'stepsProcessed',
        'group_task_todo': 'groupTaskTodo',
        'lock_after_step': 'lockAfterStep'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, user=None, steps_processed=None, group_task_todo=None, lock_after_step=None):  # noqa: E501
        """GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._user = None
        self._steps_processed = None
        self._group_task_todo = None
        self._lock_after_step = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if user is not None:
            self.user = user
        if steps_processed is not None:
            self.steps_processed = steps_processed
        if group_task_todo is not None:
            self.group_task_todo = group_task_todo
        if lock_after_step is not None:
            self.lock_after_step = lock_after_step

    @property
    def context(self):
        """Gets the context of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The context of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: OneOfGroupTaskTodoLinkJsonldGroupTaskTodoLinkItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param context: The context of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: OneOfGroupTaskTodoLinkJsonldGroupTaskTodoLinkItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param id: The id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The type of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param type: The type of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The created_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param created_at: The created_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The updated_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param updated_at: The updated_at of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param id: The id of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user(self):
        """Gets the user of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The user of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param user: The user of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def steps_processed(self):
        """Gets the steps_processed of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The steps_processed of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: int
        """
        return self._steps_processed

    @steps_processed.setter
    def steps_processed(self, steps_processed):
        """Sets the steps_processed of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param steps_processed: The steps_processed of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: int
        """

        self._steps_processed = steps_processed

    @property
    def group_task_todo(self):
        """Gets the group_task_todo of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The group_task_todo of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: str
        """
        return self._group_task_todo

    @group_task_todo.setter
    def group_task_todo(self, group_task_todo):
        """Sets the group_task_todo of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param group_task_todo: The group_task_todo of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :type: str
        """

        self._group_task_todo = group_task_todo

    @property
    def lock_after_step(self):
        """Gets the lock_after_step of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501


        :return: The lock_after_step of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._lock_after_step

    @lock_after_step.setter
    def lock_after_step(self, lock_after_step):
        """Sets the lock_after_step of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.


        :param lock_after_step: The lock_after_step of this GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead.  # noqa: E501
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
        if issubclass(GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead, dict):
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
        if not isinstance(other, GroupTaskTodoLinkJsonldGroupTaskTodoLinkItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
