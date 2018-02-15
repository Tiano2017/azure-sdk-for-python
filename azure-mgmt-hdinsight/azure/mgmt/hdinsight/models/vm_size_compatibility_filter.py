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


class VmSizeCompatibilityFilter(Model):
    """The virtual machine type compatibility filter.

    :param filter_mode: The mode for the filter.
    :type filter_mode: str
    :param regions: The list of regions.
    :type regions: list[str]
    :param cluster_flavors: The list of cluster types available.
    :type cluster_flavors: list[str]
    :param node_types: The list of node types.
    :type node_types: list[str]
    :param cluster_versions: The list of cluster versions.
    :type cluster_versions: list[str]
    :param vmsizes: The list of virtual machine sizes.
    :type vmsizes: list[str]
    """

    _attribute_map = {
        'filter_mode': {'key': 'FilterMode', 'type': 'str'},
        'regions': {'key': 'Regions', 'type': '[str]'},
        'cluster_flavors': {'key': 'ClusterFlavors', 'type': '[str]'},
        'node_types': {'key': 'NodeTypes', 'type': '[str]'},
        'cluster_versions': {'key': 'ClusterVersions', 'type': '[str]'},
        'vmsizes': {'key': 'vmsizes', 'type': '[str]'},
    }

    def __init__(self, filter_mode=None, regions=None, cluster_flavors=None, node_types=None, cluster_versions=None, vmsizes=None):
        super(VmSizeCompatibilityFilter, self).__init__()
        self.filter_mode = filter_mode
        self.regions = regions
        self.cluster_flavors = cluster_flavors
        self.node_types = node_types
        self.cluster_versions = cluster_versions
        self.vmsizes = vmsizes