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

class TermsOfUseTermsOfUseWrite(object):
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
        'active': 'bool',
        'id': 'int',
        'excerpt': 'str',
        'text': 'str',
        'organization': 'str',
        'terms_of_use_pdf': 'str'
    }

    attribute_map = {
        'active': 'active',
        'id': 'id',
        'excerpt': 'excerpt',
        'text': 'text',
        'organization': 'organization',
        'terms_of_use_pdf': 'termsOfUsePDF'
    }

    def __init__(self, active=None, id=None, excerpt=None, text=None, organization=None, terms_of_use_pdf=None):  # noqa: E501
        """TermsOfUseTermsOfUseWrite - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._id = None
        self._excerpt = None
        self._text = None
        self._organization = None
        self._terms_of_use_pdf = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if id is not None:
            self.id = id
        if excerpt is not None:
            self.excerpt = excerpt
        if text is not None:
            self.text = text
        if organization is not None:
            self.organization = organization
        if terms_of_use_pdf is not None:
            self.terms_of_use_pdf = terms_of_use_pdf

    @property
    def active(self):
        """Gets the active of this TermsOfUseTermsOfUseWrite.  # noqa: E501


        :return: The active of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TermsOfUseTermsOfUseWrite.


        :param active: The active of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def id(self):
        """Gets the id of this TermsOfUseTermsOfUseWrite.  # noqa: E501


        :return: The id of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TermsOfUseTermsOfUseWrite.


        :param id: The id of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def excerpt(self):
        """Gets the excerpt of this TermsOfUseTermsOfUseWrite.  # noqa: E501


        :return: The excerpt of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :rtype: str
        """
        return self._excerpt

    @excerpt.setter
    def excerpt(self, excerpt):
        """Sets the excerpt of this TermsOfUseTermsOfUseWrite.


        :param excerpt: The excerpt of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :type: str
        """

        self._excerpt = excerpt

    @property
    def text(self):
        """Gets the text of this TermsOfUseTermsOfUseWrite.  # noqa: E501


        :return: The text of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TermsOfUseTermsOfUseWrite.


        :param text: The text of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def organization(self):
        """Gets the organization of this TermsOfUseTermsOfUseWrite.  # noqa: E501


        :return: The organization of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this TermsOfUseTermsOfUseWrite.


        :param organization: The organization of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def terms_of_use_pdf(self):
        """Gets the terms_of_use_pdf of this TermsOfUseTermsOfUseWrite.  # noqa: E501


        :return: The terms_of_use_pdf of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :rtype: str
        """
        return self._terms_of_use_pdf

    @terms_of_use_pdf.setter
    def terms_of_use_pdf(self, terms_of_use_pdf):
        """Sets the terms_of_use_pdf of this TermsOfUseTermsOfUseWrite.


        :param terms_of_use_pdf: The terms_of_use_pdf of this TermsOfUseTermsOfUseWrite.  # noqa: E501
        :type: str
        """

        self._terms_of_use_pdf = terms_of_use_pdf

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
        if issubclass(TermsOfUseTermsOfUseWrite, dict):
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
        if not isinstance(other, TermsOfUseTermsOfUseWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
