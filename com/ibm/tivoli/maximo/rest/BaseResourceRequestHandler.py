def ():
    '''returns BaseResourceRequestHandler\n\n
    ()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String mboName)\n
    '''
def lookup():
    '''returns ServiceRemote\n\n
    lookup(final String name)\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def setBlockAccessList():
    '''returns None\n\n
    setBlockAccessList(final Set<String> blockAccessList)\n
    '''
def isRequestNoCache():
    '''returns boolean\n\n
    isRequestNoCache(final ResourceRequest req)\n
    '''
def isUseCache():
    '''returns boolean\n\n
    isUseCache(final Resource res, final ResourceRequest req)\n
    '''
def isResourceModified():
    '''returns boolean\n\n
    isResourceModified(final Resource resource, final ResourceRequest request)\n
    '''
def setMXSession():
    '''returns None\n\n
    setMXSession(final MXSession mxSession, final UserInfo userInfo)\n
    '''
def setHandlerName():
    '''returns None\n\n
    setHandlerName(final String handlerName)\n
    '''
def getDelagateHandler():
    '''returns String\n\n
    getDelagateHandler(final String resourceType, final String resourceName)\n
    '''
def handleRequest():
    '''returns ResourceResponse\n\n
    handleRequest(final ResourceRequest req)\n
    '''
def isRoot():
    '''returns boolean\n\n
    isRoot()\n
    '''
def setRoot():
    '''returns None\n\n
    setRoot(final boolean rootHandler)\n
    '''
