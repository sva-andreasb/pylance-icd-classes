def ():
    '''returns SelectChannelEndPoint\n\n
    (final SocketChannel channel, final SelectorManager.SelectSet selectSet, final SelectionKey key, final int maxIdleTime)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def getSelectionKey():
    '''returns SelectionKey\n\n
    getSelectionKey()\n
    '''
def getSelectManager():
    '''returns SelectorManager\n\n
    getSelectManager()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection connection)\n
    '''
def getIdleTimestamp():
    '''returns long\n\n
    getIdleTimestamp()\n
    '''
def schedule():
    '''returns None\n\n
    schedule()\n
    '''
def asyncDispatch():
    '''returns None\n\n
    asyncDispatch()\n
    '''
def dispatch():
    '''returns None\n\n
    dispatch()\n
    '''
def cancelTimeout():
    '''returns None\n\n
    cancelTimeout(final Timeout.Task task)\n
    '''
def scheduleTimeout():
    '''returns None\n\n
    scheduleTimeout(final Timeout.Task task, final long timeoutMs)\n
    '''
def setCheckForIdle():
    '''returns None\n\n
    setCheckForIdle(final boolean check)\n
    '''
def isCheckForIdle():
    '''returns boolean\n\n
    isCheckForIdle()\n
    '''
def checkIdleTimestamp():
    '''returns None\n\n
    checkIdleTimestamp(final long now)\n
    '''
def onIdleExpired():
    '''returns None\n\n
    onIdleExpired(final long idleForMs)\n
    '''
def fill():
    '''returns int\n\n
    fill(final Buffer buffer)\n
    '''
def flush():
    '''returns int\n\n
    flush(final Buffer header, final Buffer buffer, final Buffer trailer)\n
    flush(final Buffer buffer)\n
    '''
def blockReadable():
    '''returns boolean\n\n
    blockReadable(final long timeoutMs)\n
    '''
def blockWritable():
    '''returns boolean\n\n
    blockWritable(final long timeoutMs)\n
    '''
def scheduleWrite():
    '''returns None\n\n
    scheduleWrite()\n
    '''
def isWritable():
    '''returns boolean\n\n
    isWritable()\n
    '''
def hasProgressed():
    '''returns boolean\n\n
    hasProgressed()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final int timeMs)\n
    '''
