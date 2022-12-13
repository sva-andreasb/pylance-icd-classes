def Socket():
'''public Socket(final int fd)
'''
pass
def shutdown():
'''public final void shutdown()
public final void shutdown(final boolean read, final boolean write)
'''
pass
def isShutdown():
'''public final boolean isShutdown()
'''
pass
def isInputShutdown():
'''public final boolean isInputShutdown()
'''
pass
def isOutputShutdown():
'''public final boolean isOutputShutdown()
'''
pass
def sendTo():
'''public final int sendTo(final ByteBuffer buf, final int pos, final int limit, final InetAddress addr, final int port)
'''
pass
def sendToAddress():
'''public final int sendToAddress(final long memoryAddress, final int pos, final int limit, final InetAddress addr, final int port)
'''
pass
def sendToAddresses():
'''public final int sendToAddresses(final long memoryAddress, final int length, final InetAddress addr, final int port)
'''
pass
def recvFrom():
'''public final DatagramSocketAddress recvFrom(final ByteBuffer buf, final int pos, final int limit)
'''
pass
def recvFromAddress():
'''public final DatagramSocketAddress recvFromAddress(final long memoryAddress, final int pos, final int limit)
'''
pass
def recvFd():
'''public final int recvFd()
'''
pass
def sendFd():
'''public final int sendFd(final int fdToSend)
'''
pass
def connect():
'''public final boolean connect(final SocketAddress socketAddress)
'''
pass
def finishConnect():
'''public final boolean finishConnect()
'''
pass
def disconnect():
'''public final void disconnect()
'''
pass
def bind():
'''public final void bind(final SocketAddress socketAddress)
'''
pass
def listen():
'''public final void listen(final int backlog)
'''
pass
def accept():
'''public final int accept(final byte[] addr)
'''
pass
def remoteAddress():
'''public final InetSocketAddress remoteAddress()
'''
pass
def localAddress():
'''public final InetSocketAddress localAddress()
'''
pass
def getReceiveBufferSize():
'''public final int getReceiveBufferSize()
'''
pass
def getSendBufferSize():
'''public final int getSendBufferSize()
'''
pass
def isKeepAlive():
'''public final boolean isKeepAlive()
'''
pass
def isTcpNoDelay():
'''public final boolean isTcpNoDelay()
'''
pass
def isReuseAddress():
'''public final boolean isReuseAddress()
'''
pass
def isReusePort():
'''public final boolean isReusePort()
'''
pass
def isBroadcast():
'''public final boolean isBroadcast()
'''
pass
def getSoLinger():
'''public final int getSoLinger()
'''
pass
def getSoError():
'''public final int getSoError()
'''
pass
def getTrafficClass():
'''public final int getTrafficClass()
'''
pass
def setKeepAlive():
'''public final void setKeepAlive(final boolean keepAlive)
'''
pass
def setReceiveBufferSize():
'''public final void setReceiveBufferSize(final int receiveBufferSize)
'''
pass
def setSendBufferSize():
'''public final void setSendBufferSize(final int sendBufferSize)
'''
pass
def setTcpNoDelay():
'''public final void setTcpNoDelay(final boolean tcpNoDelay)
'''
pass
def setSoLinger():
'''public final void setSoLinger(final int soLinger)
'''
pass
def setReuseAddress():
'''public final void setReuseAddress(final boolean reuseAddress)
'''
pass
def setReusePort():
'''public final void setReusePort(final boolean reusePort)
'''
pass
def setBroadcast():
'''public final void setBroadcast(final boolean broadcast)
'''
pass
def setTrafficClass():
'''public final void setTrafficClass(final int trafficClass)
'''
pass
def toString():
'''public String toString()
'''
pass
def newSocketStream():
'''public static Socket newSocketStream()
'''
pass
def newSocketDgram():
'''public static Socket newSocketDgram()
'''
pass
def newSocketDomain():
'''public static Socket newSocketDomain()
'''
pass
def initialize():
'''public static void initialize()
'''
pass
