HTTP_GET = "String  \"GET\""
HTTP_POST = "String  \"POST\""
HTTP_PUT = "String  \"PUT\""
HTTP_DELETE = "String  \"DELETE\""
HTTP_PATCH = "String  \"PATCH\""
HTTP_HEAD = "String  \"HEAD\""
def ():
    '''returns RESTRequest\n\n
    (final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost)\n
    (final HttpServletRequest request)\n
    '''
def getPrincipal():
    '''returns Principal\n\n
    getPrincipal()\n
    '''
def getHeaderParams():
    '''returns BaseHttpHeaders\n\n
    getHeaderParams()\n
    '''
def getHttpMethod():
    '''returns String\n\n
    getHttpMethod()\n
    '''
def getResponseFormat():
    '''returns String\n\n
    getResponseFormat()\n
    '''
def getRequestFormat():
    '''returns String\n\n
    getRequestFormat()\n
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
def isPATCH():
    '''returns boolean\n\n
    isPATCH()\n
    '''
def isHEAD():
    '''returns boolean\n\n
    isHEAD()\n
    '''
def getResponseMIMEType():
    '''returns String\n\n
    getResponseMIMEType()\n
    '''
def getRequestMIMEType():
    '''returns String\n\n
    getRequestMIMEType()\n
    '''
def getQueryParam():
    '''returns String\n\n
    getQueryParam(final String param)\n
    getQueryParam(final String param, final String def)\n
    '''
def getIntegerQueryParam():
    '''returns Integer\n\n
    getIntegerQueryParam(final String param)\n
    '''
def getBooleanQueryParam():
    '''returns Boolean\n\n
    getBooleanQueryParam(final String param, final boolean def)\n
    '''
def getClientAddr():
    '''returns String\n\n
    getClientAddr()\n
    '''
def getClientHost():
    '''returns String\n\n
    getClientHost()\n
    '''
