def ():
    '''returns OioDatagramChannel\n\n
    ()\n
    (final MulticastSocket socket)\n
    '''
def metadata():
    '''returns ChannelMetadata\n\n
    metadata()\n
    '''
def config():
    '''returns DatagramChannelConfig\n\n
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
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def localAddress():
    '''returns InetSocketAddress\n\n
    localAddress()\n
    '''
def remoteAddress():
    '''returns InetSocketAddress\n\n
    remoteAddress()\n
    '''
def joinGroup():
    '''returns ChannelFuture\n\n
    joinGroup(final InetAddress multicastAddress)\n
    joinGroup(final InetAddress multicastAddress, final ChannelPromise promise)\n
    joinGroup(final InetSocketAddress multicastAddress, final NetworkInterface networkInterface)\n
    joinGroup(final InetSocketAddress multicastAddress, final NetworkInterface networkInterface, final ChannelPromise promise)\n
    joinGroup(final InetAddress multicastAddress, final NetworkInterface networkInterface, final InetAddress source)\n
    joinGroup(final InetAddress multicastAddress, final NetworkInterface networkInterface, final InetAddress source, final ChannelPromise promise)\n
    '''
def leaveGroup():
    '''returns ChannelFuture\n\n
    leaveGroup(final InetAddress multicastAddress)\n
    leaveGroup(final InetAddress multicastAddress, final ChannelPromise promise)\n
    leaveGroup(final InetSocketAddress multicastAddress, final NetworkInterface networkInterface)\n
    leaveGroup(final InetSocketAddress multicastAddress, final NetworkInterface networkInterface, final ChannelPromise promise)\n
    leaveGroup(final InetAddress multicastAddress, final NetworkInterface networkInterface, final InetAddress source)\n
    leaveGroup(final InetAddress multicastAddress, final NetworkInterface networkInterface, final InetAddress source, final ChannelPromise promise)\n
    '''
def block():
    '''returns ChannelFuture\n\n
    block(final InetAddress multicastAddress, final NetworkInterface networkInterface, final InetAddress sourceToBlock)\n
    block(final InetAddress multicastAddress, final NetworkInterface networkInterface, final InetAddress sourceToBlock, final ChannelPromise promise)\n
    block(final InetAddress multicastAddress, final InetAddress sourceToBlock)\n
    block(final InetAddress multicastAddress, final InetAddress sourceToBlock, final ChannelPromise promise)\n
    '''
