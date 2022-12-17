RESOLVE_LOCALLY = "short  0"
RESOLVE_ON_SERVER = "short  1"
RESOLVE_LOCALLY_THEN_ON_SERVER = "short  2"
def ():
    '''returns SocksConnection\n\n
    (final String host, final int remotePort, final String proxyServer, final int proxyPort, final String userId, final String proxyPassword, final long n, final short resolveOption)\n
    (final int n, final String s, final int n2, final String s2, final String s3, final long n3, final short n4)\n
    '''
def onConnectionClosed():
    '''returns None\n\n
    onConnectionClosed(final int n, final Connection connection)\n
    '''
def setKeepAliveParams():
    '''returns None\n\n
    setKeepAliveParams(final long n, final byte[] array)\n
    '''
def setBytesToReceive():
    '''returns None\n\n
    setBytesToReceive(final int bytesToReceive)\n
    '''
def sendMessage():
    '''returns None\n\n
    sendMessage(final byte[] array, final byte b)\n
    '''
def close():
    '''returns None\n\n
    close(final int n)\n
    close()\n
    '''
