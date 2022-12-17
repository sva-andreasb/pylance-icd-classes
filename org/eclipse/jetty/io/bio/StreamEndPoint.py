def ():
    '''returns StreamEndPoint\n\n
    (final InputStream in, final OutputStream out)\n
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
def shutdownOutput():
    '''returns None\n\n
    shutdownOutput()\n
    '''
def isInputShutdown():
    '''returns boolean\n\n
    isInputShutdown()\n
    '''
def shutdownInput():
    '''returns None\n\n
    shutdownInput()\n
    '''
def isOutputShutdown():
    '''returns boolean\n\n
    isOutputShutdown()\n
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
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def setInputStream():
    '''returns None\n\n
    setInputStream(final InputStream in)\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def setOutputStream():
    '''returns None\n\n
    setOutputStream(final OutputStream out)\n
    '''
def getMaxIdleTime():
    '''returns int\n\n
    getMaxIdleTime()\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final int timeMs)\n
    '''
