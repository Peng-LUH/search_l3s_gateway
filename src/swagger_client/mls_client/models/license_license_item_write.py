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

class LicenseLicenseItemWrite(object):
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
        'type': 'str',
        'count': 'int',
        'organization': 'str',
        'available': 'int',
        'setted': 'int',
        'note': 'str'
    }

    attribute_map = {
        'type': 'type',
        'count': 'count',
        'organization': 'organization',
        'available': 'available',
        'setted': 'setted',
        'note': 'note'
    }

    def __init__(self, type=None, count=None, organization=None, available=None, setted=None, note=None):  # noqa: E501
        """LicenseLicenseItemWrite - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._count = None
        self._organization = None
        self._available = None
        self._setted = None
        self._note = None
        self.discriminator = None
        self.type = type
        if count is not None:
            self.count = count
        self.organization = organization
        if available is not None:
            self.available = available
        if setted is not None:
            self.setted = setted
        if note is not None:
            self.note = note

    @property
    def type(self):
        """Gets the type of this LicenseLicenseItemWrite.  # noqa: E501


        :return: The type of this LicenseLicenseItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LicenseLicenseItemWrite.


        :param type: The type of this LicenseLicenseItemWrite.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def count(self):
        """Gets the count of this LicenseLicenseItemWrite.  # noqa: E501


        :return: The count of this LicenseLicenseItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this LicenseLicenseItemWrite.


        :param count: The count of this LicenseLicenseItemWrite.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def organization(self):
        """Gets the organization of this LicenseLicenseItemWrite.  # noqa: E501


        :return: The organization of this LicenseLicenseItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this LicenseLicenseItemWrite.


        :param organization: The organization of this LicenseLicenseItemWrite.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def available(self):
        """Gets the available of this LicenseLicenseItemWrite.  # noqa: E501


        :return: The available of this LicenseLicenseItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this LicenseLicenseItemWrite.


        :param available: The available of this LicenseLicenseItemWrite.  # noqa: E501
        :type: int
        """

        self._available = available

    @property
    def setted(self):
        """Gets the setted of this LicenseLicenseItemWrite.  # noqa: E501


        :return: The setted of this LicenseLicenseItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._setted

    @setted.setter
    def setted(self, setted):
        """Sets the setted of this LicenseLicenseItemWrite.


        :param setted: The setted of this LicenseLicenseItemWrite.  # noqa: E501
        :type: int
        """

        self._setted = setted

    @property
    def note(self):
        """Gets the note of this LicenseLicenseItemWrite.  # noqa: E501


        :return: The note of this LicenseLicenseItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this LicenseLicenseItemWrite.


        :param note: The note of this LicenseLicenseItemWrite.  # noqa: E501
        :type: str
        """

        self._note = note

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
        if issubclass(LicenseLicenseItemWrite, dict):
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
        if not isinstance(other, LicenseLicenseItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
