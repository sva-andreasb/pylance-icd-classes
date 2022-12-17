def getReceiveBufferSize():
    '''returns int\n\n
    getReceiveBufferSize()\n
    '''
def getSendBufferSize():
    '''returns int\n\n
    getSendBufferSize()\n
    '''
def getSoLinger():
    '''returns int\n\n
    getSoLinger()\n
    '''
def getTrafficClass():
    '''returns int\n\n
    getTrafficClass()\n
    '''
def isKeepAlive():
    '''returns boolean\n\n
    isKeepAlive()\n
    '''
def isReuseAddress():
    '''returns boolean\n\n
    isReuseAddress()\n
    '''
def isTcpNoDelay():
    '''returns boolean\n\n
    isTcpNoDelay()\n
    '''
def isTcpCork():
    '''returns boolean\n\n
    isTcpCork()\n
    '''
def getSoBusyPoll():
    '''returns int\n\n
    getSoBusyPoll()\n
    '''
def getTcpNotSentLowAt():
    '''returns long\n\n
    getTcpNotSentLowAt()\n
    '''
def getTcpKeepIdle():
    '''returns int\n\n
    getTcpKeepIdle()\n
    '''
def getTcpKeepIntvl():
    '''returns int\n\n
    getTcpKeepIntvl()\n
    '''
def getTcpKeepCnt():
    '''returns int\n\n
    getTcpKeepCnt()\n
    '''
def getTcpUserTimeout():
    '''returns int\n\n
    getTcpUserTimeout()\n
    '''
def setKeepAlive():
    '''returns EpollSocketChannelConfig\n\n
    setKeepAlive(final boolean keepAlive)\n
    '''
def setPerformancePreferences():
    '''returns EpollSocketChannelConfig\n\n
    setPerformancePreferences(final int connectionTime, final int latency, final int bandwidth)\n
    '''
def setReceiveBufferSize():
    '''returns EpollSocketChannelConfig\n\n
    setReceiveBufferSize(final int receiveBufferSize)\n
    '''
def setReuseAddress():
    '''returns EpollSocketChannelConfig\n\n
    setReuseAddress(final boolean reuseAddress)\n
    '''
def setSendBufferSize():
    '''returns EpollSocketChannelConfig\n\n
    setSendBufferSize(final int sendBufferSize)\n
    '''
def setSoLinger():
    '''returns EpollSocketChannelConfig\n\n
    setSoLinger(final int soLinger)\n
    '''
def setTcpNoDelay():
    '''returns EpollSocketChannelConfig\n\n
    setTcpNoDelay(final boolean tcpNoDelay)\n
    '''
def setTcpCork():
    '''returns EpollSocketChannelConfig\n\n
    setTcpCork(final boolean tcpCork)\n
    '''
def setSoBusyPoll():
    '''returns EpollSocketChannelConfig\n\n
    setSoBusyPoll(final int loopMicros)\n
    '''
def setTcpNotSentLowAt():
    '''returns EpollSocketChannelConfig\n\n
    setTcpNotSentLowAt(final long tcpNotSentLowAt)\n
    '''
def setTrafficClass():
    '''returns EpollSocketChannelConfig\n\n
    setTrafficClass(final int trafficClass)\n
    '''
def setTcpKeepIdle():
    '''returns EpollSocketChannelConfig\n\n
    setTcpKeepIdle(final int seconds)\n
    '''
def setTcpKeepIntvl():
    '''returns EpollSocketChannelConfig\n\n
    setTcpKeepIntvl(final int seconds)\n
    '''
def setTcpKeepCntl():
    '''returns EpollSocketChannelConfig\n\n
    setTcpKeepCntl(final int probes)\n
    '''
def setTcpKeepCnt():
    '''returns EpollSocketChannelConfig\n\n
    setTcpKeepCnt(final int probes)\n
    '''
def setTcpUserTimeout():
    '''returns EpollSocketChannelConfig\n\n
    setTcpUserTimeout(final int milliseconds)\n
    '''
def isIpTransparent():
    '''returns boolean\n\n
    isIpTransparent()\n
    '''
def setIpTransparent():
    '''returns EpollSocketChannelConfig\n\n
    setIpTransparent(final boolean transparent)\n
    '''
def setTcpMd5Sig():
    '''returns EpollSocketChannelConfig\n\n
    setTcpMd5Sig(final Map<InetAddress, byte[]> keys)\n
    '''
def setTcpQuickAck():
    '''returns EpollSocketChannelConfig\n\n
    setTcpQuickAck(final boolean quickAck)\n
    '''
def isTcpQuickAck():
    '''returns boolean\n\n
    isTcpQuickAck()\n
    '''
def setTcpFastOpenConnect():
    '''returns EpollSocketChannelConfig\n\n
    setTcpFastOpenConnect(final boolean fastOpenConnect)\n
    '''
def isTcpFastOpenConnect():
    '''returns boolean\n\n
    isTcpFastOpenConnect()\n
    '''
def isAllowHalfClosure():
    '''returns boolean\n\n
    isAllowHalfClosure()\n
    '''
def setAllowHalfClosure():
    '''returns EpollSocketChannelConfig\n\n
    setAllowHalfClosure(final boolean allowHalfClosure)\n
    '''
def setConnectTimeoutMillis():
    '''returns EpollSocketChannelConfig\n\n
    setConnectTimeoutMillis(final int connectTimeoutMillis)\n
    '''
def setMaxMessagesPerRead():
    '''returns EpollSocketChannelConfig\n\n
    setMaxMessagesPerRead(final int maxMessagesPerRead)\n
    '''
def setWriteSpinCount():
    '''returns EpollSocketChannelConfig\n\n
    setWriteSpinCount(final int writeSpinCount)\n
    '''
def setAllocator():
    '''returns EpollSocketChannelConfig\n\n
    setAllocator(final ByteBufAllocator allocator)\n
    '''
def setRecvByteBufAllocator():
    '''returns EpollSocketChannelConfig\n\n
    setRecvByteBufAllocator(final RecvByteBufAllocator allocator)\n
    '''
def setAutoRead():
    '''returns EpollSocketChannelConfig\n\n
    setAutoRead(final boolean autoRead)\n
    '''
def setAutoClose():
    '''returns EpollSocketChannelConfig\n\n
    setAutoClose(final boolean autoClose)\n
    '''
def setWriteBufferHighWaterMark():
    '''returns EpollSocketChannelConfig\n\n
    setWriteBufferHighWaterMark(final int writeBufferHighWaterMark)\n
    '''
def setWriteBufferLowWaterMark():
    '''returns EpollSocketChannelConfig\n\n
    setWriteBufferLowWaterMark(final int writeBufferLowWaterMark)\n
    '''
def setWriteBufferWaterMark():
    '''returns EpollSocketChannelConfig\n\n
    setWriteBufferWaterMark(final WriteBufferWaterMark writeBufferWaterMark)\n
    '''
def setMessageSizeEstimator():
    '''returns EpollSocketChannelConfig\n\n
    setMessageSizeEstimator(final MessageSizeEstimator estimator)\n
    '''
def setEpollMode():
    '''returns EpollSocketChannelConfig\n\n
    setEpollMode(final EpollMode mode)\n
    '''
