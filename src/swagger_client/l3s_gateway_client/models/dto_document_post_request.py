# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoDocumentPostRequest(object):
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
        'owner': 'list[str]',
        'contents': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'contents': 'contents',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, owner=None, contents=None, created_at=None, updated_at=None):  # noqa: E501
        """DtoDocumentPostRequest - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._contents = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        if owner is not None:
            self.owner = owner
        if contents is not None:
            self.contents = contents
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def owner(self):
        """Gets the owner of this DtoDocumentPostRequest.  # noqa: E501


        :return: The owner of this DtoDocumentPostRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DtoDocumentPostRequest.


        :param owner: The owner of this DtoDocumentPostRequest.  # noqa: E501
        :type: list[str]
        """

        self._owner = owner

    @property
    def contents(self):
        """Gets the contents of this DtoDocumentPostRequest.  # noqa: E501


        :return: The contents of this DtoDocumentPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this DtoDocumentPostRequest.


        :param contents: The contents of this DtoDocumentPostRequest.  # noqa: E501
        :type: str
        """

        self._contents = contents

    @property
    def created_at(self):
        """Gets the created_at of this DtoDocumentPostRequest.  # noqa: E501


        :return: The created_at of this DtoDocumentPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DtoDocumentPostRequest.


        :param created_at: The created_at of this DtoDocumentPostRequest.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DtoDocumentPostRequest.  # noqa: E501


        :return: The updated_at of this DtoDocumentPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DtoDocumentPostRequest.


        :param updated_at: The updated_at of this DtoDocumentPostRequest.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(DtoDocumentPostRequest, dict):
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
        if not isinstance(other, DtoDocumentPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
