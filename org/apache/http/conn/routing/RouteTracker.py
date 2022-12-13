def RouteTracker():
'''public RouteTracker(final HttpHost target, final InetAddress local)
public RouteTracker(final HttpRoute route)
'''
pass
def reset():
'''public void reset()
'''
pass
def connectTarget():
'''public final void connectTarget(final boolean secure)
'''
pass
def connectProxy():
'''public final void connectProxy(final HttpHost proxy, final boolean secure)
'''
pass
def tunnelTarget():
'''public final void tunnelTarget(final boolean secure)
'''
pass
def tunnelProxy():
'''public final void tunnelProxy(final HttpHost proxy, final boolean secure)
'''
pass
def layerProtocol():
'''public final void layerProtocol(final boolean secure)
'''
pass
def getTargetHost():
'''public final HttpHost getTargetHost()
'''
pass
def getLocalAddress():
'''public final InetAddress getLocalAddress()
'''
pass
def getHopCount():
'''public final int getHopCount()
'''
pass
def getHopTarget():
'''public final HttpHost getHopTarget(final int hop)
'''
pass
def getProxyHost():
'''public final HttpHost getProxyHost()
'''
pass
def isConnected():
'''public final boolean isConnected()
'''
pass
def getTunnelType():
'''public final TunnelType getTunnelType()
'''
pass
def isTunnelled():
'''public final boolean isTunnelled()
'''
pass
def getLayerType():
'''public final LayerType getLayerType()
'''
pass
def isLayered():
'''public final boolean isLayered()
'''
pass
def isSecure():
'''public final boolean isSecure()
'''
pass
def toRoute():
'''public final HttpRoute toRoute()
'''
pass
def equals():
'''public final boolean equals(final Object o)
'''
pass
def hashCode():
'''public final int hashCode()
'''
pass
def toString():
'''public final String toString()
'''
pass
def clone():
'''public Object clone()
'''
pass
