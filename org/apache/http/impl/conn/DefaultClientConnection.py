def DefaultClientConnection():
    '''    public DefaultClientConnection()
    '''
def getId():
    '''    public String getId()
    '''
def getTargetHost():
    '''    public final HttpHost getTargetHost()
    '''
def isSecure():
    '''    public final boolean isSecure()
    '''
def getSocket():
    '''    public final Socket getSocket()
    '''
def getSSLSession():
    '''    public SSLSession getSSLSession()
    '''
def opening():
    '''    public void opening(final Socket sock, final HttpHost target)
    '''
def openCompleted():
    '''    public void openCompleted(final boolean secure, final HttpParams params)
    '''
def shutdown():
    '''    public void shutdown()
    '''
def close():
    '''    public void close()
    '''
def bind():
    '''    public void bind(final Socket socket)
    '''
def update():
    '''    public void update(final Socket sock, final HttpHost target, final boolean secure, final HttpParams params)
    '''
def receiveResponseHeader():
    '''    public HttpResponse receiveResponseHeader()
    '''
def sendRequestHeader():
    '''    public void sendRequestHeader(final HttpRequest request)
    '''
def getAttribute():
    '''    public Object getAttribute(final String id)
    '''
def removeAttribute():
    '''    public Object removeAttribute(final String id)
    '''
def setAttribute():
    '''    public void setAttribute(final String id, final Object obj)
    '''
