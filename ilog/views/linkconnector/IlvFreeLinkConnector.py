def ():
    '''returns IlvFreeLinkConnector\n\n
    ()\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvLinkImage ilvLinkImage, final boolean b)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    write(final IlvOutputStream ilvOutputStream, final IlvLinkImage key, final boolean b)\n
    '''
def detach():
    '''returns None\n\n
    detach(final boolean b)\n
    detach(final IlvLinkImage ilvLinkImage, final boolean b, final boolean b2)\n
    '''
def read():
    '''returns None\n\n
    read(final IlvInputStream ilvInputStream, final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def connectLink():
    '''returns None\n\n
    connectLink(final IlvLinkImage ilvLinkImage, final IlvPoint ilvPoint, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def disconnectLink():
    '''returns None\n\n
    disconnectLink(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def disconnectAllLinks():
    '''returns None\n\n
    disconnectAllLinks()\n
    '''
def allowsConnectionPointMove():
    '''returns boolean\n\n
    allowsConnectionPointMove(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def connectionPointMoveAllowed():
    '''returns None\n\n
    connectionPointMoveAllowed(final boolean c)\n
    '''
def getClosestConnectionPoint():
    '''returns IlvPoint\n\n
    getClosestConnectionPoint(final IlvPoint ilvPoint, final Object o, final Object o2, final Object o3, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def linkRemoved():
    '''returns None\n\n
    linkRemoved(final IlvLinkImage ilvLinkImage)\n
    '''
def getGhostBoundingBox():
    '''returns IlvRect\n\n
    getGhostBoundingBox(final IlvTransformer ilvTransformer)\n
    '''
