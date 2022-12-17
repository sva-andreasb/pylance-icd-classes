DEFAULT_RECONNECTION_DELAY_MILLIS = "int  30000"
def ():
    '''returns FactoryData\n\n
    (final String name, final OutputStream os, final Socket socket, final InetAddress inetAddress, final String host, final int port, final int connectTimeoutMillis, final int reconnectionDelayMillis, final boolean immediateFail, final Layout<? extends Serializable> layout, final int bufferSize)\n
    (final String name, final OutputStream os, final Socket socket, final InetAddress inetAddress, final String host, final int port, final int connectTimeoutMillis, final int reconnectionDelayMillis, final boolean immediateFail, final Layout<? extends Serializable> layout, final int bufferSize, final SocketOptions socketOptions)\n
    (final OutputStreamManager owner)\n
    (final String host, final int port, final int connectTimeoutMillis, final int reconnectDelayMillis, final boolean immediateFail, final Layout<? extends Serializable> layout, final int bufferSize, final SocketOptions socketOptions)\n
    '''
def getConnectTimeoutMillis():
    '''returns int\n\n
    getConnectTimeoutMillis()\n
    '''
def getSocketOptions():
    '''returns SocketOptions\n\n
    getSocketOptions()\n
    '''
def getSocket():
    '''returns Socket\n\n
    getSocket()\n
    '''
def getReconnectionDelayMillis():
    '''returns int\n\n
    getReconnectionDelayMillis()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    '''
def latch():
    '''returns None\n\n
    latch()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def createManager():
    '''returns M\n\n
    createManager(final String name, final T data)\n
    '''
def resolveHost():
    '''returns List<InetSocketAddress>\n\n
    resolveHost(final String host, final int port)\n
    '''
