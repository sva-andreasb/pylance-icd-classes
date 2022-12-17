def ():
    '''returns OioSctpChannel\n\n
    ()\n
    (final com.sun.nio.sctp.SctpChannel ch)\n
    (final Channel parent, final com.sun.nio.sctp.SctpChannel ch)\n
    '''
def localAddress():
    '''returns InetSocketAddress\n\n
    localAddress()\n
    '''
def remoteAddress():
    '''returns InetSocketAddress\n\n
    remoteAddress()\n
    '''
def parent():
    '''returns SctpServerChannel\n\n
    parent()\n
    '''
def metadata():
    '''returns ChannelMetadata\n\n
    metadata()\n
    '''
def config():
    '''returns SctpChannelConfig\n\n
    config()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def association():
    '''returns Association\n\n
    association()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def allLocalAddresses():
    '''returns Set<InetSocketAddress>\n\n
    allLocalAddresses()\n
    '''
def allRemoteAddresses():
    '''returns Set<InetSocketAddress>\n\n
    allRemoteAddresses()\n
    '''
def bindAddress():
    '''returns ChannelFuture\n\n
    bindAddress(final InetAddress localAddress)\n
    bindAddress(final InetAddress localAddress, final ChannelPromise promise)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def unbindAddress():
    '''returns ChannelFuture\n\n
    unbindAddress(final InetAddress localAddress)\n
    unbindAddress(final InetAddress localAddress, final ChannelPromise promise)\n
    '''
