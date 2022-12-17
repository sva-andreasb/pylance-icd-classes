def setReuseAddress():
    '''returns EpollServerSocketChannelConfig\n\n
    setReuseAddress(final boolean reuseAddress)\n
    '''
def setReceiveBufferSize():
    '''returns EpollServerSocketChannelConfig\n\n
    setReceiveBufferSize(final int receiveBufferSize)\n
    '''
def setPerformancePreferences():
    '''returns EpollServerSocketChannelConfig\n\n
    setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)\n
    '''
def setBacklog():
    '''returns EpollServerSocketChannelConfig\n\n
    setBacklog(final int backlog)\n
    '''
def setConnectTimeoutMillis():
    '''returns EpollServerSocketChannelConfig\n\n
    setConnectTimeoutMillis(final int connectTimeoutMillis)\n
    '''
def setMaxMessagesPerRead():
    '''returns EpollServerSocketChannelConfig\n\n
    setMaxMessagesPerRead(final int maxMessagesPerRead)\n
    '''
def setWriteSpinCount():
    '''returns EpollServerSocketChannelConfig\n\n
    setWriteSpinCount(final int writeSpinCount)\n
    '''
def setAllocator():
    '''returns EpollServerSocketChannelConfig\n\n
    setAllocator(final ByteBufAllocator allocator)\n
    '''
def setRecvByteBufAllocator():
    '''returns EpollServerSocketChannelConfig\n\n
    setRecvByteBufAllocator(final RecvByteBufAllocator allocator)\n
    '''
def setAutoRead():
    '''returns EpollServerSocketChannelConfig\n\n
    setAutoRead(final boolean autoRead)\n
    '''
def setWriteBufferHighWaterMark():
    '''returns EpollServerSocketChannelConfig\n\n
    setWriteBufferHighWaterMark(final int writeBufferHighWaterMark)\n
    '''
def setWriteBufferLowWaterMark():
    '''returns EpollServerSocketChannelConfig\n\n
    setWriteBufferLowWaterMark(final int writeBufferLowWaterMark)\n
    '''
def setWriteBufferWaterMark():
    '''returns EpollServerSocketChannelConfig\n\n
    setWriteBufferWaterMark(final WriteBufferWaterMark writeBufferWaterMark)\n
    '''
def setMessageSizeEstimator():
    '''returns EpollServerSocketChannelConfig\n\n
    setMessageSizeEstimator(final MessageSizeEstimator estimator)\n
    '''
def setTcpMd5Sig():
    '''returns EpollServerSocketChannelConfig\n\n
    setTcpMd5Sig(final Map<InetAddress, byte[]> keys)\n
    '''
def isReusePort():
    '''returns boolean\n\n
    isReusePort()\n
    '''
def setReusePort():
    '''returns EpollServerSocketChannelConfig\n\n
    setReusePort(final boolean reusePort)\n
    '''
def isFreeBind():
    '''returns boolean\n\n
    isFreeBind()\n
    '''
def setFreeBind():
    '''returns EpollServerSocketChannelConfig\n\n
    setFreeBind(final boolean freeBind)\n
    '''
def isIpTransparent():
    '''returns boolean\n\n
    isIpTransparent()\n
    '''
def setIpTransparent():
    '''returns EpollServerSocketChannelConfig\n\n
    setIpTransparent(final boolean transparent)\n
    '''
def setTcpDeferAccept():
    '''returns EpollServerSocketChannelConfig\n\n
    setTcpDeferAccept(final int deferAccept)\n
    '''
def getTcpDeferAccept():
    '''returns int\n\n
    getTcpDeferAccept()\n
    '''
