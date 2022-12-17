HTTP_GET = "String  \"GET\""
HTTP_POST = "String  \"POST\""
HTTP_PUT = "String  \"PUT\""
HTTP_DELETE = "String  \"DELETE\""
def ():
    '''returns ResourceRequest\n\n
    (final String resourceType, final List<String> resourcePath, final Map<String, String[]> queryParams, final HttpHeaders headerParams, final RESTSession session, final String httpMethod, final String format, final String reqURL)\n
    (final ResourceRequest req)\n
    '''
def isReleaseResourceRequest():
    '''returns boolean\n\n
    isReleaseResourceRequest()\n
    '''
def isUseSessionForCollection():
    '''returns boolean\n\n
    isUseSessionForCollection()\n
    '''
def getResourceLocatorId():
    '''returns String\n\n
    getResourceLocatorId()\n
    '''
def getRequestURL():
    '''returns String\n\n
    getRequestURL()\n
    '''
def getResourceType():
    '''returns String\n\n
    getResourceType()\n
    '''
def getFormat():
    '''returns String\n\n
    getFormat()\n
    '''
def isUseLocationForCreate():
    '''returns boolean\n\n
    isUseLocationForCreate()\n
    '''
def getResourcePath():
    '''returns List<String>\n\n
    getResourcePath()\n
    '''
def getHeaderParams():
    '''returns HttpHeaders\n\n
    getHeaderParams()\n
    '''
def getSession():
    '''returns RESTSession\n\n
    getSession()\n
    '''
def getHttpMethod():
    '''returns String\n\n
    getHttpMethod()\n
    '''
def isPOST():
    '''returns boolean\n\n
    isPOST()\n
    '''
def isPUT():
    '''returns boolean\n\n
    isPUT()\n
    '''
def isDELETE():
    '''returns boolean\n\n
    isDELETE()\n
    '''
def isGET():
    '''returns boolean\n\n
    isGET()\n
    '''
def setClientAddr():
    '''returns None\n\n
    setClientAddr(final String remoteAddr)\n
    '''
def getClientAddr():
    '''returns String\n\n
    getClientAddr()\n
    '''
def setClientHost():
    '''returns None\n\n
    setClientHost(final String remoteHost)\n
    '''
def getClientHost():
    '''returns String\n\n
    getClientHost()\n
    '''
def getMXSession():
    '''returns MXSession\n\n
    getMXSession()\n
    '''
def getApiKey():
    '''returns String\n\n
    getApiKey()\n
    '''
def getQueryParam():
    '''returns String\n\n
    getQueryParam(final String param)\n
    '''
def isApiCall():
    '''returns boolean\n\n
    isApiCall()\n
    '''
def isEnableSession():
    '''returns boolean\n\n
    isEnableSession()\n
    '''
def setProcessUserInfo():
    '''returns None\n\n
    setProcessUserInfo(final UserInfo userInfo)\n
    '''
def getProcessUserInfo():
    '''returns UserInfo\n\n
    getProcessUserInfo()\n
    '''
