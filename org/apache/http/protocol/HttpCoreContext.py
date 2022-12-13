HTTP_CONNECTION = "String  \"http.connection\""
HTTP_REQUEST = "String  \"http.request\""
HTTP_RESPONSE = "String  \"http.response\""
HTTP_TARGET_HOST = "String  \"http.target_host\""
HTTP_REQ_SENT = "String  \"http.request_sent\""
def create():
    '''    public static HttpCoreContext create()
    '''
def adapt():
    '''    public static HttpCoreContext adapt(final HttpContext context)
    '''
def HttpCoreContext():
    '''    public HttpCoreContext(final HttpContext context)
    public HttpCoreContext()
    '''
def getAttribute():
    '''    public Object getAttribute(final String id)
    public <T> T getAttribute(final String attribname, final Class<T> clazz)
    '''
def setAttribute():
    '''    public void setAttribute(final String id, final Object obj)
    '''
def removeAttribute():
    '''    public Object removeAttribute(final String id)
    '''
def getConnection():
    '''    public <T extends HttpConnection> T getConnection(final Class<T> clazz)
    public HttpConnection getConnection()
    '''
def getRequest():
    '''    public HttpRequest getRequest()
    '''
def isRequestSent():
    '''    public boolean isRequestSent()
    '''
def getResponse():
    '''    public HttpResponse getResponse()
    '''
def setTargetHost():
    '''    public void setTargetHost(final HttpHost host)
    '''
def getTargetHost():
    '''    public HttpHost getTargetHost()
    '''
