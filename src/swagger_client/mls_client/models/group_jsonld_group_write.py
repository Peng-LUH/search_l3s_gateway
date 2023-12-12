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

class GroupJsonldGroupWrite(object):
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
        'context': 'OneOfGroupJsonldGroupWriteContext',
        'id': 'str',
        'type': 'str',
        'title': 'str',
        'organization': 'str',
        'users': 'list[str]',
        'mls1_id': 'int'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'title': 'title',
        'organization': 'organization',
        'users': 'users',
        'mls1_id': 'mls1Id'
    }

    def __init__(self, context=None, id=None, type=None, title=None, organization=None, users=None, mls1_id=None):  # noqa: E501
        """GroupJsonldGroupWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._title = None
        self._organization = None
        self._users = None
        self._mls1_id = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self.title = title
        self.organization = organization
        if users is not None:
            self.users = users
        if mls1_id is not None:
            self.mls1_id = mls1_id

    @property
    def context(self):
        """Gets the context of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The context of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: OneOfGroupJsonldGroupWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this GroupJsonldGroupWrite.


        :param context: The context of this GroupJsonldGroupWrite.  # noqa: E501
        :type: OneOfGroupJsonldGroupWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The id of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupJsonldGroupWrite.


        :param id: The id of this GroupJsonldGroupWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The type of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupJsonldGroupWrite.


        :param type: The type of this GroupJsonldGroupWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The title of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupJsonldGroupWrite.


        :param title: The title of this GroupJsonldGroupWrite.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def organization(self):
        """Gets the organization of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The organization of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this GroupJsonldGroupWrite.


        :param organization: The organization of this GroupJsonldGroupWrite.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def users(self):
        """Gets the users of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The users of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this GroupJsonldGroupWrite.


        :param users: The users of this GroupJsonldGroupWrite.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def mls1_id(self):
        """Gets the mls1_id of this GroupJsonldGroupWrite.  # noqa: E501


        :return: The mls1_id of this GroupJsonldGroupWrite.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this GroupJsonldGroupWrite.


        :param mls1_id: The mls1_id of this GroupJsonldGroupWrite.  # noqa: E501
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
        if issubclass(GroupJsonldGroupWrite, dict):
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
        if not isinstance(other, GroupJsonldGroupWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other