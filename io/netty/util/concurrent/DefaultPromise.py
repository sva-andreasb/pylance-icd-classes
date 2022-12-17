def ():
    '''returns DefaultPromise\n\n
    (final EventExecutor executor)\n
    '''
def setSuccess():
    '''returns Promise<V>\n\n
    setSuccess(final V result)\n
    '''
def trySuccess():
    '''returns boolean\n\n
    trySuccess(final V result)\n
    '''
def setFailure():
    '''returns Promise<V>\n\n
    setFailure(final Throwable cause)\n
    '''
def tryFailure():
    '''returns boolean\n\n
    tryFailure(final Throwable cause)\n
    '''
def setUncancellable():
    '''returns boolean\n\n
    setUncancellable()\n
    '''
def isSuccess():
    '''returns boolean\n\n
    isSuccess()\n
    '''
def isCancellable():
    '''returns boolean\n\n
    isCancellable()\n
    '''
def cause():
    '''returns Throwable\n\n
    cause()\n
    '''
def addListener():
    '''returns Promise<V>\n\n
    addListener(final GenericFutureListener<? extends Future<? super V>> listener)\n
    '''
def addListeners():
    '''returns Promise<V>\n\n
    addListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)\n
    '''
def removeListener():
    '''returns Promise<V>\n\n
    removeListener(final GenericFutureListener<? extends Future<? super V>> listener)\n
    '''
def removeListeners():
    '''returns Promise<V>\n\n
    removeListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)\n
    '''
def await():
    '''returns boolean\n\n
    await()\n
    await(final long timeout, final TimeUnit unit)\n
    await(final long timeoutMillis)\n
    '''
def awaitUninterruptibly():
    '''returns boolean\n\n
    awaitUninterruptibly()\n
    awaitUninterruptibly(final long timeout, final TimeUnit unit)\n
    awaitUninterruptibly(final long timeoutMillis)\n
    '''
def getNow():
    '''returns V\n\n
    getNow()\n
    '''
def get():
    '''returns V\n\n
    get()\n
    get(final long timeout, final TimeUnit unit)\n
    '''
def cancel():
    '''returns boolean\n\n
    cancel(final boolean mayInterruptIfRunning)\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
def sync():
    '''returns Promise<V>\n\n
    sync()\n
    '''
def syncUninterruptibly():
    '''returns Promise<V>\n\n
    syncUninterruptibly()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def fillInStackTrace():
    '''returns Throwable\n\n
    fillInStackTrace()\n
    '''
