def ():
    '''returns AbstractRouteHandler\n\n
    ()\n
    '''
def setRouteInfo():
    '''returns None\n\n
    setRouteInfo(final RouteInfo routeInfo)\n
    '''
def setMethod():
    '''returns None\n\n
    setMethod(final String method)\n
    '''
def authenticateRequest():
    '''returns MXSession\n\n
    authenticateRequest(final OslcRequest request)\n
    '''
def setAuthHandler():
    '''returns None\n\n
    setAuthHandler(final MaximoAuthenticator maxAuthHandler)\n
    '''
def setResReqPath():
    '''returns None\n\n
    setResReqPath(final String resourceReq)\n
    '''
def setPathTokens():
    '''returns None\n\n
    setPathTokens(final List<String> pathTokens)\n
    '''
def getProvider():
    '''returns String\n\n
    getProvider()\n
    '''
def setLogger():
    '''returns None\n\n
    setLogger(final MXLogger logger)\n
    '''
def setCorrelator():
    '''returns None\n\n
    setCorrelator(final MXCorrelator correlator)\n
    '''
def getPathTokenAllowedValuesMeta():
    '''returns Set<String>\n\n
    getPathTokenAllowedValuesMeta(final String token)\n
    '''
def getQueryParamsMeta():
    '''returns List<QueryParamsInfo>\n\n
    getQueryParamsMeta(final String path)\n
    '''
def getQueryParamAllowedValuesMeta():
    '''returns Set<String>\n\n
    getQueryParamAllowedValuesMeta(final String qparam)\n
    '''
def setRequestData():
    '''returns None\n\n
    setRequestData(final byte[] resourceBytes)\n
    '''
def isPathTokensOptional():
    '''returns boolean\n\n
    isPathTokensOptional()\n
    '''
