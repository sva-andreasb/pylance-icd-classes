SYSTAT_PORT = "int  11"
NETSTAT_PORT = "int  15"
QUOTE_OF_DAY_PORT = "int  17"
CHARGEN_PORT = "int  19"
DEFAULT_PORT = "int  19"
def ():
    '''returns CharGenUDPClient\n\n
    ()\n
    '''
def send():
    '''returns None\n\n
    send(final InetAddress host, final int port)\n
    send(final InetAddress host)\n
    '''
def receive():
    '''returns byte[]\n\n
    receive()\n
    '''
