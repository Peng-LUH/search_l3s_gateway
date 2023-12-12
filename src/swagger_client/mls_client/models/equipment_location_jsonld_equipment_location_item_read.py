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

class EquipmentLocationJsonldEquipmentLocationItemRead(object):
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
        'context': 'OneOfEquipmentLocationJsonldEquipmentLocationItemReadContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'location': 'str',
        'area': 'str',
        'comment': 'str',
        'equipment': 'list[str]',
        'organization': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'location': 'location',
        'area': 'area',
        'comment': 'comment',
        'equipment': 'equipment',
        'organization': 'organization'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, location=None, area=None, comment=None, equipment=None, organization=None):  # noqa: E501
        """EquipmentLocationJsonldEquipmentLocationItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._location = None
        self._area = None
        self._comment = None
        self._equipment = None
        self._organization = None
        self.discriminator = None
        if context is not None:
            self.context = context
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
    def context(self):
        """Gets the context of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The context of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: OneOfEquipmentLocationJsonldEquipmentLocationItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param context: The context of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: OneOfEquipmentLocationJsonldEquipmentLocationItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The id of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param id: The id of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The type of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param type: The type of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The created_at of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param created_at: The created_at of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The updated_at of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param updated_at: The updated_at of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The id of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param id: The id of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The location of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param location: The location of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def area(self):
        """Gets the area of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The area of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param area: The area of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def comment(self):
        """Gets the comment of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The comment of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param comment: The comment of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def equipment(self):
        """Gets the equipment of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The equipment of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param equipment: The equipment of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :type: list[str]
        """

        self._equipment = equipment

    @property
    def organization(self):
        """Gets the organization of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501


        :return: The organization of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this EquipmentLocationJsonldEquipmentLocationItemRead.


        :param organization: The organization of this EquipmentLocationJsonldEquipmentLocationItemRead.  # noqa: E501
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
        if issubclass(EquipmentLocationJsonldEquipmentLocationItemRead, dict):
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
        if not isinstance(other, EquipmentLocationJsonldEquipmentLocationItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other