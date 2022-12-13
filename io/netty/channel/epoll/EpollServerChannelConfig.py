def getOption():
    '''public <T> T getOption(final ChannelOption<T> option)
    '''
def setOption():
    '''public <T> boolean setOption(final ChannelOption<T> option, final T value)
    '''
def isReuseAddress():
    '''public boolean isReuseAddress()
    '''
def setReuseAddress():
    '''public EpollServerChannelConfig setReuseAddress(final boolean reuseAddress)
    '''
def getReceiveBufferSize():
    '''public int getReceiveBufferSize()
    '''
def setReceiveBufferSize():
    '''public EpollServerChannelConfig setReceiveBufferSize(final int receiveBufferSize)
    '''
def getBacklog():
    '''public int getBacklog()
    '''
def setBacklog():
    '''public EpollServerChannelConfig setBacklog(final int backlog)
    '''
def getTcpFastopen():
    '''public int getTcpFastopen()
    '''
def setTcpFastopen():
    '''public EpollServerChannelConfig setTcpFastopen(final int pendingFastOpenRequestsThreshold)
    '''
def setPerformancePreferences():
    '''public EpollServerChannelConfig setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)
    '''
def setConnectTimeoutMillis():
    '''public EpollServerChannelConfig setConnectTimeoutMillis(final int connectTimeoutMillis)
    '''
def setMaxMessagesPerRead():
    '''public EpollServerChannelConfig setMaxMessagesPerRead(final int maxMessagesPerRead)
    '''
def setWriteSpinCount():
    '''public EpollServerChannelConfig setWriteSpinCount(final int writeSpinCount)
    '''
def setAllocator():
    '''public EpollServerChannelConfig setAllocator(final ByteBufAllocator allocator)
    '''
def setRecvByteBufAllocator():
    '''public EpollServerChannelConfig setRecvByteBufAllocator(final RecvByteBufAllocator allocator)
    '''
def setAutoRead():
    '''public EpollServerChannelConfig setAutoRead(final boolean autoRead)
    '''
def setWriteBufferHighWaterMark():
    '''public EpollServerChannelConfig setWriteBufferHighWaterMark(final int writeBufferHighWaterMark)
    '''
def setWriteBufferLowWaterMark():
    '''public EpollServerChannelConfig setWriteBufferLowWaterMark(final int writeBufferLowWaterMark)
    '''
def setWriteBufferWaterMark():
    '''public EpollServerChannelConfig setWriteBufferWaterMark(final WriteBufferWaterMark writeBufferWaterMark)
    '''
def setMessageSizeEstimator():
    '''public EpollServerChannelConfig setMessageSizeEstimator(final MessageSizeEstimator estimator)
    '''
def setEpollMode():
    '''public EpollServerChannelConfig setEpollMode(final EpollMode mode)
    '''
