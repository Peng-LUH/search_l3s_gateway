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

class TraineeNoticeTraineeNoticeRead(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'title': 'str',
        'content': 'str',
        'user': 'str',
        'task_step': 'AnyOfTraineeNoticeTraineeNoticeReadTaskStep',
        'task_todo': 'str',
        'files': 'list[TraineeNoticeFileTraineeNoticeRead]',
        'mls1_id': 'int'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'title': 'title',
        'content': 'content',
        'user': 'user',
        'task_step': 'taskStep',
        'task_todo': 'taskTodo',
        'files': 'files',
        'mls1_id': 'mls1Id'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, title=None, content=None, user=None, task_step=None, task_todo=None, files=None, mls1_id=None):  # noqa: E501
        """TraineeNoticeTraineeNoticeRead - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._title = None
        self._content = None
        self._user = None
        self._task_step = None
        self._task_todo = None
        self._files = None
        self._mls1_id = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if user is not None:
            self.user = user
        if task_step is not None:
            self.task_step = task_step
        if task_todo is not None:
            self.task_todo = task_todo
        if files is not None:
            self.files = files
        if mls1_id is not None:
            self.mls1_id = mls1_id

    @property
    def created_at(self):
        """Gets the created_at of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The created_at of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TraineeNoticeTraineeNoticeRead.


        :param created_at: The created_at of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The updated_at of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TraineeNoticeTraineeNoticeRead.


        :param updated_at: The updated_at of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The id of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TraineeNoticeTraineeNoticeRead.


        :param id: The id of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The title of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TraineeNoticeTraineeNoticeRead.


        :param title: The title of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The content of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TraineeNoticeTraineeNoticeRead.


        :param content: The content of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def user(self):
        """Gets the user of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The user of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TraineeNoticeTraineeNoticeRead.


        :param user: The user of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def task_step(self):
        """Gets the task_step of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The task_step of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: AnyOfTraineeNoticeTraineeNoticeReadTaskStep
        """
        return self._task_step

    @task_step.setter
    def task_step(self, task_step):
        """Sets the task_step of this TraineeNoticeTraineeNoticeRead.


        :param task_step: The task_step of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: AnyOfTraineeNoticeTraineeNoticeReadTaskStep
        """

        self._task_step = task_step

    @property
    def task_todo(self):
        """Gets the task_todo of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The task_todo of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: str
        """
        return self._task_todo

    @task_todo.setter
    def task_todo(self, task_todo):
        """Sets the task_todo of this TraineeNoticeTraineeNoticeRead.


        :param task_todo: The task_todo of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: str
        """

        self._task_todo = task_todo

    @property
    def files(self):
        """Gets the files of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The files of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: list[TraineeNoticeFileTraineeNoticeRead]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this TraineeNoticeTraineeNoticeRead.


        :param files: The files of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: list[TraineeNoticeFileTraineeNoticeRead]
        """

        self._files = files

    @property
    def mls1_id(self):
        """Gets the mls1_id of this TraineeNoticeTraineeNoticeRead.  # noqa: E501


        :return: The mls1_id of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this TraineeNoticeTraineeNoticeRead.


        :param mls1_id: The mls1_id of this TraineeNoticeTraineeNoticeRead.  # noqa: E501
        :type: int
        """

        self._mls1_id = mls1_id

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
        if issubclass(TraineeNoticeTraineeNoticeRead, dict):
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
        if not isinstance(other, TraineeNoticeTraineeNoticeRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
