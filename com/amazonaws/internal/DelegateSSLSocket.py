def DelegateSSLSocket():
'''public DelegateSSLSocket(final SSLSocket sock)
'''
pass
def connect():
'''public void connect(final SocketAddress endpoint)
public void connect(final SocketAddress endpoint, final int timeout)
'''
pass
def bind():
'''public void bind(final SocketAddress bindpoint)
'''
pass
def getInetAddress():
'''public InetAddress getInetAddress()
'''
pass
def getLocalAddress():
'''public InetAddress getLocalAddress()
'''
pass
def getPort():
'''public int getPort()
'''
pass
def getLocalPort():
'''public int getLocalPort()
'''
pass
def getRemoteSocketAddress():
'''public SocketAddress getRemoteSocketAddress()
'''
pass
def getLocalSocketAddress():
'''public SocketAddress getLocalSocketAddress()
'''
pass
def getChannel():
'''public SocketChannel getChannel()
'''
pass
def getInputStream():
'''public InputStream getInputStream()
'''
pass
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def setTcpNoDelay():
'''public void setTcpNoDelay(final boolean on)
'''
pass
def getTcpNoDelay():
'''public boolean getTcpNoDelay()
'''
pass
def setSoLinger():
'''public void setSoLinger(final boolean on, final int linger)
'''
pass
def getSoLinger():
'''public int getSoLinger()
'''
pass
def sendUrgentData():
'''public void sendUrgentData(final int data)
'''
pass
def setOOBInline():
'''public void setOOBInline(final boolean on)
'''
pass
def getOOBInline():
'''public boolean getOOBInline()
'''
pass
def setSoTimeout():
'''public void setSoTimeout(final int timeout)
'''
pass
def getSoTimeout():
'''public int getSoTimeout()
'''
pass
def setSendBufferSize():
'''public void setSendBufferSize(final int size)
'''
pass
def getSendBufferSize():
'''public int getSendBufferSize()
'''
pass
def setReceiveBufferSize():
'''public void setReceiveBufferSize(final int size)
'''
pass
def getReceiveBufferSize():
'''public int getReceiveBufferSize()
'''
pass
def setKeepAlive():
'''public void setKeepAlive(final boolean on)
'''
pass
def getKeepAlive():
'''public boolean getKeepAlive()
'''
pass
def setTrafficClass():
'''public void setTrafficClass(final int tc)
'''
pass
def getTrafficClass():
'''public int getTrafficClass()
'''
pass
def setReuseAddress():
'''public void setReuseAddress(final boolean on)
'''
pass
def getReuseAddress():
'''public boolean getReuseAddress()
'''
pass
def close():
'''public void close()
'''
pass
def shutdownInput():
'''public void shutdownInput()
'''
pass
def shutdownOutput():
'''public void shutdownOutput()
'''
pass
def toString():
'''public String toString()
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isBound():
'''public boolean isBound()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def isInputShutdown():
'''public boolean isInputShutdown()
'''
pass
def isOutputShutdown():
'''public boolean isOutputShutdown()
'''
pass
def setPerformancePreferences():
'''public void setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)
'''
pass
def getSupportedCipherSuites():
'''public String[] getSupportedCipherSuites()
'''
pass
def getEnabledCipherSuites():
'''public String[] getEnabledCipherSuites()
'''
pass
def setEnabledCipherSuites():
'''public void setEnabledCipherSuites(final String[] suites)
'''
pass
def getSupportedProtocols():
'''public String[] getSupportedProtocols()
'''
pass
def getEnabledProtocols():
'''public String[] getEnabledProtocols()
'''
pass
def setEnabledProtocols():
'''public void setEnabledProtocols(final String[] protocols)
'''
pass
def getSession():
'''public SSLSession getSession()
'''
pass
def addHandshakeCompletedListener():
'''public void addHandshakeCompletedListener(final HandshakeCompletedListener listener)
'''
pass
def removeHandshakeCompletedListener():
'''public void removeHandshakeCompletedListener(final HandshakeCompletedListener listener)
'''
pass
def startHandshake():
'''public void startHandshake()
'''
pass
def setUseClientMode():
'''public void setUseClientMode(final boolean mode)
'''
pass
def getUseClientMode():
'''public boolean getUseClientMode()
'''
pass
def setNeedClientAuth():
'''public void setNeedClientAuth(final boolean need)
'''
pass
def getNeedClientAuth():
'''public boolean getNeedClientAuth()
'''
pass
def setWantClientAuth():
'''public void setWantClientAuth(final boolean want)
'''
pass
def getWantClientAuth():
'''public boolean getWantClientAuth()
'''
pass
def setEnableSessionCreation():
'''public void setEnableSessionCreation(final boolean flag)
'''
pass
def getEnableSessionCreation():
'''public boolean getEnableSessionCreation()
'''
pass
