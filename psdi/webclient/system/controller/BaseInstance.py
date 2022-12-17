EXCEPTION_NONE = "int  -1"
EXCEPTION_WARNING = "int  0"
EXCEPTION_REQUIREDFIELD = "int  1"
EXCEPTION_YESNOCANCEL = "int  2"
EXCEPTION_ERROR = "int  3"
EXCEPTION_SMARTFILL = "int  4"
EXCEPTION_INFO = "int  5"
NO_PROMPT_WITH_WARNING = "int  0"
PROMPT_WHEN_WARNING_EXIST = "int  1"
FORCE_WARNING_HANDLING = "int  2"
def ():
    '''returns BaseInstance\n\n
    ()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getSafeId():
    '''returns String\n\n
    getSafeId()\n
    '''
def setRenderId():
    '''returns None\n\n
    setRenderId(final String id)\n
    '''
def getRenderId():
    '''returns String\n\n
    getRenderId()\n
    '''
def setWebClientSession():
    '''returns None\n\n
    setWebClientSession(final WebClientSession wcs)\n
    '''
def getWebClientSession():
    '''returns WebClientSession\n\n
    getWebClientSession()\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final BaseInstance child)\n
    addChild(final BaseInstance child, final int index)\n
    '''
def getChildren():
    '''returns List<BaseInstance>\n\n
    getChildren()\n
    '''
def clearChildren():
    '''returns None\n\n
    clearChildren()\n
    '''
def getParentInstance():
    '''returns BaseInstance\n\n
    getParentInstance()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final BaseInstance parent)\n
    '''
def hasLocalProperty():
    '''returns boolean\n\n
    hasLocalProperty(final String key)\n
    '''
def isOnTableRow():
    '''returns boolean\n\n
    isOnTableRow()\n
    '''
def getRowNum():
    '''returns String\n\n
    getRowNum()\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String key)\n
    '''
def initProperty():
    '''returns None\n\n
    initProperty()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String key, final String value, final boolean systemCheck, final boolean showWarnings)\n
    setProperty(final String key, final String value)\n
    '''
def removeProperty():
    '''returns None\n\n
    removeProperty(final String key)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String key)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String property)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String property, final int defaultValue)\n
    '''
def getParent():
    '''returns ControlHandler\n\n
    getParent()\n
    '''
def handleEvent():
    '''returns int\n\n
    handleEvent(final WebClientEvent event)\n
    handleEvent(final String methodName, final WebClientEvent event)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def getDescriptor():
    '''returns BaseDescriptor\n\n
    getDescriptor()\n
    '''
def setDescriptor():
    '''returns None\n\n
    setDescriptor(final BaseDescriptor descriptor)\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getLocalizedType():
    '''returns String\n\n
    getLocalizedType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final String type)\n
    '''
def getChildCount():
    '''returns int\n\n
    getChildCount()\n
    '''
def setConsiderInDesigner():
    '''returns None\n\n
    setConsiderInDesigner(final boolean flag)\n
    '''
def getConsiderInDesigner():
    '''returns boolean\n\n
    getConsiderInDesigner()\n
    '''
def clearProperties():
    '''returns None\n\n
    clearProperties()\n
    '''
def clone():
    '''returns Object\n\n
    clone(final String newId)\n
    clone(final String newId, final String childIdAppend)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def hasPropertyChanged():
    '''returns boolean\n\n
    hasPropertyChanged(final String property)\n
    '''
def hasAnyPropertyChanged():
    '''returns boolean\n\n
    hasAnyPropertyChanged()\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def getPage():
    '''returns PageInstance\n\n
    getPage()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addRefreshListener():
    '''returns None\n\n
    addRefreshListener(final String componentId)\n
    '''
def isDynamicContainer():
    '''returns boolean\n\n
    isDynamicContainer()\n
    '''
def getRefreshListeners():
    '''returns String\n\n
    getRefreshListeners()\n
    '''
def setDynamicContainer():
    '''returns None\n\n
    setDynamicContainer(final boolean isDynamic)\n
    '''
def maintainControlId():
    '''returns boolean\n\n
    maintainControlId()\n
    '''
def getChildIndex():
    '''returns int\n\n
    getChildIndex()\n
    '''
def getIdExtension():
    '''returns String\n\n
    getIdExtension()\n
    '''
def setOnTable():
    '''returns None\n\n
    setOnTable(final boolean isOnTable)\n
    '''
def isOnTable():
    '''returns boolean\n\n
    isOnTable()\n
    '''
