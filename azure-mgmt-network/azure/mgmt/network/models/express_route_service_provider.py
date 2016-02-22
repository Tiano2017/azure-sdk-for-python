# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class ExpressRouteServiceProvider(Resource):
    """
    ExpressRouteResourceProvider object

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    :param list peering_locations: Gets or list of peering locations
    :param list bandwidths_offered: Gets or bandwidths offered
    :param str provisioning_state: Gets or sets Provisioning state of the
     resource
    """

    _required = []

    _attribute_map = {
        'peering_locations': {'key': 'properties.peeringLocations', 'type': '[str]', 'flatten': True},
        'bandwidths_offered': {'key': 'properties.bandwidthsOffered', 'type': '[ExpressRouteServiceProviderBandwidthsOffered]', 'flatten': True},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str', 'flatten': True},
    }

    def __init__(self, id=None, name=None, type=None, location=None, tags=None, peering_locations=None, bandwidths_offered=None, provisioning_state=None):
        super(ExpressRouteServiceProvider, self).__init__(id=id, name=name, type=type, location=location, tags=tags)
        self.peering_locations = peering_locations
        self.bandwidths_offered = bandwidths_offered
        self.provisioning_state = provisioning_state