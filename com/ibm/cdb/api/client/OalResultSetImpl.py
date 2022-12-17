def ():
    '''returns OalResultSetImpl\n\n
    (final String sessionId, final DataServerInterface api, final String query, final Guid mss, final String[] permissions)\n
    '''
def getXML():
    '''returns String\n\n
    getXML(final int depth)\n
    getXML(final int attributeIndex, final int depth)\n
    getXML(final String attributeName, final int depth)\n
    '''
def getString():
    '''returns String\n\n
    getString(final int attributeIndex)\n
    getString(final String attributeName)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final int attributeIndex)\n
    getLong(final String attributeName)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final int attributeIndex)\n
    getBoolean(final String attributeName)\n
    '''
def getModelObject():
    '''returns ModelObject\n\n
    getModelObject(final int depth)\n
    getModelObject(final int attributeIndex, final int depth)\n
    getModelObject(final String attributeName, final int depth)\n
    '''
def getMetaData():
    '''returns ObjectClass\n\n
    getMetaData()\n
    '''
def hasAttribute():
    '''returns boolean\n\n
    hasAttribute(final int attributeIndex)\n
    hasAttribute(final String attributeName)\n
    '''
def getResultMetaData():
    '''returns ResultMetaData\n\n
    getResultMetaData()\n
    '''
def next():
    '''returns boolean\n\n
    next()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setFetchSize():
    '''returns None\n\n
    setFetchSize(final int rows)\n
    '''
def getFetchSize():
    '''returns int\n\n
    getFetchSize()\n
    '''
def absolute():
    '''returns boolean\n\n
    absolute(final int index)\n
    '''
def first():
    '''returns boolean\n\n
    first()\n
    '''
def last():
    '''returns boolean\n\n
    last()\n
    '''
def getPosition():
    '''returns int\n\n
    getPosition()\n
    '''
def relative():
    '''returns boolean\n\n
    relative(final int index)\n
    '''
def previous():
    '''returns boolean\n\n
    previous()\n
    '''
def isFirst():
    '''returns boolean\n\n
    isFirst()\n
    '''
def isLast():
    '''returns boolean\n\n
    isLast()\n
    '''
def isBeforeFirst():
    '''returns boolean\n\n
    isBeforeFirst()\n
    '''
def isAfterLast():
    '''returns boolean\n\n
    isAfterLast()\n
    '''
