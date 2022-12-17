def ():
    '''returns IlvCachingLinkConnector\n\n
    ()\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvLinkImage ilvLinkImage, final boolean b)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setCacheSize():
    '''returns None\n\n
    setCacheSize(int d)\n
    '''
def getCacheSize():
    '''returns int\n\n
    getCacheSize()\n
    '''
def getConnectionPoint():
    '''returns IlvPoint\n\n
    getConnectionPoint(final IlvLinkImage ilvLinkImage, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def detach():
    '''returns None\n\n
    detach(final boolean b)\n
    detach(final IlvLinkImage ilvLinkImage, final boolean b, final boolean b2)\n
    '''
def linkRemoved():
    '''returns None\n\n
    linkRemoved(final IlvLinkImage ilvLinkImage)\n
    '''
def disconnectLink():
    '''returns None\n\n
    disconnectLink(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def disconnectAllLinks():
    '''returns None\n\n
    disconnectAllLinks()\n
    '''
def linkChanged():
    '''returns None\n\n
    linkChanged(final IlvLinkImage ilvLinkImage)\n
    '''
