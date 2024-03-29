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

class TaskJsonldTaskRead(object):
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
        'context': 'OneOfTaskJsonldTaskReadContext',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'title': 'str',
        'creator': 'str',
        'last_editor': 'str',
        'task_set': 'str',
        'description': 'str',
        'due': 'float',
        'is_work_in_groups': 'bool',
        'lifecycle': 'str',
        'app_tags': 'list[str]',
        'task_steps': 'list[str]',
        'task_todos': 'list[str]',
        'group_task_todos': 'list[str]',
        'skills': 'list[TaskSkillJsonldTaskRead]',
        'original_task': 'AnyOfTaskJsonldTaskReadOriginalTask',
        'copy_source': 'AnyOfTaskJsonldTaskReadCopySource',
        'major_version': 'int',
        'minor_version': 'int',
        'updater': 'str',
        'preview_image': 'AnyOfTaskJsonldTaskReadPreviewImage',
        'equipment_maintenances': 'list[str]',
        'external_content_organization_copy_source': 'str'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'context': '@context',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'title': 'title',
        'creator': 'creator',
        'last_editor': 'lastEditor',
        'task_set': 'taskSet',
        'description': 'description',
        'due': 'due',
        'is_work_in_groups': 'isWorkInGroups',
        'lifecycle': 'lifecycle',
        'app_tags': 'appTags',
        'task_steps': 'taskSteps',
        'task_todos': 'taskTodos',
        'group_task_todos': 'groupTaskTodos',
        'skills': 'skills',
        'original_task': 'originalTask',
        'copy_source': 'copySource',
        'major_version': 'majorVersion',
        'minor_version': 'minorVersion',
        'updater': 'updater',
        'preview_image': 'previewImage',
        'equipment_maintenances': 'equipmentMaintenances',
        'external_content_organization_copy_source': 'externalContentOrganizationCopySource'
    }

    def __init__(self, id=None, type=None, context=None, created_at=None, updated_at=None, id=None, title=None, creator=None, last_editor=None, task_set=None, description=None, due=None, is_work_in_groups=None, lifecycle='DRAFT', app_tags=None, task_steps=None, task_todos=None, group_task_todos=None, skills=None, original_task=None, copy_source=None, major_version=1, minor_version=None, updater=None, preview_image=None, equipment_maintenances=None, external_content_organization_copy_source=None):  # noqa: E501
        """TaskJsonldTaskRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._context = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._title = None
        self._creator = None
        self._last_editor = None
        self._task_set = None
        self._description = None
        self._due = None
        self._is_work_in_groups = None
        self._lifecycle = None
        self._app_tags = None
        self._task_steps = None
        self._task_todos = None
        self._group_task_todos = None
        self._skills = None
        self._original_task = None
        self._copy_source = None
        self._major_version = None
        self._minor_version = None
        self._updater = None
        self._preview_image = None
        self._equipment_maintenances = None
        self._external_content_organization_copy_source = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if context is not None:
            self.context = context
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        self.title = title
        if creator is not None:
            self.creator = creator
        if last_editor is not None:
            self.last_editor = last_editor
        if task_set is not None:
            self.task_set = task_set
        if description is not None:
            self.description = description
        if due is not None:
            self.due = due
        if is_work_in_groups is not None:
            self.is_work_in_groups = is_work_in_groups
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if app_tags is not None:
            self.app_tags = app_tags
        if task_steps is not None:
            self.task_steps = task_steps
        if task_todos is not None:
            self.task_todos = task_todos
        if group_task_todos is not None:
            self.group_task_todos = group_task_todos
        if skills is not None:
            self.skills = skills
        if original_task is not None:
            self.original_task = original_task
        if copy_source is not None:
            self.copy_source = copy_source
        if major_version is not None:
            self.major_version = major_version
        if minor_version is not None:
            self.minor_version = minor_version
        if updater is not None:
            self.updater = updater
        if preview_image is not None:
            self.preview_image = preview_image
        if equipment_maintenances is not None:
            self.equipment_maintenances = equipment_maintenances
        if external_content_organization_copy_source is not None:
            self.external_content_organization_copy_source = external_content_organization_copy_source

    @property
    def id(self):
        """Gets the id of this TaskJsonldTaskRead.  # noqa: E501


        :return: The id of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskJsonldTaskRead.


        :param id: The id of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TaskJsonldTaskRead.  # noqa: E501


        :return: The type of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskJsonldTaskRead.


        :param type: The type of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def context(self):
        """Gets the context of this TaskJsonldTaskRead.  # noqa: E501


        :return: The context of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: OneOfTaskJsonldTaskReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this TaskJsonldTaskRead.


        :param context: The context of this TaskJsonldTaskRead.  # noqa: E501
        :type: OneOfTaskJsonldTaskReadContext
        """

        self._context = context

    @property
    def created_at(self):
        """Gets the created_at of this TaskJsonldTaskRead.  # noqa: E501


        :return: The created_at of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskJsonldTaskRead.


        :param created_at: The created_at of this TaskJsonldTaskRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskJsonldTaskRead.  # noqa: E501


        :return: The updated_at of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskJsonldTaskRead.


        :param updated_at: The updated_at of this TaskJsonldTaskRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TaskJsonldTaskRead.  # noqa: E501


        :return: The id of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskJsonldTaskRead.


        :param id: The id of this TaskJsonldTaskRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TaskJsonldTaskRead.  # noqa: E501


        :return: The title of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskJsonldTaskRead.


        :param title: The title of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def creator(self):
        """Gets the creator of this TaskJsonldTaskRead.  # noqa: E501


        :return: The creator of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TaskJsonldTaskRead.


        :param creator: The creator of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def last_editor(self):
        """Gets the last_editor of this TaskJsonldTaskRead.  # noqa: E501


        :return: The last_editor of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this TaskJsonldTaskRead.


        :param last_editor: The last_editor of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._last_editor = last_editor

    @property
    def task_set(self):
        """Gets the task_set of this TaskJsonldTaskRead.  # noqa: E501


        :return: The task_set of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._task_set

    @task_set.setter
    def task_set(self, task_set):
        """Sets the task_set of this TaskJsonldTaskRead.


        :param task_set: The task_set of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._task_set = task_set

    @property
    def description(self):
        """Gets the description of this TaskJsonldTaskRead.  # noqa: E501


        :return: The description of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskJsonldTaskRead.


        :param description: The description of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due(self):
        """Gets the due of this TaskJsonldTaskRead.  # noqa: E501


        :return: The due of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: float
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this TaskJsonldTaskRead.


        :param due: The due of this TaskJsonldTaskRead.  # noqa: E501
        :type: float
        """

        self._due = due

    @property
    def is_work_in_groups(self):
        """Gets the is_work_in_groups of this TaskJsonldTaskRead.  # noqa: E501


        :return: The is_work_in_groups of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: bool
        """
        return self._is_work_in_groups

    @is_work_in_groups.setter
    def is_work_in_groups(self, is_work_in_groups):
        """Sets the is_work_in_groups of this TaskJsonldTaskRead.


        :param is_work_in_groups: The is_work_in_groups of this TaskJsonldTaskRead.  # noqa: E501
        :type: bool
        """

        self._is_work_in_groups = is_work_in_groups

    @property
    def lifecycle(self):
        """Gets the lifecycle of this TaskJsonldTaskRead.  # noqa: E501


        :return: The lifecycle of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """Sets the lifecycle of this TaskJsonldTaskRead.


        :param lifecycle: The lifecycle of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._lifecycle = lifecycle

    @property
    def app_tags(self):
        """Gets the app_tags of this TaskJsonldTaskRead.  # noqa: E501


        :return: The app_tags of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_tags

    @app_tags.setter
    def app_tags(self, app_tags):
        """Sets the app_tags of this TaskJsonldTaskRead.


        :param app_tags: The app_tags of this TaskJsonldTaskRead.  # noqa: E501
        :type: list[str]
        """

        self._app_tags = app_tags

    @property
    def task_steps(self):
        """Gets the task_steps of this TaskJsonldTaskRead.  # noqa: E501


        :return: The task_steps of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_steps

    @task_steps.setter
    def task_steps(self, task_steps):
        """Sets the task_steps of this TaskJsonldTaskRead.


        :param task_steps: The task_steps of this TaskJsonldTaskRead.  # noqa: E501
        :type: list[str]
        """

        self._task_steps = task_steps

    @property
    def task_todos(self):
        """Gets the task_todos of this TaskJsonldTaskRead.  # noqa: E501


        :return: The task_todos of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_todos

    @task_todos.setter
    def task_todos(self, task_todos):
        """Sets the task_todos of this TaskJsonldTaskRead.


        :param task_todos: The task_todos of this TaskJsonldTaskRead.  # noqa: E501
        :type: list[str]
        """

        self._task_todos = task_todos

    @property
    def group_task_todos(self):
        """Gets the group_task_todos of this TaskJsonldTaskRead.  # noqa: E501


        :return: The group_task_todos of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_task_todos

    @group_task_todos.setter
    def group_task_todos(self, group_task_todos):
        """Sets the group_task_todos of this TaskJsonldTaskRead.


        :param group_task_todos: The group_task_todos of this TaskJsonldTaskRead.  # noqa: E501
        :type: list[str]
        """

        self._group_task_todos = group_task_todos

    @property
    def skills(self):
        """Gets the skills of this TaskJsonldTaskRead.  # noqa: E501


        :return: The skills of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: list[TaskSkillJsonldTaskRead]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this TaskJsonldTaskRead.


        :param skills: The skills of this TaskJsonldTaskRead.  # noqa: E501
        :type: list[TaskSkillJsonldTaskRead]
        """

        self._skills = skills

    @property
    def original_task(self):
        """Gets the original_task of this TaskJsonldTaskRead.  # noqa: E501


        :return: The original_task of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: AnyOfTaskJsonldTaskReadOriginalTask
        """
        return self._original_task

    @original_task.setter
    def original_task(self, original_task):
        """Sets the original_task of this TaskJsonldTaskRead.


        :param original_task: The original_task of this TaskJsonldTaskRead.  # noqa: E501
        :type: AnyOfTaskJsonldTaskReadOriginalTask
        """

        self._original_task = original_task

    @property
    def copy_source(self):
        """Gets the copy_source of this TaskJsonldTaskRead.  # noqa: E501


        :return: The copy_source of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: AnyOfTaskJsonldTaskReadCopySource
        """
        return self._copy_source

    @copy_source.setter
    def copy_source(self, copy_source):
        """Sets the copy_source of this TaskJsonldTaskRead.


        :param copy_source: The copy_source of this TaskJsonldTaskRead.  # noqa: E501
        :type: AnyOfTaskJsonldTaskReadCopySource
        """

        self._copy_source = copy_source

    @property
    def major_version(self):
        """Gets the major_version of this TaskJsonldTaskRead.  # noqa: E501


        :return: The major_version of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: int
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """Sets the major_version of this TaskJsonldTaskRead.


        :param major_version: The major_version of this TaskJsonldTaskRead.  # noqa: E501
        :type: int
        """

        self._major_version = major_version

    @property
    def minor_version(self):
        """Gets the minor_version of this TaskJsonldTaskRead.  # noqa: E501


        :return: The minor_version of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: int
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, minor_version):
        """Sets the minor_version of this TaskJsonldTaskRead.


        :param minor_version: The minor_version of this TaskJsonldTaskRead.  # noqa: E501
        :type: int
        """

        self._minor_version = minor_version

    @property
    def updater(self):
        """Gets the updater of this TaskJsonldTaskRead.  # noqa: E501


        :return: The updater of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._updater

    @updater.setter
    def updater(self, updater):
        """Sets the updater of this TaskJsonldTaskRead.


        :param updater: The updater of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._updater = updater

    @property
    def preview_image(self):
        """Gets the preview_image of this TaskJsonldTaskRead.  # noqa: E501


        :return: The preview_image of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: AnyOfTaskJsonldTaskReadPreviewImage
        """
        return self._preview_image

    @preview_image.setter
    def preview_image(self, preview_image):
        """Sets the preview_image of this TaskJsonldTaskRead.


        :param preview_image: The preview_image of this TaskJsonldTaskRead.  # noqa: E501
        :type: AnyOfTaskJsonldTaskReadPreviewImage
        """

        self._preview_image = preview_image

    @property
    def equipment_maintenances(self):
        """Gets the equipment_maintenances of this TaskJsonldTaskRead.  # noqa: E501


        :return: The equipment_maintenances of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipment_maintenances

    @equipment_maintenances.setter
    def equipment_maintenances(self, equipment_maintenances):
        """Sets the equipment_maintenances of this TaskJsonldTaskRead.


        :param equipment_maintenances: The equipment_maintenances of this TaskJsonldTaskRead.  # noqa: E501
        :type: list[str]
        """

        self._equipment_maintenances = equipment_maintenances

    @property
    def external_content_organization_copy_source(self):
        """Gets the external_content_organization_copy_source of this TaskJsonldTaskRead.  # noqa: E501


        :return: The external_content_organization_copy_source of this TaskJsonldTaskRead.  # noqa: E501
        :rtype: str
        """
        return self._external_content_organization_copy_source

    @external_content_organization_copy_source.setter
    def external_content_organization_copy_source(self, external_content_organization_copy_source):
        """Sets the external_content_organization_copy_source of this TaskJsonldTaskRead.


        :param external_content_organization_copy_source: The external_content_organization_copy_source of this TaskJsonldTaskRead.  # noqa: E501
        :type: str
        """

        self._external_content_organization_copy_source = external_content_organization_copy_source

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
        if issubclass(TaskJsonldTaskRead, dict):
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
        if not isinstance(other, TaskJsonldTaskRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
