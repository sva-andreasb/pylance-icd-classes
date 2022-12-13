def ConnectionHandler():
    '''    public ConnectionHandler()
    '''
def setMasterCnlListener():
    '''    public synchronized void setMasterCnlListener(final int value, final MasterCnlListener value2)
    '''
def removeMasterCnlListener():
    '''    public synchronized void removeMasterCnlListener(final int value)
    '''
def setListenerForCnl():
    '''    public synchronized void setListenerForCnl(final int n, final CnlMsgListener cnlMsgListener)
    '''
def removeListenerForCnl():
    '''    public synchronized void removeListenerForCnl(final int n)
    '''
def setKeepAliveRate():
    '''    public synchronized void setKeepAliveRate(final long keepAliveRate)
    '''
def connect():
    '''    public synchronized void connect(final String s, Connection[] defaultConnectionList, final VpkMsgOut vpkMsgOut)
    '''
def close():
    '''    public synchronized void close(final int n)
    '''
def getLocalAddress():
    '''    public InetAddress getLocalAddress()
    '''
def isReady():
    '''    public synchronized boolean isReady()
    '''
def send():
    '''    public synchronized boolean send(final VpkMsgOut vpkMsgOut, final byte b)
    '''
def getConnectionInfo():
    '''    public ConnectionInfo getConnectionInfo()
    '''
def encryptConnection():
    '''    public void encryptConnection(final byte[] key)
    '''
def onConnectionClosed():
    '''    public void onConnectionClosed(final int n, final Connection connection)
    '''
def onConnected():
    '''    public void onConnected(final Connection connection)
    '''
def onConnectFailed():
    '''    public void onConnectFailed()
    '''
def onProtocolErrorOccured():
    '''    public void onProtocolErrorOccured()
    '''
def onReceive():
    '''    public void onReceive(final byte[] array, final Connection connection)
    '''
def toOpaque():
    '''    public byte[] toOpaque(final VpkMsgOut vpkMsgOut)
    '''
def getConnection():
    '''    public Connection getConnection()
    '''
