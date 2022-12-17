MAX_DATA_LENGTH = "int  512"
MIN_DATA_LENGTH = "int  0"
def ():
    '''returns TFTPDataPacket\n\n
    (final InetAddress destination, final int port, final int blockNumber, final byte[] data, final int offset, final int length)\n
    (final InetAddress destination, final int port, final int blockNumber, final byte[] data)\n
    '''
def newDatagram():
    '''returns DatagramPacket\n\n
    newDatagram()\n
    '''
def getBlockNumber():
    '''returns int\n\n
    getBlockNumber()\n
    '''
def setBlockNumber():
    '''returns None\n\n
    setBlockNumber(final int blockNumber)\n
    '''
def setData():
    '''returns None\n\n
    setData(final byte[] data, final int offset, final int length)\n
    '''
def getDataLength():
    '''returns int\n\n
    getDataLength()\n
    '''
def getDataOffset():
    '''returns int\n\n
    getDataOffset()\n
    '''
def getData():
    '''returns byte[]\n\n
    getData()\n
    '''
