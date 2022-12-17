def ():
    '''returns DelegateSocket\n\n
    (final Socket sock)\n
    '''
def connect():
    '''returns None\n\n
    connect(final SocketAddress endpoint)\n
    connect(final SocketAddress endpoint, final int timeout)\n
    '''
def bind():
    '''returns None\n\n
    bind(final SocketAddress bindpoint)\n
    '''
def getInetAddress():
    '''returns InetAddress\n\n
    getInetAddress()\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getLocalPort():
    '''returns int\n\n
    getLocalPort()\n
    '''
def getRemoteSocketAddress():
    '''returns SocketAddress\n\n
    getRemoteSocketAddress()\n
    '''
def getLocalSocketAddress():
    '''returns SocketAddress\n\n
    getLocalSocketAddress()\n
    '''
def getChannel():
    '''returns SocketChannel\n\n
    getChannel()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
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
    setSoLinger(final boolean on, final int linger)\n
    '''
def getSoLinger():
    '''returns int\n\n
    getSoLinger()\n
    '''
def sendUrgentData():
    '''returns None\n\n
    sendUrgentData(final int data)\n
    '''
def setOOBInline():
    '''returns None\n\n
    setOOBInline(final boolean on)\n
    '''
def getOOBInline():
    '''returns boolean\n\n
    getOOBInline()\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def setSendBufferSize():
    '''returns None\n\n
    setSendBufferSize(final int size)\n
    '''
def getSendBufferSize():
    '''returns int\n\n
    getSendBufferSize()\n
    '''
def setReceiveBufferSize():
    '''returns None\n\n
    setReceiveBufferSize(final int size)\n
    '''
def getReceiveBufferSize():
    '''returns int\n\n
    getReceiveBufferSize()\n
    '''
def setKeepAlive():
    '''returns None\n\n
    setKeepAlive(final boolean on)\n
    '''
def getKeepAlive():
    '''returns boolean\n\n
    getKeepAlive()\n
    '''
def setTrafficClass():
    '''returns None\n\n
    setTrafficClass(final int tc)\n
    '''
def getTrafficClass():
    '''returns int\n\n
    getTrafficClass()\n
    '''
def setReuseAddress():
    '''returns None\n\n
    setReuseAddress(final boolean on)\n
    '''
def getReuseAddress():
    '''returns boolean\n\n
    getReuseAddress()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def shutdownInput():
    '''returns None\n\n
    shutdownInput()\n
    '''
def shutdownOutput():
    '''returns None\n\n
    shutdownOutput()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isBound():
    '''returns boolean\n\n
    isBound()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def isInputShutdown():
    '''returns boolean\n\n
    isInputShutdown()\n
    '''
def isOutputShutdown():
    '''returns boolean\n\n
    isOutputShutdown()\n
    '''
def setPerformancePreferences():
    '''returns None\n\n
    setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)\n
    '''
