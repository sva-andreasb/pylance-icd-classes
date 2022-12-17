NO_IDLE_TIMEOUT_MS = "long  -1L"
def ():
    '''returns IdleExpiryManager\n\n
    (final int maxReceiveSize, final long connectionMaxIdleMs, final Metrics metrics, final Time time, final String metricGrpPrefix, final Map<String, String> metricTags, final boolean metricsPerConnection, final boolean recordTimePerConnection, final ChannelBuilder channelBuilder, final MemoryPool memoryPool, final LogContext logContext)\n
    (final int maxReceiveSize, final long connectionMaxIdleMs, final Metrics metrics, final Time time, final String metricGrpPrefix, final Map<String, String> metricTags, final boolean metricsPerConnection, final ChannelBuilder channelBuilder, final LogContext logContext)\n
    (final long connectionMaxIdleMS, final Metrics metrics, final Time time, final String metricGrpPrefix, final ChannelBuilder channelBuilder, final LogContext logContext)\n
    (final Metrics metrics, final String metricGrpPrefix, final Map<String, String> metricTags, final boolean metricsPerConnection)\n
    (final Time time, final long connectionsMaxIdleMs)\n
    '''
def connect():
    '''returns None\n\n
    connect(final String id, final InetSocketAddress address, final int sendBufferSize, final int receiveBufferSize)\n
    '''
def register():
    '''returns None\n\n
    register(final String id, final SocketChannel socketChannel)\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close(final String id)\n
    close()\n
    '''
def send():
    '''returns None\n\n
    send(final Send send)\n
    '''
def poll():
    '''returns None\n\n
    poll(long timeout)\n
    '''
def completedSends():
    '''returns List<Send>\n\n
    completedSends()\n
    '''
def completedReceives():
    '''returns List<NetworkReceive>\n\n
    completedReceives()\n
    '''
def connected():
    '''returns List<String>\n\n
    connected()\n
    '''
def mute():
    '''returns None\n\n
    mute(final String id)\n
    '''
def unmute():
    '''returns None\n\n
    unmute(final String id)\n
    '''
def muteAll():
    '''returns None\n\n
    muteAll()\n
    '''
def unmuteAll():
    '''returns None\n\n
    unmuteAll()\n
    '''
def isChannelReady():
    '''returns boolean\n\n
    isChannelReady(final String id)\n
    '''
def channels():
    '''returns List<KafkaChannel>\n\n
    channels()\n
    '''
def channel():
    '''returns KafkaChannel\n\n
    channel(final String id)\n
    '''
def closingChannel():
    '''returns KafkaChannel\n\n
    closingChannel(final String id)\n
    '''
def keys():
    '''returns Set<SelectionKey>\n\n
    keys()\n
    '''
def numStagedReceives():
    '''returns int\n\n
    numStagedReceives(final KafkaChannel channel)\n
    '''
def measure():
    '''returns double\n\n
    measure(final MetricConfig config, final long now)\n
    '''
def maybeRegisterConnectionMetrics():
    '''returns None\n\n
    maybeRegisterConnectionMetrics(final String connectionId)\n
    '''
def recordBytesSent():
    '''returns None\n\n
    recordBytesSent(final String connectionId, final long bytes)\n
    '''
def recordBytesReceived():
    '''returns None\n\n
    recordBytesReceived(final String connection, final int bytes)\n
    '''
def update():
    '''returns None\n\n
    update(final String connectionId, final long currentTimeNanos)\n
    '''
def remove():
    '''returns None\n\n
    remove(final String connectionId)\n
    '''
