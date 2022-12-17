def addListener():
    '''returns Future<V>\n\n
    addListener(final GenericFutureListener<? extends Future<? super V>> listener)\n
    '''
def addListeners():
    '''returns Future<V>\n\n
    addListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)\n
    '''
def removeListener():
    '''returns Future<V>\n\n
    removeListener(final GenericFutureListener<? extends Future<? super V>> listener)\n
    '''
def removeListeners():
    '''returns Future<V>\n\n
    removeListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)\n
    '''
def await():
    '''returns boolean\n\n
    await()\n
    await(final long timeout, final TimeUnit unit)\n
    await(final long timeoutMillis)\n
    '''
def sync():
    '''returns Future<V>\n\n
    sync()\n
    '''
def syncUninterruptibly():
    '''returns Future<V>\n\n
    syncUninterruptibly()\n
    '''
def awaitUninterruptibly():
    '''returns boolean\n\n
    awaitUninterruptibly()\n
    awaitUninterruptibly(final long timeout, final TimeUnit unit)\n
    awaitUninterruptibly(final long timeoutMillis)\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
def isCancellable():
    '''returns boolean\n\n
    isCancellable()\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def cancel():
    '''returns boolean\n\n
    cancel(final boolean mayInterruptIfRunning)\n
    '''
