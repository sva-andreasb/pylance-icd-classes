RESOLVE_LOCALLY = "short  0"
RESOLVE_ON_SERVER = "short  1"
RESOLVE_LOCALLY_THEN_ON_SERVER = "short  2"
def SocksConnection():
    '''    public SocksConnection(final String host, final int remotePort, final String proxyServer, final int proxyPort, final String userId, final String proxyPassword, final long n, final short resolveOption)
    public SocksConnection(final int n, final String s, final int n2, final String s2, final String s3, final long n3, final short n4)
    '''
def onConnectionClosed():
    '''    public void onConnectionClosed(final int n, final Connection connection)
    '''
def setKeepAliveParams():
    '''    public void setKeepAliveParams(final long n, final byte[] array)
    '''
def setBytesToReceive():
    '''    public void setBytesToReceive(final int bytesToReceive)
    '''
def sendMessage():
    '''    public void sendMessage(final byte[] array, final byte b)
    '''
def close():
    '''    public void close(final int n)
    public void close()
    '''
