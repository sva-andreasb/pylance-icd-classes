REQUEST_TYPE = "String  \"lightselect\""
def getLastSelectedObject():
    '''returns Object\n\n
    getLastSelectedObject(final ServletContext servletContext, final Object key)\n
    '''
def setLastSelectedObject():
    '''returns None\n\n
    setLastSelectedObject(final ServletContext servletContext, final Object key, final Object value)\n
    '''
def handleRequest():
    '''returns boolean\n\n
    handleRequest(final HttpServletRequest httpServletRequest, final HttpServletResponse httpServletResponse)\n
    '''
def ():
    '''returns IlvSelectionResponse\n\n
    (final HttpServletRequest h, final HttpServletResponse i)\n
    '''
def getHttpRequest():
    '''returns HttpServletRequest\n\n
    getHttpRequest()\n
    '''
def getHttpResponse():
    '''returns HttpServletResponse\n\n
    getHttpResponse()\n
    '''
def putProperty():
    '''returns None\n\n
    putProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def isNoSelection():
    '''returns boolean\n\n
    isNoSelection()\n
    '''
def setNoSelection():
    '''returns None\n\n
    setNoSelection(final boolean b)\n
    '''
def isRemoveAll():
    '''returns boolean\n\n
    isRemoveAll()\n
    '''
def setRemoveAll():
    '''returns None\n\n
    setRemoveAll(final boolean a)\n
    '''
def isImageRefresh():
    '''returns boolean\n\n
    isImageRefresh()\n
    '''
def setImageRefresh():
    '''returns None\n\n
    setImageRefresh(final boolean g)\n
    '''
def getAddList():
    '''returns List\n\n
    getAddList()\n
    '''
def getRemoveList():
    '''returns List\n\n
    getRemoveList()\n
    '''
def getUpdatedCapablities():
    '''returns Map\n\n
    getUpdatedCapablities()\n
    '''
def addToSelection():
    '''returns None\n\n
    addToSelection(final Rectangle rectangle, final List list)\n
    addToSelection(final Rectangle rectangle, final List list, final Point2D.Float[] array)\n
    '''
def addAllToSelection():
    '''returns None\n\n
    addAllToSelection(final List list)\n
    '''
def removeToSelection():
    '''returns None\n\n
    removeToSelection(final Rectangle rectangle, final List list)\n
    '''
def removeFromSelection():
    '''returns None\n\n
    removeFromSelection(final Rectangle rectangle, final List list)\n
    removeFromSelection(final Rectangle rectangle, final List list, final Point2D.Float[] array)\n
    '''
def removeAllToSelection():
    '''returns None\n\n
    removeAllToSelection(final List list)\n
    '''
def removeAllFromSelection():
    '''returns None\n\n
    removeAllFromSelection(final List list)\n
    '''
def addUpdatedCapability():
    '''returns None\n\n
    addUpdatedCapability(final String s, final Object o)\n
    addUpdatedCapability(final String s, final String s2, final boolean b)\n
    addUpdatedCapability(final String s, final String s2)\n
    addUpdatedCapability(final String s, final int i)\n
    addUpdatedCapability(final String s, final float f)\n
    '''
