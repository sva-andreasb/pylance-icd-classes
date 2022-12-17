def ():
    '''returns ChannelEndPoint\n\n
    (final ByteChannel channel)\n
    '''
def isBlocking():
    '''returns boolean\n\n
    isBlocking()\n
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
def shutdownInput():
    '''returns None\n\n
    shutdownInput()\n
    '''
def shutdownOutput():
    '''returns None\n\n
    shutdownOutput()\n
    '''
def isOutputShutdown():
    '''returns boolean\n\n
    isOutputShutdown()\n
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
def getChannel():
    '''returns ByteChannel\n\n
    getChannel()\n
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
def getTransport():
    '''returns Object\n\n
    getTransport()\n
    '''
def getMaxIdleTime():
    '''returns int\n\n
    getMaxIdleTime()\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final int timeMs)\n
    '''
