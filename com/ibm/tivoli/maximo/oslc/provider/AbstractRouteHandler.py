def AbstractRouteHandler():
    '''    public AbstractRouteHandler()
    '''
def setRouteInfo():
    '''    public void setRouteInfo(final RouteInfo routeInfo)
    '''
def setMethod():
    '''    public void setMethod(final String method)
    '''
def authenticateRequest():
    '''    public MXSession authenticateRequest(final OslcRequest request)
    '''
def setAuthHandler():
    '''    public void setAuthHandler(final MaximoAuthenticator maxAuthHandler)
    '''
def setResReqPath():
    '''    public void setResReqPath(final String resourceReq)
    '''
def setPathTokens():
    '''    public void setPathTokens(final List<String> pathTokens)
    '''
def getProvider():
    '''    public String getProvider()
    '''
def setLogger():
    '''    public void setLogger(final MXLogger logger)
    '''
def setCorrelator():
    '''    public void setCorrelator(final MXCorrelator correlator)
    '''
def getPathTokensMeta():
    '''    public Map<String, String> getPathTokensMeta()
    '''
def getPathTokenAllowedValuesMeta():
    '''    public Set<String> getPathTokenAllowedValuesMeta(final String token)
    '''
def getQueryParamsMeta():
    '''    public Map<String, String> getQueryParamsMeta()
    public List<QueryParamsInfo> getQueryParamsMeta(final String path)
    '''
def getQueryParamAllowedValuesMeta():
    '''    public Set<String> getQueryParamAllowedValuesMeta(final String qparam)
    '''
def setRequestData():
    '''    public void setRequestData(final byte[] resourceBytes)
    '''
def isPathTokensOptional():
    '''    public boolean isPathTokensOptional()
    '''
