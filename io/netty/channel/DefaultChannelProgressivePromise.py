def ():
    '''returns DefaultChannelProgressivePromise\n\n
    (final Channel channel)\n
    (final Channel channel, final EventExecutor executor)\n
    '''
def channel():
    '''returns Channel\n\n
    channel()\n
    '''
def setSuccess():
    '''returns ChannelProgressivePromise\n\n
    setSuccess()\n
    setSuccess(final Void result)\n
    '''
def trySuccess():
    '''returns boolean\n\n
    trySuccess()\n
    '''
def setFailure():
    '''returns ChannelProgressivePromise\n\n
    setFailure(final Throwable cause)\n
    '''
def setProgress():
    '''returns ChannelProgressivePromise\n\n
    setProgress(final long progress, final long total)\n
    '''
def addListener():
    '''returns ChannelProgressivePromise\n\n
    addListener(final GenericFutureListener<? extends Future<? super Void>> listener)\n
    '''
def addListeners():
    '''returns ChannelProgressivePromise\n\n
    addListeners(final GenericFutureListener<? extends Future<? super Void>>... listeners)\n
    '''
def removeListener():
    '''returns ChannelProgressivePromise\n\n
    removeListener(final GenericFutureListener<? extends Future<? super Void>> listener)\n
    '''
def removeListeners():
    '''returns ChannelProgressivePromise\n\n
    removeListeners(final GenericFutureListener<? extends Future<? super Void>>... listeners)\n
    '''
def sync():
    '''returns ChannelProgressivePromise\n\n
    sync()\n
    '''
def syncUninterruptibly():
    '''returns ChannelProgressivePromise\n\n
    syncUninterruptibly()\n
    '''
def await():
    '''returns ChannelProgressivePromise\n\n
    await()\n
    '''
def awaitUninterruptibly():
    '''returns ChannelProgressivePromise\n\n
    awaitUninterruptibly()\n
    '''
def flushCheckpoint():
    '''returns None\n\n
    flushCheckpoint()\n
    flushCheckpoint(final long checkpoint)\n
    '''
def promise():
    '''returns ChannelProgressivePromise\n\n
    promise()\n
    '''
def unvoid():
    '''returns ChannelProgressivePromise\n\n
    unvoid()\n
    '''
def isVoid():
    '''returns boolean\n\n
    isVoid()\n
    '''
