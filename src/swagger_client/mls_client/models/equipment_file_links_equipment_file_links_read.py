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

class EquipmentFileLinksEquipmentFileLinksRead(object):
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
        'id': 'int',
        'equipment': 'str',
        'link_name': 'str',
        'link_destination': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'equipment': 'equipment',
        'link_name': 'linkName',
        'link_destination': 'linkDestination'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, equipment=None, link_name=None, link_destination=None):  # noqa: E501
        """EquipmentFileLinksEquipmentFileLinksRead - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._equipment = None
        self._link_name = None
        self._link_destination = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if equipment is not None:
            self.equipment = equipment
        if link_name is not None:
            self.link_name = link_name
        if link_destination is not None:
            self.link_destination = link_destination

    @property
    def created_at(self):
        """Gets the created_at of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501


        :return: The created_at of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EquipmentFileLinksEquipmentFileLinksRead.


        :param created_at: The created_at of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501


        :return: The updated_at of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EquipmentFileLinksEquipmentFileLinksRead.


        :param updated_at: The updated_at of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501


        :return: The id of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentFileLinksEquipmentFileLinksRead.


        :param id: The id of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def equipment(self):
        """Gets the equipment of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501


        :return: The equipment of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :rtype: str
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this EquipmentFileLinksEquipmentFileLinksRead.


        :param equipment: The equipment of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :type: str
        """

        self._equipment = equipment

    @property
    def link_name(self):
        """Gets the link_name of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501


        :return: The link_name of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :rtype: str
        """
        return self._link_name

    @link_name.setter
    def link_name(self, link_name):
        """Sets the link_name of this EquipmentFileLinksEquipmentFileLinksRead.


        :param link_name: The link_name of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :type: str
        """

        self._link_name = link_name

    @property
    def link_destination(self):
        """Gets the link_destination of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501


        :return: The link_destination of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :rtype: str
        """
        return self._link_destination

    @link_destination.setter
    def link_destination(self, link_destination):
        """Sets the link_destination of this EquipmentFileLinksEquipmentFileLinksRead.


        :param link_destination: The link_destination of this EquipmentFileLinksEquipmentFileLinksRead.  # noqa: E501
        :type: str
        """

        self._link_destination = link_destination

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
        if issubclass(EquipmentFileLinksEquipmentFileLinksRead, dict):
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
        if not isinstance(other, EquipmentFileLinksEquipmentFileLinksRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
