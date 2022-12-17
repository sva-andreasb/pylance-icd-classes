NETASCII_EOL = "String  \"\r\n\""
def ():
    '''returns SocketClient\n\n
    ()\n
    '''
def connect():
    '''returns None\n\n
    connect(final InetAddress host, final int port)\n
    connect(final String hostname, final int port)\n
    connect(final InetAddress host, final int port, final InetAddress localAddr, final int localPort)\n
    connect(final String hostname, final int port, final InetAddress localAddr, final int localPort)\n
    connect(final InetAddress host)\n
    connect(final String hostname)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def setDefaultPort():
    '''returns None\n\n
    setDefaultPort(final int port)\n
    '''
def getDefaultPort():
    '''returns int\n\n
    getDefaultPort()\n
    '''
def setDefaultTimeout():
    '''returns None\n\n
    setDefaultTimeout(final int timeout)\n
    '''
def getDefaultTimeout():
    '''returns int\n\n
    getDefaultTimeout()\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def setTcpNoDelay():
    '''returns None\n\n
    setTcpNoDelay(final boolean on)\n
    '''
def getTcpNoDelay():
    '''returns boolean\n\n
    getTcpNoDelay()\n
    '''
def setSoLinger():
    '''returns None\n\n
    setSoLinger(final boolean on, final int val)\n
    '''
def getSoLinger():
    '''returns int\n\n
    getSoLinger()\n
    '''
def getLocalPort():
    '''returns int\n\n
    getLocalPort()\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def getRemotePort():
    '''returns int\n\n
    getRemotePort()\n
    '''
def getRemoteAddress():
    '''returns InetAddress\n\n
    getRemoteAddress()\n
    '''
def verifyRemote():
    '''returns boolean\n\n
    verifyRemote(final Socket socket)\n
    '''
def setSocketFactory():
    '''returns None\n\n
    setSocketFactory(final SocketFactory factory)\n
    '''
