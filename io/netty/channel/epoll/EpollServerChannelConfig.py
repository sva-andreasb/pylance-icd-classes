def isReuseAddress():
    '''returns boolean\n\n
    isReuseAddress()\n
    '''
def setReuseAddress():
    '''returns EpollServerChannelConfig\n\n
    setReuseAddress(final boolean reuseAddress)\n
    '''
def getReceiveBufferSize():
    '''returns int\n\n
    getReceiveBufferSize()\n
    '''
def setReceiveBufferSize():
    '''returns EpollServerChannelConfig\n\n
    setReceiveBufferSize(final int receiveBufferSize)\n
    '''
def getBacklog():
    '''returns int\n\n
    getBacklog()\n
    '''
def setBacklog():
    '''returns EpollServerChannelConfig\n\n
    setBacklog(final int backlog)\n
    '''
def getTcpFastopen():
    '''returns int\n\n
    getTcpFastopen()\n
    '''
def setTcpFastopen():
    '''returns EpollServerChannelConfig\n\n
    setTcpFastopen(final int pendingFastOpenRequestsThreshold)\n
    '''
def setPerformancePreferences():
    '''returns EpollServerChannelConfig\n\n
    setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)\n
    '''
def setConnectTimeoutMillis():
    '''returns EpollServerChannelConfig\n\n
    setConnectTimeoutMillis(final int connectTimeoutMillis)\n
    '''
def setMaxMessagesPerRead():
    '''returns EpollServerChannelConfig\n\n
    setMaxMessagesPerRead(final int maxMessagesPerRead)\n
    '''
def setWriteSpinCount():
    '''returns EpollServerChannelConfig\n\n
    setWriteSpinCount(final int writeSpinCount)\n
    '''
def setAllocator():
    '''returns EpollServerChannelConfig\n\n
    setAllocator(final ByteBufAllocator allocator)\n
    '''
def setRecvByteBufAllocator():
    '''returns EpollServerChannelConfig\n\n
    setRecvByteBufAllocator(final RecvByteBufAllocator allocator)\n
    '''
def setAutoRead():
    '''returns EpollServerChannelConfig\n\n
    setAutoRead(final boolean autoRead)\n
    '''
def setWriteBufferHighWaterMark():
    '''returns EpollServerChannelConfig\n\n
    setWriteBufferHighWaterMark(final int writeBufferHighWaterMark)\n
    '''
def setWriteBufferLowWaterMark():
    '''returns EpollServerChannelConfig\n\n
    setWriteBufferLowWaterMark(final int writeBufferLowWaterMark)\n
    '''
def setWriteBufferWaterMark():
    '''returns EpollServerChannelConfig\n\n
    setWriteBufferWaterMark(final WriteBufferWaterMark writeBufferWaterMark)\n
    '''
def setMessageSizeEstimator():
    '''returns EpollServerChannelConfig\n\n
    setMessageSizeEstimator(final MessageSizeEstimator estimator)\n
    '''
def setEpollMode():
    '''returns EpollServerChannelConfig\n\n
    setEpollMode(final EpollMode mode)\n
    '''
