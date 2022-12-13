DEFAULT_PORT = "int  514"
MIN_CLIENT_PORT = "int  512"
MAX_CLIENT_PORT = "int  1023"
def RCommandClient():
    '''public RCommandClient()
    '''
def connect():
    '''public void connect(final InetAddress host, final int port, final InetAddress localAddr)
    public void connect(final InetAddress host, final int port)
    public void connect(final String hostname, final int port)
    public void connect(final String hostname, final int port, final InetAddress localAddr)
    public void connect(final InetAddress host, final int port, final InetAddress localAddr, final int localPort)
    public void connect(final String hostname, final int port, final InetAddress localAddr, final int localPort)
    '''
def rcommand():
    '''public void rcommand(final String localUsername, final String remoteUsername, final String command, final boolean separateErrorStream)
    public void rcommand(final String localUsername, final String remoteUsername, final String command)
    '''
