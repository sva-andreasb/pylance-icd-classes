def ():
    '''returns GlobalTrafficShapingHandler\n\n
    (final ScheduledExecutorService executor, final long writeLimit, final long readLimit, final long checkInterval, final long maxTime)\n
    (final ScheduledExecutorService executor, final long writeLimit, final long readLimit, final long checkInterval)\n
    (final ScheduledExecutorService executor, final long writeLimit, final long readLimit)\n
    (final ScheduledExecutorService executor, final long checkInterval)\n
    (final EventExecutor executor)\n
    '''
def getMaxGlobalWriteSize():
    '''returns long\n\n
    getMaxGlobalWriteSize()\n
    '''
def setMaxGlobalWriteSize():
    '''returns None\n\n
    setMaxGlobalWriteSize(final long maxGlobalWriteSize)\n
    '''
def queuesSize():
    '''returns long\n\n
    queuesSize()\n
    '''
def handlerAdded():
    '''returns None\n\n
    handlerAdded(final ChannelHandlerContext ctx)\n
    '''
def handlerRemoved():
    '''returns None\n\n
    handlerRemoved(final ChannelHandlerContext ctx)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
