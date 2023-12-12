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

class TaskStepCategoryTaskStepCategoryRead(object):
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
        'id': 'int',
        'title': 'str',
        'color': 'str',
        'organization': 'str',
        'icon': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'color': 'color',
        'organization': 'organization',
        'icon': 'icon'
    }

    def __init__(self, id=None, title=None, color=None, organization=None, icon=None):  # noqa: E501
        """TaskStepCategoryTaskStepCategoryRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._color = None
        self._organization = None
        self._icon = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.title = title
        if color is not None:
            self.color = color
        if organization is not None:
            self.organization = organization
        if icon is not None:
            self.icon = icon

    @property
    def id(self):
        """Gets the id of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501


        :return: The id of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskStepCategoryTaskStepCategoryRead.


        :param id: The id of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501


        :return: The title of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskStepCategoryTaskStepCategoryRead.


        :param title: The title of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def color(self):
        """Gets the color of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501


        :return: The color of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TaskStepCategoryTaskStepCategoryRead.


        :param color: The color of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def organization(self):
        """Gets the organization of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501


        :return: The organization of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this TaskStepCategoryTaskStepCategoryRead.


        :param organization: The organization of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def icon(self):
        """Gets the icon of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501


        :return: The icon of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this TaskStepCategoryTaskStepCategoryRead.


        :param icon: The icon of this TaskStepCategoryTaskStepCategoryRead.  # noqa: E501
        :type: str
        """

        self._icon = icon

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
        if issubclass(TaskStepCategoryTaskStepCategoryRead, dict):
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
        if not isinstance(other, TaskStepCategoryTaskStepCategoryRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other