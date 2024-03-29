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

class EquipmentLocationEquipmentLocationWrite(object):
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
        'location': 'str',
        'area': 'str',
        'comment': 'str',
        'equipment': 'list[str]',
        'organization': 'str'
    }

    attribute_map = {
        'location': 'location',
        'area': 'area',
        'comment': 'comment',
        'equipment': 'equipment',
        'organization': 'organization'
    }

    def __init__(self, location=None, area=None, comment=None, equipment=None, organization=None):  # noqa: E501
        """EquipmentLocationEquipmentLocationWrite - a model defined in Swagger"""  # noqa: E501
        self._location = None
        self._area = None
        self._comment = None
        self._equipment = None
        self._organization = None
        self.discriminator = None
        if location is not None:
            self.location = location
        if area is not None:
            self.area = area
        if comment is not None:
            self.comment = comment
        if equipment is not None:
            self.equipment = equipment
        if organization is not None:
            self.organization = organization

    @property
    def location(self):
        """Gets the location of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501


        :return: The location of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EquipmentLocationEquipmentLocationWrite.


        :param location: The location of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def area(self):
        """Gets the area of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501


        :return: The area of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this EquipmentLocationEquipmentLocationWrite.


        :param area: The area of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def comment(self):
        """Gets the comment of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501


        :return: The comment of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this EquipmentLocationEquipmentLocationWrite.


        :param comment: The comment of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def equipment(self):
        """Gets the equipment of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501


        :return: The equipment of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this EquipmentLocationEquipmentLocationWrite.


        :param equipment: The equipment of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :type: list[str]
        """

        self._equipment = equipment

    @property
    def organization(self):
        """Gets the organization of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501


        :return: The organization of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this EquipmentLocationEquipmentLocationWrite.


        :param organization: The organization of this EquipmentLocationEquipmentLocationWrite.  # noqa: E501
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
        if issubclass(EquipmentLocationEquipmentLocationWrite, dict):
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
        if not isinstance(other, EquipmentLocationEquipmentLocationWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
