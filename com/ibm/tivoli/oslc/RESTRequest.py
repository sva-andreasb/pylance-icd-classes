HTTP_GET = "String  \"GET\""
HTTP_POST = "String  \"POST\""
HTTP_PUT = "String  \"PUT\""
HTTP_DELETE = "String  \"DELETE\""
HTTP_PATCH = "String  \"PATCH\""
HTTP_HEAD = "String  \"HEAD\""
def RESTRequest():
    '''public RESTRequest(final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost)
    public RESTRequest(final HttpServletRequest request)
    '''
def getPrincipal():
    '''public Principal getPrincipal()
    '''
def getHeaderParams():
    '''public BaseHttpHeaders getHeaderParams()
    '''
def getHttpMethod():
    '''public String getHttpMethod()
    '''
def getResponseFormat():
    '''public String getResponseFormat()
    '''
def getRequestFormat():
    '''public String getRequestFormat()
    '''
def getQueryParams():
    '''public Map<String, String[]> getQueryParams()
    '''
def isPOST():
    '''public boolean isPOST()
    '''
def isPUT():
    '''public boolean isPUT()
    '''
def isDELETE():
    '''public boolean isDELETE()
    '''
def isGET():
    '''public boolean isGET()
    '''
def isPATCH():
    '''public boolean isPATCH()
    '''
def isHEAD():
    '''public boolean isHEAD()
    '''
def getResponseMIMEType():
    '''public String getResponseMIMEType()
    '''
def getRequestMIMEType():
    '''public String getRequestMIMEType()
    '''
def getQueryParam():
    '''public String getQueryParam(final String param)
    public String getQueryParam(final String param, final String def)
    '''
def getIntegerQueryParam():
    '''public Integer getIntegerQueryParam(final String param)
    '''
def getBooleanQueryParam():
    '''public Boolean getBooleanQueryParam(final String param, final boolean def)
    '''
def getClientAddr():
    '''public String getClientAddr()
    '''
def getClientHost():
    '''public String getClientHost()
    '''
