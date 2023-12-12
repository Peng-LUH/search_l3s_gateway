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

class ProjectTodoJsonldProjectTodoRead(object):
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
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'project': 'str',
        'assigner': 'str',
        'user': 'str',
        'scored_points': 'float',
        'max_points': 'float',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'note': 'str',
        'instructors_to_notify': 'list[str]',
        'task_todos': 'list[str]'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'project': 'project',
        'assigner': 'assigner',
        'user': 'user',
        'scored_points': 'scoredPoints',
        'max_points': 'maxPoints',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'note': 'note',
        'instructors_to_notify': 'instructorsToNotify',
        'task_todos': 'taskTodos'
    }

    def __init__(self, id=None, type=None, created_at=None, updated_at=None, id=None, project=None, assigner=None, user=None, scored_points=None, max_points=None, start_time=None, end_time=None, note=None, instructors_to_notify=None, task_todos=None):  # noqa: E501
        """ProjectTodoJsonldProjectTodoRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._project = None
        self._assigner = None
        self._user = None
        self._scored_points = None
        self._max_points = None
        self._start_time = None
        self._end_time = None
        self._note = None
        self._instructors_to_notify = None
        self._task_todos = None
        self.discriminator = None
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
        self.project = project
        if assigner is not None:
            self.assigner = assigner
        self.user = user
        if scored_points is not None:
            self.scored_points = scored_points
        if max_points is not None:
            self.max_points = max_points
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if note is not None:
            self.note = note
        if instructors_to_notify is not None:
            self.instructors_to_notify = instructors_to_notify
        if task_todos is not None:
            self.task_todos = task_todos

    @property
    def id(self):
        """Gets the id of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The id of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectTodoJsonldProjectTodoRead.


        :param id: The id of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The type of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectTodoJsonldProjectTodoRead.


        :param type: The type of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The created_at of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProjectTodoJsonldProjectTodoRead.


        :param created_at: The created_at of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The updated_at of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProjectTodoJsonldProjectTodoRead.


        :param updated_at: The updated_at of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The id of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectTodoJsonldProjectTodoRead.


        :param id: The id of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The project of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectTodoJsonldProjectTodoRead.


        :param project: The project of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def assigner(self):
        """Gets the assigner of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The assigner of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: str
        """
        return self._assigner

    @assigner.setter
    def assigner(self, assigner):
        """Sets the assigner of this ProjectTodoJsonldProjectTodoRead.


        :param assigner: The assigner of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: str
        """

        self._assigner = assigner

    @property
    def user(self):
        """Gets the user of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The user of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ProjectTodoJsonldProjectTodoRead.


        :param user: The user of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def scored_points(self):
        """Gets the scored_points of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The scored_points of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: float
        """
        return self._scored_points

    @scored_points.setter
    def scored_points(self, scored_points):
        """Sets the scored_points of this ProjectTodoJsonldProjectTodoRead.


        :param scored_points: The scored_points of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: float
        """

        self._scored_points = scored_points

    @property
    def max_points(self):
        """Gets the max_points of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The max_points of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: float
        """
        return self._max_points

    @max_points.setter
    def max_points(self, max_points):
        """Sets the max_points of this ProjectTodoJsonldProjectTodoRead.


        :param max_points: The max_points of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: float
        """

        self._max_points = max_points

    @property
    def start_time(self):
        """Gets the start_time of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The start_time of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ProjectTodoJsonldProjectTodoRead.


        :param start_time: The start_time of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The end_time of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ProjectTodoJsonldProjectTodoRead.


        :param end_time: The end_time of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def note(self):
        """Gets the note of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The note of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ProjectTodoJsonldProjectTodoRead.


        :param note: The note of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def instructors_to_notify(self):
        """Gets the instructors_to_notify of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The instructors_to_notify of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._instructors_to_notify

    @instructors_to_notify.setter
    def instructors_to_notify(self, instructors_to_notify):
        """Sets the instructors_to_notify of this ProjectTodoJsonldProjectTodoRead.


        :param instructors_to_notify: The instructors_to_notify of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: list[str]
        """

        self._instructors_to_notify = instructors_to_notify

    @property
    def task_todos(self):
        """Gets the task_todos of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501


        :return: The task_todos of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_todos

    @task_todos.setter
    def task_todos(self, task_todos):
        """Sets the task_todos of this ProjectTodoJsonldProjectTodoRead.


        :param task_todos: The task_todos of this ProjectTodoJsonldProjectTodoRead.  # noqa: E501
        :type: list[str]
        """

        self._task_todos = task_todos

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
        if issubclass(ProjectTodoJsonldProjectTodoRead, dict):
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
        if not isinstance(other, ProjectTodoJsonldProjectTodoRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other