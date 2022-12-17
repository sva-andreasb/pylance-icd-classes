def ():
    '''returns OioSocketChannel\n\n
    ()\n
    (final Socket socket)\n
    (final Channel parent, final Socket socket)\n
    '''
def parent():
    '''returns ServerSocketChannel\n\n
    parent()\n
    '''
def config():
    '''returns OioSocketChannelConfig\n\n
    config()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
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
def shutdownOutput():
    '''returns ChannelFuture\n\n
    shutdownOutput()\n
    shutdownOutput(final ChannelPromise promise)\n
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
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture shutdownOutputFuture)\n
    operationComplete(final ChannelFuture shutdownInputFuture)\n
    '''
def localAddress():
    '''returns InetSocketAddress\n\n
    localAddress()\n
    '''
def remoteAddress():
    '''returns InetSocketAddress\n\n
    remoteAddress()\n
    '''
