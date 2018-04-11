# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_operation import AzureOperationPoller
import uuid
from .operations.profiles_operations import ProfilesOperations
from .operations.endpoints_operations import EndpointsOperations
from .operations.origins_operations import OriginsOperations
from .operations.custom_domains_operations import CustomDomainsOperations
from .operations.resource_usage_operations import ResourceUsageOperations
from .operations.operations import Operations
from .operations.edge_nodes_operations import EdgeNodesOperations
from . import models


class CdnManagementClientConfiguration(AzureConfiguration):
    """Configuration for CdnManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure
     subscription.
    :type resource_group_name: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, resource_group_name, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if resource_group_name is None:
            raise ValueError("Parameter 'resource_group_name' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(CdnManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-cdn/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name


class CdnManagementClient(object):
    """Use these APIs to manage Azure CDN resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.

    :ivar config: Configuration for client.
    :vartype config: CdnManagementClientConfiguration

    :ivar profiles: Profiles operations
    :vartype profiles: azure.mgmt.cdn.operations.ProfilesOperations
    :ivar endpoints: Endpoints operations
    :vartype endpoints: azure.mgmt.cdn.operations.EndpointsOperations
    :ivar origins: Origins operations
    :vartype origins: azure.mgmt.cdn.operations.OriginsOperations
    :ivar custom_domains: CustomDomains operations
    :vartype custom_domains: azure.mgmt.cdn.operations.CustomDomainsOperations
    :ivar resource_usage: ResourceUsage operations
    :vartype resource_usage: azure.mgmt.cdn.operations.ResourceUsageOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.cdn.operations.Operations
    :ivar edge_nodes: EdgeNodes operations
    :vartype edge_nodes: azure.mgmt.cdn.operations.EdgeNodesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure
     subscription.
    :type resource_group_name: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, resource_group_name, base_url=None):

        self.config = CdnManagementClientConfiguration(credentials, subscription_id, resource_group_name, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-10-12'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.profiles = ProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.origins = OriginsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.custom_domains = CustomDomainsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.resource_usage = ResourceUsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.edge_nodes = EdgeNodesOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def check_name_availability(
            self, name, custom_headers=None, raw=False, **operation_config):
        """Check the availability of a resource name. This is needed for resources
        where name is globally unique, such as a CDN endpoint.

        :param name: The resource name to validate.
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.cdn.models.ErrorResponseException>`
        """
        check_name_availability_input = models.CheckNameAvailabilityInput(name=name)

        # Construct URL
        url = self.check_name_availability.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(check_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_name_availability.metadata = {'url': '/providers/Microsoft.Cdn/checkNameAvailability'}

    def check_name_availability_with_subscription(
            self, name, custom_headers=None, raw=False, **operation_config):
        """Check the availability of a resource name. This is needed for resources
        where name is globally unique, such as a CDN endpoint.

        :param name: The resource name to validate.
        :type name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.cdn.models.ErrorResponseException>`
        """
        check_name_availability_input = models.CheckNameAvailabilityInput(name=name)

        # Construct URL
        url = self.check_name_availability_with_subscription.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(check_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_name_availability_with_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/checkNameAvailability'}

    def validate_probe(
            self, probe_url, custom_headers=None, raw=False, **operation_config):
        """Check if the probe path is a valid path and the file can be accessed.
        Probe path is the path to a file hosted on the origin server to help
        accelerate the delivery of dynamic content via the CDN endpoint. This
        path is relative to the origin path specified in the endpoint
        configuration.

        :param probe_url: The probe URL to validate.
        :type probe_url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ValidateProbeOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.cdn.models.ValidateProbeOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.cdn.models.ErrorResponseException>`
        """
        validate_probe_input = models.ValidateProbeInput(probe_url=probe_url)

        # Construct URL
        url = self.validate_probe.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(validate_probe_input, 'ValidateProbeInput')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ValidateProbeOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    validate_probe.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Cdn/validateProbe'}
