def getHeader():
    '''    public String getHeader(final String header)
    '''
def getHttpResponse():
    '''    public HttpResponse getHttpResponse()
    '''
def getCurrentDepth():
    '''    public int getCurrentDepth()
    '''
def readText():
    '''    public String readText()
    '''
def isStartOfDocument():
    '''    public boolean isStartOfDocument()
    '''
def testExpression():
    '''    public boolean testExpression(final String expression)
    public boolean testExpression(final String expression, final int stackDepth)
    '''
def getCurrentParentElement():
    '''    public String getCurrentParentElement()
    '''
def nextToken():
    '''    public JsonToken nextToken()
    '''
def peek():
    '''    public JsonToken peek()
    '''
def getJsonParser():
    '''    public JsonParser getJsonParser()
    '''
def getMetadata():
    '''    public Map<String, String> getMetadata()
    '''
def registerMetadataExpression():
    '''    public void registerMetadataExpression(final String expression, final int targetDepth, final String storageKey)
    '''
def setCurrentHeader():
    '''    public void setCurrentHeader(final String currentHeader)
    '''
def getCurrentToken():
    '''    public JsonToken getCurrentToken()
    '''
def getLastParsedParentElement():
    '''    public String getLastParsedParentElement()
    '''
def isInsideResponseHeader():
    '''    public boolean isInsideResponseHeader()
    '''
def getUnmarshaller():
    '''    public <T> Unmarshaller<T, JsonUnmarshallerContext> getUnmarshaller(final Class<T> type)
    '''
