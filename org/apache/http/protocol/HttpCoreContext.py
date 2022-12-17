HTTP_CONNECTION = "String  \"http.connection\""
HTTP_REQUEST = "String  \"http.request\""
HTTP_RESPONSE = "String  \"http.response\""
HTTP_TARGET_HOST = "String  \"http.target_host\""
HTTP_REQ_SENT = "String  \"http.request_sent\""
def ():
    '''returns HttpCoreContext\n\n
    (final HttpContext context)\n
    ()\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String id)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String id, final Object obj)\n
    '''
def removeAttribute():
    '''returns Object\n\n
    removeAttribute(final String id)\n
    '''
def getConnection():
    '''returns HttpConnection\n\n
    getConnection()\n
    '''
def getRequest():
    '''returns HttpRequest\n\n
    getRequest()\n
    '''
def isRequestSent():
    '''returns boolean\n\n
    isRequestSent()\n
    '''
def getResponse():
    '''returns HttpResponse\n\n
    getResponse()\n
    '''
def setTargetHost():
    '''returns None\n\n
    setTargetHost(final HttpHost host)\n
    '''
def getTargetHost():
    '''returns HttpHost\n\n
    getTargetHost()\n
    '''
