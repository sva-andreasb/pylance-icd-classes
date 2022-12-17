def ():
    '''returns AgentConnection\n\n
    (final int serverPort, final String mux, final int muxPort, final String proxy, final int proxyPort, final boolean useIEProxy, final String proxyUsername, final String proxyPass, final boolean popupAuthDialog, final long n)\n
    (final int muxPort, final String proxy, final int proxyPort, final boolean useIEProxy, final String proxyUsername, final String proxyPass, final boolean popupAuthDialog, final long n)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final byte[] array, final byte b)\n
    '''
def getConnectionInfo():
    '''returns ConnectionInfo\n\n
    getConnectionInfo()\n
    '''
def close():
    '''returns None\n\n
    close(final int closeReason)\n
    '''
def setKeepAliveParams():
    '''returns None\n\n
    setKeepAliveParams(final long n, final byte[] array)\n
    '''
def setBytesToReceive():
    '''returns None\n\n
    setBytesToReceive(final int bytesToReceive)\n
    '''
def setAppName():
    '''returns None\n\n
    setAppName(final String appName)\n
    '''
