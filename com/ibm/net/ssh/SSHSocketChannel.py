def connect():
    '''returns boolean\n\n
    connect(final SocketAddress remote)\n
    connect(final SocketAddress remote, final int timeout)\n
    '''
def finishConnect():
    '''returns boolean\n\n
    finishConnect()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isConnectionPending():
    '''returns boolean\n\n
    isConnectionPending()\n
    '''
def socket():
    '''returns Socket\n\n
    socket()\n
    '''
def read():
    '''returns int\n\n
    read(final ByteBuffer[] dsts, final int offset, final int length)\n
    read(final ByteBuffer dst)\n
    '''
def write():
    '''returns int\n\n
    write(final ByteBuffer[] srcs, final int offset, final int length)\n
    write(final ByteBuffer src)\n
    '''
def implCloseSelectableChannel():
    '''returns None\n\n
    implCloseSelectableChannel()\n
    '''
def implConfigureBlocking():
    '''returns None\n\n
    implConfigureBlocking(final boolean block)\n
    '''
