# -*- coding: utf-8 -*-
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.rotterdam import Rotterdam


class IGSBlueLayer(IBrowserRequest):
    '''GroupServer Blue Layer'''
    # Layers just inherit from IBrowserRequest.


class IGSBlueSkin(IGSBlueLayer, Rotterdam):
    '''GroupServer Blue Skin'''
    # Skins inherit from a bunch of layers. In this case the blue layer
    # and the core Zope Rotterdam layer.
