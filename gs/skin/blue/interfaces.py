# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.rotterdam import Rotterdam


class IGSBlueLayer(IBrowserRequest):
    '''GroupServer Blue Layer'''
    # Layers just inherit from IBrowserRequest.


class IGSBlueSkin(IGSBlueLayer, Rotterdam):
    '''GroupServer Blue Skin'''
    # Skins inherit from a bunch of layers. In this case the blue layer
    # and the core Zope Rotterdam layer.
