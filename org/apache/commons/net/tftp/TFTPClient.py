DEFAULT_MAX_TIMEOUTS = "int  5"
def ():
    '''returns TFTPClient\n\n
    ()\n
    '''
def setMaxTimeouts():
    '''returns None\n\n
    setMaxTimeouts(final int numTimeouts)\n
    '''
def getMaxTimeouts():
    '''returns int\n\n
    getMaxTimeouts()\n
    '''
def receiveFile():
    '''returns int\n\n
    receiveFile(final String filename, final int mode, OutputStream output, InetAddress host, final int port)\n
    receiveFile(final String filename, final int mode, final OutputStream output, final String hostname, final int port)\n
    receiveFile(final String filename, final int mode, final OutputStream output, final InetAddress host)\n
    receiveFile(final String filename, final int mode, final OutputStream output, final String hostname)\n
    '''
def sendFile():
    '''returns None\n\n
    sendFile(final String filename, final int mode, InputStream input, InetAddress host, final int port)\n
    sendFile(final String filename, final int mode, final InputStream input, final String hostname, final int port)\n
    sendFile(final String filename, final int mode, final InputStream input, final InetAddress host)\n
    sendFile(final String filename, final int mode, final InputStream input, final String hostname)\n
    '''
