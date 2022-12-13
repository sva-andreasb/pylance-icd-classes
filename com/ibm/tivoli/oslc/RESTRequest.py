HTTP_GET = "String GET""
HTTP_POST = "String POST""
HTTP_PUT = "String PUT""
HTTP_DELETE = "String DELETE""
HTTP_PATCH = "String PATCH""
HTTP_HEAD = "String HEAD""
def RESTRequest():
'''public RESTRequest(final Map<String, List<String>> headers, final Map<String, String[]> queryParams, final String httpMethod, final String clientAddr, final String clientHost)
public RESTRequest(final HttpServletRequest request)
'''
pass
def getPrincipal():
'''public Principal getPrincipal()
'''
pass
def getHeaderParams():
'''public BaseHttpHeaders getHeaderParams()
'''
pass
def getHttpMethod():
'''public String getHttpMethod()
'''
pass
def getResponseFormat():
'''public String getResponseFormat()
'''
pass
def getRequestFormat():
'''public String getRequestFormat()
'''
pass
def getQueryParams():
'''public Map<String, String[]> getQueryParams()
'''
pass
def isPOST():
'''public boolean isPOST()
'''
pass
def isPUT():
'''public boolean isPUT()
'''
pass
def isDELETE():
'''public boolean isDELETE()
'''
pass
def isGET():
'''public boolean isGET()
'''
pass
def isPATCH():
'''public boolean isPATCH()
'''
pass
def isHEAD():
'''public boolean isHEAD()
'''
pass
def getResponseMIMEType():
'''public String getResponseMIMEType()
'''
pass
def getRequestMIMEType():
'''public String getRequestMIMEType()
'''
pass
def getQueryParam():
'''public String getQueryParam(final String param)
public String getQueryParam(final String param, final String def)
'''
pass
def getIntegerQueryParam():
'''public Integer getIntegerQueryParam(final String param)
'''
pass
def getBooleanQueryParam():
'''public Boolean getBooleanQueryParam(final String param, final boolean def)
'''
pass
def getClientAddr():
'''public String getClientAddr()
'''
pass
def getClientHost():
'''public String getClientHost()
'''
pass
