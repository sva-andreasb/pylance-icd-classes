def ready():
    '''returns boolean\n\n
    ready()\n
    '''
def finishConnect():
    '''returns boolean\n\n
    finishConnect()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def socketChannel():
    '''returns SocketChannel\n\n
    socketChannel()\n
    '''
def selectionKey():
    '''returns SelectionKey\n\n
    selectionKey()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def hasPendingWrites():
    '''returns boolean\n\n
    hasPendingWrites()\n
    '''
def handshake():
    '''returns None\n\n
    handshake()\n
    '''
def read():
    '''returns long\n\n
    read(final ByteBuffer dst)\n
    read(final ByteBuffer[] dsts)\n
    read(final ByteBuffer[] dsts, final int offset, final int length)\n
    '''
def write():
    '''returns long\n\n
    write(final ByteBuffer src)\n
    write(final ByteBuffer[] srcs, final int offset, final int length)\n
    write(final ByteBuffer[] srcs)\n
    '''
def peerPrincipal():
    '''returns Principal\n\n
    peerPrincipal()\n
    '''
def sslSession():
    '''returns SSLSession\n\n
    sslSession()\n
    '''
def addInterestOps():
    '''returns None\n\n
    addInterestOps(final int ops)\n
    '''
def removeInterestOps():
    '''returns None\n\n
    removeInterestOps(final int ops)\n
    '''
def isMute():
    '''returns boolean\n\n
    isMute()\n
    '''
def hasBytesBuffered():
    '''returns boolean\n\n
    hasBytesBuffered()\n
    '''
def transferFrom():
    '''returns long\n\n
    transferFrom(final FileChannel fileChannel, final long position, final long count)\n
    '''
