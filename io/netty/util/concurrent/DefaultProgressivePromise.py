def ():
    '''returns DefaultProgressivePromise\n\n
    (final EventExecutor executor)\n
    '''
def setProgress():
    '''returns ProgressivePromise<V>\n\n
    setProgress(final long progress, long total)\n
    '''
def tryProgress():
    '''returns boolean\n\n
    tryProgress(final long progress, long total)\n
    '''
def addListener():
    '''returns ProgressivePromise<V>\n\n
    addListener(final GenericFutureListener<? extends Future<? super V>> listener)\n
    '''
def addListeners():
    '''returns ProgressivePromise<V>\n\n
    addListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)\n
    '''
def removeListener():
    '''returns ProgressivePromise<V>\n\n
    removeListener(final GenericFutureListener<? extends Future<? super V>> listener)\n
    '''
def removeListeners():
    '''returns ProgressivePromise<V>\n\n
    removeListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)\n
    '''
def sync():
    '''returns ProgressivePromise<V>\n\n
    sync()\n
    '''
def syncUninterruptibly():
    '''returns ProgressivePromise<V>\n\n
    syncUninterruptibly()\n
    '''
def await():
    '''returns ProgressivePromise<V>\n\n
    await()\n
    '''
def awaitUninterruptibly():
    '''returns ProgressivePromise<V>\n\n
    awaitUninterruptibly()\n
    '''
def setSuccess():
    '''returns ProgressivePromise<V>\n\n
    setSuccess(final V result)\n
    '''
def setFailure():
    '''returns ProgressivePromise<V>\n\n
    setFailure(final Throwable cause)\n
    '''
