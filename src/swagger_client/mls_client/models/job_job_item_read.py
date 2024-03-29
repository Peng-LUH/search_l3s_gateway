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

class JobJobItemRead(object):
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
        'title': 'str',
        'users': 'list[str]',
        'organization': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'title': 'title',
        'users': 'users',
        'organization': 'organization'
    }

    def __init__(self, created_at=None, updated_at=None, title=None, users=None, organization=None):  # noqa: E501
        """JobJobItemRead - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._title = None
        self._users = None
        self._organization = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if title is not None:
            self.title = title
        if users is not None:
            self.users = users
        if organization is not None:
            self.organization = organization

    @property
    def created_at(self):
        """Gets the created_at of this JobJobItemRead.  # noqa: E501


        :return: The created_at of this JobJobItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this JobJobItemRead.


        :param created_at: The created_at of this JobJobItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this JobJobItemRead.  # noqa: E501


        :return: The updated_at of this JobJobItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this JobJobItemRead.


        :param updated_at: The updated_at of this JobJobItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def title(self):
        """Gets the title of this JobJobItemRead.  # noqa: E501


        :return: The title of this JobJobItemRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this JobJobItemRead.


        :param title: The title of this JobJobItemRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def users(self):
        """Gets the users of this JobJobItemRead.  # noqa: E501


        :return: The users of this JobJobItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this JobJobItemRead.


        :param users: The users of this JobJobItemRead.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def organization(self):
        """Gets the organization of this JobJobItemRead.  # noqa: E501


        :return: The organization of this JobJobItemRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this JobJobItemRead.


        :param organization: The organization of this JobJobItemRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

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
        if issubclass(JobJobItemRead, dict):
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
        if not isinstance(other, JobJobItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
