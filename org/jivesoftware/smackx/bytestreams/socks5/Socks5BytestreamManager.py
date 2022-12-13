def getBytestreamManager():
    '''public static synchronized Socks5BytestreamManager getBytestreamManager(final XMPPConnection connection)
    '''
def addIncomingBytestreamListener():
    '''public void addIncomingBytestreamListener(final BytestreamListener listener)
    public void addIncomingBytestreamListener(final BytestreamListener listener, final Jid initiatorJID)
    '''
def removeIncomingBytestreamListener():
    '''public void removeIncomingBytestreamListener(final BytestreamListener listener)
    public void removeIncomingBytestreamListener(final Jid initiatorJID)
    '''
def ignoreBytestreamRequestOnce():
    '''public void ignoreBytestreamRequestOnce(final String sessionID)
    '''
def disableService():
    '''public synchronized void disableService()
    '''
def getTargetResponseTimeout():
    '''public int getTargetResponseTimeout()
    '''
def setTargetResponseTimeout():
    '''public void setTargetResponseTimeout(final int targetResponseTimeout)
    '''
def getProxyConnectionTimeout():
    '''public int getProxyConnectionTimeout()
    '''
def setProxyConnectionTimeout():
    '''public void setProxyConnectionTimeout(final int proxyConnectionTimeout)
    '''
def isProxyPrioritizationEnabled():
    '''public boolean isProxyPrioritizationEnabled()
    '''
def setProxyPrioritizationEnabled():
    '''public void setProxyPrioritizationEnabled(final boolean proxyPrioritizationEnabled)
    '''
def establishSession():
    '''public Socks5BytestreamSession establishSession(final Jid targetJID)
    public Socks5BytestreamSession establishSession(final Jid targetJID, final String sessionID)
    '''
def determineProxies():
    '''public List<Jid> determineProxies()
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
