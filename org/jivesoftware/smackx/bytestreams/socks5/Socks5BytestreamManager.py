def addIncomingBytestreamListener():
    '''returns None\n\n
    addIncomingBytestreamListener(final BytestreamListener listener)\n
    addIncomingBytestreamListener(final BytestreamListener listener, final Jid initiatorJID)\n
    '''
def removeIncomingBytestreamListener():
    '''returns None\n\n
    removeIncomingBytestreamListener(final BytestreamListener listener)\n
    removeIncomingBytestreamListener(final Jid initiatorJID)\n
    '''
def ignoreBytestreamRequestOnce():
    '''returns None\n\n
    ignoreBytestreamRequestOnce(final String sessionID)\n
    '''
def getTargetResponseTimeout():
    '''returns int\n\n
    getTargetResponseTimeout()\n
    '''
def setTargetResponseTimeout():
    '''returns None\n\n
    setTargetResponseTimeout(final int targetResponseTimeout)\n
    '''
def getProxyConnectionTimeout():
    '''returns int\n\n
    getProxyConnectionTimeout()\n
    '''
def setProxyConnectionTimeout():
    '''returns None\n\n
    setProxyConnectionTimeout(final int proxyConnectionTimeout)\n
    '''
def isProxyPrioritizationEnabled():
    '''returns boolean\n\n
    isProxyPrioritizationEnabled()\n
    '''
def setProxyPrioritizationEnabled():
    '''returns None\n\n
    setProxyPrioritizationEnabled(final boolean proxyPrioritizationEnabled)\n
    '''
def establishSession():
    '''returns Socks5BytestreamSession\n\n
    establishSession(final Jid targetJID)\n
    establishSession(final Jid targetJID, final String sessionID)\n
    '''
def determineProxies():
    '''returns List<Jid>\n\n
    determineProxies()\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
