SO_TIMEOUT = "String  \"http.socket.timeout\""
TCP_NODELAY = "String  \"http.tcp.nodelay\""
SO_SNDBUF = "String  \"http.socket.sendbuffer\""
SO_RCVBUF = "String  \"http.socket.receivebuffer\""
SO_LINGER = "String  \"http.socket.linger\""
CONNECTION_TIMEOUT = "String  \"http.connection.timeout\""
STALE_CONNECTION_CHECK = "String  \"http.connection.stalecheck\""
def getSoTimeout():
    '''returns int\n\n
    getSoTimeout()\n
    '''
def setSoTimeout():
    '''returns None\n\n
    setSoTimeout(final int timeout)\n
    '''
def setTcpNoDelay():
    '''returns None\n\n
    setTcpNoDelay(final boolean value)\n
    '''
def getTcpNoDelay():
    '''returns boolean\n\n
    getTcpNoDelay()\n
    '''
def getSendBufferSize():
    '''returns int\n\n
    getSendBufferSize()\n
    '''
def setSendBufferSize():
    '''returns None\n\n
    setSendBufferSize(final int size)\n
    '''
def getReceiveBufferSize():
    '''returns int\n\n
    getReceiveBufferSize()\n
    '''
def setReceiveBufferSize():
    '''returns None\n\n
    setReceiveBufferSize(final int size)\n
    '''
def getLinger():
    '''returns int\n\n
    getLinger()\n
    '''
def setLinger():
    '''returns None\n\n
    setLinger(final int value)\n
    '''
def getConnectionTimeout():
    '''returns int\n\n
    getConnectionTimeout()\n
    '''
def setConnectionTimeout():
    '''returns None\n\n
    setConnectionTimeout(final int timeout)\n
    '''
def isStaleCheckingEnabled():
    '''returns boolean\n\n
    isStaleCheckingEnabled()\n
    '''
def setStaleCheckingEnabled():
    '''returns None\n\n
    setStaleCheckingEnabled(final boolean value)\n
    '''
