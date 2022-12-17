DEFAULT_PORT = "int  514"
MIN_CLIENT_PORT = "int  512"
MAX_CLIENT_PORT = "int  1023"
def ():
    '''returns RCommandClient\n\n
    ()\n
    '''
def connect():
    '''returns None\n\n
    connect(final InetAddress host, final int port, final InetAddress localAddr)\n
    connect(final InetAddress host, final int port)\n
    connect(final String hostname, final int port)\n
    connect(final String hostname, final int port, final InetAddress localAddr)\n
    connect(final InetAddress host, final int port, final InetAddress localAddr, final int localPort)\n
    connect(final String hostname, final int port, final InetAddress localAddr, final int localPort)\n
    '''
def rcommand():
    '''returns None\n\n
    rcommand(final String localUsername, final String remoteUsername, final String command, final boolean separateErrorStream)\n
    rcommand(final String localUsername, final String remoteUsername, final String command)\n
    '''
