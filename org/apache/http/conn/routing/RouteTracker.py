def RouteTracker():
    '''public RouteTracker(final HttpHost target, final InetAddress local)
    public RouteTracker(final HttpRoute route)
    '''
def reset():
    '''public void reset()
    '''
def connectTarget():
    '''public final void connectTarget(final boolean secure)
    '''
def connectProxy():
    '''public final void connectProxy(final HttpHost proxy, final boolean secure)
    '''
def tunnelTarget():
    '''public final void tunnelTarget(final boolean secure)
    '''
def tunnelProxy():
    '''public final void tunnelProxy(final HttpHost proxy, final boolean secure)
    '''
def layerProtocol():
    '''public final void layerProtocol(final boolean secure)
    '''
def getTargetHost():
    '''public final HttpHost getTargetHost()
    '''
def getLocalAddress():
    '''public final InetAddress getLocalAddress()
    '''
def getHopCount():
    '''public final int getHopCount()
    '''
def getHopTarget():
    '''public final HttpHost getHopTarget(final int hop)
    '''
def getProxyHost():
    '''public final HttpHost getProxyHost()
    '''
def isConnected():
    '''public final boolean isConnected()
    '''
def getTunnelType():
    '''public final TunnelType getTunnelType()
    '''
def isTunnelled():
    '''public final boolean isTunnelled()
    '''
def getLayerType():
    '''public final LayerType getLayerType()
    '''
def isLayered():
    '''public final boolean isLayered()
    '''
def isSecure():
    '''public final boolean isSecure()
    '''
def toRoute():
    '''public final HttpRoute toRoute()
    '''
def equals():
    '''public final boolean equals(final Object o)
    '''
def hashCode():
    '''public final int hashCode()
    '''
def toString():
    '''public final String toString()
    '''
def clone():
    '''public Object clone()
    '''
