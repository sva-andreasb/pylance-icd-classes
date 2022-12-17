def ():
    '''returns PendingWriteQueue\n\n
    (final ChannelHandlerContext ctx)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def bytes():
    '''returns long\n\n
    bytes()\n
    '''
def add():
    '''returns None\n\n
    add(final Object msg, final ChannelPromise promise)\n
    '''
def removeAndWriteAll():
    '''returns ChannelFuture\n\n
    removeAndWriteAll()\n
    '''
def removeAndFailAll():
    '''returns None\n\n
    removeAndFailAll(final Throwable cause)\n
    '''
def removeAndFail():
    '''returns None\n\n
    removeAndFail(final Throwable cause)\n
    '''
def removeAndWrite():
    '''returns ChannelFuture\n\n
    removeAndWrite()\n
    '''
def remove():
    '''returns ChannelPromise\n\n
    remove()\n
    '''
def current():
    '''returns Object\n\n
    current()\n
    '''
def newObject():
    '''returns PendingWrite\n\n
    newObject(final ObjectPool.Handle<PendingWrite> handle)\n
    '''
