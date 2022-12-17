CLUSTER_MEMBER_ATTR = "String  \"memberName\""
CLUSTER_NODE_ATTR = "String  \"nodeName\""
def ():
    '''returns ResourceValidationHelper\n\n
    (final String earFile, final String sessionId, final Hashtable prefs, final String operation, final boolean init)\n
    (final AppDeploymentController controller, final String sessionId, final String operation, final boolean init)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    init(final String operation)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getResourceJNDINames():
    '''returns List\n\n
    getResourceJNDINames(final String resType)\n
    '''
def getResourceObjectsWithRefKeys():
    '''returns Hashtable\n\n
    getResourceObjectsWithRefKeys(final String moduleUri, final String resType)\n
    '''
def taskResourceValidation():
    '''returns Hashtable\n\n
    taskResourceValidation(final String taskName)\n
    '''
def appResourceValidation():
    '''returns Vector\n\n
    appResourceValidation()\n
    '''
def getAppResourceObjects():
    '''returns Hashtable\n\n
    getAppResourceObjects()\n
    '''
def _getInAppRefObjects():
    '''returns Hashtable\n\n
    _getInAppRefObjects(final String uri)\n
    '''
def printValueTable():
    '''returns None\n\n
    printValueTable()\n
    '''
def printScopeTable():
    '''returns None\n\n
    printScopeTable()\n
    '''
def printAppTable():
    '''returns None\n\n
    printAppTable()\n
    '''
