def ():
    '''returns OslcJSONStructureObject\n\n
    (final String operaton, final String osName, final String lang, final int size, final boolean isEvent, final boolean isResponse)\n
    (final Document input)\n
    (final JSONArtifact data, final String mosName, final String path, final String messageType, final UserInfo userInfo, final boolean leanJson)\n
    (final Element data)\n
    ()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getObjectPath():
    '''returns String\n\n
    getObjectPath()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def createChildrenData():
    '''returns None\n\n
    createChildrenData(final String name)\n
    '''
def getChildrenData():
    '''returns List\n\n
    getChildrenData(final String name)\n
    getChildrenData()\n
    '''
def hasDetailData():
    '''returns boolean\n\n
    hasDetailData(final String childPath)\n
    '''
def getChildrenKeys():
    '''returns Iterator\n\n
    getChildrenKeys()\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def isCurrentActionNull():
    '''returns boolean\n\n
    isCurrentActionNull()\n
    '''
def isHidden():
    '''returns boolean\n\n
    isHidden()\n
    '''
def getCurrentData():
    '''returns String\n\n
    getCurrentData()\n
    getCurrentData(final String col)\n
    '''
def getCurrentObject():
    '''returns StructureObject\n\n
    getCurrentObject()\n
    '''
def getParentData():
    '''returns String\n\n
    getParentData()\n
    getParentData(final String col)\n
    '''
def getParentJSONData():
    '''returns JSONObject\n\n
    getParentJSONData()\n
    '''
def getParentPath():
    '''returns String\n\n
    getParentPath()\n
    '''
def setParentJSONData():
    '''returns None\n\n
    setParentJSONData(final JSONObject parent, final String path)\n
    '''
def getAttr():
    '''returns String\n\n
    getAttr(final String col, final String attr)\n
    getAttr(final String attr)\n
    '''
def removeFromCurrentData():
    '''returns None\n\n
    removeFromCurrentData(final String col)\n
    '''
def removeChildData():
    '''returns None\n\n
    removeChildData(final String childName, final int index)\n
    '''
def removeChildren():
    '''returns None\n\n
    removeChildren(final String childName)\n
    '''
def getRowStamp():
    '''returns String\n\n
    getRowStamp()\n
    '''
def getCurrentDataAsBytes():
    '''returns byte[]\n\n
    getCurrentDataAsBytes(final String col)\n
    '''
def getCurrentDataAsBinaryText():
    '''returns String\n\n
    getCurrentDataAsBinaryText(final String col)\n
    '''
def isCurrentDataNull():
    '''returns boolean\n\n
    isCurrentDataNull(final String col)\n
    '''
def isGLDataNull():
    '''returns boolean\n\n
    isGLDataNull(final String col)\n
    isGLDataNull(final String col, final String orgId)\n
    '''
def isInCurrentData():
    '''returns boolean\n\n
    isInCurrentData(final String col)\n
    '''
def isCurrentDataChanged():
    '''returns boolean\n\n
    isCurrentDataChanged(final String col)\n
    '''
def getCurrentDataAsDouble():
    '''returns double\n\n
    getCurrentDataAsDouble(final String col)\n
    '''
def getCurrentDataAsInt():
    '''returns int\n\n
    getCurrentDataAsInt(final String col)\n
    '''
def getCurrentDataAsLong():
    '''returns long\n\n
    getCurrentDataAsLong(final String col)\n
    '''
def getCurrentDataAsDate():
    '''returns Date\n\n
    getCurrentDataAsDate(final String col)\n
    '''
def getCurrentDataAsBoolean():
    '''returns boolean\n\n
    getCurrentDataAsBoolean(final String col)\n
    '''
def getCurrentDataAsElement():
    '''returns Element\n\n
    getCurrentDataAsElement(final String key)\n
    '''
def getCurrentDataAsList():
    '''returns List\n\n
    getCurrentDataAsList(final String key)\n
    '''
def isCurrentDataObject():
    '''returns boolean\n\n
    isCurrentDataObject(final String col)\n
    '''
def getGL():
    '''returns String\n\n
    getGL(final String col)\n
    getGL(final String col, final String orgId)\n
    '''
def getGLComponent():
    '''returns String\n\n
    getGLComponent(final String col, final int order, final String orgId)\n
    '''
def getCurrentAction():
    '''returns String\n\n
    getCurrentAction()\n
    '''
def setCurrentData():
    '''returns None\n\n
    setCurrentData(final String colname, final String data)\n
    setCurrentData(final String colname, final Date data)\n
    setCurrentData(final String colname, final double data)\n
    setCurrentData(final String colname, final long data)\n
    setCurrentData(final String colname, final boolean data)\n
    setCurrentData(final String colname, final int data)\n
    setCurrentData(final String colname, final byte[] data)\n
    '''
def setCurrentAction():
    '''returns None\n\n
    setCurrentAction(final String action)\n
    '''
def setCurrentDataNull():
    '''returns None\n\n
    setCurrentDataNull(final String colname)\n
    '''
def setGL():
    '''returns None\n\n
    setGL(final String colname, final String[] glSegments, final String orgId)\n
    setGL(final String colname, final String glString)\n
    '''
def setXPathData():
    '''returns None\n\n
    setXPathData(final String xPathExpression, final String data)\n
    '''
def getCurrentDataAsString():
    '''returns String\n\n
    getCurrentDataAsString(final String col)\n
    '''
def getCurrentNamespacePrefix():
    '''returns String\n\n
    getCurrentNamespacePrefix()\n
    '''
def getCurrentNamespaceURI():
    '''returns String\n\n
    getCurrentNamespaceURI()\n
    '''
def setCurrentNamespace():
    '''returns None\n\n
    setCurrentNamespace(final String pref, final String uri)\n
    '''
def setNamespaces():
    '''returns None\n\n
    setNamespaces(final String key, final String data)\n
    '''
def getLocalRef():
    '''returns String\n\n
    getLocalRef()\n
    '''
def getOverrideType():
    '''returns int\n\n
    getOverrideType(final String col, final int currentType)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
