UNDEFINED = "int  0"
FILE_NOT_FOUND = "int  1"
ACCESS_VIOLATION = "int  2"
OUT_OF_SPACE = "int  3"
ILLEGAL_OPERATION = "int  4"
UNKNOWN_TID = "int  5"
FILE_EXISTS = "int  6"
NO_SUCH_USER = "int  7"
def ():
    '''returns TFTPErrorPacket\n\n
    (final InetAddress destination, final int port, final int error, final String message)\n
    '''
def newDatagram():
    '''returns DatagramPacket\n\n
    newDatagram()\n
    '''
def getError():
    '''returns int\n\n
    getError()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
