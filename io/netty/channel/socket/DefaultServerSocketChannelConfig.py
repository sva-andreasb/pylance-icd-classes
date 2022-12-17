def ():
    '''returns DefaultServerSocketChannelConfig\n\n
    (final ServerSocketChannel channel, final ServerSocket javaSocket)\n
    '''
def isReuseAddress():
    '''returns boolean\n\n
    isReuseAddress()\n
    '''
def setReuseAddress():
    '''returns ServerSocketChannelConfig\n\n
    setReuseAddress(final boolean reuseAddress)\n
    '''
def getReceiveBufferSize():
    '''returns int\n\n
    getReceiveBufferSize()\n
    '''
def setReceiveBufferSize():
    '''returns ServerSocketChannelConfig\n\n
    setReceiveBufferSize(final int receiveBufferSize)\n
    '''
def setPerformancePreferences():
    '''returns ServerSocketChannelConfig\n\n
    setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)\n
    '''
def getBacklog():
    '''returns int\n\n
    getBacklog()\n
    '''
def setBacklog():
    '''returns ServerSocketChannelConfig\n\n
    setBacklog(final int backlog)\n
    '''
def setConnectTimeoutMillis():
    '''returns ServerSocketChannelConfig\n\n
    setConnectTimeoutMillis(final int connectTimeoutMillis)\n
    '''
def setMaxMessagesPerRead():
    '''returns ServerSocketChannelConfig\n\n
    setMaxMessagesPerRead(final int maxMessagesPerRead)\n
    '''
def setWriteSpinCount():
    '''returns ServerSocketChannelConfig\n\n
    setWriteSpinCount(final int writeSpinCount)\n
    '''
def setAllocator():
    '''returns ServerSocketChannelConfig\n\n
    setAllocator(final ByteBufAllocator allocator)\n
    '''
def setRecvByteBufAllocator():
    '''returns ServerSocketChannelConfig\n\n
    setRecvByteBufAllocator(final RecvByteBufAllocator allocator)\n
    '''
def setAutoRead():
    '''returns ServerSocketChannelConfig\n\n
    setAutoRead(final boolean autoRead)\n
    '''
def setWriteBufferHighWaterMark():
    '''returns ServerSocketChannelConfig\n\n
    setWriteBufferHighWaterMark(final int writeBufferHighWaterMark)\n
    '''
def setWriteBufferLowWaterMark():
    '''returns ServerSocketChannelConfig\n\n
    setWriteBufferLowWaterMark(final int writeBufferLowWaterMark)\n
    '''
def setWriteBufferWaterMark():
    '''returns ServerSocketChannelConfig\n\n
    setWriteBufferWaterMark(final WriteBufferWaterMark writeBufferWaterMark)\n
    '''
def setMessageSizeEstimator():
    '''returns ServerSocketChannelConfig\n\n
    setMessageSizeEstimator(final MessageSizeEstimator estimator)\n
    '''
