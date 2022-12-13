def getBytestreamManager():
'''public static synchronized Socks5BytestreamManager getBytestreamManager(final XMPPConnection connection)
'''
pass
def addIncomingBytestreamListener():
'''public void addIncomingBytestreamListener(final BytestreamListener listener)
public void addIncomingBytestreamListener(final BytestreamListener listener, final Jid initiatorJID)
'''
pass
def removeIncomingBytestreamListener():
'''public void removeIncomingBytestreamListener(final BytestreamListener listener)
public void removeIncomingBytestreamListener(final Jid initiatorJID)
'''
pass
def ignoreBytestreamRequestOnce():
'''public void ignoreBytestreamRequestOnce(final String sessionID)
'''
pass
def disableService():
'''public synchronized void disableService()
'''
pass
def getTargetResponseTimeout():
'''public int getTargetResponseTimeout()
'''
pass
def setTargetResponseTimeout():
'''public void setTargetResponseTimeout(final int targetResponseTimeout)
'''
pass
def getProxyConnectionTimeout():
'''public int getProxyConnectionTimeout()
'''
pass
def setProxyConnectionTimeout():
'''public void setProxyConnectionTimeout(final int proxyConnectionTimeout)
'''
pass
def isProxyPrioritizationEnabled():
'''public boolean isProxyPrioritizationEnabled()
'''
pass
def setProxyPrioritizationEnabled():
'''public void setProxyPrioritizationEnabled(final boolean proxyPrioritizationEnabled)
'''
pass
def establishSession():
'''public Socks5BytestreamSession establishSession(final Jid targetJID)
public Socks5BytestreamSession establishSession(final Jid targetJID, final String sessionID)
'''
pass
def determineProxies():
'''public List<Jid> determineProxies()
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
