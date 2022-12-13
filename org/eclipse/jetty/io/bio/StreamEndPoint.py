def StreamEndPoint():
    '''public StreamEndPoint(final InputStream in, final OutputStream out)
    '''
def isBlocking():
    '''public boolean isBlocking()
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
def isClosed():
    '''public final boolean isClosed()
    '''
def shutdownOutput():
    '''public void shutdownOutput()
    '''
def isInputShutdown():
    '''public boolean isInputShutdown()
    '''
def shutdownInput():
    '''public void shutdownInput()
    '''
def isOutputShutdown():
    '''public boolean isOutputShutdown()
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
def getTransport():
    '''public Object getTransport()
    '''
def getInputStream():
    '''public InputStream getInputStream()
    '''
def setInputStream():
    '''public void setInputStream(final InputStream in)
    '''
def getOutputStream():
    '''public OutputStream getOutputStream()
    '''
def setOutputStream():
    '''public void setOutputStream(final OutputStream out)
    '''
def getMaxIdleTime():
    '''public int getMaxIdleTime()
    '''
def setMaxIdleTime():
    '''public void setMaxIdleTime(final int timeMs)
    '''
