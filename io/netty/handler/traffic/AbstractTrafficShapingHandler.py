DEFAULT_CHECK_INTERVAL = "long  1000L"
DEFAULT_MAX_TIME = "long  15000L"
def configure():
    '''returns None\n\n
    configure(final long newWriteLimit, final long newReadLimit, final long newCheckInterval)\n
    configure(final long newWriteLimit, final long newReadLimit)\n
    configure(final long newCheckInterval)\n
    '''
def getWriteLimit():
    '''returns long\n\n
    getWriteLimit()\n
    '''
def setWriteLimit():
    '''returns None\n\n
    setWriteLimit(final long writeLimit)\n
    '''
def getReadLimit():
    '''returns long\n\n
    getReadLimit()\n
    '''
def setReadLimit():
    '''returns None\n\n
    setReadLimit(final long readLimit)\n
    '''
def getCheckInterval():
    '''returns long\n\n
    getCheckInterval()\n
    '''
def setCheckInterval():
    '''returns None\n\n
    setCheckInterval(final long checkInterval)\n
    '''
def setMaxTimeWait():
    '''returns None\n\n
    setMaxTimeWait(final long maxTime)\n
    '''
def getMaxTimeWait():
    '''returns long\n\n
    getMaxTimeWait()\n
    '''
def getMaxWriteDelay():
    '''returns long\n\n
    getMaxWriteDelay()\n
    '''
def setMaxWriteDelay():
    '''returns None\n\n
    setMaxWriteDelay(final long maxWriteDelay)\n
    '''
def getMaxWriteSize():
    '''returns long\n\n
    getMaxWriteSize()\n
    '''
def setMaxWriteSize():
    '''returns None\n\n
    setMaxWriteSize(final long maxWriteSize)\n
    '''
def channelRead():
    '''returns None\n\n
    channelRead(final ChannelHandlerContext ctx, final Object msg)\n
    '''
def handlerRemoved():
    '''returns None\n\n
    handlerRemoved(final ChannelHandlerContext ctx)\n
    '''
def read():
    '''returns None\n\n
    read(final ChannelHandlerContext ctx)\n
    '''
def write():
    '''returns None\n\n
    write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)\n
    '''
def channelRegistered():
    '''returns None\n\n
    channelRegistered(final ChannelHandlerContext ctx)\n
    '''
def trafficCounter():
    '''returns TrafficCounter\n\n
    trafficCounter()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
