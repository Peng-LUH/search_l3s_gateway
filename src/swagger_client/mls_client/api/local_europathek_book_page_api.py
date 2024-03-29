# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LocalEuropathekBookPageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_local_europathek_book_page_collection(self, **kwargs):  # noqa: E501
        """Retrieves the collection of LocalEuropathekBookPage resources.  # noqa: E501

        Retrieves the collection of LocalEuropathekBookPage resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_local_europathek_book_page_collection(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The collection page number
        :param int items_per_page: The number of items per page
        :param bool pagination: Enable or disable pagination
        :param str title:
        :param int book_page:
        :param list[int] book_page:
        :param str book:
        :param list[str] book:
        :return: InlineResponse20043
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_local_europathek_book_page_collection_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_local_europathek_book_page_collection_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_local_europathek_book_page_collection_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves the collection of LocalEuropathekBookPage resources.  # noqa: E501

        Retrieves the collection of LocalEuropathekBookPage resources.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_local_europathek_book_page_collection_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The collection page number
        :param int items_per_page: The number of items per page
        :param bool pagination: Enable or disable pagination
        :param str title:
        :param int book_page:
        :param list[int] book_page:
        :param str book:
        :param list[str] book:
        :return: InlineResponse20043
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'items_per_page', 'pagination', 'title', 'book_page', 'book_page', 'book', 'book']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_local_europathek_book_page_collection" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'items_per_page' in params:
            query_params.append(('itemsPerPage', params['items_per_page']))  # noqa: E501
        if 'pagination' in params:
            query_params.append(('pagination', params['pagination']))  # noqa: E501
        if 'title' in params:
            query_params.append(('title', params['title']))  # noqa: E501
        if 'book_page' in params:
            query_params.append(('bookPage', params['book_page']))  # noqa: E501
        if 'book_page' in params:
            query_params.append(('bookPage[]', params['book_page']))  # noqa: E501
            collection_formats['bookPage[]'] = 'multi'  # noqa: E501
        if 'book' in params:
            query_params.append(('book', params['book']))  # noqa: E501
        if 'book' in params:
            query_params.append(('book[]', params['book']))  # noqa: E501
            collection_formats['book[]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/local-europathek-book-pages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20043',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_local_europathek_book_page_item(self, id, **kwargs):  # noqa: E501
        """Retrieves a LocalEuropathekBookPage resource.  # noqa: E501

        Retrieves a LocalEuropathekBookPage resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_local_europathek_book_page_item(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Resource identifier (required)
        :return: LocalEuropathekBookPageJsonldLocalEuropathekBookPageItemRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_local_europathek_book_page_item_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_local_europathek_book_page_item_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_local_europathek_book_page_item_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a LocalEuropathekBookPage resource.  # noqa: E501

        Retrieves a LocalEuropathekBookPage resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_local_europathek_book_page_item_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Resource identifier (required)
        :return: LocalEuropathekBookPageJsonldLocalEuropathekBookPageItemRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_local_europathek_book_page_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_local_europathek_book_page_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/ld+json', 'application/json', 'text/html', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/mls-api/local-europathek-book-pages/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LocalEuropathekBookPageJsonldLocalEuropathekBookPageItemRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
