def ConnectionHandler():
'''public ConnectionHandler()
'''
pass
def setMasterCnlListener():
'''public synchronized void setMasterCnlListener(final int value, final MasterCnlListener value2)
'''
pass
def removeMasterCnlListener():
'''public synchronized void removeMasterCnlListener(final int value)
'''
pass
def setListenerForCnl():
'''public synchronized void setListenerForCnl(final int n, final CnlMsgListener cnlMsgListener)
'''
pass
def removeListenerForCnl():
'''public synchronized void removeListenerForCnl(final int n)
'''
pass
def setKeepAliveRate():
'''public synchronized void setKeepAliveRate(final long keepAliveRate)
'''
pass
def connect():
'''public synchronized void connect(final String s, Connection[] defaultConnectionList, final VpkMsgOut vpkMsgOut)
'''
pass
def close():
'''public synchronized void close(final int n)
'''
pass
def getLocalAddress():
'''public InetAddress getLocalAddress()
'''
pass
def isReady():
'''public synchronized boolean isReady()
'''
pass
def send():
'''public synchronized boolean send(final VpkMsgOut vpkMsgOut, final byte b)
'''
pass
def getConnectionInfo():
'''public ConnectionInfo getConnectionInfo()
'''
pass
def encryptConnection():
'''public void encryptConnection(final byte[] key)
'''
pass
def onConnectionClosed():
'''public void onConnectionClosed(final int n, final Connection connection)
'''
pass
def onConnected():
'''public void onConnected(final Connection connection)
'''
pass
def onConnectFailed():
'''public void onConnectFailed()
'''
pass
def onProtocolErrorOccured():
'''public void onProtocolErrorOccured()
'''
pass
def onReceive():
'''public void onReceive(final byte[] array, final Connection connection)
'''
pass
def toOpaque():
'''public byte[] toOpaque(final VpkMsgOut vpkMsgOut)
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
