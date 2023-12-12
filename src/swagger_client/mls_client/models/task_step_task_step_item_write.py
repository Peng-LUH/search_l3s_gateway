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

class TaskStepTaskStepItemWrite(object):
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
        'title': 'str',
        'content': 'list[str]',
        'helping_topics': 'list[str]',
        'task_step_category': 'str',
        'parent': 'AnyOfTaskStepTaskStepItemWriteParent',
        'position': 'int',
        'stop': 'bool',
        'files': 'list[str]',
        'mls1_id': 'int'
    }

    attribute_map = {
        'title': 'title',
        'content': 'content',
        'helping_topics': 'helpingTopics',
        'task_step_category': 'taskStepCategory',
        'parent': 'parent',
        'position': 'position',
        'stop': 'stop',
        'files': 'files',
        'mls1_id': 'mls1Id'
    }

    def __init__(self, title=None, content=None, helping_topics=None, task_step_category=None, parent=None, position=None, stop=None, files=None, mls1_id=None):  # noqa: E501
        """TaskStepTaskStepItemWrite - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._content = None
        self._helping_topics = None
        self._task_step_category = None
        self._parent = None
        self._position = None
        self._stop = None
        self._files = None
        self._mls1_id = None
        self.discriminator = None
        self.title = title
        if content is not None:
            self.content = content
        if helping_topics is not None:
            self.helping_topics = helping_topics
        if task_step_category is not None:
            self.task_step_category = task_step_category
        if parent is not None:
            self.parent = parent
        if position is not None:
            self.position = position
        if stop is not None:
            self.stop = stop
        if files is not None:
            self.files = files
        if mls1_id is not None:
            self.mls1_id = mls1_id

    @property
    def title(self):
        """Gets the title of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The title of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskStepTaskStepItemWrite.


        :param title: The title of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The content of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TaskStepTaskStepItemWrite.


        :param content: The content of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._content = content

    @property
    def helping_topics(self):
        """Gets the helping_topics of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The helping_topics of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._helping_topics

    @helping_topics.setter
    def helping_topics(self, helping_topics):
        """Sets the helping_topics of this TaskStepTaskStepItemWrite.


        :param helping_topics: The helping_topics of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._helping_topics = helping_topics

    @property
    def task_step_category(self):
        """Gets the task_step_category of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The task_step_category of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._task_step_category

    @task_step_category.setter
    def task_step_category(self, task_step_category):
        """Sets the task_step_category of this TaskStepTaskStepItemWrite.


        :param task_step_category: The task_step_category of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: str
        """

        self._task_step_category = task_step_category

    @property
    def parent(self):
        """Gets the parent of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The parent of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: AnyOfTaskStepTaskStepItemWriteParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this TaskStepTaskStepItemWrite.


        :param parent: The parent of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: AnyOfTaskStepTaskStepItemWriteParent
        """

        self._parent = parent

    @property
    def position(self):
        """Gets the position of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The position of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TaskStepTaskStepItemWrite.


        :param position: The position of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def stop(self):
        """Gets the stop of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The stop of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this TaskStepTaskStepItemWrite.


        :param stop: The stop of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: bool
        """

        self._stop = stop

    @property
    def files(self):
        """Gets the files of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The files of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this TaskStepTaskStepItemWrite.


        :param files: The files of this TaskStepTaskStepItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def mls1_id(self):
        """Gets the mls1_id of this TaskStepTaskStepItemWrite.  # noqa: E501


        :return: The mls1_id of this TaskStepTaskStepItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this TaskStepTaskStepItemWrite.


        :param mls1_id: The mls1_id of this TaskStepTaskStepItemWrite.  # noqa: E501
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
        if issubclass(TaskStepTaskStepItemWrite, dict):
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
        if not isinstance(other, TaskStepTaskStepItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other