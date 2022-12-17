def ():
    '''returns SslConnection\n\n
    (final SSLEngine engine, final EndPoint endp)\n
    (final SSLEngine engine, final EndPoint endp, final long timeStamp)\n
    '''
def isAllowRenegotiate():
    '''returns boolean\n\n
    isAllowRenegotiate()\n
    '''
def setAllowRenegotiate():
    '''returns None\n\n
    setAllowRenegotiate(final boolean allowRenegotiate)\n
    '''
def handle():
    '''returns Connection\n\n
    handle()\n
    '''
def isIdle():
    '''returns boolean\n\n
    isIdle()\n
    '''
def isSuspended():
    '''returns boolean\n\n
    isSuspended()\n
    '''
def onClose():
    '''returns None\n\n
    onClose()\n
    '''
def onIdleExpired():
    '''returns None\n\n
    onIdleExpired(final long idleForMs)\n
    onIdleExpired(final long idleForMs)\n
    '''
def onInputShutdown():
    '''returns None\n\n
    onInputShutdown()\n
    '''
def getSslEndPoint():
    '''returns AsyncEndPoint\n\n
    getSslEndPoint()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getSslEngine():
    '''returns SSLEngine\n\n
    getSslEngine()\n
    '''
def getEndpoint():
    '''returns AsyncEndPoint\n\n
    getEndpoint()\n
    '''
def shutdownOutput():
    '''returns None\n\n
    shutdownOutput()\n
    '''
def isOutputShutdown():
    '''returns boolean\n\n
    isOutputShutdown()\n
    '''
def shutdownInput():
    '''returns None\n\n
    shutdownInput()\n
    '''
def isInputShutdown():
    '''returns boolean\n\n
    isInputShutdown()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def fill():
    '''returns int\n\n
    fill(final Buffer buffer)\n
    '''
def flush():
    '''returns None\n\n
    flush(final Buffer buffer)\n
    flush(final Buffer header, final Buffer buffer, final Buffer trailer)\n
    flush()\n
    '''
def blockReadable():
    '''returns boolean\n\n
    blockReadable(final long millisecs)\n
    '''
def blockWritable():
    '''returns boolean\n\n
    blockWritable(final long millisecs)\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def getTransport():
    '''returns Object\n\n
    getTransport()\n
    '''
def asyncDispatch():
    '''returns None\n\n
    asyncDispatch()\n
    '''
def scheduleWrite():
    '''returns None\n\n
    scheduleWrite()\n
    '''
def setCheckForIdle():
    '''returns None\n\n
    setCheckForIdle(final boolean check)\n
    '''
def isCheckForIdle():
    '''returns boolean\n\n
    isCheckForIdle()\n
    '''
def scheduleTimeout():
    '''returns None\n\n
    scheduleTimeout(final Timeout.Task task, final long timeoutMs)\n
    '''
def cancelTimeout():
    '''returns None\n\n
    cancelTimeout(final Timeout.Task task)\n
    '''
def isWritable():
    '''returns boolean\n\n
    isWritable()\n
    '''
def hasProgressed():
    '''returns boolean\n\n
    hasProgressed()\n
    '''
def getLocalAddr():
    '''returns String\n\n
    getLocalAddr()\n
    '''
def getLocalHost():
    '''returns String\n\n
    getLocalHost()\n
    '''
def getLocalPort():
    '''returns int\n\n
    getLocalPort()\n
    '''
def getRemoteAddr():
    '''returns String\n\n
    getRemoteAddr()\n
    '''
def getRemoteHost():
    '''returns String\n\n
    getRemoteHost()\n
    '''
def getRemotePort():
    '''returns int\n\n
    getRemotePort()\n
    '''
def isBlocking():
    '''returns boolean\n\n
    isBlocking()\n
    '''
def getMaxIdleTime():
    '''returns int\n\n
    getMaxIdleTime()\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final int timeMs)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection connection)\n
    '''
