# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LearningProfileDto(object):
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
        'media_type': 'str',
        'language': 'str',
        'semantic_density': 'float',
        'semantic_gravity': 'float',
        'processing_time_per_unit': 'str',
        'learning_history_id': 'str',
        'preferred_didactic_method': 'str',
        'user_id': 'str',
        'id': 'str'
    }

    attribute_map = {
        'media_type': 'mediaType',
        'language': 'language',
        'semantic_density': 'semanticDensity',
        'semantic_gravity': 'semanticGravity',
        'processing_time_per_unit': 'processingTimePerUnit',
        'learning_history_id': 'learningHistoryId',
        'preferred_didactic_method': 'preferredDidacticMethod',
        'user_id': 'userId',
        'id': 'id'
    }

    def __init__(self, media_type=None, language=None, semantic_density=None, semantic_gravity=None, processing_time_per_unit=None, learning_history_id=None, preferred_didactic_method=None, user_id=None, id=None):  # noqa: E501
        """LearningProfileDto - a model defined in Swagger"""  # noqa: E501
        self._media_type = None
        self._language = None
        self._semantic_density = None
        self._semantic_gravity = None
        self._processing_time_per_unit = None
        self._learning_history_id = None
        self._preferred_didactic_method = None
        self._user_id = None
        self._id = None
        self.discriminator = None
        if media_type is not None:
            self.media_type = media_type
        if language is not None:
            self.language = language
        if semantic_density is not None:
            self.semantic_density = semantic_density
        if semantic_gravity is not None:
            self.semantic_gravity = semantic_gravity
        if processing_time_per_unit is not None:
            self.processing_time_per_unit = processing_time_per_unit
        if learning_history_id is not None:
            self.learning_history_id = learning_history_id
        if preferred_didactic_method is not None:
            self.preferred_didactic_method = preferred_didactic_method
        self.user_id = user_id
        self.id = id

    @property
    def media_type(self):
        """Gets the media_type of this LearningProfileDto.  # noqa: E501

        Used to validate that the user is the owner of the target repository.  # noqa: E501

        :return: The media_type of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this LearningProfileDto.

        Used to validate that the user is the owner of the target repository.  # noqa: E501

        :param media_type: The media_type of this LearningProfileDto.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def language(self):
        """Gets the language of this LearningProfileDto.  # noqa: E501


        :return: The language of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LearningProfileDto.


        :param language: The language of this LearningProfileDto.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def semantic_density(self):
        """Gets the semantic_density of this LearningProfileDto.  # noqa: E501


        :return: The semantic_density of this LearningProfileDto.  # noqa: E501
        :rtype: float
        """
        return self._semantic_density

    @semantic_density.setter
    def semantic_density(self, semantic_density):
        """Sets the semantic_density of this LearningProfileDto.


        :param semantic_density: The semantic_density of this LearningProfileDto.  # noqa: E501
        :type: float
        """

        self._semantic_density = semantic_density

    @property
    def semantic_gravity(self):
        """Gets the semantic_gravity of this LearningProfileDto.  # noqa: E501


        :return: The semantic_gravity of this LearningProfileDto.  # noqa: E501
        :rtype: float
        """
        return self._semantic_gravity

    @semantic_gravity.setter
    def semantic_gravity(self, semantic_gravity):
        """Sets the semantic_gravity of this LearningProfileDto.


        :param semantic_gravity: The semantic_gravity of this LearningProfileDto.  # noqa: E501
        :type: float
        """

        self._semantic_gravity = semantic_gravity

    @property
    def processing_time_per_unit(self):
        """Gets the processing_time_per_unit of this LearningProfileDto.  # noqa: E501


        :return: The processing_time_per_unit of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._processing_time_per_unit

    @processing_time_per_unit.setter
    def processing_time_per_unit(self, processing_time_per_unit):
        """Sets the processing_time_per_unit of this LearningProfileDto.


        :param processing_time_per_unit: The processing_time_per_unit of this LearningProfileDto.  # noqa: E501
        :type: str
        """

        self._processing_time_per_unit = processing_time_per_unit

    @property
    def learning_history_id(self):
        """Gets the learning_history_id of this LearningProfileDto.  # noqa: E501


        :return: The learning_history_id of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._learning_history_id

    @learning_history_id.setter
    def learning_history_id(self, learning_history_id):
        """Sets the learning_history_id of this LearningProfileDto.


        :param learning_history_id: The learning_history_id of this LearningProfileDto.  # noqa: E501
        :type: str
        """

        self._learning_history_id = learning_history_id

    @property
    def preferred_didactic_method(self):
        """Gets the preferred_didactic_method of this LearningProfileDto.  # noqa: E501


        :return: The preferred_didactic_method of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._preferred_didactic_method

    @preferred_didactic_method.setter
    def preferred_didactic_method(self, preferred_didactic_method):
        """Sets the preferred_didactic_method of this LearningProfileDto.


        :param preferred_didactic_method: The preferred_didactic_method of this LearningProfileDto.  # noqa: E501
        :type: str
        """

        self._preferred_didactic_method = preferred_didactic_method

    @property
    def user_id(self):
        """Gets the user_id of this LearningProfileDto.  # noqa: E501


        :return: The user_id of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this LearningProfileDto.


        :param user_id: The user_id of this LearningProfileDto.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def id(self):
        """Gets the id of this LearningProfileDto.  # noqa: E501


        :return: The id of this LearningProfileDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LearningProfileDto.


        :param id: The id of this LearningProfileDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(LearningProfileDto, dict):
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
        if not isinstance(other, LearningProfileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
