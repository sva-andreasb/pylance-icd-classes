SO_TIMEOUT = "String  \"http.socket.timeout\""
TCP_NODELAY = "String  \"http.tcp.nodelay\""
SO_SNDBUF = "String  \"http.socket.sendbuffer\""
SO_RCVBUF = "String  \"http.socket.receivebuffer\""
SO_LINGER = "String  \"http.socket.linger\""
CONNECTION_TIMEOUT = "String  \"http.connection.timeout\""
STALE_CONNECTION_CHECK = "String  \"http.connection.stalecheck\""
def getSoTimeout():
    '''public int getSoTimeout()
    '''
def setSoTimeout():
    '''public void setSoTimeout(final int timeout)
    '''
def setTcpNoDelay():
    '''public void setTcpNoDelay(final boolean value)
    '''
def getTcpNoDelay():
    '''public boolean getTcpNoDelay()
    '''
def getSendBufferSize():
    '''public int getSendBufferSize()
    '''
def setSendBufferSize():
    '''public void setSendBufferSize(final int size)
    '''
def getReceiveBufferSize():
    '''public int getReceiveBufferSize()
    '''
def setReceiveBufferSize():
    '''public void setReceiveBufferSize(final int size)
    '''
def getLinger():
    '''public int getLinger()
    '''
def setLinger():
    '''public void setLinger(final int value)
    '''
def getConnectionTimeout():
    '''public int getConnectionTimeout()
    '''
def setConnectionTimeout():
    '''public void setConnectionTimeout(final int timeout)
    '''
def isStaleCheckingEnabled():
    '''public boolean isStaleCheckingEnabled()
    '''
def setStaleCheckingEnabled():
    '''public void setStaleCheckingEnabled(final boolean value)
    '''
