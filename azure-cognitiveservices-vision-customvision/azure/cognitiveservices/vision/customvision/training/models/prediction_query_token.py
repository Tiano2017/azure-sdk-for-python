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


class PredictionQueryToken(Model):
    """PredictionQueryToken.

    :param session:
    :type session: str
    :param continuation:
    :type continuation: str
    :param max_count:
    :type max_count: int
    :param order_by: Possible values include: 'Newest', 'Oldest', 'Suggested'
    :type order_by: str or
     ~azure.cognitiveservices.vision.customvision.training.models.enum
    :param tags:
    :type tags:
     list[~azure.cognitiveservices.vision.customvision.training.models.PredictionQueryTag]
    :param iteration_id:
    :type iteration_id: str
    :param start_time:
    :type start_time: datetime
    :param end_time:
    :type end_time: datetime
    :param application:
    :type application: str
    """

    _attribute_map = {
        'session': {'key': 'Session', 'type': 'str'},
        'continuation': {'key': 'Continuation', 'type': 'str'},
        'max_count': {'key': 'MaxCount', 'type': 'int'},
        'order_by': {'key': 'OrderBy', 'type': 'str'},
        'tags': {'key': 'Tags', 'type': '[PredictionQueryTag]'},
        'iteration_id': {'key': 'IterationId', 'type': 'str'},
        'start_time': {'key': 'StartTime', 'type': 'iso-8601'},
        'end_time': {'key': 'EndTime', 'type': 'iso-8601'},
        'application': {'key': 'Application', 'type': 'str'},
    }

    def __init__(self, session=None, continuation=None, max_count=None, order_by=None, tags=None, iteration_id=None, start_time=None, end_time=None, application=None):
        super(PredictionQueryToken, self).__init__()
        self.session = session
        self.continuation = continuation
        self.max_count = max_count
        self.order_by = order_by
        self.tags = tags
        self.iteration_id = iteration_id
        self.start_time = start_time
        self.end_time = end_time
        self.application = application