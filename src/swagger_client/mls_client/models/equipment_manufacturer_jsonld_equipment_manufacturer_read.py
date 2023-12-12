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

class EquipmentManufacturerJsonldEquipmentManufacturerRead(object):
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
        'id': 'int',
        'name': 'str',
        'organization': 'str'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'name': 'name',
        'organization': 'organization'
    }

    def __init__(self, id=None, type=None, id=None, name=None, organization=None):  # noqa: E501
        """EquipmentManufacturerJsonldEquipmentManufacturerRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._id = None
        self._name = None
        self._organization = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization

    @property
    def id(self):
        """Gets the id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501


        :return: The id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.


        :param id: The id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501


        :return: The type of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EquipmentManufacturerJsonldEquipmentManufacturerRead.


        :param type: The type of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501


        :return: The id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.


        :param id: The id of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501


        :return: The name of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EquipmentManufacturerJsonldEquipmentManufacturerRead.


        :param name: The name of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501


        :return: The organization of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this EquipmentManufacturerJsonldEquipmentManufacturerRead.


        :param organization: The organization of this EquipmentManufacturerJsonldEquipmentManufacturerRead.  # noqa: E501
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
        if issubclass(EquipmentManufacturerJsonldEquipmentManufacturerRead, dict):
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
        if not isinstance(other, EquipmentManufacturerJsonldEquipmentManufacturerRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other