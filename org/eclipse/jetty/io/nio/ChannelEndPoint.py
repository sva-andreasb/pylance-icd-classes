def ChannelEndPoint():
    '''    public ChannelEndPoint(final ByteChannel channel)
    '''
def isBlocking():
    '''    public boolean isBlocking()
    '''
def blockReadable():
    '''    public boolean blockReadable(final long millisecs)
    '''
def blockWritable():
    '''    public boolean blockWritable(final long millisecs)
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def shutdownInput():
    '''    public void shutdownInput()
    '''
def shutdownOutput():
    '''    public void shutdownOutput()
    '''
def isOutputShutdown():
    '''    public boolean isOutputShutdown()
    '''
def isInputShutdown():
    '''    public boolean isInputShutdown()
    '''
def close():
    '''    public void close()
    '''
def fill():
    '''    public int fill(final Buffer buffer)
    '''
def flush():
    '''    public int flush(final Buffer buffer)
    public int flush(final Buffer header, final Buffer buffer, final Buffer trailer)
    public void flush()
    '''
def getChannel():
    '''    public ByteChannel getChannel()
    '''
def getLocalAddr():
    '''    public String getLocalAddr()
    '''
def getLocalHost():
    '''    public String getLocalHost()
    '''
def getLocalPort():
    '''    public int getLocalPort()
    '''
def getRemoteAddr():
    '''    public String getRemoteAddr()
    '''
def getRemoteHost():
    '''    public String getRemoteHost()
    '''
def getRemotePort():
    '''    public int getRemotePort()
    '''
def getTransport():
    '''    public Object getTransport()
    '''
def getMaxIdleTime():
    '''    public int getMaxIdleTime()
    '''
def setMaxIdleTime():
    '''    public void setMaxIdleTime(final int timeMs)
    '''
