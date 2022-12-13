def HttpRoute():
    '''    public HttpRoute(final HttpHost target, final InetAddress local, final HttpHost[] proxies, final boolean secure, final TunnelType tunnelled, final LayerType layered)
    public HttpRoute(final HttpHost target, final InetAddress local, final HttpHost proxy, final boolean secure, final TunnelType tunnelled, final LayerType layered)
    public HttpRoute(final HttpHost target, final InetAddress local, final boolean secure)
    public HttpRoute(final HttpHost target)
    public HttpRoute(final HttpHost target, final InetAddress local, final HttpHost proxy, final boolean secure)
    public HttpRoute(final HttpHost target, final HttpHost proxy)
    '''
def getTargetHost():
    '''    public final HttpHost getTargetHost()
    '''
def getLocalAddress():
    '''    public final InetAddress getLocalAddress()
    '''
def getLocalSocketAddress():
    '''    public final InetSocketAddress getLocalSocketAddress()
    '''
def getHopCount():
    '''    public final int getHopCount()
    '''
def getHopTarget():
    '''    public final HttpHost getHopTarget(final int hop)
    '''
def getProxyHost():
    '''    public final HttpHost getProxyHost()
    '''
def getTunnelType():
    '''    public final TunnelType getTunnelType()
    '''
def isTunnelled():
    '''    public final boolean isTunnelled()
    '''
def getLayerType():
    '''    public final LayerType getLayerType()
    '''
def isLayered():
    '''    public final boolean isLayered()
    '''
def isSecure():
    '''    public final boolean isSecure()
    '''
def equals():
    '''    public final boolean equals(final Object obj)
    '''
def hashCode():
    '''    public final int hashCode()
    '''
def toString():
    '''    public final String toString()
    '''
def clone():
    '''    public Object clone()
    '''
