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

from msrest.serialization import Model


class AzureAsyncOperationResult(Model):
    """The response body contains the status of the specified asynchronous
    operation, indicating whether it has succeeded, is in progress, or has
    failed. Note that this status is distinct from the HTTP status code
    returned for the Get Operation Status operation itself. If the asynchronous
    operation succeeded, the response body includes the HTTP status code for
    the successful request. If the asynchronous operation failed, the response
    body includes the HTTP status code for the failed request and error
    information regarding the failure.

    :param status: Status of the Azure async operation. Possible values are:
     'InProgress', 'Succeeded', and 'Failed'. Possible values include:
     'InProgress', 'Succeeded', 'Failed'
    :type status: str or
     ~azure.mgmt.network.v2017_11_01.models.NetworkOperationStatus
    :param error:
    :type error: ~azure.mgmt.network.v2017_11_01.models.Error
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(self, status=None, error=None):
        self.status = status
        self.error = error
