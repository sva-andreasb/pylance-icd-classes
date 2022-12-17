def ():
    '''returns IlvGrapher\n\n
    ()\n
    (final int n)\n
    (final int n, final int n2)\n
    (final IlvInputStream ilvInputStream)\n
    (final IlvGrapher ilvGrapher)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def writePrefix():
    '''returns None\n\n
    writePrefix(final IlvOutputStream ilvOutputStream, final boolean b)\n
    '''
def writeSuffix():
    '''returns None\n\n
    writeSuffix(final IlvOutputStream ilvOutputStream, final boolean b)\n
    '''
def readPrefix():
    '''returns None\n\n
    readPrefix(final IlvInputStream ilvInputStream, final boolean b)\n
    '''
def readSuffix():
    '''returns None\n\n
    readSuffix(final IlvInputStream ilvInputStream, final boolean b)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic obj, final int n, final boolean b)\n
    '''
def addNode():
    '''returns None\n\n
    addNode(final IlvGraphic ilvGraphic, final boolean b)\n
    addNode(final IlvGraphic ilvGraphic, final int n, final boolean b)\n
    '''
def addLink():
    '''returns None\n\n
    addLink(final IlvLinkImage ilvLinkImage, final boolean b)\n
    addLink(final IlvLinkImage ilvLinkImage, final int n, final boolean b)\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    hasMoreElements()\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns IlvGraphic\n\n
    nextElement()\n
    nextElement()\n
    nextElement()\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def removeLink():
    '''returns None\n\n
    removeLink(final IlvLinkImage obj, final boolean b)\n
    '''
def removeNode():
    '''returns None\n\n
    removeNode(final IlvGraphic obj, final boolean b)\n
    '''
def setLayer():
    '''returns None\n\n
    setLayer(final IlvGraphic ilvGraphic, final int n, final boolean b)\n
    '''
def replaceObject():
    '''returns None\n\n
    replaceObject(final IlvGraphic obj, final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def makeNode():
    '''returns None\n\n
    makeNode(final IlvGraphic ilvGraphic)\n
    '''
def unmakeNode():
    '''returns None\n\n
    unmakeNode(final IlvGraphic obj)\n
    '''
def getSelectedMovingObjects():
    '''returns IlvGraphicEnumeration\n\n
    getSelectedMovingObjects(final boolean[] array)\n
    '''
def setCrossingAwareLinksFrozen():
    '''returns None\n\n
    setCrossingAwareLinksFrozen(final boolean f)\n
    '''
def isCrossingAwareLinksFrozen():
    '''returns boolean\n\n
    isCrossingAwareLinksFrozen()\n
    '''
def setVisibleBranch():
    '''returns None\n\n
    setVisibleBranch(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)\n
    setVisibleBranch(final IlvGraphic ilvGraphic, final int n, final boolean b, final boolean b2)\n
    setVisibleBranch(final IlvGraphic ilvGraphic, final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4)\n
    '''
