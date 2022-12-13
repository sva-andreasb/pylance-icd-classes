def addListener():
    '''public Future<V> addListener(final GenericFutureListener<? extends Future<? super V>> listener)
    '''
def addListeners():
    '''public Future<V> addListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)
    '''
def removeListener():
    '''public Future<V> removeListener(final GenericFutureListener<? extends Future<? super V>> listener)
    '''
def removeListeners():
    '''public Future<V> removeListeners(final GenericFutureListener<? extends Future<? super V>>... listeners)
    '''
def await():
    '''public Future<V> await()
    public boolean await(final long timeout, final TimeUnit unit)
    public boolean await(final long timeoutMillis)
    '''
def sync():
    '''public Future<V> sync()
    '''
def syncUninterruptibly():
    '''public Future<V> syncUninterruptibly()
    '''
def awaitUninterruptibly():
    '''public Future<V> awaitUninterruptibly()
    public boolean awaitUninterruptibly(final long timeout, final TimeUnit unit)
    public boolean awaitUninterruptibly(final long timeoutMillis)
    '''
def isDone():
    '''public boolean isDone()
    '''
def isCancellable():
    '''public boolean isCancellable()
    '''
def isCancelled():
    '''public boolean isCancelled()
    '''
def cancel():
    '''public boolean cancel(final boolean mayInterruptIfRunning)
    '''
