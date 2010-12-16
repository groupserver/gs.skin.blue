# coding=utf-8
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.app.rotterdam import Rotterdam

# Layers just inherit from IBrowserRequest.
class IGSBlueLayer(IBrowserRequest):
    '''GroupServer Blue Layer'''
# Skins inherit from a bunch of layers. In this case the blue layer
# and the core Zope Rotterdam layer.
class IGSBlueSkin(IGSBlueLayer, Rotterdam):
    '''GroupServer Blue Skin'''

