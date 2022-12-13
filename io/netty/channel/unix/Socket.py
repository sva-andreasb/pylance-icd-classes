def Socket():
    '''    public Socket(final int fd)
    '''
def shutdown():
    '''    public final void shutdown()
    public final void shutdown(final boolean read, final boolean write)
    '''
def isShutdown():
    '''    public final boolean isShutdown()
    '''
def isInputShutdown():
    '''    public final boolean isInputShutdown()
    '''
def isOutputShutdown():
    '''    public final boolean isOutputShutdown()
    '''
def sendTo():
    '''    public final int sendTo(final ByteBuffer buf, final int pos, final int limit, final InetAddress addr, final int port)
    '''
def sendToAddress():
    '''    public final int sendToAddress(final long memoryAddress, final int pos, final int limit, final InetAddress addr, final int port)
    '''
def sendToAddresses():
    '''    public final int sendToAddresses(final long memoryAddress, final int length, final InetAddress addr, final int port)
    '''
def recvFrom():
    '''    public final DatagramSocketAddress recvFrom(final ByteBuffer buf, final int pos, final int limit)
    '''
def recvFromAddress():
    '''    public final DatagramSocketAddress recvFromAddress(final long memoryAddress, final int pos, final int limit)
    '''
def recvFd():
    '''    public final int recvFd()
    '''
def sendFd():
    '''    public final int sendFd(final int fdToSend)
    '''
def connect():
    '''    public final boolean connect(final SocketAddress socketAddress)
    '''
def finishConnect():
    '''    public final boolean finishConnect()
    '''
def disconnect():
    '''    public final void disconnect()
    '''
def bind():
    '''    public final void bind(final SocketAddress socketAddress)
    '''
def listen():
    '''    public final void listen(final int backlog)
    '''
def accept():
    '''    public final int accept(final byte[] addr)
    '''
def remoteAddress():
    '''    public final InetSocketAddress remoteAddress()
    '''
def localAddress():
    '''    public final InetSocketAddress localAddress()
    '''
def getReceiveBufferSize():
    '''    public final int getReceiveBufferSize()
    '''
def getSendBufferSize():
    '''    public final int getSendBufferSize()
    '''
def isKeepAlive():
    '''    public final boolean isKeepAlive()
    '''
def isTcpNoDelay():
    '''    public final boolean isTcpNoDelay()
    '''
def isReuseAddress():
    '''    public final boolean isReuseAddress()
    '''
def isReusePort():
    '''    public final boolean isReusePort()
    '''
def isBroadcast():
    '''    public final boolean isBroadcast()
    '''
def getSoLinger():
    '''    public final int getSoLinger()
    '''
def getSoError():
    '''    public final int getSoError()
    '''
def getTrafficClass():
    '''    public final int getTrafficClass()
    '''
def setKeepAlive():
    '''    public final void setKeepAlive(final boolean keepAlive)
    '''
def setReceiveBufferSize():
    '''    public final void setReceiveBufferSize(final int receiveBufferSize)
    '''
def setSendBufferSize():
    '''    public final void setSendBufferSize(final int sendBufferSize)
    '''
def setTcpNoDelay():
    '''    public final void setTcpNoDelay(final boolean tcpNoDelay)
    '''
def setSoLinger():
    '''    public final void setSoLinger(final int soLinger)
    '''
def setReuseAddress():
    '''    public final void setReuseAddress(final boolean reuseAddress)
    '''
def setReusePort():
    '''    public final void setReusePort(final boolean reusePort)
    '''
def setBroadcast():
    '''    public final void setBroadcast(final boolean broadcast)
    '''
def setTrafficClass():
    '''    public final void setTrafficClass(final int trafficClass)
    '''
def toString():
    '''    public String toString()
    '''
def newSocketStream():
    '''    public static Socket newSocketStream()
    '''
def newSocketDgram():
    '''    public static Socket newSocketDgram()
    '''
def newSocketDomain():
    '''    public static Socket newSocketDomain()
    '''
def initialize():
    '''    public static void initialize()
    '''
