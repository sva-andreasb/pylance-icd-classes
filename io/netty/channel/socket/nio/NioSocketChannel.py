def ():
    '''returns NioSocketChannel\n\n
    ()\n
    (final SelectorProvider provider)\n
    (final java.nio.channels.SocketChannel socket)\n
    (final Channel parent, final java.nio.channels.SocketChannel socket)\n
    '''
def parent():
    '''returns ServerSocketChannel\n\n
    parent()\n
    '''
def config():
    '''returns SocketChannelConfig\n\n
    config()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def isOutputShutdown():
    '''returns boolean\n\n
    isOutputShutdown()\n
    '''
def isInputShutdown():
    '''returns boolean\n\n
    isInputShutdown()\n
    '''
def isShutdown():
    '''returns boolean\n\n
    isShutdown()\n
    '''
def localAddress():
    '''returns InetSocketAddress\n\n
    localAddress()\n
    '''
def remoteAddress():
    '''returns InetSocketAddress\n\n
    remoteAddress()\n
    '''
def shutdownOutput():
    '''returns ChannelFuture\n\n
    shutdownOutput()\n
    shutdownOutput(final ChannelPromise promise)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def shutdownInput():
    '''returns ChannelFuture\n\n
    shutdownInput()\n
    shutdownInput(final ChannelPromise promise)\n
    '''
def shutdown():
    '''returns ChannelFuture\n\n
    shutdown()\n
    shutdown(final ChannelPromise promise)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture shutdownOutputFuture)\n
    operationComplete(final ChannelFuture shutdownInputFuture)\n
    '''
def setSendBufferSize():
    '''returns NioSocketChannelConfig\n\n
    setSendBufferSize(final int sendBufferSize)\n
    '''
