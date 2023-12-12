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

class EquipmentFileLinksJsonldEquipmentFileLinksWrite(object):
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
        'context': 'OneOfEquipmentFileLinksJsonldEquipmentFileLinksWriteContext',
        'id': 'str',
        'type': 'str',
        'equipment': 'str',
        'link_name': 'str',
        'link_destination': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'equipment': 'equipment',
        'link_name': 'linkName',
        'link_destination': 'linkDestination'
    }

    def __init__(self, context=None, id=None, type=None, equipment=None, link_name=None, link_destination=None):  # noqa: E501
        """EquipmentFileLinksJsonldEquipmentFileLinksWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._equipment = None
        self._link_name = None
        self._link_destination = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if equipment is not None:
            self.equipment = equipment
        if link_name is not None:
            self.link_name = link_name
        if link_destination is not None:
            self.link_destination = link_destination

    @property
    def context(self):
        """Gets the context of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501


        :return: The context of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :rtype: OneOfEquipmentFileLinksJsonldEquipmentFileLinksWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.


        :param context: The context of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :type: OneOfEquipmentFileLinksJsonldEquipmentFileLinksWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501


        :return: The id of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.


        :param id: The id of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501


        :return: The type of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.


        :param type: The type of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def equipment(self):
        """Gets the equipment of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501


        :return: The equipment of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :rtype: str
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.


        :param equipment: The equipment of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :type: str
        """

        self._equipment = equipment

    @property
    def link_name(self):
        """Gets the link_name of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501


        :return: The link_name of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :rtype: str
        """
        return self._link_name

    @link_name.setter
    def link_name(self, link_name):
        """Sets the link_name of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.


        :param link_name: The link_name of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :type: str
        """

        self._link_name = link_name

    @property
    def link_destination(self):
        """Gets the link_destination of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501


        :return: The link_destination of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
        :rtype: str
        """
        return self._link_destination

    @link_destination.setter
    def link_destination(self, link_destination):
        """Sets the link_destination of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.


        :param link_destination: The link_destination of this EquipmentFileLinksJsonldEquipmentFileLinksWrite.  # noqa: E501
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
        if issubclass(EquipmentFileLinksJsonldEquipmentFileLinksWrite, dict):
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
        if not isinstance(other, EquipmentFileLinksJsonldEquipmentFileLinksWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other