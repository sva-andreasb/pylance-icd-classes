def DelegateSSLSocket():
    '''    public DelegateSSLSocket(final SSLSocket sock)
    '''
def connect():
    '''    public void connect(final SocketAddress endpoint)
    public void connect(final SocketAddress endpoint, final int timeout)
    '''
def bind():
    '''    public void bind(final SocketAddress bindpoint)
    '''
def getInetAddress():
    '''    public InetAddress getInetAddress()
    '''
def getLocalAddress():
    '''    public InetAddress getLocalAddress()
    '''
def getPort():
    '''    public int getPort()
    '''
def getLocalPort():
    '''    public int getLocalPort()
    '''
def getRemoteSocketAddress():
    '''    public SocketAddress getRemoteSocketAddress()
    '''
def getLocalSocketAddress():
    '''    public SocketAddress getLocalSocketAddress()
    '''
def getChannel():
    '''    public SocketChannel getChannel()
    '''
def getInputStream():
    '''    public InputStream getInputStream()
    '''
def getOutputStream():
    '''    public OutputStream getOutputStream()
    '''
def setTcpNoDelay():
    '''    public void setTcpNoDelay(final boolean on)
    '''
def getTcpNoDelay():
    '''    public boolean getTcpNoDelay()
    '''
def setSoLinger():
    '''    public void setSoLinger(final boolean on, final int linger)
    '''
def getSoLinger():
    '''    public int getSoLinger()
    '''
def sendUrgentData():
    '''    public void sendUrgentData(final int data)
    '''
def setOOBInline():
    '''    public void setOOBInline(final boolean on)
    '''
def getOOBInline():
    '''    public boolean getOOBInline()
    '''
def setSoTimeout():
    '''    public void setSoTimeout(final int timeout)
    '''
def getSoTimeout():
    '''    public int getSoTimeout()
    '''
def setSendBufferSize():
    '''    public void setSendBufferSize(final int size)
    '''
def getSendBufferSize():
    '''    public int getSendBufferSize()
    '''
def setReceiveBufferSize():
    '''    public void setReceiveBufferSize(final int size)
    '''
def getReceiveBufferSize():
    '''    public int getReceiveBufferSize()
    '''
def setKeepAlive():
    '''    public void setKeepAlive(final boolean on)
    '''
def getKeepAlive():
    '''    public boolean getKeepAlive()
    '''
def setTrafficClass():
    '''    public void setTrafficClass(final int tc)
    '''
def getTrafficClass():
    '''    public int getTrafficClass()
    '''
def setReuseAddress():
    '''    public void setReuseAddress(final boolean on)
    '''
def getReuseAddress():
    '''    public boolean getReuseAddress()
    '''
def close():
    '''    public void close()
    '''
def shutdownInput():
    '''    public void shutdownInput()
    '''
def shutdownOutput():
    '''    public void shutdownOutput()
    '''
def toString():
    '''    public String toString()
    '''
def isConnected():
    '''    public boolean isConnected()
    '''
def isBound():
    '''    public boolean isBound()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def isInputShutdown():
    '''    public boolean isInputShutdown()
    '''
def isOutputShutdown():
    '''    public boolean isOutputShutdown()
    '''
def setPerformancePreferences():
    '''    public void setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)
    '''
def getSupportedCipherSuites():
    '''    public String[] getSupportedCipherSuites()
    '''
def getEnabledCipherSuites():
    '''    public String[] getEnabledCipherSuites()
    '''
def setEnabledCipherSuites():
    '''    public void setEnabledCipherSuites(final String[] suites)
    '''
def getSupportedProtocols():
    '''    public String[] getSupportedProtocols()
    '''
def getEnabledProtocols():
    '''    public String[] getEnabledProtocols()
    '''
def setEnabledProtocols():
    '''    public void setEnabledProtocols(final String[] protocols)
    '''
def getSession():
    '''    public SSLSession getSession()
    '''
def addHandshakeCompletedListener():
    '''    public void addHandshakeCompletedListener(final HandshakeCompletedListener listener)
    '''
def removeHandshakeCompletedListener():
    '''    public void removeHandshakeCompletedListener(final HandshakeCompletedListener listener)
    '''
def startHandshake():
    '''    public void startHandshake()
    '''
def setUseClientMode():
    '''    public void setUseClientMode(final boolean mode)
    '''
def getUseClientMode():
    '''    public boolean getUseClientMode()
    '''
def setNeedClientAuth():
    '''    public void setNeedClientAuth(final boolean need)
    '''
def getNeedClientAuth():
    '''    public boolean getNeedClientAuth()
    '''
def setWantClientAuth():
    '''    public void setWantClientAuth(final boolean want)
    '''
def getWantClientAuth():
    '''    public boolean getWantClientAuth()
    '''
def setEnableSessionCreation():
    '''    public void setEnableSessionCreation(final boolean flag)
    '''
def getEnableSessionCreation():
    '''    public boolean getEnableSessionCreation()
    '''
