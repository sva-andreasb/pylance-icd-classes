def SslConnection():
'''public SslConnection(final SSLEngine engine, final EndPoint endp)
public SslConnection(final SSLEngine engine, final EndPoint endp, final long timeStamp)
'''
pass
def isAllowRenegotiate():
'''public boolean isAllowRenegotiate()
'''
pass
def setAllowRenegotiate():
'''public void setAllowRenegotiate(final boolean allowRenegotiate)
'''
pass
def handle():
'''public Connection handle()
'''
pass
def isIdle():
'''public boolean isIdle()
'''
pass
def isSuspended():
'''public boolean isSuspended()
'''
pass
def onClose():
'''public void onClose()
'''
pass
def onIdleExpired():
'''public void onIdleExpired(final long idleForMs)
public void onIdleExpired(final long idleForMs)
'''
pass
def onInputShutdown():
'''public void onInputShutdown()
'''
pass
def getSslEndPoint():
'''public AsyncEndPoint getSslEndPoint()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def getSslEngine():
'''public SSLEngine getSslEngine()
'''
pass
def getEndpoint():
'''public AsyncEndPoint getEndpoint()
'''
pass
def shutdownOutput():
'''public void shutdownOutput()
'''
pass
def isOutputShutdown():
'''public boolean isOutputShutdown()
'''
pass
def shutdownInput():
'''public void shutdownInput()
'''
pass
def isInputShutdown():
'''public boolean isInputShutdown()
'''
pass
def close():
'''public void close()
'''
pass
def fill():
'''public int fill(final Buffer buffer)
'''
pass
def flush():
'''public int flush(final Buffer buffer)
public int flush(final Buffer header, final Buffer buffer, final Buffer trailer)
public void flush()
'''
pass
def blockReadable():
'''public boolean blockReadable(final long millisecs)
'''
pass
def blockWritable():
'''public boolean blockWritable(final long millisecs)
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def getTransport():
'''public Object getTransport()
'''
pass
def asyncDispatch():
'''public void asyncDispatch()
'''
pass
def scheduleWrite():
'''public void scheduleWrite()
'''
pass
def setCheckForIdle():
'''public void setCheckForIdle(final boolean check)
'''
pass
def isCheckForIdle():
'''public boolean isCheckForIdle()
'''
pass
def scheduleTimeout():
'''public void scheduleTimeout(final Timeout.Task task, final long timeoutMs)
'''
pass
def cancelTimeout():
'''public void cancelTimeout(final Timeout.Task task)
'''
pass
def isWritable():
'''public boolean isWritable()
'''
pass
def hasProgressed():
'''public boolean hasProgressed()
'''
pass
def getLocalAddr():
'''public String getLocalAddr()
'''
pass
def getLocalHost():
'''public String getLocalHost()
'''
pass
def getLocalPort():
'''public int getLocalPort()
'''
pass
def getRemoteAddr():
'''public String getRemoteAddr()
'''
pass
def getRemoteHost():
'''public String getRemoteHost()
'''
pass
def getRemotePort():
'''public int getRemotePort()
'''
pass
def isBlocking():
'''public boolean isBlocking()
'''
pass
def getMaxIdleTime():
'''public int getMaxIdleTime()
'''
pass
def setMaxIdleTime():
'''public void setMaxIdleTime(final int timeMs)
'''
pass
def getConnection():
'''public Connection getConnection()
'''
pass
def setConnection():
'''public void setConnection(final Connection connection)
'''
pass
