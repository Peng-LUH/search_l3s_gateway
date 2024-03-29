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

class ExternalEuropathekBookExternalEuropathekBookXOrganizationRead(object):
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
        'title': 'str',
        'product': 'str',
        'code': 'str',
        'europa': 'str',
        'type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'product': 'product',
        'code': 'code',
        'europa': 'europa',
        'type': 'type'
    }

    def __init__(self, title=None, product=None, code=None, europa=None, type='EUROPATHEK'):  # noqa: E501
        """ExternalEuropathekBookExternalEuropathekBookXOrganizationRead - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._product = None
        self._code = None
        self._europa = None
        self._type = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if product is not None:
            self.product = product
        if code is not None:
            self.code = code
        if europa is not None:
            self.europa = europa
        if type is not None:
            self.type = type

    @property
    def title(self):
        """Gets the title of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501


        :return: The title of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.


        :param title: The title of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def product(self):
        """Gets the product of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501


        :return: The product of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.


        :param product: The product of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def code(self):
        """Gets the code of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501


        :return: The code of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.


        :param code: The code of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def europa(self):
        """Gets the europa of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501


        :return: The europa of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._europa

    @europa.setter
    def europa(self, europa):
        """Sets the europa of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.


        :param europa: The europa of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :type: str
        """

        self._europa = europa

    @property
    def type(self):
        """Gets the type of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501


        :return: The type of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.


        :param type: The type of this ExternalEuropathekBookExternalEuropathekBookXOrganizationRead.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ExternalEuropathekBookExternalEuropathekBookXOrganizationRead, dict):
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
        if not isinstance(other, ExternalEuropathekBookExternalEuropathekBookXOrganizationRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
