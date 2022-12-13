HTTP_CONNECTION = "String  http.connection""
HTTP_REQUEST = "String  http.request""
HTTP_RESPONSE = "String  http.response""
HTTP_TARGET_HOST = "String  http.target_host""
HTTP_REQ_SENT = "String  http.request_sent""
def create():
'''public static HttpCoreContext create()
'''
pass
def adapt():
'''public static HttpCoreContext adapt(final HttpContext context)
'''
pass
def HttpCoreContext():
'''public HttpCoreContext(final HttpContext context)
public HttpCoreContext()
'''
pass
def getAttribute():
'''public Object getAttribute(final String id)
public <T> T getAttribute(final String attribname, final Class<T> clazz)
'''
pass
def setAttribute():
'''public void setAttribute(final String id, final Object obj)
'''
pass
def removeAttribute():
'''public Object removeAttribute(final String id)
'''
pass
def getConnection():
'''public <T extends HttpConnection> T getConnection(final Class<T> clazz)
public HttpConnection getConnection()
'''
pass
def getRequest():
'''public HttpRequest getRequest()
'''
pass
def isRequestSent():
'''public boolean isRequestSent()
'''
pass
def getResponse():
'''public HttpResponse getResponse()
'''
pass
def setTargetHost():
'''public void setTargetHost(final HttpHost host)
'''
pass
def getTargetHost():
'''public HttpHost getTargetHost()
'''
pass
