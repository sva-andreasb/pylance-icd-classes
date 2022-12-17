def ():
    '''returns ServerBootstrap\n\n
    ()\n
    '''
def group():
    '''returns ServerBootstrap\n\n
    group(final EventLoopGroup group)\n
    group(final EventLoopGroup parentGroup, final EventLoopGroup childGroup)\n
    '''
def childHandler():
    '''returns ServerBootstrap\n\n
    childHandler(final ChannelHandler childHandler)\n
    '''
def initChannel():
    '''returns None\n\n
    initChannel(final Channel ch)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def validate():
    '''returns ServerBootstrap\n\n
    validate()\n
    '''
def clone():
    '''returns ServerBootstrap\n\n
    clone()\n
    '''
def childGroup():
    '''returns EventLoopGroup\n\n
    childGroup()\n
    '''
def channelRead():
    '''returns None\n\n
    channelRead(final ChannelHandlerContext ctx, final Object msg)\n
    '''
def operationComplete():
    '''returns None\n\n
    operationComplete(final ChannelFuture future)\n
    '''
def exceptionCaught():
    '''returns None\n\n
    exceptionCaught(final ChannelHandlerContext ctx, final Throwable cause)\n
    '''
