def DefaultDatagramChannelConfig():
    '''    public DefaultDatagramChannelConfig(final DatagramChannel channel, final DatagramSocket javaSocket)
    '''
def getOption():
    '''    public <T> T getOption(final ChannelOption<T> option)
    '''
def setOption():
    '''    public <T> boolean setOption(final ChannelOption<T> option, final T value)
    '''
def isBroadcast():
    '''    public boolean isBroadcast()
    '''
def setBroadcast():
    '''    public DatagramChannelConfig setBroadcast(final boolean broadcast)
    '''
def getInterface():
    '''    public InetAddress getInterface()
    '''
def setInterface():
    '''    public DatagramChannelConfig setInterface(final InetAddress interfaceAddress)
    '''
def isLoopbackModeDisabled():
    '''    public boolean isLoopbackModeDisabled()
    '''
def setLoopbackModeDisabled():
    '''    public DatagramChannelConfig setLoopbackModeDisabled(final boolean loopbackModeDisabled)
    '''
def getNetworkInterface():
    '''    public NetworkInterface getNetworkInterface()
    '''
def setNetworkInterface():
    '''    public DatagramChannelConfig setNetworkInterface(final NetworkInterface networkInterface)
    '''
def isReuseAddress():
    '''    public boolean isReuseAddress()
    '''
def setReuseAddress():
    '''    public DatagramChannelConfig setReuseAddress(final boolean reuseAddress)
    '''
def getReceiveBufferSize():
    '''    public int getReceiveBufferSize()
    '''
def setReceiveBufferSize():
    '''    public DatagramChannelConfig setReceiveBufferSize(final int receiveBufferSize)
    '''
def getSendBufferSize():
    '''    public int getSendBufferSize()
    '''
def setSendBufferSize():
    '''    public DatagramChannelConfig setSendBufferSize(final int sendBufferSize)
    '''
def getTimeToLive():
    '''    public int getTimeToLive()
    '''
def setTimeToLive():
    '''    public DatagramChannelConfig setTimeToLive(final int ttl)
    '''
def getTrafficClass():
    '''    public int getTrafficClass()
    '''
def setTrafficClass():
    '''    public DatagramChannelConfig setTrafficClass(final int trafficClass)
    '''
def setWriteSpinCount():
    '''    public DatagramChannelConfig setWriteSpinCount(final int writeSpinCount)
    '''
def setConnectTimeoutMillis():
    '''    public DatagramChannelConfig setConnectTimeoutMillis(final int connectTimeoutMillis)
    '''
def setMaxMessagesPerRead():
    '''    public DatagramChannelConfig setMaxMessagesPerRead(final int maxMessagesPerRead)
    '''
def setAllocator():
    '''    public DatagramChannelConfig setAllocator(final ByteBufAllocator allocator)
    '''
def setRecvByteBufAllocator():
    '''    public DatagramChannelConfig setRecvByteBufAllocator(final RecvByteBufAllocator allocator)
    '''
def setAutoRead():
    '''    public DatagramChannelConfig setAutoRead(final boolean autoRead)
    '''
def setAutoClose():
    '''    public DatagramChannelConfig setAutoClose(final boolean autoClose)
    '''
def setWriteBufferHighWaterMark():
    '''    public DatagramChannelConfig setWriteBufferHighWaterMark(final int writeBufferHighWaterMark)
    '''
def setWriteBufferLowWaterMark():
    '''    public DatagramChannelConfig setWriteBufferLowWaterMark(final int writeBufferLowWaterMark)
    '''
def setWriteBufferWaterMark():
    '''    public DatagramChannelConfig setWriteBufferWaterMark(final WriteBufferWaterMark writeBufferWaterMark)
    '''
def setMessageSizeEstimator():
    '''    public DatagramChannelConfig setMessageSizeEstimator(final MessageSizeEstimator estimator)
    '''
