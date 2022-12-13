DEFAULT_MAX_TIMEOUTS = "int  5"
def TFTPClient():
    '''public TFTPClient()
    '''
def setMaxTimeouts():
    '''public void setMaxTimeouts(final int numTimeouts)
    '''
def getMaxTimeouts():
    '''public int getMaxTimeouts()
    '''
def receiveFile():
    '''public int receiveFile(final String filename, final int mode, OutputStream output, InetAddress host, final int port)
    public int receiveFile(final String filename, final int mode, final OutputStream output, final String hostname, final int port)
    public int receiveFile(final String filename, final int mode, final OutputStream output, final InetAddress host)
    public int receiveFile(final String filename, final int mode, final OutputStream output, final String hostname)
    '''
def sendFile():
    '''public void sendFile(final String filename, final int mode, InputStream input, InetAddress host, final int port)
    public void sendFile(final String filename, final int mode, final InputStream input, final String hostname, final int port)
    public void sendFile(final String filename, final int mode, final InputStream input, final InetAddress host)
    public void sendFile(final String filename, final int mode, final InputStream input, final String hostname)
    '''
