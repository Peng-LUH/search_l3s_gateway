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

class UserJsonldUserItemRead(object):
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
        'context': 'OneOfUserJsonldUserItemReadContext',
        'id': 'str',
        'type': 'str',
        'keycloak_uuid': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'username': 'str',
        'groups': 'list[GroupJsonldUserItemRead]',
        'roles': 'list[str]',
        'firstname': 'str',
        'lastname': 'str',
        'name': 'str',
        'email': 'str',
        'state': 'bool',
        'organizations': 'list[str]',
        'created_forms': 'list[str]',
        'user_options': 'str',
        'tasks_todo': 'list[str]',
        'group_task_todo_links': 'list[str]',
        'directories': 'list[str]',
        'documents': 'list[str]',
        'inactive_organizations': 'list[str]',
        'christiani_id': 'str',
        'shared_directories': 'list[str]',
        'shared_documents': 'list[str]',
        'autofachmann_id': 'int',
        'external_europathek_books': 'list[str]',
        'shown_groups': 'list[GroupJsonldUserItemRead]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'keycloak_uuid': 'keycloakUuid',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'username': 'username',
        'groups': 'groups',
        'roles': 'roles',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'name': 'name',
        'email': 'email',
        'state': 'state',
        'organizations': 'organizations',
        'created_forms': 'createdForms',
        'user_options': 'userOptions',
        'tasks_todo': 'tasksTodo',
        'group_task_todo_links': 'groupTaskTodoLinks',
        'directories': 'directories',
        'documents': 'documents',
        'inactive_organizations': 'inactiveOrganizations',
        'christiani_id': 'christianiId',
        'shared_directories': 'sharedDirectories',
        'shared_documents': 'sharedDocuments',
        'autofachmann_id': 'autofachmannId',
        'external_europathek_books': 'externalEuropathekBooks',
        'shown_groups': 'shownGroups'
    }

    def __init__(self, context=None, id=None, type=None, keycloak_uuid=None, created_at=None, updated_at=None, id=None, username=None, groups=None, roles=None, firstname=None, lastname=None, name=None, email=None, state=None, organizations=None, created_forms=None, user_options=None, tasks_todo=None, group_task_todo_links=None, directories=None, documents=None, inactive_organizations=None, christiani_id=None, shared_directories=None, shared_documents=None, autofachmann_id=None, external_europathek_books=None, shown_groups=None):  # noqa: E501
        """UserJsonldUserItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._keycloak_uuid = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._username = None
        self._groups = None
        self._roles = None
        self._firstname = None
        self._lastname = None
        self._name = None
        self._email = None
        self._state = None
        self._organizations = None
        self._created_forms = None
        self._user_options = None
        self._tasks_todo = None
        self._group_task_todo_links = None
        self._directories = None
        self._documents = None
        self._inactive_organizations = None
        self._christiani_id = None
        self._shared_directories = None
        self._shared_documents = None
        self._autofachmann_id = None
        self._external_europathek_books = None
        self._shown_groups = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if keycloak_uuid is not None:
            self.keycloak_uuid = keycloak_uuid
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if groups is not None:
            self.groups = groups
        if roles is not None:
            self.roles = roles
        self.firstname = firstname
        self.lastname = lastname
        if name is not None:
            self.name = name
        self.email = email
        if state is not None:
            self.state = state
        if organizations is not None:
            self.organizations = organizations
        if created_forms is not None:
            self.created_forms = created_forms
        if user_options is not None:
            self.user_options = user_options
        if tasks_todo is not None:
            self.tasks_todo = tasks_todo
        if group_task_todo_links is not None:
            self.group_task_todo_links = group_task_todo_links
        if directories is not None:
            self.directories = directories
        if documents is not None:
            self.documents = documents
        if inactive_organizations is not None:
            self.inactive_organizations = inactive_organizations
        if christiani_id is not None:
            self.christiani_id = christiani_id
        if shared_directories is not None:
            self.shared_directories = shared_directories
        if shared_documents is not None:
            self.shared_documents = shared_documents
        if autofachmann_id is not None:
            self.autofachmann_id = autofachmann_id
        if external_europathek_books is not None:
            self.external_europathek_books = external_europathek_books
        if shown_groups is not None:
            self.shown_groups = shown_groups

    @property
    def context(self):
        """Gets the context of this UserJsonldUserItemRead.  # noqa: E501


        :return: The context of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: OneOfUserJsonldUserItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this UserJsonldUserItemRead.


        :param context: The context of this UserJsonldUserItemRead.  # noqa: E501
        :type: OneOfUserJsonldUserItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this UserJsonldUserItemRead.  # noqa: E501


        :return: The id of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserJsonldUserItemRead.


        :param id: The id of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this UserJsonldUserItemRead.  # noqa: E501


        :return: The type of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserJsonldUserItemRead.


        :param type: The type of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def keycloak_uuid(self):
        """Gets the keycloak_uuid of this UserJsonldUserItemRead.  # noqa: E501


        :return: The keycloak_uuid of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._keycloak_uuid

    @keycloak_uuid.setter
    def keycloak_uuid(self, keycloak_uuid):
        """Sets the keycloak_uuid of this UserJsonldUserItemRead.


        :param keycloak_uuid: The keycloak_uuid of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._keycloak_uuid = keycloak_uuid

    @property
    def created_at(self):
        """Gets the created_at of this UserJsonldUserItemRead.  # noqa: E501


        :return: The created_at of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserJsonldUserItemRead.


        :param created_at: The created_at of this UserJsonldUserItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserJsonldUserItemRead.  # noqa: E501


        :return: The updated_at of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserJsonldUserItemRead.


        :param updated_at: The updated_at of this UserJsonldUserItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this UserJsonldUserItemRead.  # noqa: E501


        :return: The id of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserJsonldUserItemRead.


        :param id: The id of this UserJsonldUserItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserJsonldUserItemRead.  # noqa: E501


        :return: The username of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserJsonldUserItemRead.


        :param username: The username of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def groups(self):
        """Gets the groups of this UserJsonldUserItemRead.  # noqa: E501


        :return: The groups of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[GroupJsonldUserItemRead]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserJsonldUserItemRead.


        :param groups: The groups of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[GroupJsonldUserItemRead]
        """

        self._groups = groups

    @property
    def roles(self):
        """Gets the roles of this UserJsonldUserItemRead.  # noqa: E501


        :return: The roles of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserJsonldUserItemRead.


        :param roles: The roles of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def firstname(self):
        """Gets the firstname of this UserJsonldUserItemRead.  # noqa: E501


        :return: The firstname of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this UserJsonldUserItemRead.


        :param firstname: The firstname of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this UserJsonldUserItemRead.  # noqa: E501


        :return: The lastname of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this UserJsonldUserItemRead.


        :param lastname: The lastname of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")  # noqa: E501

        self._lastname = lastname

    @property
    def name(self):
        """Gets the name of this UserJsonldUserItemRead.  # noqa: E501

        just to combine $firstname and $lastname, needs no column in database  # noqa: E501

        :return: The name of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserJsonldUserItemRead.

        just to combine $firstname and $lastname, needs no column in database  # noqa: E501

        :param name: The name of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this UserJsonldUserItemRead.  # noqa: E501


        :return: The email of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserJsonldUserItemRead.


        :param email: The email of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def state(self):
        """Gets the state of this UserJsonldUserItemRead.  # noqa: E501


        :return: The state of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: bool
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UserJsonldUserItemRead.


        :param state: The state of this UserJsonldUserItemRead.  # noqa: E501
        :type: bool
        """

        self._state = state

    @property
    def organizations(self):
        """Gets the organizations of this UserJsonldUserItemRead.  # noqa: E501


        :return: The organizations of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this UserJsonldUserItemRead.


        :param organizations: The organizations of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._organizations = organizations

    @property
    def created_forms(self):
        """Gets the created_forms of this UserJsonldUserItemRead.  # noqa: E501


        :return: The created_forms of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._created_forms

    @created_forms.setter
    def created_forms(self, created_forms):
        """Sets the created_forms of this UserJsonldUserItemRead.


        :param created_forms: The created_forms of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._created_forms = created_forms

    @property
    def user_options(self):
        """Gets the user_options of this UserJsonldUserItemRead.  # noqa: E501


        :return: The user_options of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._user_options

    @user_options.setter
    def user_options(self, user_options):
        """Sets the user_options of this UserJsonldUserItemRead.


        :param user_options: The user_options of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._user_options = user_options

    @property
    def tasks_todo(self):
        """Gets the tasks_todo of this UserJsonldUserItemRead.  # noqa: E501


        :return: The tasks_todo of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._tasks_todo

    @tasks_todo.setter
    def tasks_todo(self, tasks_todo):
        """Sets the tasks_todo of this UserJsonldUserItemRead.


        :param tasks_todo: The tasks_todo of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._tasks_todo = tasks_todo

    @property
    def group_task_todo_links(self):
        """Gets the group_task_todo_links of this UserJsonldUserItemRead.  # noqa: E501


        :return: The group_task_todo_links of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_task_todo_links

    @group_task_todo_links.setter
    def group_task_todo_links(self, group_task_todo_links):
        """Sets the group_task_todo_links of this UserJsonldUserItemRead.


        :param group_task_todo_links: The group_task_todo_links of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._group_task_todo_links = group_task_todo_links

    @property
    def directories(self):
        """Gets the directories of this UserJsonldUserItemRead.  # noqa: E501


        :return: The directories of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        """Sets the directories of this UserJsonldUserItemRead.


        :param directories: The directories of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._directories = directories

    @property
    def documents(self):
        """Gets the documents of this UserJsonldUserItemRead.  # noqa: E501


        :return: The documents of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this UserJsonldUserItemRead.


        :param documents: The documents of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._documents = documents

    @property
    def inactive_organizations(self):
        """Gets the inactive_organizations of this UserJsonldUserItemRead.  # noqa: E501


        :return: The inactive_organizations of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._inactive_organizations

    @inactive_organizations.setter
    def inactive_organizations(self, inactive_organizations):
        """Sets the inactive_organizations of this UserJsonldUserItemRead.


        :param inactive_organizations: The inactive_organizations of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._inactive_organizations = inactive_organizations

    @property
    def christiani_id(self):
        """Gets the christiani_id of this UserJsonldUserItemRead.  # noqa: E501


        :return: The christiani_id of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._christiani_id

    @christiani_id.setter
    def christiani_id(self, christiani_id):
        """Sets the christiani_id of this UserJsonldUserItemRead.


        :param christiani_id: The christiani_id of this UserJsonldUserItemRead.  # noqa: E501
        :type: str
        """

        self._christiani_id = christiani_id

    @property
    def shared_directories(self):
        """Gets the shared_directories of this UserJsonldUserItemRead.  # noqa: E501


        :return: The shared_directories of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_directories

    @shared_directories.setter
    def shared_directories(self, shared_directories):
        """Sets the shared_directories of this UserJsonldUserItemRead.


        :param shared_directories: The shared_directories of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_directories = shared_directories

    @property
    def shared_documents(self):
        """Gets the shared_documents of this UserJsonldUserItemRead.  # noqa: E501


        :return: The shared_documents of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_documents

    @shared_documents.setter
    def shared_documents(self, shared_documents):
        """Sets the shared_documents of this UserJsonldUserItemRead.


        :param shared_documents: The shared_documents of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_documents = shared_documents

    @property
    def autofachmann_id(self):
        """Gets the autofachmann_id of this UserJsonldUserItemRead.  # noqa: E501


        :return: The autofachmann_id of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: int
        """
        return self._autofachmann_id

    @autofachmann_id.setter
    def autofachmann_id(self, autofachmann_id):
        """Sets the autofachmann_id of this UserJsonldUserItemRead.


        :param autofachmann_id: The autofachmann_id of this UserJsonldUserItemRead.  # noqa: E501
        :type: int
        """

        self._autofachmann_id = autofachmann_id

    @property
    def external_europathek_books(self):
        """Gets the external_europathek_books of this UserJsonldUserItemRead.  # noqa: E501


        :return: The external_europathek_books of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_europathek_books

    @external_europathek_books.setter
    def external_europathek_books(self, external_europathek_books):
        """Sets the external_europathek_books of this UserJsonldUserItemRead.


        :param external_europathek_books: The external_europathek_books of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[str]
        """

        self._external_europathek_books = external_europathek_books

    @property
    def shown_groups(self):
        """Gets the shown_groups of this UserJsonldUserItemRead.  # noqa: E501


        :return: The shown_groups of this UserJsonldUserItemRead.  # noqa: E501
        :rtype: list[GroupJsonldUserItemRead]
        """
        return self._shown_groups

    @shown_groups.setter
    def shown_groups(self, shown_groups):
        """Sets the shown_groups of this UserJsonldUserItemRead.


        :param shown_groups: The shown_groups of this UserJsonldUserItemRead.  # noqa: E501
        :type: list[GroupJsonldUserItemRead]
        """

        self._shown_groups = shown_groups

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
        if issubclass(UserJsonldUserItemRead, dict):
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
        if not isinstance(other, UserJsonldUserItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other