def SslConnection():
    '''public SslConnection(final SSLEngine engine, final EndPoint endp)
    public SslConnection(final SSLEngine engine, final EndPoint endp, final long timeStamp)
    '''
def isAllowRenegotiate():
    '''public boolean isAllowRenegotiate()
    '''
def setAllowRenegotiate():
    '''public void setAllowRenegotiate(final boolean allowRenegotiate)
    '''
def handle():
    '''public Connection handle()
    '''
def isIdle():
    '''public boolean isIdle()
    '''
def isSuspended():
    '''public boolean isSuspended()
    '''
def onClose():
    '''public void onClose()
    '''
def onIdleExpired():
    '''public void onIdleExpired(final long idleForMs)
    public void onIdleExpired(final long idleForMs)
    '''
def onInputShutdown():
    '''public void onInputShutdown()
    '''
def getSslEndPoint():
    '''public AsyncEndPoint getSslEndPoint()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def getSslEngine():
    '''public SSLEngine getSslEngine()
    '''
def getEndpoint():
    '''public AsyncEndPoint getEndpoint()
    '''
def shutdownOutput():
    '''public void shutdownOutput()
    '''
def isOutputShutdown():
    '''public boolean isOutputShutdown()
    '''
def shutdownInput():
    '''public void shutdownInput()
    '''
def isInputShutdown():
    '''public boolean isInputShutdown()
    '''
def close():
    '''public void close()
    '''
def fill():
    '''public int fill(final Buffer buffer)
    '''
def flush():
    '''public int flush(final Buffer buffer)
    public int flush(final Buffer header, final Buffer buffer, final Buffer trailer)
    public void flush()
    '''
def blockReadable():
    '''public boolean blockReadable(final long millisecs)
    '''
def blockWritable():
    '''public boolean blockWritable(final long millisecs)
    '''
def isOpen():
    '''public boolean isOpen()
    '''
def getTransport():
    '''public Object getTransport()
    '''
def asyncDispatch():
    '''public void asyncDispatch()
    '''
def scheduleWrite():
    '''public void scheduleWrite()
    '''
def setCheckForIdle():
    '''public void setCheckForIdle(final boolean check)
    '''
def isCheckForIdle():
    '''public boolean isCheckForIdle()
    '''
def scheduleTimeout():
    '''public void scheduleTimeout(final Timeout.Task task, final long timeoutMs)
    '''
def cancelTimeout():
    '''public void cancelTimeout(final Timeout.Task task)
    '''
def isWritable():
    '''public boolean isWritable()
    '''
def hasProgressed():
    '''public boolean hasProgressed()
    '''
def getLocalAddr():
    '''public String getLocalAddr()
    '''
def getLocalHost():
    '''public String getLocalHost()
    '''
def getLocalPort():
    '''public int getLocalPort()
    '''
def getRemoteAddr():
    '''public String getRemoteAddr()
    '''
def getRemoteHost():
    '''public String getRemoteHost()
    '''
def getRemotePort():
    '''public int getRemotePort()
    '''
def isBlocking():
    '''public boolean isBlocking()
    '''
def getMaxIdleTime():
    '''public int getMaxIdleTime()
    '''
def setMaxIdleTime():
    '''public void setMaxIdleTime(final int timeMs)
    '''
def getConnection():
    '''public Connection getConnection()
    '''
def setConnection():
    '''public void setConnection(final Connection connection)
    '''
