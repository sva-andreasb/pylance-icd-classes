DEFAULT_CHECK_INTERVAL = "long  1000L"
DEFAULT_MAX_TIME = "long  15000L"
def configure():
    '''public void configure(final long newWriteLimit, final long newReadLimit, final long newCheckInterval)
    public void configure(final long newWriteLimit, final long newReadLimit)
    public void configure(final long newCheckInterval)
    '''
def getWriteLimit():
    '''public long getWriteLimit()
    '''
def setWriteLimit():
    '''public void setWriteLimit(final long writeLimit)
    '''
def getReadLimit():
    '''public long getReadLimit()
    '''
def setReadLimit():
    '''public void setReadLimit(final long readLimit)
    '''
def getCheckInterval():
    '''public long getCheckInterval()
    '''
def setCheckInterval():
    '''public void setCheckInterval(final long checkInterval)
    '''
def setMaxTimeWait():
    '''public void setMaxTimeWait(final long maxTime)
    '''
def getMaxTimeWait():
    '''public long getMaxTimeWait()
    '''
def getMaxWriteDelay():
    '''public long getMaxWriteDelay()
    '''
def setMaxWriteDelay():
    '''public void setMaxWriteDelay(final long maxWriteDelay)
    '''
def getMaxWriteSize():
    '''public long getMaxWriteSize()
    '''
def setMaxWriteSize():
    '''public void setMaxWriteSize(final long maxWriteSize)
    '''
def channelRead():
    '''public void channelRead(final ChannelHandlerContext ctx, final Object msg)
    '''
def handlerRemoved():
    '''public void handlerRemoved(final ChannelHandlerContext ctx)
    '''
def read():
    '''public void read(final ChannelHandlerContext ctx)
    '''
def write():
    '''public void write(final ChannelHandlerContext ctx, final Object msg, final ChannelPromise promise)
    '''
def channelRegistered():
    '''public void channelRegistered(final ChannelHandlerContext ctx)
    '''
def trafficCounter():
    '''public TrafficCounter trafficCounter()
    '''
def toString():
    '''public String toString()
    '''
def run():
    '''public void run()
    '''
