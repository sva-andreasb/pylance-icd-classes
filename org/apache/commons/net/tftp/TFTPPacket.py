READ_REQUEST = "int  1"
WRITE_REQUEST = "int  2"
DATA = "int  3"
ACKNOWLEDGEMENT = "int  4"
ERROR = "int  5"
SEGMENT_SIZE = "int  512"
def newTFTPPacket():
    '''public static final TFTPPacket newTFTPPacket(final DatagramPacket datagram)
    '''
def getType():
    '''public final int getType()
    '''
def getAddress():
    '''public final InetAddress getAddress()
    '''
def getPort():
    '''public final int getPort()
    '''
def setPort():
    '''public final void setPort(final int port)
    '''
def setAddress():
    '''public final void setAddress(final InetAddress address)
    '''
