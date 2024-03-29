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

class DocumentsDocumentItemColumnWrite(object):
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
        'shared_for_groups': 'list[str]',
        'shared_users': 'list[str]'
    }

    attribute_map = {
        'shared_for_groups': 'sharedForGroups',
        'shared_users': 'sharedUsers'
    }

    def __init__(self, shared_for_groups=None, shared_users=None):  # noqa: E501
        """DocumentsDocumentItemColumnWrite - a model defined in Swagger"""  # noqa: E501
        self._shared_for_groups = None
        self._shared_users = None
        self.discriminator = None
        if shared_for_groups is not None:
            self.shared_for_groups = shared_for_groups
        if shared_users is not None:
            self.shared_users = shared_users

    @property
    def shared_for_groups(self):
        """Gets the shared_for_groups of this DocumentsDocumentItemColumnWrite.  # noqa: E501


        :return: The shared_for_groups of this DocumentsDocumentItemColumnWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_for_groups

    @shared_for_groups.setter
    def shared_for_groups(self, shared_for_groups):
        """Sets the shared_for_groups of this DocumentsDocumentItemColumnWrite.


        :param shared_for_groups: The shared_for_groups of this DocumentsDocumentItemColumnWrite.  # noqa: E501
        :type: list[str]
        """

        self._shared_for_groups = shared_for_groups

    @property
    def shared_users(self):
        """Gets the shared_users of this DocumentsDocumentItemColumnWrite.  # noqa: E501


        :return: The shared_users of this DocumentsDocumentItemColumnWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_users

    @shared_users.setter
    def shared_users(self, shared_users):
        """Sets the shared_users of this DocumentsDocumentItemColumnWrite.


        :param shared_users: The shared_users of this DocumentsDocumentItemColumnWrite.  # noqa: E501
        :type: list[str]
        """

        self._shared_users = shared_users

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
        if issubclass(DocumentsDocumentItemColumnWrite, dict):
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
        if not isinstance(other, DocumentsDocumentItemColumnWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
